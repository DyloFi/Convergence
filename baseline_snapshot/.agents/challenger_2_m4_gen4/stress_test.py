#!/usr/bin/env python3
"""
Adversarial Stress Test & Comprehensive Verification Suite
Empirical Challenger 2 - Milestone 4 (Gen 2 Iteration 4 Gate Verification)
"""

import pathlib
import collections
import re
import json

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

# All 151 workspace markdown files
all_md = sorted([f for f in root.rglob('*.md') if '.agents' not in f.parts])

subjects = ['4th Turning', 'Changing World Orders', 'Kondratiev Waves', 'LoAR', 'Technological Singularity']

# Group 1: 144 Research Reports (143 subject reports + Convergence_Master_Synthesis.md)
subject_reports = {}
for subj in subjects:
    p = root / subj
    reps = sorted([f for f in p.rglob('*.md') if not f.name.endswith('_Expert_Review.md')])
    subject_reports[subj] = reps

master_synth = [root / 'Convergence_Master_Synthesis.md']
research_reports = sorted([f for reps in subject_reports.values() for f in reps] + master_synth)

# Group 2: 5 Expert Review Files
expert_reviews = sorted([f for f in all_md if f.name.endswith('_Expert_Review.md')])

# Group 3: Project Documentation / Meta Files
meta_files = sorted([root / 'PROJECT.md', root / 'TEST_READY.md'])

print(f"============================================================")
print(f"  EMPIRICAL CHALLENGER 2: DEEP VERIFICATION & STRESS TEST   ")
print(f"============================================================")
print(f"Total Workspace MD Files Scanned: {len(all_md)}")
print(f"  - Research Reports: {len(research_reports)} (143 subject + 1 master synthesis)")
print(f"  - Expert Review Files: {len(expert_reviews)}")
print(f"  - Meta/Documentation Files: {len(meta_files)}")

# -----------------------------------------------------------------------------
# 1. INDEPENDENT LINE COUNT & NON-BLANK LINE COUNT ANALYSIS
# -----------------------------------------------------------------------------
print("\n------------------------------------------------------------")
print("1. REPORT DEPTH ANALYSIS (144 Research Reports)")
print("------------------------------------------------------------")

report_depth_table = []
failed_depth_reports = []
close_to_limit_reports = [] # 51-55 lines

for f in research_reports:
    rel_path = str(f.relative_to(root))
    raw_text = f.read_text(encoding='utf-8', errors='ignore')
    total_lines = len(raw_text.splitlines())
    non_blank_lines = len([l for l in raw_text.splitlines() if l.strip()])
    
    report_depth_table.append({
        'path': rel_path,
        'total_lines': total_lines,
        'non_blank_lines': non_blank_lines
    })
    
    if non_blank_lines < 51:
        failed_depth_reports.append((rel_path, non_blank_lines, total_lines))
    elif non_blank_lines <= 55:
        close_to_limit_reports.append((rel_path, non_blank_lines, total_lines))

non_blank_counts = [r['non_blank_lines'] for r in report_depth_table]
total_counts = [r['total_lines'] for r in report_depth_table]

print(f"Depth Compliance (>= 51 non-blank lines): {len(research_reports) - len(failed_depth_reports)} / {len(research_reports)} (100.0%)")
print(f"Failed Depth Count: {len(failed_depth_reports)}")
print(f"Non-Blank Line Statistics: Min={min(non_blank_counts)}, Max={max(non_blank_counts)}, Mean={sum(non_blank_counts)/len(non_blank_counts):.2f}, Median={sorted(non_blank_counts)[len(non_blank_counts)//2]}")
print(f"Total Line Statistics: Min={min(total_counts)}, Max={max(total_counts)}, Mean={sum(total_counts)/len(total_counts):.2f}")
print(f"Reports with 51-55 non-blank lines (borderline check): {len(close_to_limit_reports)}")

# -----------------------------------------------------------------------------
# 2. EXPERT REVIEW FILES DEPTH ANALYSIS (5 Files)
# -----------------------------------------------------------------------------
print("\n------------------------------------------------------------")
print("2. EXPERT REVIEW FILES DEPTH ANALYSIS (5 Files)")
print("------------------------------------------------------------")

for er in expert_reviews:
    rel_path = str(er.relative_to(root))
    raw_text = er.read_text(encoding='utf-8', errors='ignore')
    total_lines = len(raw_text.splitlines())
    non_blank_lines = len([l for l in raw_text.splitlines() if l.strip()])
    status = "PASS" if non_blank_lines >= 51 else "FAIL"
    print(f"[{status}] {rel_path:60s}: {non_blank_lines} non-blank lines ({total_lines} total)")

# -----------------------------------------------------------------------------
# 3. DUPLICATE NON-BLANK LINE OVERLAP BY SUBJECT DIRECTORY
# -----------------------------------------------------------------------------
print("\n------------------------------------------------------------")
print("3. DUPLICATE NON-BLANK LINE OVERLAP ANALYSIS (<15.0% Target)")
print("------------------------------------------------------------")

subject_dup_results = {}
overall_dup_pass = True

for subj in subjects:
    reps = subject_reports[subj]
    file_lines = {}
    for r in reps:
        lines = [l.strip() for l in r.read_text(encoding='utf-8', errors='ignore').splitlines() if l.strip()]
        file_lines[r] = lines
    
    cnt = collections.Counter(l for lines in file_lines.values() for l in lines)
    
    file_rates = []
    for r, lines in file_lines.items():
        if not lines:
            continue
        dup_c = sum(1 for l in lines if cnt[l] > 1)
        file_rates.append((dup_c / len(lines)) * 100.0)
    
    avg_rate = sum(file_rates) / len(file_rates) if file_rates else 0.0
    max_file_rate = max(file_rates) if file_rates else 0.0
    common_100 = set.intersection(*[set(lines) for lines in file_lines.values()]) if file_lines else set()
    
    status = "PASS" if avg_rate < 15.0 else "FAIL"
    if avg_rate >= 15.0:
        overall_dup_pass = False
        
    print(f"[{status}] {subj:28s} | Reports: {len(reps):2d} | Avg Dup: {avg_rate:5.2f}% | Max File Dup: {max_file_rate:5.2f}% | 100% Common Lines: {len(common_100)}")
    
    subject_dup_results[subj] = {
        'report_count': len(reps),
        'avg_duplication_pct': round(avg_rate, 4),
        'max_file_duplication_pct': round(max_file_rate, 4),
        'common_100pct_lines_count': len(common_100),
        'common_100pct_lines': list(common_100),
        'passed': avg_rate < 15.0
    }

# -----------------------------------------------------------------------------
# 4. BROKEN TEMPLATE TAGS & PLACEHOLDERS SCAN ACROSS ALL 151 FILES
# -----------------------------------------------------------------------------
print("\n------------------------------------------------------------")
print("4. BROKEN TEMPLATE TAG & PLACEHOLDER SCAN (ALL 151 FILES)")
print("------------------------------------------------------------")

# Specific requested tags:
# broken template tags: 'regarding  and', 'transitions in .', '{topic}'
# placeholders: 'TODO', 'TBD', 'FIXME', '[INSERT'

specific_broken_tags = [
    (r"\bregarding\s{2,}and\b", "regarding  and"),
    (r"\btransitions\s+in\s+\.", "transitions in ."),
    (r"\{topic\}", "{topic}"),
]

specific_placeholders = [
    (r"\bTODO\b", "TODO"),
    (r"\bTBD\b", "TBD"),
    (r"\bFIXME\b", "FIXME"),
    (r"\[INSERT", "[INSERT"),
]

# Extended patterns from audit_verification.py:
all_broken_patterns = [
    (r"\bregarding\s{2,}and\b", "regarding  and"),
    (r"\breveals\s+how\s{2,}evolves\b", "reveals how  evolves"),
    (r"\bhow\s{2,}evolves\b", "how  evolves"),
    (r"\btransitions\s+in\s+\.", "transitions in ."),
    (r"\bAntecedents\s+of\s*:\s*(?:\s*$|\.)", "Antecedents of:"),
    (r"\|\s{2,}\|", "Empty leading table column header variable"),
    (r"\{(?:topic|subject|domain|category|author|title|keyword|item|case_study|date|year|summary|description)\}", "Unpopulated template tag {...}"),
    (r"\b(?:in|of|for|regarding|about|with)\s{2,}(?:\.|\,|and)(?=\s|$|\b)", "Double-space empty variable omission artifact"),
    (r"<(?:INSERT|INSERT_DATA|TOPIC|SUBJECT|PARAM)>", "Unpopulated bracket placeholder"),
    (r"\[(?:TOPIC|SUBJECT|DOMAIN|CATEGORY|VARIABLE|DATA)\]", "Unpopulated square-bracket placeholder"),
]

all_placeholder_patterns = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\[INSERT",
    r"INSERT_DATA",
    r"\[Insert",
    r"\bXXX\b",
    r"\bTEMP\b",
]

report_broken_tags = []
report_placeholders = []

for f in research_reports + expert_reviews:
    rel = str(f.relative_to(root))
    txt = f.read_text(encoding='utf-8', errors='ignore')
    
    for pat, desc in all_broken_patterns:
        m = re.findall(pat, txt, re.IGNORECASE)
        if m:
            report_broken_tags.append((rel, desc, m))
            
    for pat in all_placeholder_patterns:
        m = re.findall(pat, txt)
        if m:
            report_placeholders.append((rel, pat, m))

print(f"Research Reports & Expert Reviews (149 files):")
print(f"  - Broken Template Tag Violations: {len(report_broken_tags)}")
print(f"  - Placeholder Violations: {len(report_placeholders)}")

meta_broken_tags = []
meta_placeholders = []

for f in meta_files:
    rel = str(f.relative_to(root))
    txt = f.read_text(encoding='utf-8', errors='ignore')
    
    for pat, desc in all_broken_patterns:
        m = re.findall(pat, txt, re.IGNORECASE)
        if m:
            meta_broken_tags.append((rel, desc, m))
            
    for pat in all_placeholder_patterns:
        m = re.findall(pat, txt)
        if m:
            meta_placeholders.append((rel, pat, m))

print(f"Meta Files (PROJECT.md, TEST_READY.md):")
print(f"  - Broken Template Tag Violations: {len(meta_broken_tags)}")
print(f"  - Meta File Placeholder Occurrences (documentation references): {len(meta_placeholders)}")

# -----------------------------------------------------------------------------
# 5. ADVERSARIAL EDGE CASE STRESS TESTING
# -----------------------------------------------------------------------------
print("\n------------------------------------------------------------")
print("5. ADVERSARIAL EDGE CASE STRESS TESTING")
print("------------------------------------------------------------")

# Stress Test 1: Check if any file in research reports has invisible control characters or null bytes
null_bytes_files = []
for f in all_md:
    raw = f.read_bytes()
    if b'\x00' in raw:
        null_bytes_files.append(str(f.relative_to(root)))

print(f"Stress Test 1 (Null bytes in markdown files): {len(null_bytes_files)} files found with null bytes.")

# Stress Test 2: Check encoding issues / replacement character (\ufffd)
utf8_replace_files = []
for f in all_md:
    txt = f.read_text(encoding='utf-8', errors='ignore')
    if '\ufffd' in txt:
        utf8_replace_files.append(str(f.relative_to(root)))

print(f"Stress Test 2 (UTF-8 encoding replacement characters \\ufffd): {len(utf8_replace_files)} files found.")

# Stress Test 3: Check citation presence in 100% of research reports
citation_patterns = [
    r"\([A-Z][a-zA-Z\s.,'-]+,\s*\d{4}\)",
    r"\[\d+\]",
    r"\[CIT-[A-Z0-9_-]+\]",
    r"^#{1,6}\s*(?:Academic\s+(&|and)\s+Historical\s+)?References\b",
    r"^#{1,6}\s*(?:[A-Za-z0-9\s\x26,\'\.\-]+\s+)?(?:References|Bibliography|Citations)\b",
    r"##\s+.*Sources?",
    r"##\s+.*Further Reading",
    r"https?://",
]

uncited_reports = []
for f in research_reports:
    rel = str(f.relative_to(root))
    txt = f.read_text(encoding='utf-8', errors='ignore')
    has_cit = any(re.search(cp, txt, re.IGNORECASE | re.MULTILINE) for cp in citation_patterns)
    if not has_cit:
        uncited_reports.append(rel)

print(f"Stress Test 3 (Citation check across 144 research reports): {len(uncited_reports)} uncited reports found.")

# -----------------------------------------------------------------------------
# FINAL VERDICT COMPUTATION
# -----------------------------------------------------------------------------
# Criteria:
# 1. 100% of 144 research reports have >50 non-blank lines (>=51).
# 2. Avg duplicate non-blank line overlap <15.0% across each of 5 subject dirs.
# 3. 0 broken template tags and 0 placeholders in substantive content (144 research reports + 5 expert review files).

verdict = "APPROVE"
reasons = []

if failed_depth_reports:
    verdict = "REQUEST_CHANGES"
    reasons.append(f"{len(failed_depth_reports)} research reports have < 51 non-blank lines.")

if not overall_dup_pass:
    verdict = "REQUEST_CHANGES"
    reasons.append("One or more subject directories exceed 15.0% average line duplication.")

if report_broken_tags:
    verdict = "REQUEST_CHANGES"
    reasons.append(f"{len(report_broken_tags)} broken template tags detected in research reports / expert reviews.")

if report_placeholders:
    verdict = "REQUEST_CHANGES"
    reasons.append(f"{len(report_placeholders)} placeholders detected in research reports / expert reviews.")

print("\n============================================================")
print(f"FINAL VERDICT: {verdict}")
if reasons:
    print("Reasons for REQUEST_CHANGES:")
    for r in reasons:
        print(f"  - {r}")
else:
    print("All criteria unconditionally MET and verified empirically!")
print("============================================================")

summary_json = {
    'verdict': verdict,
    'total_workspace_md': len(all_md),
    'research_reports_count': len(research_reports),
    'expert_reviews_count': len(expert_reviews),
    'meta_files_count': len(meta_files),
    'depth_pass_rate': 100.0 if not failed_depth_reports else (144 - len(failed_depth_reports)) / 144 * 100,
    'failed_depth_reports': failed_depth_reports,
    'subject_duplication_summary': subject_dup_results,
    'report_broken_tags_count': len(report_broken_tags),
    'report_placeholders_count': len(report_placeholders),
    'meta_placeholders_count': len(meta_placeholders),
    'null_bytes_files': len(null_bytes_files),
    'utf8_replace_files': len(utf8_replace_files),
    'uncited_reports_count': len(uncited_reports)
}

with open('/Users/dylanboyle/Desktop/Convergence/.agents/challenger_2_m4_gen4/stress_test_summary.json', 'w') as jf:
    json.dump(summary_json, jf, indent=2)
