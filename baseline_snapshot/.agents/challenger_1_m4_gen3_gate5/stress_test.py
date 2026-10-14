#!/usr/bin/env python3
"""
Adversarial Stress Harness for audit_verification.py
Tests synthetic negative inputs, edge cases, and CLI flags.
"""

import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.audit_verification import ConvergenceAuditor, main, EXPERT_REVIEW_FILES, SUBJECT_DIRECTORIES

def setup_base_valid_repo(root_path: pathlib.Path):
    """Sets up a minimal clean valid repo in root_path."""
    for subject, filename in EXPERT_REVIEW_FILES.items():
        file_path = root_path / subject / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"Line {i+1}: Valid expert review content (Author, 2026)." for i in range(60)]
        file_path.write_text("\n".join(lines), encoding="utf-8")

    for subject in SUBJECT_DIRECTORIES:
        file_path = root_path / subject / "Subfolder" / "Report.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"Line {i+1}: Valid report content for {subject} report (Author, 2026)." for i in range(60)]
        file_path.write_text("\n".join(lines), encoding="utf-8")

    master_synth = root_path / "Convergence_Master_Synthesis.md"
    lines = [f"Line {i+1}: Master synthesis content (Author, 2026)." for i in range(100)]
    master_synth.write_text("\n".join(lines), encoding="utf-8")


class SyntheticNegativeStressTests(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)
        setup_base_valid_repo(self.root)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_01_clean_repo_passes(self):
        """Verify clean fixture passes with 0 errors."""
        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertTrue(res["passed"])
        self.assertEqual(len(res["errors"]), 0)

    def test_02_missing_expert_review(self):
        """Synthetic negative: Missing 4th Turning expert review file."""
        er_path = self.root / "4th Turning" / EXPERT_REVIEW_FILES["4th Turning"]
        er_path.unlink()

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertFalse(res["passed"])
        self.assertTrue(any("EXPERT REVIEW MISSING" in e for e in res["errors"]))

    def test_03_short_expert_review(self):
        """Synthetic negative: Expert review file with only 30 lines (needs >=51)."""
        er_path = self.root / "4th Turning" / EXPERT_REVIEW_FILES["4th Turning"]
        lines = [f"Short line {i}" for i in range(30)]
        er_path.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertFalse(res["passed"])
        self.assertTrue(any("EXPERT REVIEW DEPTH FAIL" in e for e in res["errors"]))

    def test_04_short_research_report(self):
        """Synthetic negative: Subject report with only 40 lines."""
        report_path = self.root / "LoAR" / "Subfolder" / "Report.md"
        lines = [f"Short report line {i}" for i in range(40)]
        report_path.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertFalse(res["passed"])
        self.assertTrue(any("REPORT DEPTH FAIL" in e for e in res["errors"]))

    def test_05_placeholder_tags(self):
        """Synthetic negative: Report containing placeholders like TODO, TBD, [INSERT."""
        report_path = self.root / "Kondratiev Waves" / "Subfolder" / "Report.md"
        content = report_path.read_text() + "\nThis is a TODO item and TBD analysis with [INSERT table]."
        report_path.write_text(content, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertFalse(res["passed"])
        self.assertTrue(any("PLACEHOLDER FOUND" in e for e in res["errors"]))

    def test_06_missing_citations_strict_mode(self):
        """Synthetic negative: Report lacking citations in strict vs non-strict mode."""
        report_path = self.root / "Changing World Orders" / "Subfolder" / "Report.md"
        lines = [f"Substantive plain line {i} without citations." for i in range(60)]
        report_path.write_text("\n".join(lines), encoding="utf-8")

        # Non-strict
        auditor_ns = ConvergenceAuditor(root=self.root, strict=False)
        with patch("sys.stdout", new=io.StringIO()):
            res_ns = auditor_ns.run_full_audit()
        self.assertTrue(res_ns["passed"])
        self.assertTrue(any("CITATION MISSING" in w for w in res_ns["warnings"]))

        # Strict
        auditor_s = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res_s = auditor_s.run_full_audit()
        self.assertFalse(res_s["passed"])
        self.assertTrue(any("CITATION MISSING" in e for e in res_s["errors"]))

    def test_07_malformed_table_double_pipe(self):
        """Synthetic negative: Malformed table with double pipe '||'."""
        report_path = self.root / "Technological Singularity" / "Subfolder" / "Report.md"
        corrupted_content = report_path.read_text() + "\n| Col 1 || Col 2 |\n|---|---|\n"
        report_path.write_text(corrupted_content, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertFalse(res["passed"])
        self.assertTrue(any("Double-pipe table delimiter corruption" in e for e in res["errors"]))

    def test_08_broken_template_variables(self):
        """Synthetic negative: Broken template variables like 'regarding  and' and '{topic}'."""
        report_path = self.root / "4th Turning" / "Subfolder" / "Report.md"
        corrupted_content = report_path.read_text() + "\nDiscussion regarding  and turning points.\nTopic tag {topic} active."
        report_path.write_text(corrupted_content, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertFalse(res["passed"])
        self.assertTrue(any("BROKEN TEMPLATE TAG FOUND" in e for e in res["errors"]))

    def test_09_high_cross_report_duplication(self):
        """Synthetic negative: High duplication across reports (>15%)."""
        subj_dir = self.root / "4th Turning"
        shared_lines = [f"Common duplicate boilerplate line {i}" for i in range(25)]
        for r_idx in range(4):
            rp = subj_dir / f"Dup_Report_{r_idx}.md"
            unique_lines = [f"Unique line {j} for dup report {r_idx} (Strauss, 1997)." for j in range(35)]
            rp.write_text("\n".join(shared_lines + unique_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            res = auditor.run_full_audit()
        self.assertFalse(res["passed"])
        self.assertTrue(any("CROSS-REPORT DUPLICATION FAIL" in e or "SINGLE-FILE DUPLICATION FAIL" in e for e in res["errors"]))

    def test_10_cli_exit_code_on_failure(self):
        """Verify CLI main() returns exit code 1 when errors exist."""
        report_path = self.root / "LoAR" / "Subfolder" / "Report.md"
        report_path.write_text("TODO item line 1\n", encoding="utf-8")

        test_args = ["audit_verification.py", "--root", str(self.root), "--strict"]
        with patch.object(sys, "argv", test_args), patch("sys.stdout", new=io.StringIO()):
            exit_code = main()
            self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    unittest.main()
