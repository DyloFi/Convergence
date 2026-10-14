#!/usr/bin/env python3
"""
Adversarial Edge-Case Test Harness for scripts/audit_verification.py
Tests:
1. Detection of short non-blank line counts (<51 lines).
2. Detection of missing reference headers / citations under strict mode.
3. Detection of placeholder text (TODO, TBD, FIXME, [INSERT, etc.).
4. Missing expert review files.
5. Blank lines vs non-blank lines count behavior.
6. Non-zero exit code on errors.
"""

import io
import os
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.audit_verification import (
    ConvergenceAuditor,
    EXPERT_REVIEW_FILES,
    SUBJECT_DIRECTORIES,
    main,
)


def populate_valid_mock_workspace(root: pathlib.Path):
    """Helper to set up a completely valid mock repo."""
    for subject, filename in EXPERT_REVIEW_FILES.items():
        file_path = root / subject / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"Line {i+1}: Valid expert review content (Author, 2026)." for i in range(60)]
        file_path.write_text("\n".join(lines), encoding="utf-8")

    for subject in SUBJECT_DIRECTORIES:
        file_path = root / subject / "Subfolder" / "Report.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"Line {i+1}: Substantive report line content with citation (Author, 2026)." for i in range(60)]
        file_path.write_text("\n".join(lines), encoding="utf-8")

    master_synth = root / "Convergence_Master_Synthesis.md"
    lines = [f"Line {i+1}: Master synthesis content (Kondratiev, 1925)." for i in range(100)]
    master_synth.write_text("\n".join(lines), encoding="utf-8")


class TestAdversarialEdgeCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)
        populate_valid_mock_workspace(self.root)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_short_non_blank_line_count_report(self):
        """Edge Case 1a: Report file with <51 non-blank lines (e.g. 50 total lines)."""
        target = self.root / "4th Turning" / "Subfolder" / "Report.md"
        lines = [f"Line {i+1}: Short report content (Author, 2026)." for i in range(50)]
        target.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            results = auditor.run_full_audit()

        self.assertFalse(results["passed"], "Audit should fail for 50 non-blank lines")
        self.assertTrue(any("[REPORT DEPTH FAIL]" in err for err in results["errors"]))

    def test_short_non_blank_line_count_with_blank_padding(self):
        """Edge Case 1b: Report with 80 total lines, but only 40 non-blank lines (40 whitespace lines)."""
        target = self.root / "LoAR" / "Subfolder" / "Report.md"
        content_lines = [f"Line {i+1}: Substantive line (Author, 2026)." for i in range(40)]
        blank_lines = ["   ", "", "\t", " \n "] * 10
        all_lines = content_lines + blank_lines
        target.write_text("\n".join(all_lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            results = auditor.run_full_audit()

        self.assertFalse(results["passed"], "Audit should fail when non-blank line count < 51")
        self.assertTrue(any("[REPORT DEPTH FAIL]" in err for err in results["errors"]))
        self.assertTrue(any("40 lines" in err for err in results["errors"]))

    def test_short_non_blank_line_count_expert_review(self):
        """Edge Case 1c: Expert review file with <51 non-blank lines."""
        target = self.root / "4th Turning" / "4th_Turning_Expert_Review.md"
        lines = [f"Line {i+1}: Short review (Author, 2026)." for i in range(30)]
        target.write_text("\n".join(lines), encoding="utf-8")

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            results = auditor.run_full_audit()

        self.assertFalse(results["passed"], "Audit should fail for expert review depth < 51 lines")
        self.assertTrue(any("[EXPERT REVIEW DEPTH FAIL]" in err for err in results["errors"]))

    def test_missing_reference_headers_and_citations_strict_mode(self):
        """Edge Case 2: Report lacking citation pattern or reference headers under --strict mode."""
        target = self.root / "Changing World Orders" / "Subfolder" / "Report.md"
        # 60 lines of plain text without citations, URLs, brackets, or reference section header
        lines = [f"Line {i+1}: Plain narrative text without any citations." for i in range(60)]
        target.write_text("\n".join(lines), encoding="utf-8")

        auditor_strict = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            results_strict = auditor_strict.run_full_audit()

        self.assertFalse(results_strict["passed"], "Audit should fail under strict mode when citations missing")
        self.assertTrue(any("[CITATION MISSING]" in err for err in results_strict["errors"]))

        auditor_non_strict = ConvergenceAuditor(root=self.root, strict=False)
        with patch("sys.stdout", new=io.StringIO()):
            results_non_strict = auditor_non_strict.run_full_audit()

        self.assertTrue(results_non_strict["passed"], "Audit should pass under non-strict mode when only warnings exist")
        self.assertTrue(any("[CITATION MISSING]" in warn for warn in results_non_strict["warnings"]))

    def test_placeholder_text_detection(self):
        """Edge Case 3: Report containing placeholder patterns (TODO, TBD, FIXME, [INSERT, etc.)."""
        placeholders = ["TODO", "TBD", "FIXME", "[INSERT DATA HERE]", "INSERT_DATA", "[Insert section]", "XXX", "TEMP"]

        for ph in placeholders:
            temp_root = pathlib.Path(tempfile.mkdtemp())
            populate_valid_mock_workspace(temp_root)

            target = temp_root / "Kondratiev Waves" / "Subfolder" / "Report.md"
            lines = [f"Line {i+1}: Research text (Kondratiev, 1925)." for i in range(55)]
            lines[25] = f"Need to update this section with {ph} soon."
            target.write_text("\n".join(lines), encoding="utf-8")

            auditor = ConvergenceAuditor(root=temp_root, strict=True)
            with patch("sys.stdout", new=io.StringIO()):
                results = auditor.run_full_audit()

            self.assertFalse(results["passed"], f"Audit should fail when placeholder '{ph}' is present")
            self.assertTrue(any("[PLACEHOLDER FOUND]" in err for err in results["errors"]), f"Failed to detect {ph}")

    def test_missing_expert_review_file(self):
        """Edge Case 4: Missing expert review file."""
        target = self.root / "Technological Singularity" / "Technological_Singularity_Expert_Review.md"
        target.unlink()

        auditor = ConvergenceAuditor(root=self.root, strict=True)
        with patch("sys.stdout", new=io.StringIO()):
            results = auditor.run_full_audit()

        self.assertFalse(results["passed"], "Audit should fail when expert review file is missing")
        self.assertTrue(any("[EXPERT REVIEW MISSING]" in err for err in results["errors"]))

    def test_cli_exit_code_on_failure(self):
        """Edge Case 5: Verify main() returns non-zero exit code (1) when audit fails."""
        # Cause a failure by putting TODO in a report
        target = self.root / "4th Turning" / "Subfolder" / "Report.md"
        target.write_text("TODO: Fill in report\n" * 60, encoding="utf-8")

        test_args = ["audit_verification.py", "--root", str(self.root), "--strict"]
        captured_output = io.StringIO()
        with patch.object(sys, "argv", test_args), patch("sys.stdout", captured_output):
            exit_code = main()

        self.assertEqual(exit_code, 1, "CLI main() should return exit code 1 on audit failure")


if __name__ == "__main__":
    unittest.main()
