#!/usr/bin/env python3
import pathlib
import re

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

domains = ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]

all_reports = []
for d in domains:
    dp = root / d
    for f in sorted(dp.rglob("*.md")):
        all_reports.append(f)

master = root / "Convergence_Master_Synthesis.md"
if master.exists():
    all_reports.append(master)

double_pipe_files = []
robotic_header_files = []

for r in all_reports:
    rel = str(r.relative_to(root))
    text = r.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()

    # Double pipe check
    if re.search(r"\|{2,}", text):
        double_pipe_files.append(rel)

    # Robotic header check
    file_hdr_count = 0
    for l in lines:
        if l.startswith("#") and ":" in l:
            # Check if text after colon contains repetitive doc title / monograph / deep dive suffix
            parts = l.split(":", 1)
            title_part = parts[1].strip()
            if any(term in title_part for term in ["Deep Dive", "Monograph", "Research Overview", "Framework", "Report", "Synthesis"]):
                file_hdr_count += 1
    if file_hdr_count >= 2: # 2 or more robotic headers in same file
        robotic_header_files.append((rel, file_hdr_count))

print(f"Total reports checked: {len(all_reports)}")
print(f"Files with double-pipe `||` markdown table syntax: {len(double_pipe_files)}")
for f in double_pipe_files:
    print(f"  - {f}")

print(f"\nFiles with robotic heading suffixes (2+ headers): {len(robotic_header_files)}")
for f, count in robotic_header_files:
    print(f"  - {f}: {count} headers")
