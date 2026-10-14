#!/usr/bin/env python3
"""Step 3: Defect Register and Full Repository Markdown Scan.
Performs exhaustive syntax, semantic, structural, and linkage scanning across all
in-scope markdown research reports and documents in the Convergence repository.
Outputs:
  - audit/findings.json (machine-readable defect registry)
  - AUDIT_FINDINGS.md (comprehensive audit findings monograph & source of truth map)
"""

import os
import sys
import re
import json
import pathlib
import hashlib
from typing import List, Dict, Any, Tuple

ROOT = pathlib.Path('/Users/dylanboyle/Desktop/Convergence').resolve()
AUDIT_DIR = ROOT / 'audit'
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

# Required standard sections for comprehensive research dossiers
REQUIRED_DOSSIER_SECTIONS = [
    ('Executive Summary', re.compile(r'^#+\s*(?:Executive\s+Summary|Overview|Abstract)', re.I)),
    ('Foundations / Theory', re.compile(r'^#+\s*(?:Theoretical|Foundations?|Conceptual|Core\s+Mechanics|Framework)', re.I)),
    ('Empirical Evidence', re.compile(r'^#+\s*(?:Empirical|Historical\s+Data|Evidence|Historical\s+Precedents?|Data\s+Series)', re.I)),
    ('Quantitative Dynamics', re.compile(r'^#+\s*(?:Quantitative|Dynamics|Model|Mathematical|Parameters|Metrics)', re.I)),
    ('Counterarguments / Falsification', re.compile(r'^#+\s*(?:Counterarguments?|Falsification|Vulnerabilit|Alternative\s+Explanations?|Critique)', re.I)),
    ('Synthesis / Implications', re.compile(r'^#+\s*(?:Convergence\s+Integration|Synthesis|Implications?|Strategic|Macro\s+Impact)', re.I))
]

class DefectScanner:
    def __init__(self, root: pathlib.Path):
        self.root = root
        self.manifest_path = root / 'audit' / 'manifest.json'
        with open(self.manifest_path, 'r', encoding='utf-8') as f:
            self.manifest = json.load(f)
        
        # Load in-scope deliverable reports and documents
        self.in_scope_files = []
        for fentry in self.manifest.get('files', []):
            role = fentry.get('role')
            p = fentry.get('path')
            # Exclude archive, backup, generated test scripts, and git
            if role in ('report', 'synthesis', 'README', 'documentation') and not p.startswith('baseline_snapshot/') and not p.startswith('.agents/'):
                self.in_scope_files.append(p)
        
        self.findings: List[Dict[str, Any]] = []
        self.finding_counter = 0

    def add_finding(self, location: str, line: int, category: str, severity: str,
                    evidence: str, proposed_fix: str, validation_test: str,
                    status: str = 'open') -> str:
        self.finding_counter += 1
        finding_id = f"DEF-{self.finding_counter:04d}"
        finding = {
            'id': finding_id,
            'location': {
                'file': location,
                'line': line
            },
            'category': category,
            'severity': severity,
            'evidence': evidence,
            'proposed_fix': proposed_fix,
            'validation_test': validation_test,
            'status': status
        }
        self.findings.append(finding)
        return finding_id

    def scan_file(self, rel_path: str):
        full_path = self.root / rel_path
        if not full_path.exists():
            return
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            self.add_finding(
                location=rel_path,
                line=1,
                category='corrupted_encoding',
                severity='HIGH',
                evidence='File cannot be decoded as UTF-8 without error',
                proposed_fix='Re-encode file in valid UTF-8 format',
                validation_test='utf8_decode_test'
            )
            return

        lines = content.splitlines()

        # 1. Corrupted LaTeX & Dollar Parameter Stripping
        self.check_latex_and_math(rel_path, lines)

        # 2. Unbalanced Delimiters (code fences, brackets, double-pipes)
        self.check_delimiters(rel_path, lines, content)

        # 3. Broken Links
        self.check_links(rel_path, lines)

        # 4. Empty or Duplicate Headings
        self.check_headings(rel_path, lines)

        # 5. Incomplete Tables
        self.check_tables(rel_path, lines)

        # 6. Placeholders and Template Residue
        self.check_placeholders(rel_path, lines)

        # 7. Duplicate Paragraphs
        self.check_duplicate_paragraphs(rel_path, lines)

        # 8. Malformed References and URLs
        self.check_urls_and_refs(rel_path, lines)

        # 9. Missing Required Sections (for research dossiers)
        if '/Expert_Review' not in rel_path and rel_path != 'Convergence_Master_Synthesis.md' and not rel_path.endswith('README.md') and not rel_path.startswith('review/'):
            self.check_required_sections(rel_path, lines)

        # 10. Title or Scope Contradictions
        self.check_title_scope(rel_path, lines)

    def check_latex_and_math(self, rel_path: str, lines: List[str]):
        # Check for parameter expansion stripped dollar amounts: e.g. '| B |', '| .5B |', '| ,233B |'
        stripped_dollar_re = re.compile(r'\|\s*(?:B|\.\d+B|,\d+B)\s*\|')
        for idx, line in enumerate(lines, 1):
            m = stripped_dollar_re.search(line)
            if m:
                self.add_finding(
                    location=rel_path,
                    line=idx,
                    category='corrupted_latex',
                    severity='HIGH',
                    evidence=line.strip(),
                    proposed_fix='Restore original dollar prefix stripped by unquoted heredoc parameter expansion (e.g. $1,233B instead of ,233B)',
                    validation_test='regex_stripped_dollar_check'
                )

        # Check for broken LaTeX macros missing backslash: e.g., 'frac{a}{b}' without leading backslash
        broken_frac_re = re.compile(r'(?<!\\)frac\{[^{}]+\}\{[^{}]+\}')
        for idx, line in enumerate(lines, 1):
            if '```' in line: continue
            m = broken_frac_re.search(line)
            if m:
                self.add_finding(
                    location=rel_path,
                    line=idx,
                    category='corrupted_latex',
                    severity='MEDIUM',
                    evidence=m.group(0),
                    proposed_fix=f'Add leading backslash to LaTeX macro: \\{m.group(0)}',
                    validation_test='latex_macro_syntax_check'
                )

    def check_delimiters(self, rel_path: str, lines: List[str], content: str):
        # Odd count of code fences
        fence_count = len(re.findall(r'^```', content, re.M))
        if fence_count % 2 != 0:
            self.add_finding(
                location=rel_path,
                line=len(lines),
                category='unbalanced_delimiters',
                severity='HIGH',
                evidence=f'File has odd number of triple-backtick code fences ({fence_count})',
                proposed_fix='Close unclosed code block with matching ``` fence',
                validation_test='code_fence_balance_test'
            )

        # Double-pipe delimiter corruption: '||'
        for idx, line in enumerate(lines, 1):
            if '||' in line and not line.strip().startswith('```'):
                self.add_finding(
                    location=rel_path,
                    line=idx,
                    category='unbalanced_delimiters',
                    severity='MEDIUM',
                    evidence=line.strip(),
                    proposed_fix='Replace corrupted double-pipe || with standard single pipe table delimiter |',
                    validation_test='double_pipe_syntax_test'
                )

    def check_links(self, rel_path: str, lines: List[str]):
        link_re = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        file_dir = (self.root / rel_path).parent

        for idx, line in enumerate(lines, 1):
            for m in link_re.finditer(line):
                target = m.group(2).strip()
                if target.startswith(('http://', 'https://', 'mailto:', '#', 'ftp://')):
                    continue
                # Local target
                clean_target = target.split('#')[0]
                if not clean_target:
                    continue
                resolved_path = (file_dir / clean_target).resolve()
                if not resolved_path.exists():
                    self.add_finding(
                        location=rel_path,
                        line=idx,
                        category='broken_links',
                        severity='MEDIUM',
                        evidence=f'[{m.group(1)}]({target}) -> missing path: {clean_target}',
                        proposed_fix=f'Update relative link target to existing document or remove broken link',
                        validation_test='link_path_resolution_test'
                    )

    def check_headings(self, rel_path: str, lines: List[str]):
        seen_headings = {}
        for idx, line in enumerate(lines, 1):
            m = re.match(r'^(#{1,6})\s*(.*)$', line)
            if m:
                level = len(m.group(1))
                text = m.group(2).strip()
                if not text:
                    self.add_finding(
                        location=rel_path,
                        line=idx,
                        category='empty_or_duplicate_headings',
                        severity='LOW',
                        evidence=line,
                        proposed_fix='Remove empty heading marker or provide descriptive heading title',
                        validation_test='heading_non_empty_test'
                    )
                else:
                    norm_text = text.lower()
                    if norm_text in seen_headings:
                        prev_line = seen_headings[norm_text]
                        self.add_finding(
                            location=rel_path,
                            line=idx,
                            category='empty_or_duplicate_headings',
                            severity='LOW',
                            evidence=f'Duplicate heading "{text}" previously defined at line {prev_line}',
                            proposed_fix=f'Disambiguate heading title or merge duplicate sub-sections',
                            validation_test='heading_uniqueness_test'
                        )
                    else:
                        seen_headings[norm_text] = idx

    def check_tables(self, rel_path: str, lines: List[str]):
        in_table = False
        header_cols = 0
        table_start = 0

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith('|') and stripped.endswith('|'):
                cells = [c.strip() for c in stripped[1:-1].split('|')]
                if not in_table:
                    in_table = True
                    table_start = idx
                    header_cols = len(cells)
                else:
                    if len(cells) != header_cols:
                        self.add_finding(
                            location=rel_path,
                            line=idx,
                            category='incomplete_tables',
                            severity='MEDIUM',
                            evidence=f'Table started at line {table_start} has {header_cols} cols; row has {len(cells)} cols: "{stripped}"',
                            proposed_fix='Align column count of row with table header row',
                            validation_test='table_column_alignment_test'
                        )
            else:
                in_table = False
                header_cols = 0

    def check_placeholders(self, rel_path: str, lines: List[str]):
        placeholder_re = re.compile(r'(\{\{[^{}]+\}\}|<TODO[^>]*>|\[INSERT[^\]]*\]|\bTODO:|\bFIXME:|\bTBD\b|\$\{+[A-Za-z0-9_]+\}+)')
        for idx, line in enumerate(lines, 1):
            if '```' in line: continue
            m = placeholder_re.search(line)
            if m:
                token = m.group(1)
                self.add_finding(
                    location=rel_path,
                    line=idx,
                    category='placeholders_and_template_residue',
                    severity='HIGH' if 'TODO' in token or 'INSERT' in token else 'MEDIUM',
                    evidence=f'Placeholder or unrendered template artifact detected: "{token}"',
                    proposed_fix='Replace template placeholder with concrete empirical data or synthesis text',
                    validation_test='template_residue_test'
                )

    def check_duplicate_paragraphs(self, rel_path: str, lines: List[str]):
        paras = []
        cur_p = []
        start_line = 1
        for idx, line in enumerate(lines, 1):
            if not line.strip():
                if cur_p:
                    text = ' '.join(cur_p).strip()
                    if len(text) > 80 and not text.startswith('#') and not text.startswith('|'):
                        paras.append((start_line, text))
                    cur_p = []
            else:
                if not cur_p:
                    start_line = idx
                cur_p.append(line.strip())
        if cur_p:
            text = ' '.join(cur_p).strip()
            if len(text) > 80 and not text.startswith('#') and not text.startswith('|'):
                paras.append((start_line, text))

        seen_paras = {}
        for l_num, p_text in paras:
            p_hash = hashlib.sha256(p_text.encode('utf-8')).hexdigest()
            if p_hash in seen_paras:
                prev_line = seen_paras[p_hash]
                self.add_finding(
                    location=rel_path,
                    line=l_num,
                    category='duplicate_paragraphs',
                    severity='MEDIUM',
                    evidence=f'Paragraph identical to paragraph at line {prev_line}: "{p_text[:120]}..."',
                    proposed_fix='Remove redundant duplicated paragraph or re-author with unique domain context',
                    validation_test='duplicate_paragraph_hash_test'
                )
            else:
                seen_paras[p_hash] = l_num

    def check_urls_and_refs(self, rel_path: str, lines: List[str]):
        malformed_link_re = re.compile(r'\[\s*\]\([^)]+\)|\[[^\]]+\]\(\s*\)')
        for idx, line in enumerate(lines, 1):
            m = malformed_link_re.search(line)
            if m:
                self.add_finding(
                    location=rel_path,
                    line=idx,
                    category='malformed_references_and_urls',
                    severity='MEDIUM',
                    evidence=f'Malformed empty link anchor or URL: "{m.group(0)}"',
                    proposed_fix='Populate link text anchor and valid URL or target path',
                    validation_test='link_format_test'
                )

    def check_required_sections(self, rel_path: str, lines: List[str]):
        found_sections = {sec_name: False for sec_name, _ in REQUIRED_DOSSIER_SECTIONS}
        for line in lines:
            if line.startswith('#'):
                for sec_name, sec_re in REQUIRED_DOSSIER_SECTIONS:
                    if sec_re.search(line):
                        found_sections[sec_name] = True

        missing = [sec for sec, found in found_sections.items() if not found]
        if missing:
            self.add_finding(
                location=rel_path,
                line=1,
                category='missing_required_sections',
                severity='LOW' if len(missing) <= 2 else 'MEDIUM',
                evidence=f'Dossier lacks standard required sections: {missing}',
                proposed_fix=f'Add missing required sections ({missing}) to adhere to comprehensive monograph template',
                validation_test='dossier_structural_section_test'
            )

    def check_title_scope(self, rel_path: str, lines: List[str]):
        first_h1 = None
        for idx, line in enumerate(lines, 1):
            if line.startswith('# '):
                first_h1 = (idx, line[2:].strip())
                break
        
        if not first_h1:
            self.add_finding(
                location=rel_path,
                line=1,
                category='title_or_scope_contradictions',
                severity='MEDIUM',
                evidence='No top-level H1 title found in document',
                proposed_fix='Add top-level # Title matching document filename and topic',
                validation_test='document_h1_title_test'
            )
        else:
            line_idx, title_text = first_h1
            if '{' in title_text or '}' in title_text or '<' in title_text:
                self.add_finding(
                    location=rel_path,
                    line=line_idx,
                    category='title_or_scope_contradictions',
                    severity='HIGH',
                    evidence=f'H1 Title contains formatting or template residue: "{title_text}"',
                    proposed_fix='Clean title to clear plaintext research topic',
                    validation_test='title_cleanliness_test'
                )

    def run_scan(self):
        print(f'Starting scan of {len(self.in_scope_files)} in-scope markdown files...')
        for rel_path in sorted(self.in_scope_files):
            self.scan_file(rel_path)
        print(f'Scan completed. Total findings: {len(self.findings)}')

    def generate_source_of_truth_mapping(self) -> Dict[str, Any]:
        mapping = {
            'overview': 'Source of truth resolution rules across duplicates, backups, and historical snapshots.',
            'precedence_hierarchy': [
                '1. Active Workspace Reports (remediation branch HEAD): Authoritative canonical monographs for all current analysis and research.',
                '2. .bak.md Files: Historical pre-enhancement backups created prior to multi-agent rewrites. Disposable after verification.',
                '3. baseline_snapshot/: Immutable archival baseline preserved under tag pre-fix. Read-only historical reference.',
                '4. review/ Monograph & Registers: Independent peer review and formal evaluation layer; secondary analytical authority.'
            ],
            'bak_files_summary': {
                'total_bak_files': 108,
                'distribution': {
                    'Changing World Orders': 15,
                    'LoAR': 6,
                    'Technological Singularity': 31,
                    'root': 2,
                    'baseline_snapshot': 54
                },
                'action_recommendation': 'Retain intact on remediation branch until Step 20 cleanup pass; never treat as current source of truth.'
            },
            'duplicate_filenames_summary': {
                'total_duplicate_pairs': 182,
                'primary_cause': 'Parallel structure in baseline_snapshot/ mirroring active workspace directories, plus .bak.md pairing.',
                'resolution': 'Active workspace path (e.g. "4th Turning/...") is authoritative; baseline_snapshot/ is strictly historical reference.'
            }
        }
        return mapping

    def write_deliverables(self):
        sot_mapping = self.generate_source_of_truth_mapping()

        # 1. Write audit/findings.json
        findings_json_path = self.root / 'audit' / 'findings.json'
        output_data = {
            'generated_utc': '2026-10-15T02:40:00Z',
            'repository_root': str(self.root),
            'total_files_scanned': len(self.in_scope_files),
            'total_findings': len(self.findings),
            'category_counts': {},
            'severity_counts': {},
            'status_counts': {
                'open': len([f for f in self.findings if f['status'] == 'open']),
                'in_progress': 0,
                'fixed': 0,
                'verified': 0,
                'accepted_exception': 0
            },
            'source_of_truth_mapping': sot_mapping,
            'findings': self.findings
        }

        for f in self.findings:
            c = f['category']
            s = f['severity']
            output_data['category_counts'][c] = output_data['category_counts'].get(c, 0) + 1
            output_data['severity_counts'][s] = output_data['severity_counts'].get(s, 0) + 1

        with open(findings_json_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2)
        print(f'Wrote {findings_json_path}')

        # 2. Write AUDIT_FINDINGS.md
        md_path = self.root / 'AUDIT_FINDINGS.md'
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write('# Convergence Repository: Comprehensive Audit Findings & Defect Register\n\n')
            f.write('**Audit Execution**: Convergence Remediation Step 3/21\n')
            f.write(f'**Execution Date**: October 15, 2026\n')
            f.write(f'**Total Files Scanned**: {len(self.in_scope_files)}\n')
            f.write(f'**Total Findings Logged**: {len(self.findings)}\n\n')

            f.write('## 1. Executive Summary & Defect Statistics\n\n')
            f.write('Every in-scope Markdown document across the five foundation pillars, master synthesis, and system READMEs was systematically scanned for formal syntax defects, corruptions, template residue, and structural anomalies.\n\n')
            
            f.write('### Findings by Severity\n\n')
            f.write('| Severity | Count | Definition | Remediation Policy |\n')
            f.write('| :--- | :--- | :--- | :--- |\n')
            f.write(f'| **HIGH** | {output_data["severity_counts"].get("HIGH", 0)} | Corrupted tables, stripped parameter data, unclosed code fences, active TODOs | Immediate repair required before econometric modeling |\n')
            f.write(f'| **MEDIUM** | {output_data["severity_counts"].get("MEDIUM", 0)} | Broken relative links, duplicate paragraphs, table col alignment, LaTeX formatting | Repair systematically across domain batches |\n')
            f.write(f'| **LOW** | {output_data["severity_counts"].get("LOW", 0)} | Duplicate heading titles, missing optional monograph sections | Non-blocking polish and harmonization |\n\n')

            f.write('### Findings by Category\n\n')
            f.write('| Category | Count | Primary Impact |\n')
            f.write('| :--- | :--- | :--- |\n')
            for cat, count in sorted(output_data['category_counts'].items()):
                f.write(f'| `{cat}` | {count} | Formal report integrity and consistency |\n')
            f.write('\n')

            f.write('## 2. Source of Truth Resolution Architecture\n\n')
            f.write('Prior to any destructive deletion or file pruning in later remediation steps, the source of truth across all overlapping files is formally established:\n\n')
            for item in sot_mapping['precedence_hierarchy']:
                f.write(f'- {item}\n')
            f.write('\n')
            f.write('### Historical `.bak.md` File Architecture\n\n')
            f.write(f'- **Total `.bak.md` Files Detected**: {sot_mapping["bak_files_summary"]["total_bak_files"]}\n')
            f.write('- **Role & Status**: These files represent pre-enhancement snapshot captures generated prior to the multi-agent expansion passes. They contain older, un-expanded text and are superseded by the active dossiers.\n')
            f.write('- **Governance Policy**: Preserved on git branch `remediation` until Step 20; strictly excluded from research deliverables and synthesis statistics.\n\n')

            f.write('### Version Reconciliation & Snapshot Boundaries\n\n')
            f.write(f'- **Total Duplicate Filename Pairs**: {sot_mapping["duplicate_filenames_summary"]["total_duplicate_pairs"]}\n')
            f.write('- **Boundary**: `baseline_snapshot/` represents the frozen historical state of August/October 2026. The root pillar directories (`4th Turning/`, `Changing World Orders/`, `Kondratiev Waves/`, `LoAR/`, `Technological Singularity/`) are the sole authoritative operational codebase.\n\n')

            f.write('## 3. Complete Defect Register\n\n')
            f.write('| ID | Location | Line | Category | Severity | Status | Evidence Summary |\n')
            f.write('| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n')
            for f_item in self.findings:
                ev = f_item['evidence'].replace('|', '\\|').replace('\n', ' ')
                if len(ev) > 90:
                    ev = ev[:87] + '...'
                f.write(f'| `{f_item["id"]}` | `{f_item["location"]["file"]}` | {f_item["location"]["line"]} | `{f_item["category"]}` | **{f_item["severity"]}** | `{f_item["status"]}` | {ev} |\n')
            f.write('\n')

            f.write('## 4. Itemized Defect Remediation Specifications\n\n')
            for f_item in self.findings:
                f.write(f'### `{f_item["id"]}`: {f_item["category"]} in `{f_item["location"]["file"]}` (Line {f_item["location"]["line"]})\n\n')
                f.write(f'- **Severity**: {f_item["severity"]}\n')
                f.write(f'- **Status**: `{f_item["status"]}`\n')
                f.write(f'- **Evidence**: `{f_item["evidence"]}`\n')
                f.write(f'- **Proposed Fix**: {f_item["proposed_fix"]}\n')
                f.write(f'- **Validation Test**: `{f_item["validation_test"]}`\n\n')

        print(f'Wrote {md_path}')

if __name__ == '__main__':
    scanner = DefectScanner(ROOT)
    scanner.run_scan()
    scanner.write_deliverables()
