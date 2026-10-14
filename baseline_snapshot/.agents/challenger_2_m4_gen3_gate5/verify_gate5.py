#!/usr/bin/env python3
import os
import re
import glob
import json
import pathlib
import collections
from typing import Dict, List, Any

BASE_DIR = pathlib.Path("/Users/dylanboyle/Desktop/Convergence").resolve()

DOMAIN_DIRS = [
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

def scan_repository():
    reports_per_domain = {}
    all_reports = []
    
    # Gather reports per domain
    for domain in DOMAIN_DIRS:
        domain_path = BASE_DIR / domain
        reports = []
        for p in sorted(domain_path.rglob("*.md")):
            if p.name in EXPERT_REVIEW_FILES.values() or p.name.endswith("_Expert_Review.md"):
                continue
            reports.append(p)
        reports_per_domain[domain] = reports
        all_reports.extend(reports)
        
    master_synth = BASE_DIR / "Convergence_Master_Synthesis.md"
    if master_synth.exists():
        all_reports.append(master_synth)
        reports_per_domain["Master Synthesis"] = [master_synth]

    # Verify expert reviews
    expert_reviews_status = {}
    for domain, filename in EXPERT_REVIEW_FILES.items():
        p1 = BASE_DIR / domain / filename
        p2 = BASE_DIR / filename
        target = p1 if p1.exists() else (p2 if p2.exists() else None)
        if target and target.exists():
            lines = [l for l in target.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
            expert_reviews_status[domain] = {
                "exists": True,
                "path": str(target.relative_to(BASE_DIR)),
                "line_count": len(lines)
            }
        else:
            expert_reviews_status[domain] = {"exists": False, "path": None, "line_count": 0}

    # 1. Total Report Count
    total_report_count = len(all_reports)

    # 2. Line Count Distribution
    file_line_counts = []
    line_counts_per_domain = {domain: [] for domain in list(DOMAIN_DIRS) + ["Master Synthesis"]}
    reports_under_50 = []

    for r in all_reports:
        text = r.read_text(encoding="utf-8", errors="ignore")
        raw_lines = text.splitlines()
        non_blank_lines = [l for l in raw_lines if l.strip()]
        count = len(non_blank_lines)
        rel_path = str(r.relative_to(BASE_DIR))
        
        file_line_counts.append((rel_path, count, len(raw_lines)))
        
        domain_key = "Master Synthesis"
        for d in DOMAIN_DIRS:
            if rel_path.startswith(d + "/") or rel_path.startswith(d + "\\"):
                domain_key = d
                break
        line_counts_per_domain[domain_key].append(count)

        if count <= 50:
            reports_under_50.append((rel_path, count))

    # 3. Single-Report Duplicate Line Percentages per Domain Directory
    duplication_by_domain = {}
    all_single_report_dup_rates = []

    for domain in DOMAIN_DIRS:
        domain_reports = reports_per_domain[domain]
        domain_file_lines = {}
        for r in domain_reports:
            lines = [l.strip() for l in r.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
            domain_file_lines[r] = lines

        # Line frequency in domain
        counter = collections.Counter(l for lines in domain_file_lines.values() for l in lines)

        single_report_rates = {}
        for r, lines in domain_file_lines.items():
            if not lines:
                rate = 0.0
            else:
                dup_c = sum(1 for l in lines if counter[l] > 1)
                rate = (dup_c / len(lines)) * 100.0
            rel_p = str(r.relative_to(BASE_DIR))
            single_report_rates[rel_p] = rate
            all_single_report_dup_rates.append((rel_p, rate))

        rates_list = list(single_report_rates.values())
        max_rate = max(rates_list) if rates_list else 0.0
        avg_rate = sum(rates_list) / len(rates_list) if rates_list else 0.0
        min_rate = min(rates_list) if rates_list else 0.0

        duplication_by_domain[domain] = {
            "report_count": len(domain_reports),
            "max_single_dup_rate": round(max_rate, 4),
            "avg_dup_rate": round(avg_rate, 4),
            "min_single_dup_rate": round(min_rate, 4),
            "pass_max_under_15": max_rate < 15.0,
            "single_report_rates": {k: round(v, 4) for k, v in single_report_rates.items()}
        }

    # 4. Double-pipe `||` table syntax error count
    double_pipe_matches = []
    for r in all_reports:
        rel_path = str(r.relative_to(BASE_DIR))
        text = r.read_text(encoding="utf-8", errors="ignore")
        matches = re.findall(r"\|{2,}", text)
        if matches:
            double_pipe_matches.append((rel_path, len(matches)))

    # 5. Broken template slot count (`regarding  and` pattern)
    broken_template_matches = []
    for r in all_reports:
        rel_path = str(r.relative_to(BASE_DIR))
        text = r.read_text(encoding="utf-8", errors="ignore")
        matches = re.findall(r"\bregarding\s{2,}and\b", text, re.IGNORECASE)
        if matches:
            broken_template_matches.append((rel_path, len(matches)))

    # 6. Placeholder string count (`TODO`, `TBD`, `FIXME`)
    placeholder_matches = []
    for r in all_reports:
        rel_path = str(r.relative_to(BASE_DIR))
        text = r.read_text(encoding="utf-8", errors="ignore")
        found = []
        for pat in [r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b"]:
            m = re.findall(pat, text)
            if m:
                found.extend(m)
        if found:
            placeholder_matches.append((rel_path, found))

    results = {
        "expert_reviews": expert_reviews_status,
        "total_report_count": total_report_count,
        "total_report_count_verified_144": total_report_count == 144,
        "line_count_stats": {
            "total_reports": total_report_count,
            "reports_under_50_lines": len(reports_under_50),
            "pass_100pct_over_50_lines": len(reports_under_50) == 0,
            "min_lines": min([c[1] for c in file_line_counts]),
            "max_lines": max([c[1] for c in file_line_counts]),
            "avg_lines": round(sum([c[1] for c in file_line_counts]) / len(file_line_counts), 2),
            "by_domain": {
                d: {
                    "count": len(line_counts_per_domain[d]),
                    "min": min(line_counts_per_domain[d]) if line_counts_per_domain[d] else 0,
                    "max": max(line_counts_per_domain[d]) if line_counts_per_domain[d] else 0,
                    "avg": round(sum(line_counts_per_domain[d]) / len(line_counts_per_domain[d]), 2) if line_counts_per_domain[d] else 0,
                } for d in line_counts_per_domain
            }
        },
        "duplication_stats": duplication_by_domain,
        "all_domains_pass_max_dup_under_15": all(d["pass_max_under_15"] for d in duplication_by_domain.values()),
        "double_pipe_error_count": sum(c[1] for c in double_pipe_matches),
        "double_pipe_matches": double_pipe_matches,
        "double_pipe_pass_zero": sum(c[1] for c in double_pipe_matches) == 0,
        "broken_template_slot_count": sum(c[1] for c in broken_template_matches),
        "broken_template_matches": broken_template_matches,
        "broken_template_pass_zero": sum(c[1] for c in broken_template_matches) == 0,
        "placeholder_count": sum(len(f[1]) for f in placeholder_matches),
        "placeholder_matches": placeholder_matches,
        "placeholder_pass_zero": sum(len(f[1]) for f in placeholder_matches) == 0,
    }

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    scan_repository()
