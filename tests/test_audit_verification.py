#!/usr/bin/env python3
"""
Unit, integration, and regression test suite for Convergence Repository Automated Audit
& Verification Suite (scripts/audit_verification.py).

Tests:
1. Document Type Requirements (drops arbitrary 50-line rule, enforces document-type profiles)
2. Deduplication Engine (exact SHA256 file hash, paragraph duplication, near-duplicate similarity)
3. Boilerplate and Template Integrity (analytical-focus boilerplate, broken template tags, robotic headings)
4. Repeated Headings Caps (limits identical non-standard section headings)
5. Citations, URLs, DOIs, and Claim Register Coverage (detects forbidden local file:/// URLs, missing dossiers)
6. Mathematical Consistency & KaTeX Rendering (stripped dollar cells, PID leaks, malformed frac macros)
7. Finding Contract Integrity (every finding must have file, line, rule, severity, and non-empty excerpt)
8. Deliberately Invalid Documents from Real Repository Defects (regression tests)
9. Full Audit & CLI Workflow
"""

import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

# Ensure project root is on sys.path
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.audit_verification import ConvergenceAuditor, AuditFinding, main, EXPERT_REVIEW_FILES


def create_test_file(path: pathlib.Path, content: str) -> pathlib.Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


class TestDocumentTypeRequirements(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_classification_by_document_type(self):
        auditor = ConvergenceAuditor(root=self.root)
        self.assertEqual(auditor.classify_document("Convergence_Master_Synthesis.md"), "synthesis")
        self.assertEqual(auditor.classify_document("4th Turning/4th_Turning_Expert_Review.md"), "expert_review")
        self.assertEqual(auditor.classify_document("Kondratiev Waves/Kondratiev Waves Overview.md"), "overview")
        self.assertEqual(auditor.classify_document("Changing World Orders/Foundations/01_Empirical.md"), "dossier")
        self.assertEqual(auditor.classify_document("README.md"), "readme")

    def test_dossier_short_word_count_fails_regardless_of_lines(self):
        # A file with 60 lines but only 60 words (< 250 words) should fail document type requirements
        dossier_path = self.root / "4th Turning" / "Analysis" / "Short_Dossier.md"
        content = "\n".join([f"Line {i}: test word" for i in range(60)])
        create_test_file(dossier_path, content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_document_type_requirements()
        
        errors = [f for f in auditor.findings if f.rule == "doc_type_dossier_insufficient_depth"]
        self.assertTrue(len(errors) >= 1)
        self.assertEqual(errors[0].severity, "ERROR")
        self.assertTrue(len(errors[0].excerpt) > 0)

    def test_dossier_adequate_word_count_passes_without_50_line_rule(self):
        # A file with only 20 lines but 300 words passes (50-line rule dropped)
        dossier_path = self.root / "4th Turning" / "Analysis" / "Dense_Dossier.md"
        words = ["word" for _ in range(320)]
        content = "\n".join([" ".join(words[i:i+20]) for i in range(0, 320, 20)])
        create_test_file(dossier_path, content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_document_type_requirements()
        
        dossier_errors = [f for f in auditor.findings if f.file == "4th Turning/Analysis/Dense_Dossier.md"]
        self.assertEqual(len(dossier_errors), 0)

    def test_missing_expert_review_fails(self):
        # When an expert review is missing, it should record a doc_type_expert_review_missing error
        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_document_type_requirements()
        missing_errors = [f for f in auditor.findings if f.rule == "doc_type_expert_review_missing"]
        self.assertEqual(len(missing_errors), 5)


class TestDeduplicationEngine(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_exact_file_hash_duplicate_detected(self):
        content = "# Identical File\n\nThis is identical content across two files for testing hash duplication.\n" * 5
        create_test_file(self.root / "Pillar1" / "FileA.md", content)
        create_test_file(self.root / "Pillar2" / "FileB.md", content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_deduplication()

        hash_findings = [f for f in auditor.findings if f.rule == "exact_file_duplicate"]
        self.assertTrue(len(hash_findings) >= 2)
        for finding in hash_findings:
            self.assertEqual(finding.severity, "ERROR")
            self.assertTrue(finding.excerpt.startswith("SHA256:"))

    def test_paragraph_level_duplicate_detected(self):
        para = "This is a substantive quantitative paragraph explaining cross-cycle dynamics with forty distinct analytical terms that repeats across distinct dossiers verbatim without variation."
        file_a = f"# File A\n\n{para}\n\nUnique section A content with additional words."
        file_b = f"# File B\n\nUnique section B content.\n\n{para}\n\nDifferent conclusions."
        create_test_file(self.root / "Pillar1" / "FileA.md", file_a)
        create_test_file(self.root / "Pillar2" / "FileB.md", file_b)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_deduplication()

        para_findings = [f for f in auditor.findings if f.rule == "paragraph_duplicate"]
        self.assertTrue(len(para_findings) >= 2)
        for finding in para_findings:
            self.assertEqual(finding.severity, "WARNING")
            self.assertTrue(len(finding.excerpt) > 0)

    def test_near_duplicate_similarity_detected(self):
        vocabulary = ["macroeconomic", "hegemonic", "transition", "stochastic", "volatility", "regime", "structural", "paradigm"]
        base_words = [vocabulary[i % len(vocabulary)] for i in range(50)]
        file_a = " ".join(base_words) + " alpha beta gamma"
        file_b = " ".join(base_words) + " delta epsilon zeta"
        create_test_file(self.root / "Pillar1" / "SimilarA.md", file_a)
        create_test_file(self.root / "Pillar2" / "SimilarB.md", file_b)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_deduplication()

        sim_findings = [f for f in auditor.findings if f.rule == "high_similarity_report"]
        self.assertTrue(len(sim_findings) >= 2)
        for finding in sim_findings:
            self.assertEqual(finding.severity, "WARNING")


class TestTemplateAndBoilerplate(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_analytical_focus_boilerplate_detected(self):
        content = "# Research Report\n\n- Analytical Focus: Macroeconomic volatility and empirical cycles.\n\nMore details."
        create_test_file(self.root / "4th Turning" / "Report.md", content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_template_and_boilerplate()

        bp_findings = [f for f in auditor.findings if f.rule == "boilerplate_analytical_focus"]
        self.assertTrue(len(bp_findings) >= 1)
        self.assertIn("Analytical Focus", bp_findings[0].excerpt)

    def test_broken_template_tags_detected(self):
        content = "# Report\n\nThis dossier was updated on {{DATE}} by {{AUTHOR}}.\n"
        create_test_file(self.root / "LoAR" / "Report.md", content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_template_and_boilerplate()

        tag_findings = [f for f in auditor.findings if f.rule == "broken_template_tag"]
        self.assertTrue(len(tag_findings) >= 1)
        self.assertEqual(tag_findings[0].severity, "ERROR")

    def test_robotic_heading_detected(self):
        content = "# Real Title\n\n## Topic Name: Kondratiev Waves Deep Dive\n\nSubstantive content."
        create_test_file(self.root / "Kondratiev Waves" / "Report.md", content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_template_and_boilerplate()

        heading_findings = [f for f in auditor.findings if f.rule == "robotic_heading"]
        self.assertTrue(len(heading_findings) >= 1)


class TestRepeatedHeadings(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_repeated_nonstandard_heading_capped(self):
        heading = "### Non-Standard Specific Empirical Regression Framework"
        for i in range(5):
            create_test_file(self.root / f"Pillar{i}" / "Doc.md", f"{heading}\n\nContent {i}")

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_repeated_headings()

        rep_findings = [f for f in auditor.findings if f.rule == "repeated_heading_capped"]
        self.assertTrue(len(rep_findings) >= 5)


class TestCitationsUrlsAndClaimCoverage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_local_file_url_forbidden(self):
        content = "Refer to the baseline dossier at [Local Link](file:///Users/dylanboyle/Desktop/Convergence/doc.md)."
        create_test_file(self.root / "Review" / "Doc.md", content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_citations_urls_and_claim_coverage()

        url_findings = [f for f in auditor.findings if f.rule == "local_file_url"]
        self.assertTrue(len(url_findings) >= 1)
        self.assertEqual(url_findings[0].severity, "ERROR")
        self.assertIn("file:///", url_findings[0].excerpt)

    def test_claim_register_missing_source_doc_flagged(self):
        csv_content = "claim_id,source_document,claim_text\nCLM-001,NonExistentDossier.md,Heuristic claim\n"
        create_test_file(self.root / "review" / "CLAIM_EVIDENCE_REGISTER.csv", csv_content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_citations_urls_and_claim_coverage()

        claim_findings = [f for f in auditor.findings if f.rule == "unresolved_claim_source_doc"]
        self.assertTrue(len(claim_findings) >= 1)
        self.assertEqual(claim_findings[0].severity, "WARNING")


class TestMathematicalConsistency(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_stripped_dollar_cell_detected(self):
        table_line = "| 1960 | B | 53.6% | .5B |"
        create_test_file(self.root / "Pillar1" / "Table.md", f"# Table\n\n{table_line}\n")

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_mathematical_consistency()

        cell_findings = [f for f in auditor.findings if f.rule == "stripped_dollar_cell"]
        self.assertTrue(len(cell_findings) >= 1)
        self.assertEqual(cell_findings[0].severity, "ERROR")

    def test_pid_leak_artifact_detected(self):
        content = "The takeoff trajectory is modeled by $$Y_t = 36646 \\cdot e^{rt}$$."
        create_test_file(self.root / "Pillar1" / "Math.md", content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_mathematical_consistency()

        pid_findings = [f for f in auditor.findings if f.rule == "pid_leak_artifact"]
        self.assertTrue(len(pid_findings) >= 1)
        self.assertEqual(pid_findings[0].severity, "ERROR")

    def test_corrupted_frac_macro_detected(self):
        content = "$$\\frac12$$"
        create_test_file(self.root / "Pillar1" / "Math.md", content)

        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_mathematical_consistency()

        frac_findings = [f for f in auditor.findings if f.rule == "corrupted_frac_macro"]
        self.assertTrue(len(frac_findings) >= 1)
        self.assertEqual(frac_findings[0].severity, "ERROR")


class TestFindingContractIntegrity(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_finding_attributes_and_serialization(self):
        finding = AuditFinding(
            file="Changing World Orders/Monograph.md",
            line=42,
            excerpt="| 1960 | B | 53.6% |",
            rule="stripped_dollar_cell",
            severity="ERROR",
            message="Stripped dollar symbol in table cell"
        )
        self.assertEqual(finding.file, "Changing World Orders/Monograph.md")
        self.assertEqual(finding.line, 42)
        self.assertEqual(finding.rule, "stripped_dollar_cell")
        self.assertEqual(finding.severity, "ERROR")
        self.assertEqual(finding.excerpt, "| 1960 | B | 53.6% |")

        data = finding.to_dict()
        self.assertEqual(data["location"]["file"], "Changing World Orders/Monograph.md")
        self.assertEqual(data["location"]["line"], 42)
        self.assertEqual(data["rule"], "stripped_dollar_cell")
        self.assertEqual(data["severity"], "ERROR")
        self.assertEqual(data["excerpt"], "| 1960 | B | 53.6% |")


class TestDeliberatelyInvalidDocumentsFromRealDefects(unittest.TestCase):
    """
    Regression test suite using fixtures modeled directly on real defects
    identified and repaired during Convergence audit phases.
    """
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_real_defect_stripped_cbo_debt_table(self):
        defect_content = (
            "# U.S. Sovereign Debt\n\n"
            "| Year | Gross Federal Debt | Debt Held by Public (% GDP) | Total Revenues | Net Interest Outlays |\n"
            "|---|---|---|---|---|\n"
            "| **1960** | B | 53.6% | .5B | .9B |\n"
        )
        create_test_file(self.root / "CWO" / "Defect1.md", defect_content)
        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_mathematical_consistency()
        findings = [f for f in auditor.findings if f.rule == "stripped_dollar_cell"]
        self.assertTrue(len(findings) >= 1)
        self.assertIn(".5B", findings[0].excerpt)

    def test_real_defect_pid_in_synthesis_math(self):
        defect_content = (
            "## 4. Formal Mathematical Modeling\n\n"
            "$$\\dot{K}(t) = 36646 \\cdot I(t) - \\delta K(t)$$\n"
        )
        create_test_file(self.root / "Synthesis" / "Defect2.md", defect_content)
        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_mathematical_consistency()
        findings = [f for f in auditor.findings if f.rule == "pid_leak_artifact"]
        self.assertTrue(len(findings) >= 1)
        self.assertIn("36646", findings[0].excerpt)

    def test_real_defect_local_file_url_in_markdown(self):
        defect_content = (
            "Refer to the original dossier at: "
            "[Dossier Link](file:///Users/dylanboyle/Desktop/Convergence/4th%20Turning/Overview.md)\n"
        )
        create_test_file(self.root / "Synthesis" / "Defect3.md", defect_content)
        auditor = ConvergenceAuditor(root=self.root)
        auditor.check_citations_urls_and_claim_coverage()
        findings = [f for f in auditor.findings if f.rule == "local_file_url"]
        self.assertTrue(len(findings) >= 1)
        self.assertIn("file:///Users/dylanboyle", findings[0].excerpt)


class TestFullAuditAndCLI(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_run_all_checks_structure(self):
        auditor = ConvergenceAuditor(root=self.root)
        results = auditor.run_all_checks()
        self.assertIn("passed", results)
        self.assertIn("strict", results)
        self.assertIn("checks", results)
        self.assertIn("findings", results)
        self.assertIn("error_count", results)
        self.assertIn("warning_count", results)

    def test_cli_execution_with_json_flag(self):
        test_args = ["audit_verification.py", "--root", str(self.root), "--json"]
        captured = io.StringIO()
        with patch.object(sys, "argv", test_args), patch("sys.stdout", captured):
            exit_code = main()
            self.assertIn(exit_code, [0, 1])
        output = captured.getvalue()
        parsed = json.loads(output)
        self.assertIn("checks", parsed)
        self.assertIn("findings", parsed)


if __name__ == "__main__":
    unittest.main()
