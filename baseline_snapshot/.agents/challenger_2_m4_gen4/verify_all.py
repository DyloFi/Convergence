#!/usr/bin/env python3
import pathlib
import collections
import re
import json

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

# All workspace markdown files (excluding .agents directory)
all_md = sorted([f for f in root.rglob('*.md') if '.agents' not in f.parts])

print(f"=== EMPIRICAL VERIFICATION HARNESS ===")
print(f"Total workspace markdown files found: {len(all_md)}")

# Categorization
subjects = ['4th Turning', 'Changing World Orders', 'Kondratiev Waves', 'LoAR', 'Technological Singularity']

subject_reports = {}
for subj in subjects:
    p = root / subj
    reps = sorted([f for f in p.rglob('*.md') if not f.name.endswith('_Expert_Review.md')])
    subject_reports[subj] = reps

expert_reviews = sorted([f for f in all_md if f.name.endswith('_Expert_Review.md')])
master_synth = [f for f in all_md if f.name == 'Convergence_Master_Synthesis.md']
other_root_md = sorted([f for f in all_md if f.parent == root and f.name not in ['Convergence_Master_Synthesis.md']])

# The 144 research reports = 143 subject reports + 1 master synthesis file
research_reports = []
for subj in subjects:
    research_reports.extend(subject_reports[subj])
research_reports.extend(master_synth)
research_reports = sorted(research_reports)

print(f"Research reports count: {len(research_reports)} (Expected: 144)")
print(f"Expert review files count: {len(expert_reviews)} (Expected: 5)")
print(f"Other root files: {len(other_root_md)} ({[f.name for f in other_root_md]})")
print(f"Total workspace md files: {len(all_md)} (Expected: 151)")

assert len(research_reports) == 144, f"Expected 144 research reports, got {len(research_reports)}"
assert len(all_md) == 151, f"Expected 151 workspace md files, got {len(all_md)}"

# 1. Line count and non-blank line count across all 144 research reports
report_stats = []
under_51_lines = []

for report in research_reports:
    rel_path = str(report.relative_to(root))
    raw_text = report.read_text(encoding='utf-8', errors='ignore')
    all_lines = raw_text.splitlines()
    total_line_count = len(all_lines)
    non_blank_lines = [l for l in all_lines if l.strip()]
    non_blank_count = len(non_blank_lines)
    
    report_stats.append({
        'path': rel_path,
        'total_lines': total_line_count,
        'non_blank_lines': non_blank_count
    })
    
    if non_blank_count < 51:
        under_51_lines.append((rel_path, non_blank_count))

print("\n--- TASK 2: REPORT DEPTH VERIFICATION (>50 non-blank lines, i.e. >=51) ---")
print(f"Reports with >= 51 non-blank lines: {len(research_reports) - len(under_51_lines)} / {len(research_reports)}")
print(f"Reports with < 51 non-blank lines: {len(under_51_lines)}")

if under_51_lines:
    print("FAILED DEPTH REPORTS:")
    for path, count in under_51_lines:
        print(f"  - {path}: {count} non-blank lines")
else:
    print("SUCCESS: 100% of 144 research reports have >= 51 non-blank lines.")

# Min/Max/Avg non-blank lines across 144 research reports
counts = [s['non_blank_lines'] for s in report_stats]
print(f"Line depth stats (non-blank): Min={min(counts)}, Max={max(counts)}, Avg={sum(counts)/len(counts):.2f}")

# 3. Duplicate non-blank line overlap calculation across EACH of the 5 subject directories
print("\n--- TASK 3: DUPLICATE NON-BLANK LINE OVERLAP (<15.0% per directory) ---")
dup_summary = {}
dup_failed = False

for subj in subjects:
    reps = subject_reports[subj]
    file_lines = {}
    for r in reps:
        lines = [l.strip() for l in r.read_text(encoding='utf-8', errors='ignore').splitlines() if l.strip()]
        file_lines[r] = lines
    
    cnt = collections.Counter(l for lines in file_lines.values() for l in lines)
    
    rates = []
    for r, lines in file_lines.items():
        if not lines:
            continue
        dup_c = sum(1 for l in lines if cnt[l] > 1)
        rates.append((dup_c / len(lines)) * 100.0)
    
    avg_rate = sum(rates) / len(rates) if rates else 0.0
    common_100 = set.intersection(*[set(lines) for lines in file_lines.values()]) if file_lines else set()
    
    status = "PASS" if avg_rate < 15.0 else "FAIL"
    if avg_rate >= 15.0:
        dup_failed = True
        
    print(f"[{status}] {subj:28s}: {avg_rate:5.2f}% avg duplication | 100% common lines: {len(common_100)}")
    dup_summary[subj] = {
        'avg_rate': avg_rate,
        'common_100_count': len(common_100),
        'status': status
    }

# 4. Broken template tags and placeholders across all 151 workspace markdown files
print("\n--- TASK 4: BROKEN TEMPLATE TAG & PLACEHOLDER SCAN (ALL 151 FILES) ---")

placeholders = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\[INSERT",
    r"INSERT_DATA",
    r"\[Insert",
    r"\bXXX\b",
    r"\bTEMP\b",
]

broken_templates = [
    (r"\bregarding\s{2,}and\b", "Double-space variable artifact: 'regarding  and'"),
    (r"\breveals\s+how\s{2,}evolves\b", "Double-space variable artifact: 'reveals how  evolves'"),
    (r"\bhow\s{2,}evolves\b", "Double-space variable artifact: 'how  evolves'"),
    (r"\btransitions\s+in\s+\.", "Missing target variable before period: 'transitions in .'"),
    (r"\bAntecedents\s+of\s*:\s*(?:\s*$|\.)", "Incomplete title colon artifact: 'Antecedents of:'"),
    (r"\|\s{2,}\|", "Empty leading table column header variable"),
    (r"\{(?:topic|subject|domain|category|author|title|keyword|item|case_study|date|year|summary|description)\}", "Unpopulated template tag '{...}'"),
    (r"\{topic\}", "Specific unpopulated template tag '{topic}'"),
    (r"\b(?:in|of|for|regarding|about|with)\s{2,}(?:\.|\,|and)(?=\s|$|\b)", "Double-space empty variable omission artifact"),
    (r"<(?:INSERT|INSERT_DATA|TOPIC|SUBJECT|PARAM)>", "Unpopulated bracket placeholder"),
    (r"\[(?:TOPIC|SUBJECT|DOMAIN|CATEGORY|VARIABLE|DATA)\]", "Unpopulated square-bracket placeholder"),
]

placeholder_findings = []
broken_tag_findings = []

for f in all_md:
    rel_path = str(f.relative_to(root))
    text = f.read_text(encoding='utf-8', errors='ignore')
    
    # Check placeholders
    for p_pat in placeholders:
        matches = re.findall(p_pat, text)
        if matches:
            placeholder_findings.append((rel_path, p_pat, matches))
            
    # Check broken templates
    for bt_pat, desc in broken_templates:
        matches = re.findall(bt_pat, text, re.IGNORECASE)
        if matches:
            broken_tag_findings.append((rel_path, desc, matches))

print(f"Total placeholder violations found across 151 files: {len(placeholder_findings)}")
if placeholder_findings:
    for rel_path, pat, matches in placeholder_findings:
        print(f"  - {rel_path}: pattern '{pat}' matched {matches}")
else:
    print("SUCCESS: 0 placeholders found across all 151 files.")

print(f"Total broken template tag violations found across 151 files: {len(broken_tag_findings)}")
if broken_tag_findings:
    for rel_path, desc, matches in broken_tag_findings:
        print(f"  - {rel_path}: '{desc}' matched {matches}")
else:
    print("SUCCESS: 0 broken template tags found across all 151 files.")

# Aggregate Verdict
verdict = "APPROVE" if (not under_51_lines and not dup_failed and not placeholder_findings and not broken_tag_findings) else "REQUEST_CHANGES"

print(f"\n==========================================")
print(f"FINAL CHALLENGER VERDICT: {verdict}")
print(f"==========================================")

# Save JSON results for easy reference
results_payload = {
    'total_workspace_md_files': len(all_md),
    'research_reports_count': len(research_reports),
    'expert_reviews_count': len(expert_reviews),
    'under_51_lines_count': len(under_51_lines),
    'under_51_lines_list': under_51_lines,
    'dup_summary': dup_summary,
    'placeholder_findings_count': len(placeholder_findings),
    'broken_tag_findings_count': len(broken_tag_findings),
    'verdict': verdict
}

with open('/Users/dylanboyle/Desktop/Convergence/.agents/challenger_2_m4_gen4/verification_results.json', 'w') as jf:
    json.dump(results_payload, jf, indent=2)
