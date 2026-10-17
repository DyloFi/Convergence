#!/usr/bin/env python3
"""Step 13 (G6.4): bring the Step 10-12 registers in line with the merged, removed and rewritten reports.

- review/REPORT_TRIAGE.csv and audit/report_triage_inventory.json keep all 153 Step 12
  rows (they are the Step 12 record) and gain two columns: `step13_status` and
  `current_location`.
- review/CLAIM_REGISTER.csv / audit/claims_inventory.json: claims extracted from text
  that no longer exists (merged/removed files, and the pre-rewrite text of rewritten
  files) move to review/CLAIM_REGISTER_RETIRED_STEP13.csv with a reason. Key claims
  verified during the rewrites (review/step13_rewrite_claims.csv) are appended.
- audit/citations_inventory.json and review/CITATION_AUDIT.csv: citing-file paths
  that point at merged files are re-pointed to the merge target; removed files are
  dropped from the citing lists. Rewritten files are dropped from the citing lists of
  sources they no longer cite (their new sources are in review/step13_rewrite_sources.csv).

Idempotent. Usage: python3 scripts/step13_update_registers.py
"""

import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRIAGE_CSV = ROOT / "review" / "REPORT_TRIAGE.csv"
TRIAGE_JSON = ROOT / "audit" / "report_triage_inventory.json"
CLAIM_CSV = ROOT / "review" / "CLAIM_REGISTER.csv"
CLAIM_JSON = ROOT / "audit" / "claims_inventory.json"
RETIRED_CSV = ROOT / "review" / "CLAIM_REGISTER_RETIRED_STEP13.csv"
NEW_CLAIMS = ROOT / "review" / "step13_rewrite_claims.csv"
NEW_SOURCES = ROOT / "review" / "step13_rewrite_sources.csv"
CITE_JSON = ROOT / "audit" / "citations_inventory.json"
CITE_CSV = ROOT / "review" / "CITATION_AUDIT.csv"
DATE = "2026-10-17"


def read_csv(p):
    with open(p, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), list(r.fieldnames)


def write_csv(p, rows, fields):
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main():
    triage, tfields = read_csv(TRIAGE_CSV)
    rewrites_done = set()
    if NEW_CLAIMS.exists():
        rewrites_done = {r["repository_location"] for r in read_csv(NEW_CLAIMS)[0]}

    moved = {}      # removed path -> merge target ('' if deleted)
    for r in triage:
        d, path = r["triage_disposition"], r["file_path"]
        if d == "merge":
            moved[path] = r["target_merge_file"]
            r["step13_status"] = "merged"
            r["current_location"] = r["target_merge_file"]
        elif d == "delete":
            moved[path] = ""
            r["step13_status"] = "removed"
            r["current_location"] = f"archive/step13_originals/{path}.orig"
        elif d == "rewrite":
            r["step13_status"] = "rewritten" if path in rewrites_done else "rewrite pending"
            r["current_location"] = path
        else:
            r["step13_status"] = "unchanged (outside Step 13 scope)"
            r["current_location"] = path
    for extra in ("step13_status", "current_location"):
        if extra not in tfields:
            tfields.append(extra)
    write_csv(TRIAGE_CSV, triage, tfields)

    tj = json.load(open(TRIAGE_JSON, encoding="utf-8"))
    by_path = {r["file_path"]: r for r in triage}
    for rep in tj["reports"]:
        t = by_path[rep["file_path"]]
        rep["step13_status"] = t["step13_status"]
        rep["current_location"] = t["current_location"]
    counts = {}
    for t in triage:
        counts[t["step13_status"]] = counts.get(t["step13_status"], 0) + 1
    tj["step13_summary"] = {
        "date": DATE,
        "status_counts": counts,
        "active_reports_after_step13": sum(1 for t in triage if t["step13_status"] not in ("merged", "removed")),
        "change_record": "review/step13_changes.md",
    }
    json.dump(tj, open(TRIAGE_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    # ---- claims ----
    claims, cfields = read_csv(CLAIM_CSV)
    retired, rfields = ([], cfields + ["retired_reason", "retired_date"])
    if RETIRED_CSV.exists():
        retired, rfields = read_csv(RETIRED_CSV)
    retired_ids = {r["claim_id"] for r in retired}
    rewrites = {t["file_path"] for t in triage if t["triage_disposition"] == "rewrite"}
    keep = []
    for c in claims:
        loc = c["repository_location"].strip()
        reason = None
        if loc in moved:
            reason = ("source file merged into " + moved[loc] + "; claim text was not carried over (unsourced)") if moved[loc] \
                else "source file removed under Step 12 triage (delete)"
        elif loc in rewrites_done and not c["claim_id"].startswith("CLM-S13-"):
            reason = "pre-rewrite text replaced in Step 13; claim superseded by the CLM-S13 claims for this file"
        if reason:
            if c["claim_id"] not in retired_ids:
                c = dict(c)
                c["retired_reason"] = reason
                c["retired_date"] = DATE
                retired.append(c)
        else:
            keep.append(c)
    if NEW_CLAIMS.exists():
        have = {c["claim_id"] for c in keep}
        for n in read_csv(NEW_CLAIMS)[0]:
            if n["claim_id"] not in have:
                keep.append({k: n.get(k, "") for k in cfields})
    write_csv(CLAIM_CSV, keep, cfields)
    write_csv(RETIRED_CSV, retired, rfields)

    cj = json.load(open(CLAIM_JSON, encoding="utf-8"))
    cj["claims"] = keep
    cj["metadata"]["total_claims"] = len(keep)
    cj["metadata"]["verified_count"] = sum(1 for c in keep if c["verification_status"] == "verified")
    cj["metadata"]["total_reports_with_claims"] = len({c["repository_location"] for c in keep})
    cj["metadata"]["step13_retired_claims"] = len(retired)
    cj["metadata"]["step13_note"] = (
        "total_reports_audited is the Step 11 census (153). Step 13 merged 25 and removed 7 reports; "
        "claims from text that no longer exists are in review/CLAIM_REGISTER_RETIRED_STEP13.csv."
    )
    json.dump(cj, open(CLAIM_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    # ---- citations ----
    ci = json.load(open(CITE_JSON, encoding="utf-8"))
    for s in ci["sources"]:
        files = []
        for f in s.get("citing_files", []):
            if f in moved:
                f = moved[f]
                if not f:
                    continue
            if f in rewrites_done:
                continue
            if f not in files:
                files.append(f)
        s["citing_files"] = files
    if NEW_SOURCES.exists():
        existing = {(s.get("url") or "").strip() for s in ci["sources"] if s.get("url")}
        for n in read_csv(NEW_SOURCES)[0]:
            url = n["url"].strip()
            match = [s for s in ci["sources"] if (s.get("url") or "").strip() == url]
            if match:
                for f in n["citing_files"].split(";"):
                    if f and f not in match[0]["citing_files"]:
                        match[0]["citing_files"].append(f)
                continue
            ci["sources"].append({
                "author": n["author"], "year": n["year"], "title": n["title"], "venue": n["venue"],
                "doi": n.get("doi") or None, "url": url, "citing_files": [f for f in n["citing_files"].split(";") if f],
                "verification_status": "verified",
                "verification_source": f"Fetched and checked against the cited figure during Step 13 ({DATE})",
            })
            existing.add(url)
    ci["metadata"]["total_unique_sources"] = len(ci["sources"])
    ci["metadata"]["step13_note"] = (
        "citing_files re-pointed after Step 13 merges/removals; sources added for the Step 13 rewrites. "
        "Sources whose only citing files were removed keep an empty citing_files list."
    )
    json.dump(ci, open(CITE_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    rows, fields = read_csv(CITE_CSV)
    by_key = {}
    for s in ci["sources"]:
        by_key[(s.get("author") or "", str(s.get("year") or ""), s.get("title") or "")] = s
    next_id = max(int(r["citation_id"].split("-")[1]) for r in rows) + 1
    seen = set()
    for r in rows:
        s = by_key.get((r["author_or_institution"], r["year_published"], r["title"]))
        if s is not None:
            seen.add(id(s))
            r["citing_dossier_count"] = str(len(s["citing_files"]))
            r["sample_citing_dossier"] = s["citing_files"][0] if s["citing_files"] else "(no active citing file after Step 13)"
        elif r["sample_citing_dossier"] in moved:
            r["sample_citing_dossier"] = moved[r["sample_citing_dossier"]] or "(no active citing file after Step 13)"
    for s in ci["sources"]:
        if id(s) in seen or not str(s.get("verification_source", "")).startswith("Fetched and checked"):
            continue
        rows.append({
            "citation_id": f"CITE-{next_id:04d}", "author_or_institution": s["author"], "year_published": s["year"],
            "title": s["title"], "venue_or_publisher": s["venue"], "doi_or_url": s.get("doi") or s["url"],
            "citing_dossier_count": str(len(s["citing_files"])), "sample_citing_dossier": s["citing_files"][0] if s["citing_files"] else "",
            "verification_status": "verified", "verification_source": s["verification_source"],
        })
        next_id += 1
    write_csv(CITE_CSV, rows, fields)

    print(f"triage rows: {len(triage)} | status counts: {counts}")
    print(f"claims active: {len(keep)} | retired: {len(retired)}")
    print(f"citation sources: {len(ci['sources'])} | citation audit rows: {len(rows)}")


if __name__ == "__main__":
    main()
