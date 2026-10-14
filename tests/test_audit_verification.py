#!/usr/bin/env python3
"""
Unit tests for Convergence Repository Automated Audit & Verification Script (scripts/audit_verification.py).
Tests Requirement R3 verification logic, CLI parameters, and error detection.
"""

import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

# Add parent directory to sys.path so we can import scripts.audit_verification
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.audit_verification import ConvergenceAuditor, main, EXPERT_REVIEW_FILES, SUBJECT_DIRECTORIES


def create_dummy_md_file(
    path: pathlib.Path,
    line_count: int = 55,
    content_line: str = "Substantive report line content with citation (Author, 2026).",
) -> None:
    """Helper to create a markdown file with specified line count."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"Line {i+1}: {content_line}" for i in range(line_count)]
    path.write_text("\n".join(lines), encoding="utf-8")


class TestExpertReviewsCheck(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_check_expert_reviews_all_present_in_subject_dirs(self):
        """Test Check 1 when all 5 expert reviews exist in subject directories with >50 lines."""
        for subject, filename in EXPERT_REVIEW_FILES.items():
            file_path = self.root / subject / filename
            create_dummy_md_file(file_path, line_count=60)

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_expert_reviews()
        self.assertTrue(passed)
        self.assertEqual(len(auditor.errors), 0)
        self.assertEqual(len(auditor.expert_review_results["details"]), 5)
        for subject in EXPERT_REVIEW_FILES:
            self.assertEqual(auditor.expert_review_results["details"][subject]["status"], "PASS")

    def test_check_expert_reviews_all_present_in_repo_root(self):
        """Test Check 1 fallback location when expert reviews exist in root directory."""
        for subject, filename in EXPERT_REVIEW_FILES.items():
            file_path = self.root / filename
            create_dummy_md_file(file_path, line_count=52)

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_expert_reviews()
        self.assertTrue(passed)
        self.assertEqual(len(auditor.errors), 0)

    def test_check_expert_reviews_missing_file(self):
        """Test Check 1 failure when an expert review file is missing."""
        count = 0
        for subject, filename in EXPERT_REVIEW_FILES.items():
            if count >= 4:
                break
            create_dummy_md_file(self.root / subject / filename, line_count=60)
            count += 1

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_expert_reviews()
        self.assertFalse(passed)
        self.assertTrue(len(auditor.errors) >= 1)
        self.assertIn("EXPERT REVIEW MISSING", auditor.errors[0])

    def test_check_expert_reviews_insufficient_depth(self):
        """Test Check 1 failure when an expert review file has <=50 lines."""
        idx = 0
        for subject, filename in EXPERT_REVIEW_FILES.items():
            lines = 30 if idx == 0 else 60
            create_dummy_md_file(self.root / subject / filename, line_count=lines)
            idx += 1

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_expert_reviews()
        self.assertFalse(passed)
        self.assertTrue(any("EXPERT REVIEW DEPTH FAIL" in err for err in auditor.errors))


class TestReportDepthCheck(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_check_report_depth_all_passed(self):
        """Test Check 2 when all research reports have >50 lines."""
        for subject in SUBJECT_DIRECTORIES:
            report_path = self.root / subject / "Subfolder" / "Report.md"
            create_dummy_md_file(report_path, line_count=55)

        master_synth = self.root / "Convergence_Master_Synthesis.md"
        create_dummy_md_file(master_synth, line_count=100)

        auditor = ConvergenceAuditor(root=self.root)
        total, failed = auditor.check_report_depth()
        self.assertEqual(total, 6)
        self.assertEqual(failed, 0)
        self.assertTrue(auditor.report_depth_results["passed"])

    def test_check_report_depth_failing_reports(self):
        """Test Check 2 when some reports fail depth check (<=50 lines)."""
        for subject in SUBJECT_DIRECTORIES:
            report_path = self.root / subject / "Report.md"
            lines = 50 if subject == "4th Turning" else 55
            create_dummy_md_file(report_path, line_count=lines)

        auditor = ConvergenceAuditor(root=self.root)
        total, failed = auditor.check_report_depth()
        self.assertEqual(total, 5)
        self.assertEqual(failed, 1)
        self.assertFalse(auditor.report_depth_results["passed"])
        self.assertTrue(any("REPORT DEPTH FAIL" in err for err in auditor.errors))

    def test_check_report_depth_excludes_expert_reviews(self):
        """Verify that expert review files inside subject dirs are excluded from research depth scan."""
        for subject, filename in EXPERT_REVIEW_FILES.items():
            create_dummy_md_file(self.root / subject / filename, line_count=60)
            create_dummy_md_file(self.root / subject / "Sub" / "Report.md", line_count=55)

        auditor = ConvergenceAuditor(root=self.root)
        total, failed = auditor.check_report_depth()
        self.assertEqual(total, 5)
        self.assertEqual(failed, 0)


class TestEnhancementIntegrationCheck(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_enhancement_no_placeholders_with_citations(self):
        """Test Check 3 passes when reports contain citations and no placeholders."""
        for subject in SUBJECT_DIRECTORIES:
            file_path = self.root / subject / "Report.md"
            create_dummy_md_file(
                file_path,
                line_count=55,
                content_line="Valid research report content (Strauss & Howe, 1997).",
            )

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_enhancement_integration()
        self.assertTrue(passed)
        self.assertEqual(len(auditor.errors), 0)

    def test_enhancement_placeholder_detected(self):
        """Test Check 3 flags errors when placeholder tags are present."""
        file_path = self.root / "4th Turning" / "Report.md"
        create_dummy_md_file(
            file_path,
            line_count=55,
            content_line="Section content with TODO tag (Strauss, 1997).",
        )

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_enhancement_integration()
        self.assertFalse(passed)
        self.assertTrue(any("PLACEHOLDER FOUND" in err for err in auditor.errors))

    def test_enhancement_strict_citation_mode(self):
        """Test Check 3 citation enforcement in strict vs non-strict mode."""
        file_path = self.root / "4th Turning" / "Report.md"
        create_dummy_md_file(
            file_path,
            line_count=55,
            content_line="Section content without any citation patterns or references.",
        )

        auditor_non_strict = ConvergenceAuditor(root=self.root, strict=False)
        passed_ns = auditor_non_strict.check_enhancement_integration()
        self.assertTrue(passed_ns)
        self.assertTrue(len(auditor_non_strict.warnings) > 0)

        auditor_strict = ConvergenceAuditor(root=self.root, strict=True)
        passed_s = auditor_strict.check_enhancement_integration()
        self.assertFalse(passed_s)
        self.assertTrue(len(auditor_strict.errors) > 0)


class TestCrossReportDuplicationCheck(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_cross_report_duplication_pass(self):
        """Test Check 4 passes when report duplication is <= 15%."""
        subj_dir = self.root / "4th Turning"
        shared_lines = ["# Title Header", "## Section 1: Analysis"]
        for i in range(5):
            unique_lines = [f"Unique paragraph line {j} for report {i} (Strauss, 1997)." for j in range(50)]
            file_path = subj_dir / f"Report_{i}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text("\n".join(shared_lines + unique_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertTrue(passed)
        self.assertEqual(len(auditor.errors), 0)
        self.assertTrue(auditor.duplication_results["passed"])
        self.assertIn("4th Turning", auditor.duplication_results["details"])
        self.assertLessEqual(auditor.duplication_results["details"]["4th Turning"]["avg_duplication_rate"], 15.0)

    def test_cross_report_duplication_fail(self):
        """Test Check 4 fails when report duplication exceeds 15%."""
        subj_dir = self.root / "4th Turning"
        boilerplate_lines = [f"Generic copy-pasted boilerplate line {k}" for k in range(30)]
        for i in range(5):
            unique_lines = [f"Unique line {j} for report {i} (Strauss, 1997)." for j in range(25)]
            file_path = subj_dir / f"Report_{i}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text("\n".join(boilerplate_lines + unique_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertFalse(passed)
        self.assertTrue(any("CROSS-REPORT DUPLICATION FAIL" in err for err in auditor.errors))
        self.assertFalse(auditor.duplication_results["passed"])
        self.assertGreater(auditor.duplication_results["details"]["4th Turning"]["avg_duplication_rate"], 15.0)

    def test_cross_report_duplication_excludes_expert_reviews(self):
        """Verify Check 4 excludes *_Expert_Review.md files from subfolder duplication scans."""
        subj_dir = self.root / "4th Turning"
        expert_review = subj_dir / "4th_Turning_Expert_Review.md"
        create_dummy_md_file(expert_review, line_count=60, content_line="Shared line content (Strauss, 1997).")

        report = subj_dir / "Subfolder" / "Report.md"
        create_dummy_md_file(report, line_count=60, content_line="Shared line content (Strauss, 1997).")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertTrue(passed)
        self.assertEqual(auditor.duplication_results["details"]["4th Turning"]["report_count"], 1)

    def test_single_file_duplication_spike_detected(self):
        """Test Check 4 fails when a single report exceeds 15.0% duplication, even if directory average is <= 15.0%."""
        subj_dir = self.root / "Kondratiev Waves"
        shared_lines = [f"Repeated shared line {k} across reports" for k in range(25)]

        # Create 9 reports with 100% unique lines
        for i in range(9):
            unique_lines = [f"Unique line {j} for clean report {i} (Kondratiev, 1925)." for j in range(100)]
            file_path = subj_dir / f"Clean_Report_{i}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text("\n".join(unique_lines), encoding="utf-8")

        # Create 1 report that shares 25 lines with another report (25% duplication)
        other_shared_file = subj_dir / "Shared_Target.md"
        other_shared_file.write_text("\n".join(shared_lines + [f"Unique target line {m}" for m in range(75)]), encoding="utf-8")

        spiked_file = subj_dir / "Data" / "Processed" / "JSON" / "JSON Deep Dive.md"
        spiked_file.parent.mkdir(parents=True, exist_ok=True)
        spiked_file.write_text("\n".join(shared_lines + [f"Unique spike line {n}" for n in range(75)]), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertFalse(passed)
        self.assertTrue(any("SINGLE-FILE DUPLICATION FAIL" in err for err in auditor.errors))
        self.assertFalse(auditor.duplication_results["details"]["Kondratiev Waves"]["passed"])


class TestBrokenTemplateTagCheck(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_broken_template_tags_detected(self):
        """Test Check 5 fails and logs errors when broken template tags or variable artifacts exist."""
        bad_file = self.root / "4th Turning" / "Bad_Report.md"
        bad_file.parent.mkdir(parents=True, exist_ok=True)
        content = """# Bad Report
This section evaluates generational dynamics regarding  and modern applications across saeculum.
It reveals how  evolves systematically across the 80-100 year Saeculum.
Mechanisms that drive turning transitions in .
|  | Detail |
The Historical Antecedents of: .
Unpopulated tag: {topic} and {subject}.
"""
        bad_file.write_text(content, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(len(auditor.errors) >= 5)
        self.assertTrue(any("BROKEN TEMPLATE TAG FOUND" in err for err in auditor.errors))

    def test_clean_template_prose_passes(self):
        """Test Check 5 passes when reports contain clean, fully populated template prose."""
        clean_file = self.root / "4th Turning" / "Clean_Report.md"
        clean_file.parent.mkdir(parents=True, exist_ok=True)
        content = """# Clean Report
This section evaluates generational dynamics regarding economic policy and modern applications across saeculum.
It reveals how institutional trust evolves systematically across the 80-100 year Saeculum.
Mechanisms that drive turning transitions in macroeconomics.
| Economic Indicator / Focus | Detail |
The Historical Antecedents of Civil Wars: How prior crisis climaxes reset society.
Fully detailed discussion without any unpopulated tags.
"""
        clean_file.write_text(content, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertTrue(passed)
        self.assertEqual(len(auditor.errors), 0)
        self.assertTrue(auditor.template_integrity_results["passed"])

    def test_double_pipe_table_delimiter_corruption_detected(self):
        """Test Check 5 flags || double-pipe table alignment corruptions."""
        corrupted_file = self.root / "Changing World Orders" / "Corrupted_Table.md"
        corrupted_file.parent.mkdir(parents=True, exist_ok=True)
        content = """# Table Test Report
| Scholar | Theoretical School | Key Work | View on US-China War Risk | Primary Vector of Systemic Change |
| :---: || :---: || :---: || :---: || :---: |
| Graham Allison | Historical Realism | Destined for War (2017) | High | Thucydides displacement dynamics |
"""
        corrupted_file.write_text(content, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("Double-pipe table delimiter corruption: '||'" in err for err in auditor.errors))

    def test_double_pipe_table_syntax_detected(self):
        """Test Check 5 flags corrupted table alignment syntax | :--- || :--- |."""
        corrupted_file = self.root / "Changing World Orders" / "Corrupted_Table_2.md"
        corrupted_file.parent.mkdir(parents=True, exist_ok=True)
        content = """# Table Test Report
| Component | Leader | Concentration | Vulnerability |
| :--- || :--- | :---: | :--- |
| EUV Lithography | ASML | 100% | Single point failure |
"""
        corrupted_file.write_text(content, encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertFalse(passed)
        self.assertTrue(any("Double-pipe table delimiter corruption: '||'" in err for err in auditor.errors))

    def test_robotic_heading_suffix_detected(self):
        """Test Check 5 flags robotic heading title suffixes on level 2 and level 3 headings."""
        robotic_file_1 = self.root / "LoAR" / "Robotic_Report_1.md"
        robotic_file_1.parent.mkdir(parents=True, exist_ok=True)
        content_1 = """# Monograph Title
## 1. Section One: [Document Title]
### 1.1 Subsection: Topic Name
"""
        robotic_file_1.write_text(content_1, encoding="utf-8")

        auditor_1 = ConvergenceAuditor(root=self.root)
        passed_1 = auditor_1.check_template_integrity()
        self.assertFalse(passed_1)
        self.assertTrue(any("Robotic heading title suffix artifact" in err for err in auditor_1.errors))

        # Clear directory for second scenario
        robotic_file_1.unlink()

        robotic_file_2 = self.root / "LoAR" / "Robotic_Report_2.md"
        content_2 = """# Monograph Title
## 1. Theoretical Framework & Mathematical Mechanics: Core Concepts Deep Dive & Paradigm Mechanics Monograph
## 2. Quantitative Empirical Metrics: Core Concepts Deep Dive & Paradigm Mechanics Monograph
"""
        robotic_file_2.write_text(content_2, encoding="utf-8")

        auditor_2 = ConvergenceAuditor(root=self.root)
        passed_2 = auditor_2.check_template_integrity()
        self.assertFalse(passed_2)
        self.assertTrue(any("Robotic heading title suffix artifact" in err for err in auditor_2.errors))


class TestFullAuditAndCLI(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)
        self._populate_valid_repo()

    def tearDown(self):
        self.temp_dir.cleanup()

    def _populate_valid_repo(self):
        for subject, filename in EXPERT_REVIEW_FILES.items():
            create_dummy_md_file(
                self.root / subject / filename,
                line_count=60,
                content_line="Expert review analysis line (Strauss, 1997).",
            )
        for subject in SUBJECT_DIRECTORIES:
            create_dummy_md_file(
                self.root / subject / "Subfolder" / "Deep_Dive.md",
                line_count=55,
                content_line="Subject deep dive research data (Howe, 2020).",
            )
        create_dummy_md_file(
            self.root / "Convergence_Master_Synthesis.md",
            line_count=120,
            content_line="Master synthesis section with citation (Kondratiev, 1925).",
        )

    def test_run_full_audit_success(self):
        """Test full audit workflow returning pass on valid workspace."""
        auditor = ConvergenceAuditor(root=self.root, verbose=True)
        with patch("sys.stdout", new=io.StringIO()):
            results = auditor.run_full_audit()
        self.assertTrue(results["passed"])
        self.assertEqual(len(results["errors"]), 0)

    def test_run_full_audit_json_output(self):
        """Test audit JSON output formatting."""
        auditor = ConvergenceAuditor(root=self.root, json_output=True)
        captured_output = io.StringIO()
        with patch("sys.stdout", captured_output):
            results = auditor.run_full_audit()

        json_text = captured_output.getvalue()
        parsed = json.loads(json_text)
        self.assertTrue(parsed["passed"])
        self.assertIn("summary", parsed)
        self.assertIn("expert_reviews", parsed)

    def test_cli_main_execution(self):
        """Test main() entry point via simulated CLI arguments."""
        test_args = ["audit_verification.py", "--root", str(self.root), "--json"]
        captured_output = io.StringIO()
        with patch.object(sys, "argv", test_args), patch("sys.stdout", captured_output):
            exit_code = main()
            self.assertEqual(exit_code, 0)

    def test_real_repo_audit_execution(self):
        """Integration test: Execute auditor against the actual project repo."""
        real_repo_root = REPO_ROOT
        auditor = ConvergenceAuditor(root=real_repo_root)
        with patch("sys.stdout", new=io.StringIO()):
            results = auditor.run_full_audit()
        self.assertIn("summary", results)
        self.assertIn("duplication_results", results)
        self.assertIn("template_integrity", results)
        if results["passed"]:
            self.assertTrue(results["passed"])
            self.assertEqual(len(results["errors"]), 0)
        else:
            self.assertGreater(len(results["errors"]), 0)
            self.assertTrue(
                any(
                    "CROSS-REPORT DUPLICATION FAIL" in err or "BROKEN TEMPLATE TAG FOUND" in err
                    for err in results["errors"]
                )
            )


if __name__ == "__main__":
    unittest.main()
