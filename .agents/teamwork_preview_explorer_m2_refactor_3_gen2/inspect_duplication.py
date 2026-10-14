#!/usr/bin/env python3
import pathlib
import collections

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

domains = ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]

file_lines_map = {}
for d in domains:
    dp = root / d
    for f in sorted(dp.rglob("*.md")):
        if f.name.endswith("_Expert_Review.md"): continue
        rel = str(f.relative_to(root))
        lines = [l.strip() for l in f.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
        file_lines_map[rel] = lines

# Let's check the reports with >15% duplication in detail
print("--- HIGH DUPLICATION REPORT INSPECTION ---")
high_dup = ["Kondratiev Waves/Data/Processed/JSON/JSON Deep Dive.md",
            "Changing World Orders/Foundations/00_Research_Plan.md",
            "Changing World Orders/Supporting_Materials/Supporting Materials Deep Dive.md"]

for rel in high_dup:
    lines = file_lines_map[rel]
    d = rel.split('/')[0]
    domain_reps = [r for r in file_lines_map if r.startswith(d)]
    d_counter = collections.Counter(l for r in domain_reps for l in file_lines_map[r])
    dup_lines = [l for l in lines if d_counter[l] > 1]
    print(f"\nFile: {rel}")
    print(f"Total lines: {len(lines)}, Duplicate lines in domain: {len(dup_lines)} ({len(dup_lines)/len(lines)*100:.2f}%)")
    print("Sample duplicate lines in this file:")
    for l in dup_lines[:10]:
        print(f"  - [{d_counter[l]}x] {l[:90]}")

# Let's inspect shared lines across domains (inter-domain)
print("\n--- INTER-DOMAIN SHARED LINES DETAILED INSPECTION ---")
domain_lines = {}
for d in domains:
    reps = [r for r in file_lines_map if r.startswith(d)]
    d_lines = collections.Counter(l for r in reps for l in file_lines_map[r])
    domain_lines[d] = set(d_lines.keys())

for i, d1 in enumerate(domains):
    for d2 in domains[i+1:]:
        shared = domain_lines[d1].intersection(domain_lines[d2])
        non_table_shared = [l for l in shared if not l.startswith('|') and not l.startswith('---') and len(l) > 10]
        if non_table_shared:
            print(f"\nShared non-table/text lines between '{d1}' and '{d2}': {len(non_table_shared)}")
            for l in non_table_shared[:10]:
                print(f"  - {l[:100]}")
