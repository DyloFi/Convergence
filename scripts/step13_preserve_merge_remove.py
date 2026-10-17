#!/usr/bin/env python3
"""Step 13 (G6.4): preserve originals, then execute the Step 12 merge and delete dispositions.

Reads review/REPORT_TRIAGE.csv (the Step 12 register) and, for every file whose
outcome is `major revision` or `rebuild`:

1. Copies the file, byte for byte, to archive/step13_originals/<path>.orig and
   records its SHA-256 in archive/step13_originals/MANIFEST.csv. The `.orig`
   suffix keeps the archived copies out of the report scanners and link tests.
2. disposition == delete: removes the file from the active tree.
3. disposition == merge: removes the file and appends a consolidation section to
   the merge target. Only reference-list entries that are not already in the
   target are carried over. Narrative text and figures are NOT carried over: the
   Step 12 triage found them duplicated or unsourced, and Step 13 does not move
   unverified claims into other reports.
4. disposition == rewrite: preserved only; the rewrite itself is done by hand.

Idempotent: re-running skips files already archived and removed.
Usage: python3 scripts/step13_preserve_merge_remove.py [--dry-run]
"""

import csv
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRIAGE = ROOT / "review" / "REPORT_TRIAGE.csv"
ARCHIVE = ROOT / "archive" / "step13_originals"
MANIFEST = ARCHIVE / "MANIFEST.csv"
DATE = "2026-10-17"

REF_HEADING = re.compile(r"^#{1,6}\s+.*(reference|bibliograph|sources|literature|citations)", re.I)
HEADING = re.compile(r"^#{1,6}\s+")
REF_ENTRY = re.compile(r"^\s*(?:[-*]|\d+\.)\s+\S")


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_head() -> str:
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


DEFINITION = re.compile(r"^\s*(?:[-*]|\d+\.)\s+\*\*[^*]+\*\*\s*:")
YEAR = re.compile(r"\((?:1[5-9]\d\d|20\d\d)[a-z]?(?:[,;][^)]*)?\)")


def looks_like_citation(line: str) -> bool:
    """A reference entry names a dated work or a URL/DOI; glossary-style '**Term**: ...' lines are not citations."""
    if DEFINITION.match(line):
        return False
    return bool(YEAR.search(line) or "http" in line or "doi" in line.lower())


def reference_entries(text: str):
    """Return list entries that sit under a reference/bibliography heading."""
    entries, in_refs = [], False
    for line in text.splitlines():
        if HEADING.match(line):
            in_refs = bool(REF_HEADING.match(line))
            continue
        if in_refs and REF_ENTRY.match(line) and looks_like_citation(line):
            entries.append(line.strip())
    return entries


def norm_key(entry: str) -> str:
    """Normalise an entry for duplicate detection: author + year + first title words."""
    e = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", entry)
    e = re.sub(r"[*_`]", "", e).lower()
    e = re.sub(r"\(analytical focus:.*?\)", "", e)
    e = re.sub(r"[^a-z0-9 ]", " ", e)
    return " ".join(e.split()[:8])


def clean_entry(entry: str) -> str:
    e = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", entry).strip()
    # Drop template tails like "(Glossary Deep Dive Citation)." that name the dead file
    e = re.sub(r"\s*\([^()]*Deep Dive[^()]*\)\.?", ".", e).replace("..", ".")
    return "- " + e


def main(dry_run: bool = False) -> None:
    rows = list(csv.DictReader(open(TRIAGE, encoding="utf-8")))
    targets = [r for r in rows if r["outcome"] in ("major revision", "rebuild")]
    ARCHIVE.mkdir(parents=True, exist_ok=True)

    manifest = {}
    if MANIFEST.exists():
        for m in csv.DictReader(open(MANIFEST, encoding="utf-8")):
            manifest[m["original_path"]] = m

    head = git_head()
    appended = {}
    for r in targets:
        rel = r["file_path"]
        src = ROOT / rel
        arch = ARCHIVE / (rel + ".orig")
        if src.exists() and rel not in manifest:
            arch.parent.mkdir(parents=True, exist_ok=True)
            if not dry_run:
                shutil.copy2(src, arch)
            manifest[rel] = {
                "original_path": rel,
                "archived_copy": str(arch.relative_to(ROOT)),
                "sha256": sha256(src),
                "bytes": str(src.stat().st_size),
                "source_commit": head,
                "triage_outcome": r["outcome"],
                "triage_disposition": r["triage_disposition"],
                "merge_target": r["target_merge_file"] if r["triage_disposition"] == "merge" else "",
            }

        disp = r["triage_disposition"]
        if disp == "rewrite" or not src.exists():
            continue

        if disp == "merge":
            tgt = ROOT / r["target_merge_file"]
            src_text = src.read_text(encoding="utf-8")
            tgt_text = tgt.read_text(encoding="utf-8") + "".join(appended.get(str(tgt), []))
            have = {norm_key(e) for e in reference_entries(tgt_text)}
            # entries already carried over by an earlier merge into the same target
            have |= {norm_key(l) for b in appended.get(str(tgt), []) for l in b.splitlines() if l.startswith("- ")}
            new_refs, seen = [], set()
            for e in reference_entries(src_text):
                k = norm_key(e)
                if k and k not in have and k not in seen:
                    seen.add(k)
                    new_refs.append(clean_entry(e))
            block = [
                "",
                f"## Consolidated from `{pathlib.Path(rel).name}` (Step 13)",
                "",
                f"`{rel}` was merged into this report on {DATE} under the Step 12 triage "
                f"(reason given: {r['deficiency_summary'].rstrip('.').lower()}; {r['rationale'].rstrip('.')}). "
                f"Its narrative sections repeated this report and its figures were not tied to sources, so they were not copied here. "
                f"The original is kept at `archive/step13_originals/{rel}.orig` (SHA-256 `{manifest[rel]['sha256'][:12]}`).",
                "",
            ]
            if new_refs:
                block += [f"References cited in `{pathlib.Path(rel).name}` and not already listed above:", ""] + new_refs + [""]
            else:
                block += [f"Every reference cited in `{pathlib.Path(rel).name}` is already listed in this report.", ""]
            appended.setdefault(str(tgt), []).append("\n".join(block))
            print(f"MERGE  {rel} -> {r['target_merge_file']} (+{len(new_refs)} refs)")
        else:
            print(f"DELETE {rel}")
        if not dry_run:
            src.unlink()
            # remove now-empty directories
            d = src.parent
            while d != ROOT and d.exists() and not any(d.iterdir()):
                d.rmdir()
                d = d.parent

    if not dry_run:
        for tgt, blocks in appended.items():
            p = pathlib.Path(tgt)
            text = p.read_text(encoding="utf-8").rstrip("\n") + "\n" + "".join(blocks).rstrip("\n") + "\n"
            p.write_text(text, encoding="utf-8")
        fields = ["original_path", "archived_copy", "sha256", "bytes", "source_commit",
                  "triage_outcome", "triage_disposition", "merge_target"]
        with open(MANIFEST, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for k in sorted(manifest):
                w.writerow(manifest[k])
        # verify archive integrity
        for k, m in manifest.items():
            assert sha256(ROOT / m["archived_copy"]) == m["sha256"], k
        print(f"Archived {len(manifest)} originals; manifest at {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
