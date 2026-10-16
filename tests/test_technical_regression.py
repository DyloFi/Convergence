#!/usr/bin/env python3
"""
Regression test suite for Convergence technical integrity defects:
1. Syntax validity of all Python scripts in scripts/
2. Absence of corrupted ASCII control characters in markdown dossiers
3. Hermetic paths (no hardcoded machine user paths in active scripts/dossiers/synthesis/reviews)
4. Internal link and heading anchor resolution
5. Absence of boilerplate analytical-focus entries in bibliographies
6. Citation inventory and verification audit artifact integrity
7. Claim register coverage and claim inventory artifact integrity (Step 11)
8. Freshness and consistency of quantitative baseline data (WGC, CBO, METR) (Step 11)
"""

import csv
import json
import os
import pathlib
import py_compile
import re
import unittest
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent

def slugify(heading: str) -> str:
    h = heading.strip().lower()
    h = re.sub(r'[^\w\s-]', '', h)
    h = re.sub(r'[\s_]+', '-', h)
    return h.strip('-')

class TestTechnicalIntegrity(unittest.TestCase):
    def test_scripts_python_syntax(self):
        """All active scripts in scripts/ must compile with zero syntax errors."""
        scripts_dir = ROOT / "scripts"
        errors = []
        for py_path in scripts_dir.glob("*.py"):
            try:
                py_compile.compile(str(py_path), doraise=True)
            except Exception as e:
                errors.append(f"{py_path.name}: {e}")
        self.assertEqual(errors, [], f"Syntax errors found: {errors}")

    def test_no_corrupted_control_characters_in_reports(self):
        """Active research dossiers must not contain corrupted non-whitespace control characters."""
        bad_chars = set(range(0, 9)) | {11, 12} | set(range(14, 32))
        corrupted = []
        for md_path in ROOT.rglob("*.md"):
            if "baseline_snapshot" in md_path.parts or ".git" in md_path.parts or ".agents" in md_path.parts or "node_modules" in md_path.parts:
                continue
            data = md_path.read_bytes()
            found = [b for b in data if b in bad_chars]
            if found:
                corrupted.append(f"{md_path.relative_to(ROOT)} ({len(found)} control chars)")
        self.assertEqual(corrupted, [], f"Corrupted control characters in: {corrupted}")

    def test_hermetic_paths_no_hardcoded_user_paths(self):
        """Active scripts and research dossiers must be hermetic with no hardcoded machine paths."""
        errors = []
        for py_path in (ROOT / "scripts").glob("*.py"):
            text = py_path.read_text(encoding="utf-8")
            if "/Users/" in text:
                errors.append(f"{py_path.relative_to(ROOT)} contains hardcoded /Users/")
        
        pillars = ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]
        for pillar in pillars:
            for md_path in (ROOT / pillar).rglob("*.md"):
                text = md_path.read_text(encoding="utf-8")
                if "/Users/" in text:
                    errors.append(f"{md_path.relative_to(ROOT)} contains hardcoded /Users/")

        for target_name in ["Convergence_Master_Synthesis.md", "TEST_READY.md"]:
            p = ROOT / target_name
            if p.exists():
                text = p.read_text(encoding="utf-8")
                if "/Users/" in text:
                    errors.append(f"{p.relative_to(ROOT)} contains hardcoded /Users/")

        self.assertEqual(errors, [], f"Hardcoded machine paths found: {errors}")

    def test_internal_links_and_heading_anchors_resolve(self):
        """All internal links and heading anchors in active markdown files must resolve."""
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        errors = []
        
        for md_path in ROOT.rglob("*.md"):
            if any(p in md_path.parts for p in [".git", "baseline_snapshot", ".agents", "node_modules"]):
                continue
            content = md_path.read_text(encoding="utf-8")
            # Strip display and inline math to avoid KaTeX notation false positives
            content_no_math = re.sub(r'\$\$.*?\$\$', '', content, flags=re.DOTALL)
            content_no_math = re.sub(r'\$[^$\n]+\$', '', content_no_math)
            
            for m in link_pattern.finditer(content_no_math):
                text, url = m.group(1), m.group(2).strip()
                if url.startswith(("http://", "https://", "mailto:")):
                    continue
                
                parsed = urllib.parse.urlparse(url)
                path_part = urllib.parse.unquote(parsed.path)
                frag = urllib.parse.unquote(parsed.fragment)
                
                if path_part.startswith("/"):
                    target_path = (ROOT / path_part.lstrip("/")).resolve()
                elif path_part:
                    target_path = (md_path.parent / path_part).resolve()
                else:
                    target_path = md_path.resolve()
                    
                if not target_path.exists():
                    errors.append(f"{md_path.relative_to(ROOT)}: Target '{url}' does not exist ({target_path})")
                    continue
                    
                if frag and target_path.suffix == ".md":
                    t_content = target_path.read_text(encoding="utf-8")
                    headings = re.findall(r'^#+\s+(.+)$', t_content, flags=re.MULTILINE)
                    slugs = {slugify(h) for h in headings}
                    clean_frag = slugify(frag)
                    if clean_frag not in slugs:
                        errors.append(f"{md_path.relative_to(ROOT)}: Anchor '#{frag}' not found in {target_path.relative_to(ROOT)}")
                        
        self.assertEqual(errors, [], f"Broken internal links/anchors found: {errors}")

    def test_no_analytical_focus_boilerplate_in_reports(self):
        """Active research dossiers must not contain template analytical-focus boilerplate in bibliographies."""
        pattern = re.compile(r'\((?:Analytical Focus|analytical focus):', re.I)
        violations = []
        pillars = ["4th Turning", "Changing World Orders", "Kondratiev Waves", "LoAR", "Technological Singularity"]
        for pillar in pillars:
            for md_path in (ROOT / pillar).rglob("*.md"):
                if md_path.name.endswith(".bak.md"):
                    continue
                text = md_path.read_text(encoding="utf-8")
                if pattern.search(text):
                    violations.append(str(md_path.relative_to(ROOT)))
        synthesis = ROOT / "Convergence_Master_Synthesis.md"
        if synthesis.exists():
            if pattern.search(synthesis.read_text(encoding="utf-8")):
                violations.append(str(synthesis.relative_to(ROOT)))
        self.assertEqual(violations, [], f"Analytical focus boilerplate found in: {violations}")

    def test_citation_inventory_and_audit_artifacts_valid(self):
        """Citation inventory JSON and CITATION_AUDIT CSV must exist, be populated, and verify all sources."""
        inv_path = ROOT / "audit" / "citations_inventory.json"
        csv_path = ROOT / "review" / "CITATION_AUDIT.csv"
        self.assertTrue(inv_path.exists(), "audit/citations_inventory.json must exist")
        self.assertTrue(csv_path.exists(), "review/CITATION_AUDIT.csv must exist")

        with open(inv_path, "r", encoding="utf-8") as f:
            inv = json.load(f)
        self.assertGreater(inv["metadata"]["total_unique_sources"], 100)
        self.assertGreater(len(inv["sources"]), 100)
        for s in inv["sources"]:
            self.assertEqual(s["verification_status"], "verified")

        with open(csv_path, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertGreater(len(rows), 100)
        for r in rows:
            self.assertEqual(r["verification_status"], "verified")

    def test_claim_register_and_inventory_step11(self):
        """Claim register CSV and inventory JSON must exist, be populated across reports, and resolve paths."""
        reg_path = ROOT / "review" / "CLAIM_REGISTER.csv"
        inv_path = ROOT / "audit" / "claims_inventory.json"
        self.assertTrue(reg_path.exists(), "review/CLAIM_REGISTER.csv must exist")
        self.assertTrue(inv_path.exists(), "audit/claims_inventory.json must exist")

        with open(reg_path, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertGreater(len(rows), 200, "Claim register must expand from 16 to over 200 automated claims")

        for r in rows:
            self.assertTrue(r["claim_id"].startswith("CLM-"), f"Invalid claim ID: {r['claim_id']}")
            self.assertTrue(len(r["exact_claim_or_summary"]) > 0, f"Empty claim text for {r['claim_id']}")
            self.assertTrue(len(r["supporting_evidence_and_sources"]) > 0, f"Empty source for {r['claim_id']}")
            self.assertEqual(r["verification_status"], "verified")
            loc = r["repository_location"].strip()
            self.assertTrue((ROOT / loc).exists(), f"Target file does not exist: {loc}")

        with open(inv_path, "r", encoding="utf-8") as f:
            inv = json.load(f)
        self.assertGreater(inv["metadata"]["total_claims"], 200)
        self.assertEqual(inv["metadata"]["total_reports_audited"], 153)
        self.assertGreater(inv["metadata"]["total_reports_with_claims"], 100)
        self.assertEqual(inv["metadata"]["verified_count"], len(inv["claims"]))

    def test_stale_data_refreshed_vintages_and_projections(self):
        """Macroeconomic and capability benchmarks must reflect verified non-stale data."""
        cwo_emp = ROOT / "Changing World Orders/Foundations/02_Empirical_Macro_Debt_Reserves_and_Institutional_Decay.md"
        self.assertTrue(cwo_emp.exists())
        cwo_text = cwo_emp.read_text(encoding="utf-8")
        
        # Public debt for 2024 must be disaggregated as 99.0%
        self.assertIn("99.0%", cwo_text)
        self.assertNotIn("| **2024** | $35,465B | 122.4% |", cwo_text, "Gross debt % must not be conflated with public debt %")

        # WGC gold 2023 revised vintage (1,050.8t vs initial 1,037.4t) and 2025 (863.0t / 863.3t)
        self.assertIn("1,050.8 t", cwo_text)
        self.assertIn("863.0 t", cwo_text)

        # METR benchmark reliability ceiling <=16h
        loar_emp = ROOT / "LoAR/Supporting_Evidence/02_Empirical_Time_Series_Compute_Adoption_and_RWA.md"
        self.assertTrue(loar_emp.exists())
        loar_text = loar_emp.read_text(encoding="utf-8")
        self.assertIn("16 hours", loar_text)
        self.assertIn("Opus 4.5", loar_text)
        self.assertIn("Opus 4.6", loar_text)

if __name__ == "__main__":
    unittest.main()

    def test_report_standards_definitions_step12(self):
        """Report standards document must exist and define all 9 dimensions across all report types."""
        standards_path = ROOT / "review" / "REPORT_STANDARDS.md"
        self.assertTrue(standards_path.exists(), "review/REPORT_STANDARDS.md must exist")
        text = standards_path.read_text(encoding="utf-8")

        required_types = ["Dossier", "Expert Review", "Overview", "Synthesis", "Readme"]
        required_dimensions = [
            "Question", "Scope", "Summary", "Method", "Evidence",
            "Competing Views", "Limitations", "Proportional Conclusions", "References"
        ]

        for rt in required_types:
            self.assertIn(rt, text, f"Report standards missing type: {rt}")

        for dim in required_dimensions:
            self.assertIn(dim, text, f"Report standards missing dimension: {dim}")

    def test_report_triage_csv_and_inventory_step12(self):
        """Report triage CSV and JSON must cover 100% of in-scope reports with valid outcomes and weak-file triage."""
        csv_path = ROOT / "review" / "REPORT_TRIAGE.csv"
        json_path = ROOT / "audit" / "report_triage_inventory.json"
        self.assertTrue(csv_path.exists(), "review/REPORT_TRIAGE.csv must exist")
        self.assertTrue(json_path.exists(), "audit/report_triage_inventory.json must exist")

        with open(csv_path, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

        # Check complete coverage of in-scope reports
        self.assertEqual(len(rows), 153, "Triage CSV must cover 100% of in-scope reports (153 files)")

        valid_outcomes = {"accept", "minor revision", "major revision", "rebuild"}
        valid_triage = {"maintain", "refine", "rewrite", "merge", "delete"}
        weak_count = 0

        for r in rows:
            path = ROOT / r["file_path"]
            self.assertTrue(path.exists(), f"Target file does not exist: {r['file_path']}")
            self.assertIn(r["outcome"], valid_outcomes, f"Invalid outcome {r['outcome']} for {r['file_path']}")
            self.assertIn(r["triage_disposition"], valid_triage, f"Invalid triage disposition {r['triage_disposition']} for {r['file_path']}")
            self.assertTrue(int(r["word_count"]) > 0, f"Invalid word count for {r['file_path']}")
            self.assertTrue(int(r["line_count"]) > 0, f"Invalid line count for {r['file_path']}")

            if r["quality_tier"] in ["Tier 3", "Tier 4"]:
                weak_count += 1
                self.assertIn(r["triage_disposition"], {"rewrite", "merge", "delete"}, f"Weak file {r['file_path']} must be triaged into rewrite, merge, or delete")
                self.assertTrue(len(r["rationale"]) > 10, f"Weak file {r['file_path']} missing substantive rationale")
                if r["triage_disposition"] == "merge":
                    target = ROOT / r["target_merge_file"]
                    self.assertTrue(target.exists(), f"Merge target does not exist: {r['target_merge_file']}")

        # Exactly 46 weak files (38 Tier 3 + 8 Tier 4)
        self.assertEqual(weak_count, 46, f"Expected exactly 46 weak Tier 3 and 4 files, got {weak_count}")

        with open(json_path, "r", encoding="utf-8") as f:
            inv = json.load(f)

        self.assertEqual(inv["total_reports_audited"], 153)
        self.assertEqual(inv["summary_statistics"]["weak_tier3_tier4_total"], 46)
        self.assertEqual(len(inv["reports"]), 153)
