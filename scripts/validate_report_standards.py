#!/usr/bin/env python3
"""Validate a report against the nine Step 12 standards (review/REPORT_STANDARDS.md).

Step 13 rewrites must pass every check. Other reports can be scored with --all
(informational: the Step 12 triage, not this script, decides their disposition).

Checks (dossier type):
  question    - a "Question and scope" section that states a **Question.**
  scope       - the same section states a **Scope.**
  summary     - an "Executive Summary" of at most 250 words
  method      - a "Methodology" section
  evidence    - an "Empirical Evidence" section with at least 150 words
  competing   - a "Competing views and counterarguments" section with at least 80 words
  limitations - a "Limitations" section with at least 60 words
  conclusion  - a "Conclusion" section
  references  - a "References" section with at least 3 dated entries, at least 3 of them with a URL
  language    - no overclaiming or template phrases (e.g. "this proves", "publication-grade")
  provenance  - names its preserved original under archive/step13_originals/

Usage:
  python3 scripts/validate_report_standards.py               # Step 13 rewrites (exit 1 on failure)
  python3 scripts/validate_report_standards.py FILE [FILE..]  # specific files
  python3 scripts/validate_report_standards.py --all          # score every dossier (no exit code)
"""

import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRIAGE = ROOT / "review" / "REPORT_TRIAGE.csv"

BANNED = [
    r"\bthis proves\b", r"\bproves that\b", r"\binevitabl[ey]\b", r"\bguaranteed\b",
    r"publication-grade", r"\bexhaustive\b", r"Core Theoretical Insight", r"Strategic Imperative",
    r"Analytical Focus:", r"\(Deep Dive\)",
]
YEAR = re.compile(r"\b(1[5-9]\d\d|20\d\d)\b")


def sections(text):
    """Map lower-cased H2 heading -> section body."""
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m and not line.startswith("###"):
            if cur is not None:
                out[cur] = "\n".join(buf)
            cur, buf = m.group(1).strip().lower(), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf)
    return out


def words(s):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-.%]*", s))


def validate(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    sec = sections(text)
    get = lambda name: next((v for k, v in sec.items() if k.startswith(name)), None)
    results = {}
    qs = get("question and scope") or ""
    results["question"] = "**Question.**" in qs
    results["scope"] = "**Scope.**" in qs
    summ = get("executive summary")
    results["summary"] = summ is not None and 0 < words(summ) <= 250
    results["method"] = get("methodology") is not None
    ev = get("empirical evidence")
    results["evidence"] = ev is not None and words(ev) >= 150
    cv = get("competing views and counterarguments")
    results["competing"] = cv is not None and words(cv) >= 80
    lim = get("limitations")
    results["limitations"] = lim is not None and words(lim) >= 60
    results["conclusion"] = get("conclusion") is not None
    refs = get("references") or ""
    entries = [l for l in refs.splitlines() if re.match(r"^\s*[-*]\s+\S", l)]
    dated = [e for e in entries if YEAR.search(e)]
    linked = [e for e in entries if "http" in e]
    results["references"] = len(dated) >= 3 and len(linked) >= 3
    hits = [p for p in BANNED if re.search(p, text, re.I)]
    results["language"] = not hits
    results["provenance"] = "archive/step13_originals/" in text
    detail = {"summary_words": words(summ or ""), "references": len(entries), "linked_refs": len(linked), "banned": hits}
    return results, detail


def rewrite_targets():
    rows = list(csv.DictReader(open(TRIAGE, encoding="utf-8")))
    return [ROOT / r["file_path"] for r in rows if r["triage_disposition"] == "rewrite"]


def main(argv):
    if "--all" in argv:
        files = sorted(p for d in ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]
                       for p in (ROOT / d).rglob("*.md") if not p.name.endswith(".bak.md"))
        passed = 0
        for f in files:
            res, _ = validate(f)
            score = sum(res.values())
            passed += score == len(res)
            print(f"{score:2d}/{len(res)}  {f.relative_to(ROOT)}")
        print(f"\n{passed}/{len(files)} reports meet every check (informational).")
        return 0
    files = [pathlib.Path(a).resolve() for a in argv if not a.startswith("--")] or rewrite_targets()
    failed = 0
    for f in files:
        res, det = validate(f)
        bad = [k for k, v in res.items() if not v]
        status = "PASS" if not bad else "FAIL " + ", ".join(bad)
        failed += bool(bad)
        print(f"{status:<40} {f.relative_to(ROOT)}  (summary {det['summary_words']} words, {det['linked_refs']}/{det['references']} refs with URL{', banned: ' + ', '.join(det['banned']) if det['banned'] else ''})")
    print(f"\n{len(files) - failed}/{len(files)} pass all {len(res)} checks.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
