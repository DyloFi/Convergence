#!/usr/bin/env python3
"""
Empirical Stress Test Harness for scripts/audit_verification.py
Executed by Challenger 1 for Milestone 4 Gen 2 Iteration 3 Gate Verification.
"""

import sys
import pathlib
import tempfile
import unittest
import json

# Add project root to sys.path
PROJECT_ROOT = pathlib.Path("/Users/dylanboyle/Desktop/Convergence")
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_verification import ConvergenceAuditor, EXPERT_REVIEW_FILES, SUBJECT_DIRECTORIES


class SyntheticNegativeCheck4Test(unittest.TestCase):
    """Stress tests for Check 4 (Cross-report line duplication <= 15.0%)."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_duplication_boundary_15_percent_exact(self):
        """Verify 15.0% duplicate line overlap passes (boundary case)."""
        subj_dir = self.root / "4th Turning"
        # 15 duplicate lines out of 100 total lines = 15.0%
        dup_lines = [f"Shared line {i}" for i in range(15)]
        
        for rep_idx in range(5):
            unique_lines = [f"Unique line {i} in report {rep_idx} (Author, 2026)." for i in range(85)]
            file_path = subj_dir / f"Report_{rep_idx}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text("\n".join(dup_lines + unique_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertTrue(passed, "15.0% exact duplication should PASS")
        self.assertAlmostEqual(
            auditor.duplication_results["details"]["4th Turning"]["avg_duplication_rate"],
            15.0,
            places=2
        )

    def test_duplication_boundary_15_point_1_percent_fails(self):
        """Verify 15.1% duplicate line overlap fails."""
        subj_dir = self.root / "4th Turning"
        # 16 duplicate lines out of 100 total lines = 16.0% (>15.0%)
        dup_lines = [f"Shared line {i}" for i in range(16)]
        
        for rep_idx in range(5):
            unique_lines = [f"Unique line {i} in report {rep_idx} (Author, 2026)." for i in range(84)]
            file_path = subj_dir / f"Report_{rep_idx}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text("\n".join(dup_lines + unique_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertFalse(passed, "16.0% duplication (>15.0%) must FAIL")
        self.assertTrue(any("CROSS-REPORT DUPLICATION FAIL" in err for err in auditor.errors))

    def test_high_duplication_catch(self):
        """Verify 88.3% duplicate line overlap (pre-refactoring state) is caught and flagged."""
        subj_dir = self.root / "4th Turning"
        dup_lines = [f"Boilerplate appendix line {i}" for i in range(88)]
        
        for rep_idx in range(5):
            unique_lines = [f"Unique line {i} in report {rep_idx} (Author, 2026)." for i in range(12)]
            file_path = subj_dir / f"Report_{rep_idx}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text("\n".join(dup_lines + unique_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertFalse(passed)
        rate = auditor.duplication_results["details"]["4th Turning"]["avg_duplication_rate"]
        self.assertGreater(rate, 80.0)

    def test_expert_review_exclusion_in_duplication(self):
        """Verify expert review files with 100% duplicate lines do not inflate research report duplication."""
        subj_dir = self.root / "4th Turning"
        expert_review = subj_dir / "4th_Turning_Expert_Review.md"
        shared_text = "\n".join([f"Identical line {i} (Author, 2026)." for i in range(60)])
        
        expert_review.parent.mkdir(parents=True, exist_ok=True)
        expert_review.write_text(shared_text, encoding="utf-8")

        # Single research report with unique content
        report = subj_dir / "Subfolder" / "Unique_Report.md"
        unique_text = "\n".join([f"Unique content line {i} (Author, 2026)." for i in range(60)])
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(unique_text, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertTrue(passed)
        self.assertEqual(auditor.duplication_results["details"]["4th Turning"]["report_count"], 1)
        self.assertEqual(auditor.duplication_results["details"]["4th Turning"]["avg_duplication_rate"], 0.0)


class SyntheticNegativeCheck5Test(unittest.TestCase):
    """Stress tests for Check 5 (Broken Template Tags & Artifacts)."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_report(self, filename: str, content: str):
        path = self.root / "4th Turning" / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_catch_regarding_double_space_and(self):
        """Verify Check 5 catches 'regarding  and'."""
        self._create_report("rep1.md", "Evaluating crisis dynamics regarding  and institutional shifts (Author, 2026).\n" * 55)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("regarding  and" in err for err in auditor.errors))

    def test_catch_transitions_in_dot(self):
        """Verify Check 5 catches 'transitions in .'."""
        self._create_report("rep2.md", "Analysis of cyclical transitions in . Institutional responses vary (Author, 2026).\n" * 55)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("transitions in ." in err for err in auditor.errors))

    def test_catch_unpopulated_curly_topic(self):
        """Verify Check 5 catches '{topic}', '{subject}', '{domain}'."""
        self._create_report("rep3.md", "Deep dive into {topic} and {subject} evolution across cycles (Author, 2026).\n" * 55)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("Unpopulated template tag '{...}'" in err for err in auditor.errors))

    def test_catch_dangling_colon_antecedents_of(self):
        """Verify Check 5 catches dangling colons in 'Antecedents of:'."""
        self._create_report("rep4.md", "The Historical Antecedents of: How economic pressure drives realignment.\n" * 55)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("Antecedents of:" in err for err in auditor.errors))

    def test_catch_reveals_how_double_space_evolves(self):
        """Verify Check 5 catches 'reveals how  evolves'."""
        self._create_report("rep5.md", "Empirical data reveals how  evolves over long saecula (Author, 2026).\n" * 55)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("reveals how  evolves" in err for err in auditor.errors))

    def test_catch_empty_table_column_header(self):
        """Verify Check 5 catches '|  Indicator / Focus |'."""
        self._create_report("rep6.md", "|  Indicator / Focus | Detail |\n|---|---|\n| Metric | Value |\n" + "Data row line (Author, 2026).\n" * 53)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("Empty leading table column header variable" in err for err in auditor.errors))

    def test_catch_bracket_placeholders(self):
        """Verify Check 5 catches '<INSERT>' and '[TOPIC]'."""
        self._create_report("rep7.md", "Sample report with <INSERT> and [TOPIC] variable placeholders (Author, 2026).\n" * 55)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("Unpopulated bracket placeholder" in err for err in auditor.errors))
        self.assertTrue(any("Unpopulated square-bracket placeholder" in err for err in auditor.errors))

    def test_clean_template_prose_passes(self):
        """Verify fully populated clean template prose passes Check 5."""
        clean_content = """# Executive Summary: Generational Dynamics
This section evaluates generational dynamics regarding economic policy and institutional shifts across saeculum.
It reveals how institutional trust evolves systematically across the 80-100 year Saeculum.
Mechanisms that drive turning transitions in macroeconomics.
| Economic Indicator / Focus | Detail |
The Historical Antecedents of Civil Wars: How prior crisis climaxes reset society.
Fully detailed discussion without any unpopulated tags (Strauss & Howe, 1997).
""" + "Substantive line content with valid citations (Howe, 2020).\n" * 50
        self._create_report("clean.md", clean_content)
        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertTrue(passed)
        self.assertEqual(len(auditor.errors), 0)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(SyntheticNegativeCheck4Test))
    suite.addTest(loader.loadTestsFromTestCase(SyntheticNegativeCheck5Test))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
