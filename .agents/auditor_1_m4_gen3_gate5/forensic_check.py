import os
import pathlib
import collections
import re
import sys

REPO_ROOT = pathlib.Path("/Users/dylanboyle/Desktop/Convergence")

EXPERT_REVIEWS = [
    "4th Turning/4th_Turning_Expert_Review.md",
    "Changing World Orders/Changing_World_Orders_Expert_Review.md",
    "Kondratiev Waves/Kondratiev_Waves_Expert_Review.md",
    "LoAR/LoAR_Expert_Review.md",
    "Technological Singularity/Technological_Singularity_Expert_Review.md",
]

SUBJECT_DIRS = [
    "4th Turning",
    "Changing World Orders",
    "Kondratiev Waves",
    "LoAR",
    "Technological Singularity",
]

def run_forensic_audit():
    print("=== STARTING FORENSIC INTEGRITY AUDIT ===")
    violations = []
    warnings = []

    # 1. Expert Review Check
    print("\n--- 1. Expert Review Files Check ---")
    for er_rel in EXPERT_REVIEWS:
        p = REPO_ROOT / er_rel
        if not p.exists():
            violations.append(f"Missing expert review file: {er_rel}")
            print(f"FAIL: Missing {er_rel}")
        else:
            lines = [l for l in p.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
            print(f"PASS: {er_rel} exists with {len(lines)} non-blank lines.")
            if len(lines) <= 50:
                violations.append(f"Expert review file {er_rel} has <= 50 non-blank lines ({len(lines)})")

    # 2. Research Reports Depth & Count Check
    print("\n--- 2. Research Reports Depth & Count Check ---")
    reports = []
    for subj in SUBJECT_DIRS:
        subj_p = REPO_ROOT / subj
        if subj_p.exists():
            for r in sorted(subj_p.rglob("*.md")):
                if r.name not in [pathlib.Path(x).name for x in EXPERT_REVIEWS] and not r.name.endswith("_Expert_Review.md"):
                    reports.append(r)
    master_synth = REPO_ROOT / "Convergence_Master_Synthesis.md"
    if master_synth.exists() and master_synth not in reports:
        reports.append(master_synth)

    print(f"Total research reports found: {len(reports)}")
    if len(reports) < 144:
        violations.append(f"Expected at least 144 research reports, found {len(reports)}")

    depth_failures = 0
    for r in reports:
        rel_p = str(r.relative_to(REPO_ROOT))
        raw_content = r.read_text(encoding="utf-8", errors="ignore")
        raw_lines = raw_content.splitlines()
        non_blank_lines = [l for l in raw_lines if l.strip()]
        
        # Check for whitespace cheating (lines that only contain spaces/tabs/invisible characters)
        whitespace_only_lines = [l for l in raw_lines if len(l) > 0 and not l.strip()]
        invisible_char_lines = [l for l in raw_lines if re.search(r'[\u200b\u200c\u200d\ufeff\xa0]', l)]
        if invisible_char_lines:
            warnings.append(f"Invisible Unicode characters found in {rel_p}: {len(invisible_char_lines)} lines")

        if len(non_blank_lines) <= 50:
            depth_failures += 1
            violations.append(f"Report {rel_p} has {len(non_blank_lines)} non-blank lines (<= 50)")

    print(f"Report Depth Check: {len(reports) - depth_failures}/{len(reports)} reports > 50 non-blank lines.")

    # 3. Single-Report Internal Duplication & Filler Check
    print("\n--- 3. Single-Report Duplicate Lines & Filler Analysis ---")
    high_dup_reports = []
    for r in reports:
        rel_p = str(r.relative_to(REPO_ROOT))
        raw_lines = [l.strip() for l in r.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
        if not raw_lines:
            continue
        line_counts = collections.Counter(raw_lines)
        duplicated_lines_count = sum(c for line, c in line_counts.items() if c > 1)
        # Note: headers, blank lines, dividers can be repeated if common, but line-for-line duplication
        internal_dup_ratio = (duplicated_lines_count / len(raw_lines)) * 100.0
        
        if internal_dup_ratio >= 15.0:
            high_dup_reports.append((rel_p, internal_dup_ratio))
            violations.append(f"Single-report duplicate line ratio in {rel_p} is {internal_dup_ratio:.2f}% (>= 15.0%)")

    print(f"High single-report internal duplication count (>= 15%): {len(high_dup_reports)}")

    # 4. Cross-Report Duplication Analysis per Subject
    print("\n--- 4. Cross-Report Duplication Analysis per Subject Directory ---")
    for subj in SUBJECT_DIRS:
        subj_p = REPO_ROOT / subj
        if not subj_p.exists():
            continue
        subj_reports = [f for f in sorted(subj_p.rglob("*.md")) if f.name not in [pathlib.Path(x).name for x in EXPERT_REVIEWS] and not f.name.endswith("_Expert_Review.md")]
        
        file_lines = {}
        for sr in subj_reports:
            lines = [l.strip() for l in sr.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
            file_lines[sr] = lines
            
        all_lines_counter = collections.Counter(l for lines in file_lines.values() for l in lines)
        file_dup_rates = []
        for sr, lines in file_lines.items():
            if not lines:
                continue
            dup_c = sum(1 for l in lines if all_lines_counter[l] > 1)
            rate = (dup_c / len(lines)) * 100.0
            file_dup_rates.append(rate)
            
        avg_rate = sum(file_dup_rates) / len(file_dup_rates) if file_dup_rates else 0.0
        print(f"Subject '{subj}' ({len(subj_reports)} reports): avg cross-report duplication = {avg_rate:.2f}%")
        if avg_rate > 15.0:
            violations.append(f"Subject directory '{subj}' average cross-report duplication rate is {avg_rate:.2f}% (> 15.0%)")

    # 5. Template Integrity & Table Formatting Scan
    print("\n--- 5. Template Integrity & Table Formatting Check ---")
    template_artifacts = [
        (r"\bregarding\s{2,}and\b", "Double-space artifact: regarding  and"),
        (r"\breveals\s+how\s{2,}evolves\b", "Double-space artifact: reveals how  evolves"),
        (r"\bhow\s{2,}evolves\b", "Double-space artifact: how  evolves"),
        (r"\btransitions\s+in\s+\.", "Missing target variable: transitions in ."),
        (r"\bAntecedents\s+of\s*:\s*(?:\s*$|\.)", "Incomplete title colon: Antecedents of:"),
        (r"\|\s{2,}\|", "Empty table header column"),
        (r"\|{2,}", "Double-pipe table corruption: ||"),
        (r"\{(?:topic|subject|domain|category|author|title|keyword|item|case_study|date|year|summary|description)\}", "Unpopulated tag {...}"),
        (r"<(?:INSERT|INSERT_DATA|TOPIC|SUBJECT|PARAM)>", "Unpopulated bracket placeholder"),
        (r"\[(?:TOPIC|SUBJECT|DOMAIN|CATEGORY|VARIABLE|DATA|INSERT)\]", "Unpopulated square-bracket placeholder"),
        (r"\bTODO\b", "TODO tag"),
        (r"\bTBD\b", "TBD tag"),
        (r"\bFIXME\b", "FIXME tag"),
    ]

    template_violations_count = 0
    table_formatting_errors_count = 0

    for r in reports:
        rel_p = str(r.relative_to(REPO_ROOT))
        text = r.read_text(encoding="utf-8", errors="ignore")
        for pat, desc in template_artifacts:
            matches = re.findall(pat, text, re.IGNORECASE | re.MULTILINE)
            if matches:
                template_violations_count += len(matches)
                violations.append(f"Broken template pattern in {rel_p}: {desc} ({len(matches)} occurrences)")
                if "||" in desc or "table" in desc.lower():
                    table_formatting_errors_count += len(matches)

        # Check markdown table formatting syntax consistency
        table_lines = [l for l in text.splitlines() if l.strip().startswith("|")]
        for tl in table_lines:
            if "||" in tl:
                table_formatting_errors_count += 1
                violations.append(f"Table alignment error in {rel_p}: double pipe in line '{tl.strip()}'")

    print(f"Template integrity violations found: {template_violations_count}")
    print(f"Table formatting errors found: {table_formatting_errors_count}")

    print("\n=========================================")
    print(f"TOTAL VIOLATIONS DETECTED: {len(violations)}")
    print(f"TOTAL WARNINGS DETECTED: {len(warnings)}")
    print("=========================================")
    if violations:
        for v in violations:
            print(f"  🔴 {v}")
    else:
        print("  ✅ All forensic checks PASSED cleanly!")

if __name__ == "__main__":
    run_forensic_audit()
