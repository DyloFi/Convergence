#!/usr/bin/env python3
"""
Empirical Stress Test Harness for scripts/audit_verification.py
Tests edge conditions, false positives, false negatives, non-UTF8, line counting, regexes.
"""

import os
import sys
import tempfile
import pathlib
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.audit_verification import ConvergenceAuditor, EXPERT_REVIEW_FILES, SUBJECT_DIRECTORIES


class EmpiricalStressTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _setup_valid_minimal_repo(self):
        """Creates a minimal passing repo layout."""
        for subject, filename in EXPERT_REVIEW_FILES.items():
            path = self.root / subject / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join([f"Line {i} (Smith, 2020)" for i in range(60)]), encoding="utf-8")

        for subject in SUBJECT_DIRECTORIES:
            path = self.root / subject / "Report.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join([f"Report content line {i} (Jones, 2021)" for i in range(60)]), encoding="utf-8")

        master = self.root / "Convergence_Master_Synthesis.md"
        master.write_text("\n".join([f"Master line {i} https://example.com" for i in range(60)]), encoding="utf-8")

    def test_edge_1_blank_lines_bypass_depth_check(self):
        """Edge Case 1: 51 blank lines (newlines only) bypasses report depth check."""
        self._setup_valid_minimal_repo()
        blank_report = self.root / "4th Turning" / "Report.md"
        # Write 51 blank newlines
        blank_report.write_bytes(b"\n" * 51)

        auditor = ConvergenceAuditor(root=self.root)
        total, failed = auditor.check_report_depth()
        # Lines count is 51, so it passes check_report_depth even though content is completely empty!
        self.assertEqual(failed, 0, "51 blank newlines passed depth check!")
        print(f"[EDGE CASE 1 CONFIRMED] 51 blank newlines counted as {51} valid report lines.")

    def test_edge_2_line_endings_mac_and_windows(self):
        """Edge Case 2: CRLF vs LF line endings."""
        self._setup_valid_minimal_repo()
        crlf_report = self.root / "LoAR" / "Report.md"
        crlf_report.write_bytes(b"Line\r\n" * 55)

        auditor = ConvergenceAuditor(root=self.root)
        total, failed = auditor.check_report_depth()
        self.assertEqual(failed, 0)
        print("[EDGE CASE 2 PASSED] CRLF line endings handled correctly by splitlines().")

    def test_edge_3_non_utf8_binary_handling(self):
        """Edge Case 3: Files containing invalid UTF-8 bytes (e.g. latin1 / binary garbage)."""
        self._setup_valid_minimal_repo()
        bad_utf8_report = self.root / "Kondratiev Waves" / "Report.md"
        # Binary data with valid newlines and a citation pattern in ASCII bytes mixed with invalid UTF8 bytes 0xFF, 0xFE
        content = b"Header (Author, 2020)\n" + b"\xFF\xFE Invalid UTF-8 byte line\n" * 55
        bad_utf8_report.write_bytes(content)

        auditor = ConvergenceAuditor(root=self.root)
        res = auditor.run_full_audit()
        # errors="ignore" ignores invalid bytes, allowing audit to pass without throwing exception
        print(f"[EDGE CASE 3 TESTED] Non-UTF8 file passed without crash: errors count = {len(auditor.errors)}")

    def test_edge_4_placeholder_regex_gaps_and_false_positives(self):
        """Edge Case 4: Unmatched placeholders vs false positive placeholders."""
        self._setup_valid_minimal_repo()
        
        # Test 4a: Unmatched placeholders
        unmatched_file = self.root / "4th Turning" / "Report.md"
        unmatched_file.write_text(
            "\n".join([f"Line {i} [PLACEHOLDER] [WIP] [COMING SOON] [TO DO] <INSERT HERE> (Ref, 2020)" for i in range(55)]),
            encoding="utf-8"
        )
        
        auditor1 = ConvergenceAuditor(root=self.root)
        auditor1.check_enhancement_integration()
        # [PLACEHOLDER], [WIP], [COMING SOON], [TO DO], <INSERT HERE> are NOT detected by current PLACEHOLDER_PATTERNS
        print(f"[EDGE CASE 4a UNMATCHED PLACEHOLDERS] Errors found: {len(auditor1.errors)} (Expected 0 due to regex gap)")

        # Test 4b: False positive on Roman numeral XXX in historical text
        self._setup_valid_minimal_repo()
        roman_numeral_file = self.root / "Changing World Orders" / "Report.md"
        roman_numeral_file.write_text(
            "\n".join([f"Line {i}: In Chapter XXX, historical analysis shows... (Dalio, 2021)" for i in range(55)]),
            encoding="utf-8"
        )
        auditor2 = ConvergenceAuditor(root=self.root)
        auditor2.check_enhancement_integration()
        print(f"[EDGE CASE 4b FALSE POSITIVE] Roman Numeral XXX flagged as error: {auditor2.errors}")

    def test_edge_5_header_level_citations(self):
        """Edge Case 5: Citation header check for H1 (#) or H3 (###) headers."""
        self._setup_valid_minimal_repo()
        h3_file = self.root / "Technological Singularity" / "Report.md"
        # Uses ### References (H3) instead of ## References (H2)
        h3_file.write_text(
            "\n".join([f"Line {i}" for i in range(50)]) + "\n### References\n1. Kurzweil, R. (2005).\n52 lines",
            encoding="utf-8"
        )
        
        auditor_strict = ConvergenceAuditor(root=self.root, strict=True)
        auditor_strict.check_enhancement_integration()
        print(f"[EDGE CASE 5 CITATION HEADER H3] Flagged in strict mode: {auditor_strict.errors}")


if __name__ == "__main__":
    unittest.main()
