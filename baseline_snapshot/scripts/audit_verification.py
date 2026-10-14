#!/usr/bin/env python3
"""
Convergence Repository Automated Audit & Verification Script
Requirement R3: Verifies expert review files, enhancement integration, and >50 line depth.

Supported CLI Options:
  --json      Output full audit results in JSON format
  --verbose   Output verbose line-by-line / file-by-file log messages
  --strict    Enforce strict citation and enhancement checks on all reports
  --root DIR  Specify alternative repository root directory (default: parent of script)
"""

import argparse
import collections
import json
import os
import pathlib
import re
import sys
from typing import Dict, List, Any, Tuple, Optional


EXPERT_REVIEW_FILES: Dict[str, str] = {
    "4th Turning": "4th_Turning_Expert_Review.md",
    "Changing World Orders": "Changing_World_Orders_Expert_Review.md",
    "Kondratiev Waves": "Kondratiev_Waves_Expert_Review.md",
    "LoAR": "LoAR_Expert_Review.md",
    "Technological Singularity": "Technological_Singularity_Expert_Review.md",
}

SUBJECT_DIRECTORIES: List[str] = [
    "4th Turning",
    "Changing World Orders",
    "Kondratiev Waves",
    "LoAR",
    "Technological Singularity",
]

MIN_REPORT_LINES: int = 51  # Strictly > 50 lines (line count >= 51)
MAX_CROSS_REPORT_DUPLICATION_RATE: float = 15.0  # Max allowed avg duplicate line % per subject directory

PLACEHOLDER_PATTERNS: List[str] = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\[INSERT",
    r"INSERT_DATA",
    r"\[Insert",
    r"\bXXX\b",
    r"\bTEMP\b",
]

BROKEN_TEMPLATE_PATTERNS: List[Tuple[str, str]] = [
    (r"\bregarding\s{2,}and\b", "Double-space variable artifact: 'regarding  and'"),
    (r"\breveals\s+how\s{2,}evolves\b", "Double-space variable artifact: 'reveals how  evolves'"),
    (r"\bhow\s{2,}evolves\b", "Double-space variable artifact: 'how  evolves'"),
    (r"\btransitions\s+in\s+\.", "Missing target variable before period: 'transitions in .'"),
    (r"\bAntecedents\s+of\s*:\s*(?:\s*$|\.)", "Incomplete title colon artifact: 'Antecedents of:'"),
    (r"\|\s{2,}\|", "Empty leading table column header variable"),
    (r"\|{2,}", "Double-pipe table delimiter corruption: '||'"),
    (r"^#{2,3}\s+.*:\s*(?:\[Document Title\]|Topic Name\b|[A-Z0-9\s&,/\-\'\"]+(?:Deep Dive|Monograph|Overview|Synthesis|Framework|Guide|Taxonomy|Matrix|Legacy|Analysis|Research Plan))", "Robotic heading title suffix artifact"),
    (r"\{(?:topic|subject|domain|category|author|title|keyword|item|case_study|date|year|summary|description)\}", "Unpopulated template tag '{...}'"),
    (r"\b(?:in|of|for|regarding|about|with)\s{2,}(?:\.|\,|and)(?=\s|$|\b)", "Double-space empty variable omission artifact"),
    (r"<(?:INSERT|INSERT_DATA|TOPIC|SUBJECT|PARAM)>", "Unpopulated bracket placeholder"),
    (r"\[(?:TOPIC|SUBJECT|DOMAIN|CATEGORY|VARIABLE|DATA)\]", "Unpopulated square-bracket placeholder"),
]

CITATION_PATTERNS: List[str] = [
    r"\([A-Z][a-zA-Z\s.,'-]+,\s*\d{4}\)",       # e.g., (Strauss, 1997) or (Howe & Strauss, 1997)
    r"\[\d+\]",                                 # e.g., [1], [2]
    r"\[CIT-[A-Z0-9_-]+\]",                     # e.g., [CIT-4T-01]
    r"^#{1,6}\s*(?:Academic\s+(&|and)\s+Historical\s+)?References\b", # e.g., ## References or ## Academic References
    r"^#{1,6}\s*(?:[A-Za-z0-9\s\x26,\'\.\-]+\s+)?(?:References|Bibliography|Citations)\b", # e.g., ## Academic References & Bibliography
    r"##\s+.*Sources?",                         # e.g., ## Historical Sources
    r"##\s+.*Further Reading",                 # e.g., ## Further Reading
    r"https?://",                              # explicit web citations / URLs
]


class ConvergenceAuditor:
    """Automated auditor for verifying requirement R3 across Convergence research reports."""

    def __init__(
        self,
        root: Optional[pathlib.Path] = None,
        verbose: bool = False,
        strict: bool = False,
        json_output: bool = False,
    ):
        if root is None:
            self.root = pathlib.Path(__file__).resolve().parent.parent
        else:
            self.root = pathlib.Path(root).resolve()

        self.verbose = verbose
        self.strict = strict
        self.json_output = json_output

        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.expert_review_results: Dict[str, Any] = {}
        self.report_depth_results: Dict[str, Any] = {}
        self.enhancement_results: Dict[str, Any] = {}
        self.duplication_results: Dict[str, Any] = {}
        self.template_integrity_results: Dict[str, Any] = {}

    def log_verbose(self, message: str) -> None:
        """Helper to print verbose details when --verbose is active and not printing pure JSON."""
        if self.verbose and not self.json_output:
            print(f"[VERBOSE] {message}")

    def check_expert_reviews(self) -> bool:
        """
        Check 1: Verify all 5 expert review files exist and are non-empty (>50 lines).
        Checks subject directories first, then repository root as fallback.
        """
        self.log_verbose("Starting Check 1: Expert Review Files Existence & Depth...")
        all_passed = True
        details = {}

        for subject, filename in EXPERT_REVIEW_FILES.items():
            path_in_subject = self.root / subject / filename
            path_in_root = self.root / filename

            target_path = None
            if path_in_subject.exists():
                target_path = path_in_subject
            elif path_in_root.exists():
                target_path = path_in_root

            if target_path is None:
                err = f"[EXPERT REVIEW MISSING] File '{filename}' for subject '{subject}' not found."
                self.errors.append(err)
                all_passed = False
                details[subject] = {"status": "MISSING", "line_count": 0, "path": None}
                self.log_verbose(f"  FAIL: {subject} -> Missing '{filename}'")
            else:
                try:
                    lines = target_path.read_text(encoding="utf-8", errors="ignore").splitlines()
                    non_blank_lines = [line for line in lines if line.strip()]
                    line_count = len(non_blank_lines)
                except Exception as e:
                    line_count = 0

                rel_path = str(target_path.relative_to(self.root))
                if line_count < MIN_REPORT_LINES:
                    err = (
                        f"[EXPERT REVIEW DEPTH FAIL] '{rel_path}' has {line_count} lines "
                        f"(required: >50 lines, minimum {MIN_REPORT_LINES})."
                    )
                    self.errors.append(err)
                    all_passed = False
                    details[subject] = {
                        "status": "INSUFFICIENT_DEPTH",
                        "line_count": line_count,
                        "path": rel_path,
                    }
                    self.log_verbose(f"  FAIL: {rel_path} -> {line_count} lines (<{MIN_REPORT_LINES})")
                else:
                    details[subject] = {
                        "status": "PASS",
                        "line_count": line_count,
                        "path": rel_path,
                    }
                    self.log_verbose(f"  PASS: {rel_path} -> {line_count} lines")

        self.expert_review_results = {
            "passed": all_passed,
            "details": details,
        }
        return all_passed

    def check_report_depth(self) -> Tuple[int, int]:
        """
        Check 2: Verify all workspace research reports meet minimum depth standard (>50 lines).
        Scans all markdown files in subject directories and master synthesis report.
        Excludes expert review files from the research report depth count to avoid double counting.
        """
        self.log_verbose("Starting Check 2: Research Report Depth (>50 lines per report)...")
        total_scanned = 0
        failed_count = 0
        passed_reports = []
        failed_reports = []

        reports: List[pathlib.Path] = []
        for subj in SUBJECT_DIRECTORIES:
            subj_path = self.root / subj
            if subj_path.exists():
                reports.extend(sorted(subj_path.rglob("*.md")))

        master_synth = self.root / "Convergence_Master_Synthesis.md"
        if master_synth.exists() and master_synth not in reports:
            reports.append(master_synth)

        for report_path in reports:
            # Skip expert review files in research report depth scan
            if report_path.name in EXPERT_REVIEW_FILES.values() or report_path.name.endswith("_Expert_Review.md") or report_path.name.endswith(".bak.md"):
                continue

            total_scanned += 1
            rel_path = str(report_path.relative_to(self.root))

            try:
                lines = report_path.read_text(encoding="utf-8", errors="ignore").splitlines()
                non_blank_lines = [line for line in lines if line.strip()]
                line_count = len(non_blank_lines)
            except Exception as e:
                line_count = 0

            if line_count < MIN_REPORT_LINES:
                err = (
                    f"[REPORT DEPTH FAIL] '{rel_path}': {line_count} lines "
                    f"(required: >50 lines, minimum {MIN_REPORT_LINES})."
                )
                self.errors.append(err)
                failed_count += 1
                failed_reports.append({"path": rel_path, "line_count": line_count})
                self.log_verbose(f"  FAIL: {rel_path} -> {line_count} lines")
            else:
                passed_reports.append({"path": rel_path, "line_count": line_count})
                self.log_verbose(f"  PASS: {rel_path} -> {line_count} lines")

        passed = (failed_count == 0) and (total_scanned > 0)
        self.report_depth_results = {
            "passed": passed,
            "total_scanned": total_scanned,
            "passed_count": total_scanned - failed_count,
            "failed_count": failed_count,
            "failed_reports": failed_reports,
        }
        return total_scanned, failed_count

    def check_enhancement_integration(self) -> bool:
        """
        Check 3: Verify enhancement integration (citations, zero placeholders).
        Scans all markdown files in subject directories and master synthesis report.
        """
        self.log_verbose("Starting Check 3: Enhancement Integration & Integrity...")
        all_passed = True
        placeholders_found_total = 0
        missing_citations_total = 0
        file_details = []

        reports: List[pathlib.Path] = []
        for subj in SUBJECT_DIRECTORIES:
            subj_path = self.root / subj
            if subj_path.exists():
                reports.extend(sorted(subj_path.rglob("*.md")))

        master_synth = self.root / "Convergence_Master_Synthesis.md"
        if master_synth.exists() and master_synth not in reports:
            reports.append(master_synth)

        for report_path in reports:
            rel_path = str(report_path.relative_to(self.root))
            try:
                text = report_path.read_text(encoding="utf-8", errors="ignore")
            except Exception as e:
                text = ""

            # 3.1 Placeholder check
            found_ph_in_file = []
            for pattern in PLACEHOLDER_PATTERNS:
                matches = re.findall(pattern, text, re.IGNORECASE)
                if matches:
                    found_ph_in_file.extend(matches)

            if found_ph_in_file:
                unique_ph = sorted(list(set(found_ph_in_file)))
                err = f"[PLACEHOLDER FOUND] '{rel_path}' contains placeholder tags: {', '.join(unique_ph)}"
                self.errors.append(err)
                placeholders_found_total += len(found_ph_in_file)
                all_passed = False

            # 3.2 Citation / Reference check
            has_citation = False
            for c_pat in CITATION_PATTERNS:
                if re.search(c_pat, text, re.IGNORECASE | re.MULTILINE):
                    has_citation = True
                    break

            if not has_citation:
                missing_citations_total += 1
                msg = f"[CITATION MISSING] '{rel_path}' lacks academic citations or reference section."
                if self.strict:
                    self.errors.append(msg)
                    all_passed = False
                else:
                    self.warnings.append(msg)

            file_details.append(
                {
                    "path": rel_path,
                    "placeholders": found_ph_in_file,
                    "has_citation": has_citation,
                }
            )

        self.enhancement_results = {
            "passed": all_passed,
            "placeholders_found": placeholders_found_total,
            "missing_citations_count": missing_citations_total,
            "file_details": file_details,
        }
        return all_passed

    def check_cross_report_duplication(self) -> bool:
        """
        Check 4: Verify cross-report line uniqueness across subject directories.
        Flags any subject directory where average duplicated non-blank lines exceed MAX_CROSS_REPORT_DUPLICATION_RATE (15.0%).
        Excludes expert review files from subfolder duplication scans.
        """
        self.log_verbose("Starting Check 4: Cross-Report Line Duplication Analysis...")
        all_passed = True
        dir_details = {}

        for subject in SUBJECT_DIRECTORIES:
            subj_path = self.root / subject
            if not subj_path.exists():
                continue

            reports = [
                f for f in sorted(subj_path.rglob("*.md"))
                if f.name not in EXPERT_REVIEW_FILES.values() and not f.name.endswith("_Expert_Review.md") and not f.name.endswith(".bak.md")
            ]

            if not reports:
                continue

            # Extract trimmed non-blank lines per report
            file_lines = {}
            for r in reports:
                try:
                    lines = [l.strip() for l in r.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
                except Exception:
                    lines = []
                file_lines[r] = lines

            # Calculate line frequency across all reports in this subject directory
            all_lines_counter = collections.Counter(
                line for lines in file_lines.values() for line in lines
            )

            # Calculate duplication percentage per file and check single-file duplication caps
            file_dup_rates = []
            single_file_failures = []
            for r, lines in file_lines.items():
                if not lines:
                    continue
                dup_count = sum(1 for l in lines if all_lines_counter[l] > 1)
                rate = (dup_count / len(lines)) * 100.0
                file_dup_rates.append(rate)
                rel_p = str(r.relative_to(self.root))
                if rate > MAX_CROSS_REPORT_DUPLICATION_RATE:
                    single_file_failures.append((rel_p, rate))
                    all_passed = False
                    err = (
                        f"[SINGLE-FILE DUPLICATION FAIL] Report '{rel_p}' line duplication rate is {rate:.2f}% "
                        f"(exceeds maximum allowed threshold of {MAX_CROSS_REPORT_DUPLICATION_RATE:.1f}%)."
                    )
                    self.errors.append(err)
                    self.log_verbose(f"  FAIL: {rel_p} -> Single-file Duplication: {rate:.2f}% (>15.0%)")

            avg_dup_rate = sum(file_dup_rates) / len(file_dup_rates) if file_dup_rates else 0.0

            # Lines common to 100% of reports in this directory
            common_lines = set.intersection(*[set(lines) for lines in file_lines.values()]) if file_lines else set()

            if avg_dup_rate > MAX_CROSS_REPORT_DUPLICATION_RATE:
                all_passed = False
                err = (
                    f"[CROSS-REPORT DUPLICATION FAIL] Subject directory '{subject}' average line duplication "
                    f"rate is {avg_dup_rate:.2f}% (exceeds maximum allowed threshold of {MAX_CROSS_REPORT_DUPLICATION_RATE:.1f}%). "
                    f"{len(common_lines)} lines are 100% identical across all {len(reports)} reports."
                )
                self.errors.append(err)
                self.log_verbose(f"  FAIL: {subject} -> Avg Duplication: {avg_dup_rate:.2f}% (>15.0%)")
            else:
                self.log_verbose(f"  PASS: {subject} -> Avg Duplication: {avg_dup_rate:.2f}% (<=15.0%)")

            max_single_rate = max(file_dup_rates) if file_dup_rates else 0.0
            dir_details[subject] = {
                "report_count": len(reports),
                "avg_duplication_rate": round(avg_dup_rate, 2),
                "max_single_duplication_rate": round(max_single_rate, 2),
                "common_100pct_line_count": len(common_lines),
                "passed": avg_dup_rate <= MAX_CROSS_REPORT_DUPLICATION_RATE and len(single_file_failures) == 0,
            }

        self.duplication_results = {
            "passed": all_passed,
            "details": dir_details,
        }
        return all_passed

    def check_template_integrity(self) -> bool:
        """
        Check 5: Verify template integrity across research reports.
        Scans for broken template variable artifacts, unpopulated tags, double spaces, and dangling punctuation.
        """
        self.log_verbose("Starting Check 5: Template Integrity & Broken Tag Scan...")
        all_passed = True
        broken_tags_total = 0
        file_details = []

        reports: List[pathlib.Path] = []
        for subj in SUBJECT_DIRECTORIES:
            subj_path = self.root / subj
            if subj_path.exists():
                reports.extend(sorted(subj_path.rglob("*.md")))

        master_synth = self.root / "Convergence_Master_Synthesis.md"
        if master_synth.exists() and master_synth not in reports:
            reports.append(master_synth)

        for report_path in reports:
            # Skip expert review files in template integrity scan
            if report_path.name in EXPERT_REVIEW_FILES.values() or report_path.name.endswith("_Expert_Review.md") or report_path.name.endswith(".bak.md"):
                continue
            rel_path = str(report_path.relative_to(self.root))
            try:
                text = report_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                text = ""

            found_in_file = []
            for pattern, desc in BROKEN_TEMPLATE_PATTERNS:
                matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
                if matches:
                    found_in_file.append((desc, len(matches)))
                    err = f"[BROKEN TEMPLATE TAG FOUND] '{rel_path}' contains broken template artifact: {desc} (count: {len(matches)})"
                    self.errors.append(err)
                    broken_tags_total += len(matches)
                    all_passed = False

            # Secondary scan for repeated robotic heading title suffixes (suffix after colon repeated 2+ times in same report)
            hdrs = [l.strip() for l in text.splitlines() if (l.strip().startswith("## ") or l.strip().startswith("### ")) and ":" in l]
            suffixes = [h.split(":", 1)[1].strip() for h in hdrs if len(h.split(":", 1)) > 1]
            counts = collections.Counter(suffixes)
            repeated_suffixes = [s for s, c in counts.items() if c >= 2]
            if repeated_suffixes:
                desc = "Robotic heading title suffix artifact (repeated suffix after colon)"
                found_in_file.append((desc, len(repeated_suffixes)))
                err = f"[BROKEN TEMPLATE TAG FOUND] '{rel_path}' contains broken template artifact: {desc} (suffixes: {', '.join(sorted(repeated_suffixes))})"
                self.errors.append(err)
                broken_tags_total += len(repeated_suffixes)
                all_passed = False

            if found_in_file:
                self.log_verbose(f"  FAIL: {rel_path} -> {len(found_in_file)} broken template patterns detected")
            else:
                self.log_verbose(f"  PASS: {rel_path} -> Clean template prose")

            file_details.append(
                {
                    "path": rel_path,
                    "broken_patterns": found_in_file,
                }
            )

        self.template_integrity_results = {
            "passed": all_passed,
            "broken_tags_total": broken_tags_total,
            "file_details": file_details,
        }
        return all_passed

    def run_full_audit(self) -> Dict[str, Any]:
        """Runs all 5 verification checks and returns aggregated audit results dictionary."""
        review_ok = self.check_expert_reviews()
        scanned, depth_fails = self.check_report_depth()
        enhancement_ok = self.check_enhancement_integration()
        duplication_ok = self.check_cross_report_duplication()
        template_ok = self.check_template_integrity()

        overall_passed = review_ok and (depth_fails == 0) and enhancement_ok and duplication_ok and template_ok

        results = {
            "passed": overall_passed,
            "summary": {
                "expert_reviews_passed": review_ok,
                "reports_scanned": scanned,
                "depth_passed_count": scanned - depth_fails,
                "depth_failed_count": depth_fails,
                "enhancements_passed": enhancement_ok,
                "duplication_passed": duplication_ok,
                "template_integrity_passed": template_ok,
                "total_errors": len(self.errors),
                "total_warnings": len(self.warnings),
            },
            "expert_reviews": self.expert_review_results,
            "report_depth": self.report_depth_results,
            "enhancement_integration": self.enhancement_results,
            "duplication_results": self.duplication_results,
            "template_integrity": self.template_integrity_results,
            "errors": self.errors,
            "warnings": self.warnings,
        }

        if self.json_output:
            print(json.dumps(results, indent=2))
        else:
            self._print_human_readable_report(results)

        return results

    def _print_human_readable_report(self, results: Dict[str, Any]) -> None:
        """Prints clean, formatted console summary output."""
        print("=================================================================")
        print("        CONVERGENCE AUTOMATED AUDIT & VERIFICATION REPORT        ")
        print("=================================================================")
        print(f"Repository Root: {self.root}")
        print(f"Mode: Strict={self.strict}, Verbose={self.verbose}\n")

        summary = results["summary"]
        print("-----------------------------------------------------------------")
        print("AUDIT SUMMARY")
        print("-----------------------------------------------------------------")
        er_status = "PASS" if summary["expert_reviews_passed"] else "FAIL"
        print(f"  [1] Expert Review Files (5 Required):         [{er_status}]")

        rd_status = "PASS" if summary["depth_failed_count"] == 0 else "FAIL"
        print(
            f"  [2] Report Depth (>50 lines):                 [{rd_status}] "
            f"({summary['depth_passed_count']}/{summary['reports_scanned']} passed, {summary['depth_failed_count']} failed)"
        )

        en_status = "PASS" if summary["enhancements_passed"] else "FAIL"
        print(f"  [3] Enhancement & Citation Integration:     [{en_status}]")

        dup_status = "PASS" if summary.get("duplication_passed", False) else "FAIL"
        print(f"  [4] Cross-Report Uniqueness (<=15% dup):     [{dup_status}]")

        tmpl_status = "PASS" if summary.get("template_integrity_passed", False) else "FAIL"
        print(f"  [5] Template Integrity & Tag Scan:            [{tmpl_status}]")
        print("-----------------------------------------------------------------")

        if self.warnings:
            print(f"\n[WARNINGS ({len(self.warnings)})]:")
            for warn in self.warnings[:20]:
                print(f"  - {warn}")
            if len(self.warnings) > 20:
                print(f"  ... and {len(self.warnings) - 20} more warnings.")

        if self.errors:
            print(f"\n[ERRORS DETECTED ({len(self.errors)})]:")
            for err in self.errors:
                print(f"  - {err}")
            print("\n=================================================================")
            print(" [RESULT]: AUDIT FAILED - Fix errors listed above.")
            print("=================================================================")
        else:
            print("\n=================================================================")
            print(" [RESULT]: AUDIT PASSED - All requirements verified with 0 errors!")
            print("=================================================================")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convergence Repository Automated Audit & Verification Script (Requirement R3)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output audit result in JSON format",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print detailed file-by-file log output",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enforce strict citation requirements on all scanned reports",
    )
    parser.add_argument(
        "--root",
        type=str,
        default=None,
        help="Path to repository root (defaults to parent directory of script)",
    )

    args = parser.parse_args()

    root_path = pathlib.Path(args.root) if args.root else None
    auditor = ConvergenceAuditor(
        root=root_path,
        verbose=args.verbose,
        strict=args.strict,
        json_output=args.json,
    )

    results = auditor.run_full_audit()
    return 0 if results["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
