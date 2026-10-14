import pathlib
import re
from collections import defaultdict

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

# Identify all markdown files in target workspace (excluding .agents/)
all_md_files = sorted([p for p in root.rglob('*.md') if '.agents' not in p.parts])

print(f"Total Markdown files found in workspace (excluding .agents/): {len(all_md_files)}")

EXPERT_REVIEWS = {
    "4th_Turning_Expert_Review.md",
    "Changing_World_Orders_Expert_Review.md",
    "Kondratiev_Waves_Expert_Review.md",
    "LoAR_Expert_Review.md",
    "Technological_Singularity_Expert_Review.md"
}

# 1. Classify files
expert_review_files = []
research_reports = []
other_files = []

for p in all_md_files:
    if p.name in EXPERT_REVIEWS:
        expert_review_files.append(p)
    elif p.name in ["PROJECT.md", "TEST_READY.md"]:
        other_files.append(p)
    else:
        research_reports.append(p)

print(f"Expert Review Files count: {len(expert_review_files)}")
print(f"Research Reports count: {len(research_reports)}")
print(f"Other Workspace Files count: {len(other_files)}")

# 2. Line count & Non-blank line count audit
file_stats = []
failed_depth_reports = []

for p in research_reports:
    lines = p.read_text(encoding='utf-8', errors='ignore').splitlines()
    non_blank = [l for l in lines if l.strip()]
    rel_path = str(p.relative_to(root))
    file_stats.append({
        "path": rel_path,
        "raw_lines": len(lines),
        "non_blank_lines": len(non_blank)
    })
    if len(non_blank) < 51: # > 50 non-blank lines
        failed_depth_reports.append((rel_path, len(lines), len(non_blank)))

print("\n--- LINE COUNT & DEPTH AUDIT SUMMARY ---")
print(f"Total Research Reports Audited: {len(research_reports)}")
print(f"Reports with >50 non-blank lines: {len(research_reports) - len(failed_depth_reports)}")
print(f"Reports with <=50 non-blank lines: {len(failed_depth_reports)}")

if failed_depth_reports:
    print("FAILED REPORTS:")
    for path, raw, nb in failed_depth_reports:
        print(f"  - {path}: raw={raw}, non_blank={nb}")

# Min, max, avg non-blank line count
non_blank_counts = [stat['non_blank_lines'] for stat in file_stats]
raw_counts = [stat['raw_lines'] for stat in file_stats]
print(f"Non-blank line count range: min={min(non_blank_counts)}, max={max(non_blank_counts)}, avg={sum(non_blank_counts)/len(non_blank_counts):.2f}")
print(f"Raw line count range: min={min(raw_counts)}, max={max(raw_counts)}, avg={sum(raw_counts)/len(raw_counts):.2f}")

# Check expert reviews depth as well
print("\n--- EXPERT REVIEWS DEPTH AUDIT ---")
for p in expert_review_files:
    lines = p.read_text(encoding='utf-8', errors='ignore').splitlines()
    non_blank = [l for l in lines if l.strip()]
    rel_path = str(p.relative_to(root))
    print(f"{rel_path}: raw_lines={len(lines)}, non_blank_lines={len(non_blank)}")

# 3. Placeholder string check across ALL markdown files
PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\[INSERT",
    r"INSERT_DATA",
    r"\[Insert",
    r"\bXXX\b",
    r"\bTEMP\b"
]

print("\n--- PLACEHOLDER CHECK ACROSS ALL MD FILES ---")
placeholders_found = defaultdict(list)
for p in all_md_files:
    content = p.read_text(encoding='utf-8', errors='ignore')
    rel_path = str(p.relative_to(root))
    for pat in PLACEHOLDER_PATTERNS:
        matches = re.findall(pat, content)
        if matches:
            placeholders_found[rel_path].extend(matches)

if placeholders_found:
    print(f"PLACEHOLDERS DETECTED IN {len(placeholders_found)} FILES:")
    for path, matches in placeholders_found.items():
        print(f"  - {path}: {matches}")
else:
    print("Zero placeholder strings found across all markdown files in workspace!")

# 4. Verbatim Appendix Repetition Scan in 4th Turning reports (54 reports)
turning_reports = [p for p in research_reports if p.parts[len(root.parts)] == '4th Turning']
print(f"\n--- 4TH TURNING APPENDIX / REPETITION SCAN ---")
print(f"4th Turning Reports count: {len(turning_reports)}")

# Extract 5-line chunk signatures across all 54 files to check for duplicate multiline blocks
chunk_to_files = defaultdict(set)
for p in turning_reports:
    rel_path = str(p.relative_to(root))
    lines = [l.strip() for l in p.read_text(encoding='utf-8', errors='ignore').splitlines() if l.strip()]
    for i in range(len(lines) - 4):
        chunk = "\n".join(lines[i:i+5])
        # Ignore very generic headings or list items if short, but 5 full lines is substantial
        if len(chunk) > 100:
            chunk_to_files[chunk].add(rel_path)

duplicated_chunks = {chunk: files for chunk, files in chunk_to_files.items() if len(files) > 1}
print(f"Substantial 5-line duplicated chunks found across 4th Turning reports: {len(duplicated_chunks)}")
if duplicated_chunks:
    print("Sample duplicate chunks:")
    for i, (chunk, files) in enumerate(list(duplicated_chunks.items())[:5]):
        print(f"--- Duplicate Chunk {i+1} (found in {len(files)} files) ---")
        print(f"Files: {sorted(list(files))}")
        print(f"Content preview: {repr(chunk[:150])}")
