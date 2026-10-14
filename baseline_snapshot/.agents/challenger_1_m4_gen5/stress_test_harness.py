#!/usr/bin/env python3
"""
Stress Testing & Empirical Verification Harness for scripts/audit_verification.py
Author: Challenger 1 (Verification Script Stress Testing Challenger)
Gate Iteration 5 - Milestone 4

Comprehensive empirical harness testing edge cases, boundary conditions,
bypass attempts, false positives, false negatives, and --strict flag compliance.
"""

import io
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile
import unittest
from typing import Dict, List, Any

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.audit_verification import (
    ConvergenceAuditor,
    main,
    EXPERT_REVIEW_FILES,
    SUBJECT_DIRECTORIES,
    MIN_REPORT_LINES,
    MAX_CROSS_REPORT_DUPLICATION_RATE,
)


class EmpiricalStressTestAuditVerification(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_minimal_valid_repo(self):
        """Creates a minimal valid repo structure where all 5 checks pass."""
        for subject, filename in EXPERT_REVIEW_FILES.items():
            path = self.root / subject / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            lines = [f"Expert review content line {i+1} with citation (Strauss, 1997)." for i in range(60)]
            path.write_text("\n".join(lines), encoding="utf-8")

        for subject in SUBJECT_DIRECTORIES:
            path = self.root / subject / "Deep_Dive.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            lines = [f"Substantive research report line {i+1} for {subject} with citation (Author, 2026)." for i in range(60)]
            path.write_text("\n".join(lines), encoding="utf-8")

        master_synth = self.root / "Convergence_Master_Synthesis.md"
        lines = [f"Master synthesis line {i+1} with citation (Kondratiev, 1925)." for i in range(100)]
        master_synth.write_text("\n".join(lines), encoding="utf-8")

    # =========================================================================
    # TEST VECTOR 1: PLACEHOLDER BYPASS ATTEMPTS
    # =========================================================================
    def test_vector_1a_underscore_placeholder_bypass(self):
        """
        Vulnerability: Word boundary regex r'\\bTODO\\b' fails on 'TODO_ITEM', 'FIXME_NOW', 'TBD_DATA', 'XXX_CHECK'.
        Reason: In Python re, '_' is a word character (\\w). 'TODO_' has no word boundary between 'O' and '_'.
        """
        self._create_minimal_valid_repo()
        bad_report = self.root / "4th Turning" / "Bypass_Underscore.md"
        lines = [f"Substantive research line {i+1} (Strauss, 1997)." for i in range(50)]
        lines.append("Line 51: Note: TODO_SECTION and FIXME_LATER and TBD_DATA and XXX_VALUE need review.")
        bad_report.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_enhancement_integration()
        placeholder_errors = [e for e in auditor.errors if "PLACEHOLDER FOUND" in e]

        # Empirical proof: auditor fails to catch underscore placeholders
        self.assertTrue(passed, "Auditor passed despite presence of TODO_SECTION, FIXME_LATER, TBD_DATA")
        self.assertEqual(len(placeholder_errors), 0, "No placeholder error logged for underscore placeholders")

    def test_vector_1b_untracked_template_tags_bypass(self):
        """
        Vulnerability: Custom/Untracked template placeholders like [YOUR_TEXT_HERE], <PLACEHOLDER>, {custom_var}, [AUTHOR].
        Check 3 and Check 5 only match specific hardcoded template string sets.
        """
        self._create_minimal_valid_repo()
        bad_report = self.root / "4th Turning" / "Bypass_Custom_Tags.md"
        lines = [f"Substantive research line {i+1} (Strauss, 1997)." for i in range(50)]
        lines.append("Line 51: Details: [YOUR_TEXT_HERE], <PLACEHOLDER>, {custom_var}, [AUTHOR], [DATE].")
        bad_report.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed_enh = auditor.check_enhancement_integration()
        passed_tmpl = auditor.check_template_integrity()

        self.assertTrue(passed_enh and passed_tmpl, "Auditor passed despite untracked placeholder tags")
        self.assertEqual(len(auditor.errors), 0, "No errors raised for [YOUR_TEXT_HERE] or {custom_var}")

    # =========================================================================
    # TEST VECTOR 2: STRICT MODE & CITATION ENFORCEMENT ACCURACY
    # =========================================================================
    def test_vector_2a_strict_mode_conformance(self):
        """
        Verification: Verify that --strict correctly elevates missing citations from warnings to errors.
        """
        self._create_minimal_valid_repo()
        uncited_report = self.root / "4th Turning" / "Uncited_Report.md"
        lines = [f"Substantive report line {i+1} with no academic references or URLs." for i in range(60)]
        uncited_report.write_text("\n".join(lines), encoding="utf-8")

        # 1. Non-strict mode
        auditor_ns = ConvergenceAuditor(root=self.root, strict=False)
        passed_ns = auditor_ns.check_enhancement_integration()
        self.assertTrue(passed_ns, "Non-strict mode should return passed=True when citations missing")
        self.assertTrue(any("[CITATION MISSING]" in w for w in auditor_ns.warnings), "Warning logged in non-strict mode")
        self.assertEqual(len(auditor_ns.errors), 0)

        # 2. Strict mode
        auditor_s = ConvergenceAuditor(root=self.root, strict=True)
        passed_s = auditor_s.check_enhancement_integration()
        self.assertFalse(passed_s, "Strict mode must return passed=False when citations missing")
        self.assertTrue(any("[CITATION MISSING]" in e for e in auditor_s.errors), "Error logged in strict mode")

    def test_vector_2b_citation_false_positives(self):
        """
        Vulnerability: Citation pattern matching accepts trivial non-citations such as (Note, 2024), array index [1], or http://.
        """
        self._create_minimal_valid_repo()
        trivial_report = self.root / "LoAR" / "Trivial_Citation.md"
        lines = [f"Substantive report line {i+1} text." for i in range(50)]
        lines.append("Line 51: As stated in (Note, 2024) or array element [1] or http://localhost.")
        trivial_report.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        passed = auditor.check_enhancement_integration()

        # Empirical proof: Trivial string accepted as valid citation
        self.assertTrue(passed, "Auditor accepted (Note, 2024) / [1] / http:// as valid citation")

    # =========================================================================
    # TEST VECTOR 3: LINE DUPLICATION SCOPE & CROSS-SUBJECT BYPASS
    # =========================================================================
    def test_vector_3a_cross_subject_duplication_bypass(self):
        """
        Vulnerability: Check 4 iterates over SUBJECT_DIRECTORIES independently.
        It NEVER compares files in '4th Turning' against files in 'LoAR'.
        A report copied 100% across subjects bypasses Check 4.
        """
        self._create_minimal_valid_repo()
        duplicate_text = "\n".join([f"Identical copied line {i+1} across subjects (Strauss, 1997)." for i in range(60)])
        (self.root / "4th Turning" / "Plagiarized_Report.md").write_text(duplicate_text, encoding="utf-8")
        (self.root / "LoAR" / "Plagiarized_Report.md").write_text(duplicate_text, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()

        # Empirical proof: Cross-subject duplication is ignored
        self.assertTrue(passed, "Cross-subject 100% duplicate report bypassed Check 4")

    def test_vector_3b_master_synthesis_duplication_bypass(self):
        """
        Vulnerability: Convergence_Master_Synthesis.md is excluded from Check 4 duplication scanning.
        Copying 100% of Master Synthesis into a subject report bypasses Check 4.
        """
        self._create_minimal_valid_repo()
        duplicate_synth = "\n".join([f"Master synth copied line {i+1} (Kondratiev, 1925)." for i in range(70)])
        (self.root / "Convergence_Master_Synthesis.md").write_text(duplicate_synth, encoding="utf-8")
        (self.root / "Kondratiev Waves" / "Copied_Synth_Report.md").write_text(duplicate_synth, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()

        # Empirical proof: Master synthesis duplication is ignored
        self.assertTrue(passed, "Master synthesis 100% duplicate report bypassed Check 4")

    def test_vector_3c_duplication_false_positive_structural_markdown(self):
        """
        False Positive: 5 short valid reports in a directory sharing standard markdown headers & tables
        (e.g., # Section, ## Overview, | Domain | Metric |, ---) exceed 15% duplication threshold.
        """
        self.root = pathlib.Path(tempfile.mkdtemp())
        for subject, filename in EXPERT_REVIEW_FILES.items():
            path = self.root / subject / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join([f"Expert line {i}" for i in range(60)]), encoding="utf-8")

        common_lines = [
            "# Subject Overview",
            "## Executive Summary",
            "## Methodology & Theoretical Framework",
            "## Comparative Analysis Matrix",
            "| Domain | Metric | Target | Status |",
            "| :--- | :---: | :---: | :--- |",
            "## Strategic Policy Implications",
            "## Academic References & Bibliography",
            "---",
        ]
        # 5 reports in Changing World Orders, 52 lines each. 9 lines common = 17.3% duplication.
        for i in range(5):
            unique_lines = [f"Unique research text paragraph {j} for report {i} (Allison, 2017)." for j in range(43)]
            rpath = self.root / "Changing World Orders" / f"Report_{i}.md"
            rpath.parent.mkdir(parents=True, exist_ok=True)
            rpath.write_text("\n".join(common_lines + unique_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()

        # Empirical proof: False positive failure on standard markdown structure
        self.assertFalse(passed, "Standard markdown headers triggered false positive duplication error")
        self.assertTrue(any("CROSS-REPORT DUPLICATION FAIL" in e for e in auditor.errors))

    # =========================================================================
    # TEST VECTOR 4: TEMPLATE INTEGRITY & CODE BLOCK FALSE POSITIVES
    # =========================================================================
    def test_vector_4a_code_block_false_positives(self):
        """
        False Positive: Auditor scans inside markdown code blocks ```bash ... ```.
        Valid code containing '||' (shell OR / pipe) or '{topic}' triggers broken template tag errors.
        """
        self._create_minimal_valid_repo()
        code_report = self.root / "Technological Singularity" / "Code_Report.md"
        lines = [f"Substantive research line {i+1} (Vinge, 1993)." for i in range(50)]
        lines.extend([
            "```bash",
            "grep -r 'pattern' . || echo 'Not found'",
            "curl -X POST http://api.example.com -d '{\"topic\": \"singularity\"}'",
            "```",
        ])
        code_report.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()

        # Empirical proof: Code block syntax causes false positive audit failure
        self.assertFalse(passed, "Code block containing || and {topic} triggered false positive template error")
        self.assertTrue(any("Double-pipe table delimiter corruption" in e for e in auditor.errors))
        self.assertTrue(any("Unpopulated template tag '{...}'" in e for e in auditor.errors))

    def test_vector_4b_reused_natural_subtitle_false_positive(self):
        """
        False Positive: Reusing a natural subtitle like 'Overview' across sections (## Part 1: Overview vs ### Part 2: Overview).
        Check 5 secondary scan flags repeated heading suffixes as 'Robotic heading title suffix artifact'.
        """
        self._create_minimal_valid_repo()
        hdr_report = self.root / "4th Turning" / "Subtitle_Report.md"
        lines = [f"Substantive research line {i+1} (Strauss, 1997)." for i in range(50)]
        lines.extend([
            "## Section 1: Overview",
            "### Subsection 1.1: Overview",
        ])
        hdr_report.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()

        # Empirical proof: Natural reused subtitle causes false positive failure
        self.assertFalse(passed, "Reused subtitle 'Overview' triggered false positive robotic suffix error")
        self.assertTrue(any("Robotic heading title suffix artifact" in e for e in auditor.errors))

    # =========================================================================
    # TEST VECTOR 5: BOUNDARY CONDITIONS & FILE SYSTEM CORRUPTIONS
    # =========================================================================
    def test_vector_5a_depth_boundary_50_vs_51(self):
        """
        Boundary Test: Verify strict > 50 non-blank lines requirement (50 lines fail, 51 lines pass).
        """
        self._create_minimal_valid_repo()

        r50 = self.root / "4th Turning" / "Report_50_Lines.md"
        r50.write_text("\n".join([f"Line {i+1} (Strauss, 1997)." for i in range(50)]), encoding="utf-8")

        r51 = self.root / "4th Turning" / "Report_51_Lines.md"
        r51.write_text("\n".join([f"Line {i+1} (Strauss, 1997)." for i in range(51)]), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_report_depth()

        failed_paths = [item["path"] for item in auditor.report_depth_results["failed_reports"]]
        self.assertIn(str(r50.relative_to(self.root)), failed_paths, "50 non-blank lines MUST fail depth check")
        self.assertNotIn(str(r51.relative_to(self.root)), failed_paths, "51 non-blank lines MUST pass depth check")

    def test_vector_5b_whitespace_line_padding(self):
        """
        Boundary Test: Lines containing only whitespace (spaces/tabs) should be excluded from line count.
        """
        self._create_minimal_valid_repo()
        padded_report = self.root / "4th Turning" / "Padded_Report.md"
        lines = [f"Line {i+1} (Strauss, 1997)." for i in range(30)]
        lines.extend(["   \t   "] * 30)  # 30 whitespace-only lines
        padded_report.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_report_depth()

        failed_paths = [item["path"] for item in auditor.report_depth_results["failed_reports"]]
        self.assertIn(str(padded_report.relative_to(self.root)), failed_paths, "Whitespace-padded 30-line report MUST fail depth check")


if __name__ == "__main__":
    unittest.main()
