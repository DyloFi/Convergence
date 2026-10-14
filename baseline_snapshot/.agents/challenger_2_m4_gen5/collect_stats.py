#!/usr/bin/env python3
import pathlib
import re
import collections
import statistics

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

EXPERT_REVIEW_FILES = [
    '4th Turning/4th_Turning_Expert_Review.md',
    'Changing World Orders/Changing_World_Orders_Expert_Review.md',
    'Kondratiev Waves/Kondratiev_Waves_Expert_Review.md',
    'LoAR/LoAR_Expert_Review.md',
    'Technological Singularity/Technological_Singularity_Expert_Review.md',
]

subject_dirs = ['4th Turning', 'Changing World Orders', 'Kondratiev Waves', 'LoAR', 'Technological Singularity']

# Collect 144 research reports
research_reports = []
for sd in subject_dirs:
    p = root / sd
    if p.exists():
        for f in sorted(p.rglob('*.md')):
            if not f.name.endswith('_Expert_Review.md'):
                research_reports.append(f)

master_synth = root / 'Convergence_Master_Synthesis.md'
if master_synth.exists():
    research_reports.append(master_synth)

expert_files = [root / ef for ef in EXPERT_REVIEW_FILES]

def get_lines(path, non_blank_only=True):
    text = path.read_text(encoding='utf-8', errors='ignore')
    lines = text.splitlines()
    if non_blank_only:
        return [l for l in lines if l.strip()]
    return lines

# 1. Line counts distribution
res_lines_raw = [len(get_lines(f, non_blank_only=False)) for f in research_reports]
res_lines_nb = [len(get_lines(f, non_blank_only=True)) for f in research_reports]

exp_lines_raw = [len(get_lines(f, non_blank_only=False)) for f in expert_files]
exp_lines_nb = [len(get_lines(f, non_blank_only=True)) for f in expert_files]

res_pct_gt50_nb = sum(1 for c in res_lines_nb if c > 50) / len(res_lines_nb) * 100
exp_pct_gt50_nb = sum(1 for c in exp_lines_nb if c > 50) / len(exp_lines_nb) * 100

res_pct_gt50_raw = sum(1 for c in res_lines_raw if c > 50) / len(res_lines_raw) * 100
exp_pct_gt50_raw = sum(1 for c in exp_lines_raw if c > 50) / len(exp_lines_raw) * 100

print("=== 1. LINE COUNT DISTRIBUTION ===")
print("RESEARCH REPORTS (144 files):")
print(f"  Non-blank lines: Min={min(res_lines_nb)}, Max={max(res_lines_nb)}, Mean={statistics.mean(res_lines_nb):.2f}, Median={statistics.median(res_lines_nb):.2f}, % >50 lines={res_pct_gt50_nb:.2f}%")
print(f"  Raw total lines: Min={min(res_lines_raw)}, Max={max(res_lines_raw)}, Mean={statistics.mean(res_lines_raw):.2f}, Median={statistics.median(res_lines_raw):.2f}, % >50 lines={res_pct_gt50_raw:.2f}%")

print("\nEXPERT REVIEW FILES (5 files):")
print(f"  Non-blank lines: Min={min(exp_lines_nb)}, Max={max(exp_lines_nb)}, Mean={statistics.mean(exp_lines_nb):.2f}, Median={statistics.median(exp_lines_nb):.2f}, % >50 lines={exp_pct_gt50_nb:.2f}%")
print(f"  Raw total lines: Min={min(exp_lines_raw)}, Max={max(exp_lines_raw)}, Mean={statistics.mean(exp_lines_raw):.2f}, Median={statistics.median(exp_lines_raw):.2f}, % >50 lines={exp_pct_gt50_raw:.2f}%")

# 2. Duplicate line overlap percentage
def analyze_duplication(file_list):
    file_trimmed_lines = {}
    for f in file_list:
        lines = [l.strip() for l in get_lines(f, non_blank_only=True)]
        file_trimmed_lines[f] = lines
    
    # Counter across all files in list
    all_counter = collections.Counter(l for lines in file_trimmed_lines.values() for l in lines)
    
    cross_dup_rates = []
    internal_dup_rates = []
    
    for f, lines in file_trimmed_lines.items():
        if not lines:
            continue
        # cross dup: line appears > 1 in all_counter across files in group
        cross_dups = sum(1 for l in lines if all_counter[l] > 1)
        cross_rate = (cross_dups / len(lines)) * 100.0
        cross_dup_rates.append(cross_rate)
        
        # internal dup: line appears > 1 within this file's own lines
        self_counter = collections.Counter(lines)
        internal_dups = sum(1 for l in lines if self_counter[l] > 1)
        internal_rate = (internal_dups / len(lines)) * 100.0
        internal_dup_rates.append(internal_rate)
        
    return cross_dup_rates, internal_dup_rates

res_cross_rates, res_int_rates = analyze_duplication(research_reports)
exp_cross_rates, exp_int_rates = analyze_duplication(expert_files)

# Per-subject directory cross-file duplication analysis
subj_dup_stats = {}
for sd in subject_dirs:
    p = root / sd
    s_reports = [f for f in sorted(p.rglob('*.md')) if not f.name.endswith('_Expert_Review.md')]
    c_rates, i_rates = analyze_duplication(s_reports)
    subj_dup_stats[sd] = {
        'count': len(s_reports),
        'mean_cross': statistics.mean(c_rates),
        'max_cross': max(c_rates),
        'min_cross': min(c_rates),
        'mean_int': statistics.mean(i_rates),
        'max_int': max(i_rates),
    }

print("\n=== 2. DUPLICATE LINE OVERLAP PERCENTAGE ===")
print("RESEARCH REPORTS GLOBAL (144 files):")
print(f"  Cross-File Duplication Rate: Min={min(res_cross_rates):.2f}%, Max={max(res_cross_rates):.2f}%, Mean={statistics.mean(res_cross_rates):.2f}%")
print(f"  Internal Duplication Rate:   Min={min(res_int_rates):.2f}%, Max={max(res_int_rates):.2f}%, Mean={statistics.mean(res_int_rates):.2f}%")

print("\nRESEARCH REPORTS BY SUBJECT DIRECTORY:")
for sd, sstat in subj_dup_stats.items():
    print(f"  {sd} ({sstat['count']} reports): Cross Mean={sstat['mean_cross']:.2f}% (Max={sstat['max_cross']:.2f}%), Internal Mean={sstat['mean_int']:.2f}% (Max={sstat['max_int']:.2f}%)")

print("\nEXPERT REVIEW FILES (5 files):")
print(f"  Cross-File Duplication Rate: Min={min(exp_cross_rates):.2f}%, Max={max(exp_cross_rates):.2f}%, Mean={statistics.mean(exp_cross_rates):.2f}%")
print(f"  Internal Duplication Rate:   Min={min(exp_int_rates):.2f}%, Max={max(exp_int_rates):.2f}%, Mean={statistics.mean(exp_int_rates):.2f}%")
