#!/usr/bin/env python3
import pathlib
import re
import collections
import json

root = pathlib.Path("/Users/dylanboyle/Desktop/Convergence")
subject_dirs = ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]
expert_files = [
    "4th_Turning_Expert_Review.md",
    "Changing_World_Orders_Expert_Review.md",
    "Kondratiev_Waves_Expert_Review.md",
    "LoAR_Expert_Review.md",
    "Technological_Singularity_Expert_Review.md"
]

all_md_files = []
for sd in subject_dirs:
    p = root / sd
    if p.exists():
        all_md_files.extend(sorted([f for f in p.rglob("*.md") if not f.name.endswith(".bak.md")]))

master_synth = root / "Convergence_Master_Synthesis.md"
if master_synth.exists():
    all_md_files.append(master_synth)

reports = [f for f in all_md_files if f.name not in expert_files and not f.name.endswith("_Expert_Review.md") and not f.name.endswith(".bak.md")]

print("=================================================================")
print("REVIEWER 2 INDEPENDENT AUDIT & RESEARCH QUALITY ASSESSMENT")
print("=================================================================")
print(f"Total markdown files found: {len(all_md_files)}")
print(f"Total research reports: {len(reports)}")

# 1. Double pipe check
double_pipe_files = []
for f in all_md_files:
    text = f.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    for idx, line in enumerate(lines, 1):
        if "||" in line and not line.strip().startswith("```"):
            double_pipe_files.append((str(f.relative_to(root)), idx, line))

print(f"\n1. Double-pipe || Delimiter Corruptions: {len(double_pipe_files)}")

# 2. Heading prose check
robotic_heading_files = []
heading_pattern = r"^#{1,6}\s+.*:\s*(?:\[Document Title\]|Topic Name\b|\[Topic\]|\[[A-Za-z0-9_\s]+\]|[A-Z0-9\s&,/\-\'\"]+(?:Deep Dive|Monograph|Overview|Synthesis|Framework|Guide|Taxonomy|Matrix|Legacy|Analysis|Research Plan))\s*$"
for f in reports:
    text = f.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("#") and ":" in line:
            if re.search(r":\s*\[", line) or re.search(heading_pattern, line):
                robotic_heading_files.append((str(f.relative_to(root)), idx, line))

print(f"2. Robotic Heading Title Suffixes in Research Reports: {len(robotic_heading_files)}")

# 2b. Suspicious or truncated titles
suspicious_titles = []
for f in reports:
    rel = str(f.relative_to(root))
    text = f.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if lines and lines[0].startswith("#"):
        title = lines[0]
        if "  " in title or re.search(r"\b(Theoretical|Structural|Methodological|Conceptual|Analytical|Empirical|Strategic)\s*$", title) or re.search(r"\b(of|and|in|for|with|about|&)\s*$", title):
            suspicious_titles.append((rel, title))

print(f"2b. Suspicious/Truncated Report Titles: {len(suspicious_titles)}")
for rel, title in suspicious_titles:
    print(f"    - {rel} -> {title}")

# 3. Double spaces between words in body text
double_space_words = []
for f in reports:
    rel = str(f.relative_to(root))
    text = f.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("```") or line.strip().startswith("|") or line.strip().startswith("┌") or line.strip().startswith("├") or line.strip().startswith("└"):
            continue
        matches = re.findall(r"\b[a-zA-Z0-9_-]+\s{2,}[a-zA-Z0-9_-]+\b", line)
        if matches:
            for m in matches:
                double_space_words.append((rel, idx, m, line.strip()[:80]))

print(f"\n3. Double-Space Word Pair Artifacts in Body Text: {len(double_space_words)}")
for item in double_space_words:
    print(f"    - {item[0]}:{item[1]} -> match: '{item[2]}' in line: {item[3]}")

# 4. Depth & Substance
depth_fails = []
line_stats = []
no_table_files = []
no_citation_files = []
no_hist_context_files = []

hist_words = ["history", "historical", "century", "decade", "war", "revolution", "era", "crisis", "saeculum", "dynasty", "empire", "k-wave", "kondratiev", "hegemony", "industrial", "turning", "antecedent", "period", "19th", "20th", "21st", "18th", "17th", "16th", "15th", "1945", "1929", "1971", "1914", "1848", "1789"]
citation_pats = [r"\([A-Z][a-zA-Z\s.,\'-]+,\s*\d{4}\)", r"\[\d+\]", r"\[CIT-[A-Z0-9_-]+\]", r"^#{1,6}\s*.*References\b", r"https?://"]

for f in reports:
    rel_path = str(f.relative_to(root))
    lines = f.read_text(encoding="utf-8", errors="ignore").splitlines()
    non_blank = [l for l in lines if l.strip()]
    line_stats.append((len(non_blank), len(lines), rel_path))
    
    if len(non_blank) < 51:
        depth_fails.append((rel_path, len(non_blank), len(lines)))
    
    text = "\n".join(lines)
    if "|" not in text:
        no_table_files.append(rel_path)
    
    has_cit = any(re.search(pat, text, re.IGNORECASE | re.MULTILINE) for pat in citation_pats)
    if not has_cit:
        no_citation_files.append(rel_path)
        
    has_hist = any(w in text.lower() for w in hist_words)
    if not has_hist:
        no_hist_context_files.append(rel_path)

min_lines = min(s[0] for s in line_stats)
max_lines = max(s[0] for s in line_stats)
avg_lines = sum(s[0] for s in line_stats) / len(line_stats)

print(f"\n4. Depth & Substance Audit across {len(reports)} research reports:")
print(f"   - Min non-blank lines: {min_lines}")
print(f"   - Max non-blank lines: {max_lines}")
print(f"   - Avg non-blank lines: {avg_lines:.1f}")
print(f"   - Reports failing >50 non-blank lines requirement: {len(depth_fails)}")
print(f"   - Reports lacking markdown tables/datasets: {len(no_table_files)}")
print(f"   - Reports lacking formal citations: {len(no_citation_files)}")
print(f"   - Reports lacking historical context: {len(no_hist_context_files)}")

# 5. Placeholders & Broken Template Tags
placeholders = [r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b", r"\[INSERT", r"INSERT_DATA", r"\[Insert", r"\bXXX\b", r"\bTEMP\b"]
placeholder_matches = []

for f in all_md_files:
    rel_path = str(f.relative_to(root))
    text = f.read_text(encoding="utf-8", errors="ignore")
    for pat in placeholders:
        m = re.findall(pat, text)
        if m:
            placeholder_matches.append((rel_path, pat, m))

print(f"\n5. Placeholder Text Scan (TODO, TBD, FIXME, [INSERT): {len(placeholder_matches)}")

print("\n=================================================================")
