import pathlib
import re

root = pathlib.Path(".")
SUBJECT_DIRECTORIES = [
    "4th Turning",
    "Changing World Orders",
    "Kondratiev Waves",
    "LoAR",
    "Technological Singularity",
]

EXPERT_REVIEW_FILES = {
    "4th Turning": "4th_Turning_Expert_Review.md",
    "Changing World Orders": "Changing_World_Orders_Expert_Review.md",
    "Kondratiev Waves": "Kondratiev_Waves_Expert_Review.md",
    "LoAR": "LoAR_Expert_Review.md",
    "Technological Singularity": "Technological_Singularity_Expert_Review.md",
}

reports = []
for subj in SUBJECT_DIRECTORIES:
    subj_path = root / subj
    if subj_path.exists():
        for f in sorted(subj_path.rglob("*.md")):
            if f.name not in EXPERT_REVIEW_FILES.values() and not f.name.endswith("_Expert_Review.md"):
                reports.append(f)

master_synth = root / "Convergence_Master_Synthesis.md"
if master_synth.exists() and master_synth not in reports:
    reports.append(master_synth)

print(f"Total research reports in 5 core domains + synthesis: {len(reports)}")

depth_pass = 0
depth_fail = 0
ph_count = 0
broken_tag_count = 0
no_citation_count = 0
double_pipe_count = 0

placeholder_pats = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\[INSERT",
    r"INSERT_DATA",
    r"\[Insert",
    r"\bXXX\b",
    r"\bTEMP\b",
]

broken_tag_pats = [
    (r"\bregarding\s{2,}and\b", "regarding  and"),
    (r"\breveals\s+how\s{2,}evolves\b", "reveals how  evolves"),
    (r"\bhow\s{2,}evolves\b", "how  evolves"),
    (r"\btransitions\s+in\s+\.", "transitions in ."),
    (r"\bAntecedents\s+of\s*:\s*(?:\s*$|\.)", "Antecedents of: ."),
    (r"\|\s{2,}\|", "|  |"),
    (
        r"\{(?:topic|subject|domain|category|author|title|keyword|item|case_study|date|year|summary|description)\}",
        "{tag}",
    ),
    (
        r"\b(?:in|of|for|regarding|about|with)\s{2,}(?:\.|\,|and)(?=\s|$|\b)",
        "empty var omission",
    ),
    (r"<(?:INSERT|INSERT_DATA|TOPIC|SUBJECT|PARAM)>", "<INSERT>"),
    (
        r"\[(?:TOPIC|SUBJECT|DOMAIN|CATEGORY|VARIABLE|DATA)\]",
        "[TOPIC]",
    ),
]

citation_pats = [
    r"\([A-Z][a-zA-Z\s.,\x26\'-]+,\s*\d{4}\)",
    r"\[\d+\]",
    r"\[CIT-[A-Z0-9_-]+\]",
    r"^#{1,6}\s*(?:Academic\s+(&|and)\s+Historical\s+)?References\b",
    r"^#{1,6}\s*(?:[A-Za-z0-9\s\x26,\'\.\-]+\s+)?(?:References|Bibliography|Citations)\b",
    r"##\s+.*Sources?",
    r"##\s+.*Further Reading",
    r"https?://",
]

failing_depth_files = []
ph_files = []
broken_tag_files = []
no_citation_files = []
double_pipe_files = []

for r in reports:
    text = r.read_text(encoding="utf-8", errors="ignore")
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) >= 51:
        depth_pass += 1
    else:
        depth_fail += 1
        failing_depth_files.append((str(r.relative_to(root)), len(lines)))

    # Placeholders
    has_ph = False
    for pat in placeholder_pats:
        if re.search(pat, text, re.IGNORECASE):
            has_ph = True
            break
    if has_ph:
        ph_count += 1
        ph_files.append(str(r.relative_to(root)))

    # Broken tags
    has_bt = False
    for pat, desc in broken_tag_pats:
        if re.search(pat, text, re.IGNORECASE):
            has_bt = True
            break
    if has_bt:
        broken_tag_count += 1
        broken_tag_files.append(str(r.relative_to(root)))

    # Citations
    has_cit = False
    for pat in citation_pats:
        if re.search(pat, text, re.IGNORECASE | re.MULTILINE):
            has_cit = True
            break
    if not has_cit:
        no_citation_count += 1
        no_citation_files.append(str(r.relative_to(root)))

    # Double pipe in tables
    has_dp = False
    for l in text.splitlines():
        if "||" in l and "|" in l and "\\lambda" not in l:
            has_dp = True
            break
    if has_dp:
        double_pipe_count += 1
        double_pipe_files.append(str(r.relative_to(root)))

print(f"Depth Pass (>50 lines): {depth_pass}/{len(reports)}")
print(f"Depth Fail (<=50 lines): {depth_fail}")
print(f"Placeholders Found: {ph_count}")
print(f"Broken Template Tags Found: {broken_tag_count}")
print(f"Missing Citations: {no_citation_count}")
print(f"Double Pipe Table Alignment Corruptions: {double_pipe_count}")
if double_pipe_files:
    print(f"Files with Double Pipe Table Corruptions ({len(double_pipe_files)} files):")
    for f in double_pipe_files:
        print(f"  - {f}")
