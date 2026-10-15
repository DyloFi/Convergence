#!/usr/bin/env python3
"""
Regression test suite for Convergence technical integrity defects:
1. Syntax validity of all Python scripts in scripts/
2. Absence of corrupted ASCII control characters in markdown dossiers
3. Hermetic paths (no hardcoded machine user paths in active scripts/dossiers/synthesis/reviews)
4. Internal link and heading anchor resolution
"""

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

if __name__ == "__main__":
    unittest.main()
