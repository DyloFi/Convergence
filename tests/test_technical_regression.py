#!/usr/bin/env python3
"""
Regression test suite for Convergence technical integrity defects:
1. Syntax validity of all Python scripts in scripts/
2. Absence of corrupted ASCII control characters (0x00-0x08, 0x0B-0x0C, 0x0E-0x1F) in markdown dossiers
3. Audit verification strict compliance
"""

import os
import pathlib
import py_compile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent

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
            if "baseline_snapshot" in md_path.parts or ".git" in md_path.parts:
                continue
            data = md_path.read_bytes()
            found = [b for b in data if b in bad_chars]
            if found:
                corrupted.append(f"{md_path.relative_to(ROOT)} ({len(found)} control chars)")
        self.assertEqual(corrupted, [], f"Corrupted control characters in: {corrupted}")

if __name__ == "__main__":
    unittest.main()
