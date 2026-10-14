#!/usr/bin/env python3
import pathlib
import re
import collections

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

domains = ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]

all_reports = []
for d in domains:
    dp = root / d
    for f in sorted(dp.rglob("*.md")):
        rel = str(f.relative_to(root))
        all_reports.append(f)

master = root / "Convergence_Master_Synthesis.md"
if master.exists():
    all_reports.append(master)

print(f"Total reports being scanned: {len(all_reports)}")

# 1. Double-pipe markdown table alignment syntax check
double_pipe_files = []
for r in all_reports:
    rel = str(r.relative_to(root))
    text = r.read_text(encoding="utf-8", errors="ignore")
    # Match || in table alignment lines or table headers
    matches = re.findall(r"\|{2,}", text)
    if matches:
        double_pipe_files.append((rel, len(matches)))

print(f"\n--- DOUBLE-PIPE `||` TABLE ALIGNMENT SYNTAX ARTIFACTS ---")
print(f"Total files containing `||`: {len(double_pipe_files)}")
for rel, count in double_pipe_files:
    print(f"  - {rel}: {count} occurrences")

# 2. Robotic Heading Suffix Check
robotic_heading_files = []
for r in all_reports:
    rel = str(r.relative_to(root))
    lines = r.read_text(encoding="utf-8", errors="ignore").splitlines()
    file_robotic_headers = []
    for idx, l in enumerate(lines):
        if l.startswith("#"):
            # Check if line contains colon followed by document title / topic name repeat
            # e.g., "## 1. ... : Core Concepts Deep Dive & Paradigm Mechanics Monograph"
            # or "## ... : 4th Turning ..."
            if re.search(r"^#{1,6}\s+.*:\s*(?:[A-Z0-9\s&,/\-\'\"]+Deep Dive|00_|01_|4th Turning|Changing World Orders|Kondratiev Waves|LoAR|Technological Singularity)", l):
                file_robotic_headers.append((idx+1, l))
            elif re.search(r"^#{1,6}\s+.*:\s+[A-Z][a-zA-Z0-9\s&,/\-\'\"]{10,}(Monograph|Deep Dive|Framework|Overview|Report)", l):
                file_robotic_headers.append((idx+1, l))

    if file_robotic_headers:
        robotic_heading_files.append((rel, len(file_robotic_headers), file_robotic_headers))

print(f"\n--- ROBOTIC HEADING SUFFIX ARTIFACTS ---")
print(f"Total files containing robotic heading suffixes: {len(robotic_heading_files)}")
for rel, count, hdrs in robotic_heading_files:
    print(f"\nFile: {rel} ({count} robotic headers)")
    for lno, hdr in hdrs[:5]:
        print(f"  L{lno}: {hdr}")

# 3. Check for specific double-pipe pattern details
print("\nSample double-pipe table lines:")
for rel, count in double_pipe_files[:5]:
    r = root / rel
    lines = r.read_text(encoding="utf-8", errors="ignore").splitlines()
    for idx, l in enumerate(lines):
        if "||" in l:
            print(f"  {rel} (L{idx+1}): {l[:90]}")
            break
