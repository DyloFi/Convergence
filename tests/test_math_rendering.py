#!/usr/bin/env python3
"""
Unit test suite for Mathematical Rendering and Technical Integrity (Convergence Fix Step 6).
Verifies:
1. All LaTeX / math blocks in active markdown dossiers render without syntax errors via KaTeX.
2. Absence of shell/heredoc parameter-expansion artifacts ($ stripped amounts like `| B |`, `.5B`, lone PIDs).
3. Mathematical symbol definition and consistency.
"""

import json
import os
import pathlib
import re
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent

class TestMathRenderingAndIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Discover all active markdown files (excluding git, baseline snapshot, node_modules, and .bak.md)
        cls.active_files = [
            p for p in ROOT.rglob('*.md')
            if not any(part in p.parts for part in ['.git', 'baseline_snapshot', 'node_modules'])
            and not p.name.endswith('.bak.md')
        ]

    def test_no_dollar_stripping_or_pid_artifacts(self):
        """Verify no $-stripping artifacts (e.g. '| B |', '| .5B |', stray process IDs) in active dossiers."""
        stripped_patterns = [
            (re.compile(r'\|\s+[BMKk]\s+\|'), "Lone magnitude suffix cell without amount (e.g. '| B |')"),
            (re.compile(r'\|\s+\.\d+[BMKk]?\s+\|'), "Stripped leading zero/dollar cell (e.g. '| .5B |')"),
            (re.compile(r'\b(36646|36689|42735|40609|42887)\b'), "Stray heredoc process ID corruption"),
        ]

        violations = []
        for file_path in self.active_files:
            rel_path = file_path.relative_to(ROOT).as_posix()
            if rel_path.startswith('audit/') or rel_path == 'AUDIT_FINDINGS.md':
                continue
            
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            for pattern, desc in stripped_patterns:
                for match in pattern.finditer(content):
                    line_no = content[:match.start()].count('\n') + 1
                    violations.append(f"{rel_path}:{line_no} [{desc}] -> '{match.group(0)}'")

        self.assertEqual(violations, [], f"Detected $-stripping or PID artifacts:\n" + "\n".join(violations[:20]))

    def test_katex_rendering_of_all_display_math(self):
        """Verify all display math ($$...$$) across active dossiers renders cleanly via KaTeX."""
        display_blocks = []
        for file_path in self.active_files:
            rel_path = file_path.relative_to(ROOT).as_posix()
            if rel_path.startswith('audit/'):
                continue
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            # Remove code fences and inline backtick code so code examples are not mistaken for math
            clean_content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            clean_content = re.sub(r'`[^`\n]+`', '', clean_content)
            for m in re.finditer(r'\$\$(.*?)\$\$', clean_content, re.DOTALL):
                line_no = clean_content[:m.start()].count('\n') + 1
                math_text = m.group(1).strip()
                if math_text:
                    display_blocks.append({'file': rel_path, 'line': line_no, 'math': math_text, 'display': True})

        self.assertGreater(len(display_blocks), 100, "Should have identified at least 100 display math blocks")

        env = os.environ.copy()
        node_paths = []
        if (ROOT / 'node_modules').exists():
            node_paths.append(str(ROOT / 'node_modules'))
        if 'NODE_PATH' in env:
            node_paths.append(env['NODE_PATH'])
        if node_paths:
            env['NODE_PATH'] = os.pathsep.join(node_paths)

        try:
            check_katex = subprocess.run(
                ['node', '-e', 'try { require("katex"); process.exit(0); } catch(e) { process.exit(1); }'],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                env=env
            )
        except FileNotFoundError:
            raise unittest.SkipTest("Node.js is not installed; skipping KaTeX rendering test.")

        if check_katex.returncode != 0:
            raise unittest.SkipTest("Node.js 'katex' module not available; skipping KaTeX rendering test.")

        tmp_file = ROOT / 'audit' / 'tmp_test_display_math.json'
        tmp_file.parent.mkdir(parents=True, exist_ok=True)
        tmp_file.write_text(json.dumps(display_blocks), encoding='utf-8')

        node_script = """
const fs = require('fs');
const katex = require('katex');

const items = JSON.parse(fs.readFileSync(process.argv[1], 'utf8'));
let errors = [];

for (const item of items) {
    try {
        katex.renderToString(item.math, { displayMode: true, throwOnError: true });
    } catch (err) {
        errors.push({ file: item.file, line: item.line, math: item.math, error: err.message });
    }
}

if (errors.length > 0) {
    fs.writeFileSync(process.argv[2], JSON.stringify(errors, null, 2));
    process.exit(1);
} else {
    process.exit(0);
}
"""
        err_file = ROOT / 'audit' / 'tmp_test_display_math_errs.json'
        try:
            res = subprocess.run(
                ['node', '-e', node_script, str(tmp_file), str(err_file)],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                env=env
            )

            if res.returncode != 0:
                if err_file.exists():
                    errors = json.loads(err_file.read_text(encoding='utf-8'))
                    err_summary = [f"{e['file']}:{e['line']} -> {e['error']} | math: {e['math'][:80]}" for e in errors]
                    self.fail(f"KaTeX failed on {len(errors)} display math blocks:\n" + "\n".join(err_summary))
                else:
                    self.fail(f"KaTeX test runner failed with exit code {res.returncode}:\n{res.stderr}\n{res.stdout}")
        finally:
            if tmp_file.exists():
                tmp_file.unlink(missing_ok=True)
            if err_file.exists():
                err_file.unlink(missing_ok=True)

    def test_substantive_equation_symbol_definitions(self):
        """Verify core theoretical equations define required variables in surrounding context."""
        cwo_theory = ROOT / 'Changing World Orders/Supporting_Materials/Theories/Theories Deep Dive.md'
        if cwo_theory.exists():
            text = cwo_theory.read_text(encoding='utf-8')
            self.assertIn("F_t = \\exp", text)
            self.assertIn("P_{R,t}, P_{E,t}", text)
            self.assertIn("Debt", text)

        master_synth = ROOT / 'Convergence_Master_Synthesis.md'
        if master_synth.exists():
            text = master_synth.read_text(encoding='utf-8')
            self.assertIn(r"\frac{dA}{dt}", text)
            self.assertIn(r"S_{\text{inst}}", text)


if __name__ == '__main__':
    unittest.main()
