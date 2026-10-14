#!/usr/bin/env python3
import pathlib
import re
import collections
import json

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

domains = ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]

# Collect all markdown files
all_files = []
domain_files = collections.defaultdict(list)

for d in domains:
    dp = root / d
    for f in sorted(dp.rglob("*.md")):
        rel = str(f.relative_to(root))
        if f.name.endswith("_Expert_Review.md"):
            domain_files[d + " (Review)"].append(f)
        else:
            domain_files[d].append(f)
        all_files.append(f)

master = root / "Convergence_Master_Synthesis.md"
if master.exists():
    all_files.append(master)
    domain_files["Master"].append(master)

print(f"Total markdown files found: {len(all_files)}")

# 1. Line depth scan
depth_summary = {}
under_51 = []
under_60 = []

for f in all_files:
    rel = str(f.relative_to(root))
    text = f.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    non_blank = [l for l in lines if l.strip()]
    count = len(non_blank)
    if count < 51:
        under_51.append((rel, count))
    if count < 60:
        under_60.append((rel, count))
    depth_summary[rel] = count

print(f"\n--- LINE DEPTH ANALYSIS ---")
print(f"Files under 51 non-blank lines: {len(under_51)}")
print(f"Files under 60 non-blank lines: {len(under_60)}")
for rel, count in under_60:
    print(f"  {rel}: {count} non-blank lines")

# 2. Template Integrity Scan
BROKEN_TEMPLATE_PATTERNS = [
    (r"\bregarding\s{2,}and\b", "Double-space variable artifact: 'regarding  and'"),
    (r"\breveals\s+how\s{2,}evolves\b", "Double-space variable artifact: 'reveals how  evolves'"),
    (r"\bhow\s{2,}evolves\b", "Double-space variable artifact: 'how  evolves'"),
    (r"\btransitions\s+in\s+\.", "Missing target variable before period: 'transitions in .'"),
    (r"\bAntecedents\s+of\s*:\s*(?:\s*$|\.)", "Incomplete title colon artifact: 'Antecedents of:'"),
    (r"\|\s{2,}\|", "Empty leading table column header variable"),
    (r"\{(?:topic|subject|domain|category|author|title|keyword|item|case_study|date|year|summary|description)\}", "Unpopulated template tag '{...}'"),
    (r"\b(?:in|of|for|regarding|about|with)\s{2,}(?:\.|\,|and)(?=\s|$|\b)", "Double-space empty variable omission artifact"),
    (r"<(?:INSERT|INSERT_DATA|TOPIC|SUBJECT|PARAM)>", "Unpopulated bracket placeholder"),
    (r"\[(?:TOPIC|SUBJECT|DOMAIN|CATEGORY|VARIABLE|DATA)\]", "Unpopulated square-bracket placeholder"),
]

# Extended template checks
EXTENDED_PATTERNS = [
    (r"\{[a-zA-Z0-9_]+\}", "Any generic single curly brace tag {tag}"),
    (r"\[[A-Z_]{3,}\]", "Any uppercase bracket placeholder like [TAG]"),
    (r"<(?:[A-Z_]{3,})>", "Any uppercase angle bracket placeholder like <TAG>"),
    (r"\b[a-z]+\s{2,}[a-z]+\b", "Any double space between lowercase words"),
    (r"\s+\.\s+", "Isolated period surrounded by whitespace"),
    (r":\s*\.", "Colon immediately followed by period"),
    (r"\bTODO\b|\bTBD\b|\bFIXME\b|\[INSERT|INSERT_DATA|\[Insert|\bXXX\b|\bTEMP\b", "Standard placeholders"),
]

print(f"\n--- TEMPLATE INTEGRITY SCAN (Standard Patterns) ---")
template_issues = []
for f in all_files:
    rel = str(f.relative_to(root))
    text = f.read_text(encoding="utf-8", errors="ignore")
    for pat, desc in BROKEN_TEMPLATE_PATTERNS:
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            template_issues.append((rel, desc, len(matches), matches[:3]))

print(f"Standard template issues count: {len(template_issues)}")
for item in template_issues:
    print(f"  {item[0]}: {item[1]} (count: {item[2]}) -> {item[3]}")

print(f"\n--- EXTENDED TEMPLATE INTEGRITY SCAN ---")
ext_issues = []
for f in all_files:
    rel = str(f.relative_to(root))
    text = f.read_text(encoding="utf-8", errors="ignore")
    for pat, desc in EXTENDED_PATTERNS:
        matches = re.findall(pat, text)
        if matches:
            # Filter out reasonable markdown/math/code constructs if needed
            ext_issues.append((rel, desc, len(matches), matches[:3]))

print(f"Extended template issues count: {len(ext_issues)}")
# Group by description
ext_by_desc = collections.defaultdict(list)
for rel, desc, count, samples in ext_issues:
    ext_by_desc[desc].append((rel, count, samples))

for desc, items in ext_by_desc.items():
    print(f"  Pattern '{desc}': found in {len(items)} files")
    for rel, count, samples in items[:3]:
        print(f"    - {rel}: {count} matches, e.g. {samples}")

# 3. Line Duplication Analysis
# A) Intra-domain duplication
print(f"\n--- CROSS-REPORT DUPLICATION (Intra-Domain & Inter-Domain) ---")

domain_reports = {}
for d in domains:
    dp = root / d
    reports = [f for f in sorted(dp.rglob("*.md")) if not f.name.endswith("_Expert_Review.md")]
    domain_reports[d] = reports

all_research_reports = []
for d, r_list in domain_reports.items():
    all_research_reports.extend(r_list)

file_lines_map = {}
for r in all_research_reports:
    rel = str(r.relative_to(root))
    lines = [l.strip() for l in r.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
    file_lines_map[rel] = lines

# Intra-domain rates (using current audit_verification logic)
print("Intra-domain duplication rates (audit_verification logic):")
for d in domains:
    reps = [str(r.relative_to(root)) for r in domain_reports[d]]
    fl = {r: file_lines_map[r] for r in reps}
    counter = collections.Counter(l for lines in fl.values() for l in lines)
    rates = []
    for r, lines in fl.items():
        if not lines: continue
        dups = sum(1 for l in lines if counter[l] > 1)
        rates.append((dups / len(lines)) * 100.0)
    avg_rate = sum(rates) / len(rates) if rates else 0
    max_rate = max(rates) if rates else 0
    min_rate = min(rates) if rates else 0
    print(f"  {d} ({len(reps)} reports): avg={avg_rate:.2f}%, min={min_rate:.2f}%, max={max_rate:.2f}%")

# B) Inter-domain (Cross-Folder) Duplication Rate
repo_counter = collections.Counter(l for lines in file_lines_map.values() for l in lines)

print("\nInter-domain / Repo-wide duplication rates:")
repo_rates = {}
for rel, lines in file_lines_map.items():
    if not lines: continue
    dups = sum(1 for l in lines if repo_counter[l] > 1)
    rate = (dups / len(lines)) * 100.0
    repo_rates[rel] = rate

avg_repo_rate = sum(repo_rates.values()) / len(repo_rates)
max_repo_file = max(repo_rates.items(), key=lambda x: x[1])
min_repo_file = min(repo_rates.items(), key=lambda x: x[1])
print(f"  Repo-wide average duplication rate across all 143 research reports: {avg_repo_rate:.2f}%")
print(f"  Max duplicated report: {max_repo_file[0]} ({max_repo_file[1]:.2f}%)")
print(f"  Min duplicated report: {min_repo_file[0]} ({min_repo_file[1]:.2f}%)")

# Let's check reports with repo-wide duplication rate > 15%
high_dup_repo = [(r, rate) for r, rate in repo_rates.items() if rate > 15.0]
print(f"  Number of reports with repo-wide line duplication > 15.0%: {len(high_dup_repo)}")
for r, rate in sorted(high_dup_repo, key=lambda x: x[1], reverse=True)[:10]:
    print(f"    - {r}: {rate:.2f}%")

# Most common repeated lines across the repo
print("\nTop 20 most frequent lines across all 143 research reports:")
for line, count in repo_counter.most_common(20):
    print(f"  [{count} files] {line[:80]}")

# Cross-domain pair overlap matrix
print("\nCross-Domain Pair Line Sharing Matrix:")
domain_lines_set = {}
for d in domains:
    reps = [str(r.relative_to(root)) for r in domain_reports[d]]
    d_lines = set(l for r in reps for l in file_lines_map[r])
    domain_lines_set[d] = d_lines

for i, d1 in enumerate(domains):
    for d2 in domains[i+1:]:
        shared = domain_lines_set[d1].intersection(domain_lines_set[d2])
        print(f"  Shared unique lines between '{d1}' and '{d2}': {len(shared)} lines")
