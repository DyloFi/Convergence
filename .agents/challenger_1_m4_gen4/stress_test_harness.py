#!/usr/bin/env python3
"""
Stress Test & Edge Case Harness for Convergence Audit Verification Suite
Agent: Challenger 1 (challenger_1_m4_gen4)
Target: scripts/audit_verification.py
"""

import pathlib
import sys
import tempfile
import unittest
from typing import Dict, List, Tuple

# Path setup
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.audit_verification import ConvergenceAuditor, EXPERT_REVIEW_FILES, SUBJECT_DIRECTORIES, BROKEN_TEMPLATE_PATTERNS

class SyntheticEdgeCaseTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_minimal_valid_workspace(self):
        """Helper to create a fully valid mock workspace structure."""
        for subject, filename in EXPERT_REVIEW_FILES.items():
            f = self.root / subject / filename
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text("\n".join([f"Expert review content line {i} (Strauss, 1997)." for i in range(60)]))

        for subject in SUBJECT_DIRECTORIES:
            f = self.root / subject / "Report_01.md"
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text("\n".join([f"Unique report line {i} for {subject} (Howe, 2020)." for i in range(55)]))

        master = self.root / "Convergence_Master_Synthesis.md"
        master.write_text("\n".join([f"Master synthesis line {i} (Kondratiev, 1925)." for i in range(60)]))

    def test_check4_synthetic_high_duplication(self):
        """Synthetic Scenario: Verify Check 4 catches >15.0% duplicate line overlap."""
        self._create_minimal_valid_workspace()
        
        # Inject 20 shared duplicate lines into 4th Turning reports (out of 50 total lines = 40% duplication)
        shared_lines = [f"Shared duplicate line {i}" for i in range(20)]
        for r_idx in range(3):
            file_path = self.root / "4th Turning" / f"Dup_Report_{r_idx}.md"
            unique_lines = [f"Unique content line {j} for report {r_idx} (Strauss, 1997)." for j in range(30)]
            file_path.write_text("\n".join(shared_lines + unique_lines))

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertFalse(passed, "Check 4 must fail when duplication exceeds 15.0%")
        self.assertTrue(any("CROSS-REPORT DUPLICATION FAIL" in err for err in auditor.errors))
        self.assertIn("4th Turning", auditor.duplication_results["details"])
        dup_rate = auditor.duplication_results["details"]["4th Turning"]["avg_duplication_rate"]
        self.assertGreater(dup_rate, 15.0, f"Expected dup rate > 15.0%, got {dup_rate}%")
        print(f"  [PASS] Synthetic Check 4 High Duplication Test: Caught {dup_rate:.2f}% duplication rate.")

    def test_check4_borderline_duplication(self):
        """Synthetic Scenario: Verify Check 4 behavior near 15.0% threshold boundary."""
        self._create_minimal_valid_workspace()
        
        # Replace 4th Turning reports with 14% duplication (below threshold)
        subj_dir = self.root / "4th Turning"
        for old_file in subj_dir.glob("*.md"):
            if not old_file.name.endswith("_Expert_Review.md"):
                old_file.unlink()

        # 7 shared lines out of 50 total lines = 14% duplication
        shared_lines = [f"Borderline shared line {i}" for i in range(7)]
        for r_idx in range(4):
            file_path = subj_dir / f"Borderline_{r_idx}.md"
            unique_lines = [f"Unique paragraph line {j} in report {r_idx} (Howe, 1997)." for j in range(43)]
            file_path.write_text("\n".join(shared_lines + unique_lines))

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_cross_report_duplication()
        self.assertTrue(passed, "Check 4 should pass when duplication is <= 15.0%")
        dup_rate = auditor.duplication_results["details"]["4th Turning"]["avg_duplication_rate"]
        self.assertLessEqual(dup_rate, 15.0)
        print(f"  [PASS] Synthetic Check 4 Borderline Duplication Test: Passed {dup_rate:.2f}% duplication rate.")

    def test_check5_all_10_broken_template_patterns(self):
        """Synthetic Scenario: Verify Check 5 detects ALL 10 broken template tag patterns individually."""
        test_cases: List[Tuple[str, str]] = [
            ("Pattern 1: regarding  and", "regards regarding  and dynamic factors"),
            ("Pattern 2: reveals how  evolves", "This study reveals how  evolves over time"),
            ("Pattern 3: how  evolves", "Explores how  evolves in cycles"),
            ("Pattern 4: transitions in .", "Analyses turning transitions in . Next chapter"),
            ("Pattern 5: Antecedents of: .", "The Historical Antecedents of: ."),
            ("Pattern 6: |  |", "|  | Table Cell Detail |"),
            ("Pattern 7: {topic}", "Unfilled variable {topic} in text"),
            ("Pattern 8: in  .", "Systemic shifts in  . End of sentence"),
            ("Pattern 9: <INSERT>", "Placeholder <INSERT> here"),
            ("Pattern 10: [VARIABLE]", "Placeholder [VARIABLE] here"),
        ]

        for idx, (label, snippet) in enumerate(test_cases, start=1):
            with self.subTest(pattern_idx=idx, label=label):
                temp_root = pathlib.Path(tempfile.mkdtemp())
                try:
                    # Setup valid base
                    for subject, filename in EXPERT_REVIEW_FILES.items():
                        f = temp_root / subject / filename
                        f.parent.mkdir(parents=True, exist_ok=True)
                        f.write_text("\n".join([f"Line {i} (Citation, 2020)." for i in range(60)]))

                    bad_file = temp_root / "4th Turning" / f"Broken_Pattern_{idx}.md"
                    valid_lines = [f"Valid text line {i} (Strauss, 1997)." for i in range(50)]
                    bad_file.write_text("\n".join(valid_lines + [snippet]))

                    auditor = ConvergenceAuditor(root=temp_root)
                    passed = auditor.check_template_integrity()
                    self.assertFalse(passed, f"Check 5 failed to detect pattern {idx}: {label}")
                    self.assertTrue(
                        any("BROKEN TEMPLATE TAG FOUND" in err for err in auditor.errors),
                        f"Expected BROKEN TEMPLATE TAG FOUND error for pattern {idx}"
                    )
                    print(f"  [PASS] Synthetic Check 5 Pattern {idx} ({label}): Detected.")
                finally:
                    import shutil
                    shutil.rmtree(temp_root, ignore_errors=True)

    def test_check5_false_positives_not_triggered(self):
        """Synthetic Scenario: Verify Check 5 does NOT trigger false positives on valid markdown prose."""
        self._create_minimal_valid_workspace()
        
        valid_prose_file = self.root / "4th Turning" / "Valid_Prose.md"
        content = """# Valid Research Report (Strauss & Howe, 1997)

## Historical Antecedents of: How Generational Dynamics Evolve
This section examines the historical antecedents of: how generational cycles function.

|  Header One  |  Header Two  |
| :--- | :--- |
| Cell 1 | Cell 2 |

The economic transitions in Germany during the 1930s (Howe, 2020).
"""
        lines = [line for line in content.splitlines() if line.strip()]
        # Expand lines to > 50
        lines.extend([f"Substantive analytical line {i} (Strauss, 1997)." for i in range(45)])
        valid_prose_file.write_text("\n".join(lines))

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_template_integrity()
        self.assertTrue(passed, "Check 5 raised false positives on valid prose!")
        self.assertEqual(len(auditor.errors), 0)
        print("  [PASS] Synthetic Check 5 False Positive Resistance Test: No false positives raised.")

    def test_check3_placeholder_and_strict_citations(self):
        """Synthetic Scenario: Verify Check 3 placeholder detection and strict citation enforcement."""
        self._create_minimal_valid_workspace()

        # Test Placeholder Detection
        ph_file = self.root / "LoAR" / "Placeholder_Report.md"
        ph_file.write_text("\n".join([f"Line {i} TODO tag (Kurzweil, 2005)." for i in range(55)]))

        auditor = ConvergenceAuditor(root=self.root)
        passed = auditor.check_enhancement_integration()
        self.assertFalse(passed)
        self.assertTrue(any("PLACEHOLDER FOUND" in err for err in auditor.errors))
        print("  [PASS] Synthetic Check 3 Placeholder Detection: Correctly caught TODO.")

        # Test Strict Citation Missing
        ph_file.unlink()
        nocit_file = self.root / "LoAR" / "No_Citation_Report.md"
        nocit_file.write_text("\n".join([f"Generic sentence line {i} without citations." for i in range(55)]))

        auditor_strict = ConvergenceAuditor(root=self.root, strict=True)
        passed_strict = auditor_strict.check_enhancement_integration()
        self.assertFalse(passed_strict)
        self.assertTrue(any("CITATION MISSING" in err for err in auditor_strict.errors))
        print("  [PASS] Synthetic Check 3 Strict Citation Mode: Correctly caught missing citations.")

    def test_check1_and_check2_failures(self):
        """Synthetic Scenario: Verify Check 1 and Check 2 fail on missing files and insufficient depth."""
        self._create_minimal_valid_workspace()

        # Truncate one expert review file
        er_file = self.root / "4th Turning" / "4th_Turning_Expert_Review.md"
        er_file.write_text("Short content\nLine 2\n")

        auditor = ConvergenceAuditor(root=self.root)
        passed_c1 = auditor.check_expert_reviews()
        self.assertFalse(passed_c1)
        self.assertTrue(any("EXPERT REVIEW DEPTH FAIL" in err for err in auditor.errors))
        print("  [PASS] Synthetic Check 1 Expert Review Depth Fail: Correctly caught.")

        # Truncate research report file
        auditor.errors.clear()
        rep_file = self.root / "Kondratiev Waves" / "Report_01.md"
        rep_file.write_text("Only 10 lines of research report text.\n" * 10)

        total, failed = auditor.check_report_depth()
        self.assertGreater(failed, 0)
        self.assertTrue(any("REPORT DEPTH FAIL" in err for err in auditor.errors))
        print("  [PASS] Synthetic Check 2 Report Depth Fail: Correctly caught short report.")


if __name__ == "__main__":
    print("=================================================================")
    print("     SYNTHETIC STRESS TEST & EDGE CASE HARNESS EXECUTION         ")
    print("=================================================================")
    unittest.main()
