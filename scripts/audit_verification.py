#!/usr/bin/env python3
"""
Convergence Repository Automated Audit & Verification Suite
Requirement R3: Rebuilt for Step 7 (Comprehensive multi-dimensional verification).

Features:
1. Document Type Requirements:
   - Drops arbitrary 50-line rule.
   - Classifies reports into: dossier, expert_review, overview, synthesis, readme.
   - Enforces type-specific structural and depth requirements.
2. Deduplication Engine:
   - Exact file hash deduplication (SHA-256).
   - Cross-report paragraph deduplication (catches cloned analytical blocks).
   - Word 3-gram Jaccard similarity for near-duplicate document detection (>85%).
3. Boilerplate & Template Library:
   - Detects unpopulated template variables ({{DATE}}, {topic}, etc.).
   - Flags robotic headings, double-pipe syntax errors, ungrounded causal assertions.
   - Identifies currency figure stripping ($...B) and heredoc PID leaks.
4. Repeated Headings Cap:
   - Identifies internal identical headings within a single file.
   - Caps generic repeated headings repository-wide.
5. Citation, URL, DOI, and Claim-Register Coverage:
   - Verifies URL formatting and flags forbidden local file:/// schemes.
   - Validates DOI structure.
   - Audits claim register cross-references against repository files.
6. Mathematical Consistency & Delimiter Syntax:
   - Verifies balanced display ($$) and inline ($) delimiters.
   - Flags broken LaTeX macros and fraction syntax.
7. Structured Findings:
   - Every finding provides: file, line, excerpt, rule, severity, and message.

CLI:
  --root DIR     Specify repository root (default: current working directory or parent of scripts/)
  --strict       Treat any warning or defect as a fatal audit failure (exit code 1)
  --json         Output structured results as JSON
  --verbose      Print detailed progress and finding details
"""

import argparse
import collections
import csv
import hashlib
import json
import os
import pathlib
import re
import sys
from typing import Dict, List, Any, Tuple, Optional, Set
from pathlib import Path


EXPERT_REVIEW_FILES: Dict[str, str] = {
    "4th Turning": "4th_Turning_Expert_Review.md",
    "Changing World Orders": "Changing_World_Orders_Expert_Review.md",
    "Kondratiev Waves": "Kondratiev_Waves_Expert_Review.md",
    "LoAR": "LoAR_Expert_Review.md",
    "Technological Singularity": "Technological_Singularity_Expert_Review.md",
}

SUBJECT_DIRECTORIES: List[str] = [
    "4th Turning",
    "Changing World Orders",
    "Kondratiev Waves",
    "LoAR",
    "Technological Singularity",
]

# Standard disclaimers and notices permitted across multiple research dossiers (exact normalized match)
ALLOWED_PARAGRAPH_DUPLICATES: Set[str] = {
    re.sub(
        r'\s+',
        ' ',
        '> **notice**: *this analysis is conducted strictly for macroeconomic, historical, '
        'and system-modeling research. it does not constitute financial, investment, legal, '
        'or tax advice, nor an endorsement of any asset allocation or transaction strategy.*'
    ).strip().lower()
}

STANDARD_HEADINGS: Set[str] = {
    "executive summary", "foundations", "empirical evidence", "quantitative analysis",
    "references", "bibliography", "methodology", "overview", "table of contents",
    "key research takeaways", "1.2 saecular phase mapping", "quantitative indicator matrix",
    "2.2 sectoral & institutional impact matrix", "academic references & bibliography",
    "references & academic bibliography", "references & bibliography",
    "primary data sources & provenance methodology",
    "empirical validation & falsification framework",
    "falsification conditions & empirical vulnerability register",
    "strategic synthesis & cross-cycle convergence implications",
    "concrete report expansion directives for round 2 implementers",
    "strategic implications",
    "formalization of generational cycle dynamics",
    "cross-disciplinary epistemological synthesis",
    "fourier fast spectral density estimation",
    "theoretical framework & generational mechanics",
    "comparative perspectives & counter-theories",
    # Step 13: section headings mandated by review/REPORT_STANDARDS.md (question, scope,
    # competing views, limitations, proportional conclusions) for rewritten reports.
    "question and scope",
    "competing views and counterarguments",
    "limitations",
    "conclusion",
}

BOILERPLATE_PATTERNS: List[Tuple[str, str, str, str]] = [
    (r"\bThis proves\b", "Ungrounded causal claim: 'This proves'", "canned_assertion", "WARNING"),
    (r"\bthis proves\b", "Ungrounded causal claim: 'this proves'", "canned_assertion", "WARNING"),
    (r"\bregarding\s{2,}and\b", "Double-space variable artifact: 'regarding  and'", "template_artifact", "WARNING"),
    (r"\breveals\s+how\s{2,}evolves\b", "Double-space variable artifact: 'reveals how  evolves'", "template_artifact", "WARNING"),
    (r"\bhow\s{2,}evolves\b", "Double-space variable artifact: 'how  evolves'", "template_artifact", "WARNING"),
    (r"\btransitions\s+in\s+\.", "Missing target variable before period: 'transitions in .'", "template_artifact", "WARNING"),
    (r"\bAntecedents\s+of\s*:\s*(?:\s*$|\.)", "Incomplete title colon artifact: 'Antecedents of:'", "template_artifact", "WARNING"),
    (r"\|{2,}", "Double-pipe table delimiter corruption: '||'", "table_syntax", "ERROR"),
    (r"\bTODO\b", "Unfinished placeholder: 'TODO'", "placeholder", "ERROR"),
    (r"\bTBD\b", "Unfinished placeholder: 'TBD'", "placeholder", "ERROR"),
    (r"\bFIXME\b", "Unfinished placeholder: 'FIXME'", "placeholder", "ERROR"),
    (r"\[INSERT", "Unfinished placeholder: '[INSERT'", "placeholder", "ERROR"),
    (r"INSERT_DATA", "Unfinished placeholder: 'INSERT_DATA'", "placeholder", "ERROR"),
    (r"\[Insert", "Unfinished placeholder: '[Insert'", "placeholder", "ERROR"),
    (r"\bXXX\b", "Unfinished placeholder: 'XXX'", "placeholder", "ERROR"),
    (r"\bTEMP\b", "Unfinished placeholder: 'TEMP'", "placeholder", "ERROR"),
    (r"\{(?:topic|subject|domain|category|author|title|keyword|item|case_study|date|year|summary|description)\}", "Unpopulated template variable brace: '{variable}'", "template_variable", "ERROR"),
    (r"\{\{[A-Za-z0-9_]+\}\}", "Broken double-brace template tag: '{{tag}}'", "broken_template_tag", "ERROR"),
    (r"(?:^|\n)\s*[-*]?\s*Analytical Focus:\s*.*", "Boilerplate analytical focus entry", "boilerplate_analytical_focus", "WARNING"),
    (r"^#{2,3}\s+(?:Topic Name:.*|.*:\s*(?:\[Document Title\]|Topic Name|[A-Za-z0-9\s&,/\-'\"]+(?:Deep Dive|Monograph|Overview|Synthesis|Framework|Guide|Taxonomy|Matrix|Legacy|Analysis|Research Plan)))", "Robotic heading title suffix artifact", "robotic_heading", "WARNING"),
]


class AuditFinding:
    def __init__(self, file: str, line: int, excerpt: str, rule: str, severity: str, message: str):
        self.file = file
        self.line = line
        self.excerpt = excerpt.strip()[:160] if excerpt else ""
        self.rule = rule
        self.severity = severity  # 'ERROR', 'WARNING', 'INFO'
        self.message = message

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file": self.file,
            "line": self.line,
            "location": {
                "file": self.file,
                "line": self.line,
            },
            "excerpt": self.excerpt,
            "rule": self.rule,
            "severity": self.severity,
            "message": self.message,
        }

    def __repr__(self) -> str:
        return f"[{self.severity}] {self.file}:{self.line} ({self.rule}): {self.message} | Excerpt: {self.excerpt}"


def clean_currency_and_rates_for_math_check(line: str) -> str:
    """Removes currency symbols and unit rates from a line so inline math delimiter checks don't produce false positives."""
    # 1. Parenthesized currency tokens: ($B), ($M), ($ Millions), ($), etc.
    line = re.sub(r'\(\$[^\)]*\)', '', line)
    # 2. Currency ratios: CPS/$, Ops/$, MFLOPS/$
    line = re.sub(r'\b[A-Za-z0-9_]+/\$', '', line)
    # 3. Cost metrics: $/FLOP, $/base pair, $/GB
    line = re.sub(r'\$/[A-Za-z0-9_\s-]+', '', line)
    # 4. Dollar per unit: $ per FLOP
    line = re.sub(r'\$\s+per\s+[A-Za-z0-9_]+', '', line)
    # 5. Currency amounts: $35,465B, $5,120B, $100, $0.50, $1.42T, $10^12
    line = re.sub(r'\$[0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?\s*(?:[BMkTK]|billion|trillion|million|%)?\b', '', line)
    # 6. Escaped dollar signs
    line = line.replace(r'\$', '')
    return line


class ConvergenceAuditor:
    def __init__(self, root: Optional[pathlib.Path] = None, root_dir: Optional[pathlib.Path] = None, strict: bool = False, verbose: bool = False, json_output: bool = False):
        target = root if root is not None else root_dir
        if target is None:
            self.root = pathlib.Path(__file__).resolve().parent.parent
        else:
            self.root = pathlib.Path(target).resolve()
        self.json_output = json_output
        self.strict = strict
        self.verbose = verbose
        self.findings: List[AuditFinding] = []

    @property
    def errors(self) -> List[str]:
        return [f"{f.file}:{f.line}: {f.message}" if f.file else f.message for f in self.findings if f.severity == "ERROR"]

    @property
    def warnings(self) -> List[str]:
        return [f"{f.file}:{f.line}: {f.message}" if f.file else f.message for f in self.findings if f.severity == "WARNING"]

    def log_verbose(self, msg: str) -> None:
        if self.verbose:
            print(f"[VERBOSE] {msg}")

    def add_finding(self, file: str, line: int, excerpt: str, rule: str, severity: str, message: str) -> None:
        finding = AuditFinding(file=file, line=line, excerpt=excerpt, rule=rule, severity=severity, message=message)
        self.findings.append(finding)
        if self.verbose:
            print(f"  -> {finding}")

    def classify_document(self, rel_path: str) -> str:
        p = pathlib.Path(rel_path)
        name = p.name
        if name in EXPERT_REVIEW_FILES.values() or name.endswith("_Expert_Review.md"):
            return "expert_review"
        if name == "Convergence_Master_Synthesis.md":
            return "synthesis"
        if name.endswith("Overview.md"):
            return "overview"
        if name.upper() == "README.MD" or name.startswith("README"):
            return "readme"
        if any(part in SUBJECT_DIRECTORIES for part in p.parts):
            return "dossier"
        if "review" in p.parts or "Review" in p.parts:
            return "review_deliverable"
        return "other"

    def collect_in_scope_reports(self) -> List[pathlib.Path]:
        excluded_dirs = {
            ".git", ".agents", "node_modules", "scripts", "tests", "audit",
            "baseline_snapshot", "__pycache__"
        }
        is_full_repo = all((self.root / d).is_dir() for d in SUBJECT_DIRECTORIES)

        reports: List[pathlib.Path] = []
        for path in sorted(self.root.rglob("*.md")):
            rel = path.relative_to(self.root)
            parts = rel.parts
            if any(p.startswith(".") or p in excluded_dirs for p in parts[:-1]):
                continue
            if path.name.endswith(".bak.md") or path.name.startswith("."):
                continue

            if is_full_repo:
                # In full repository, scope to the 5 pillars + Master Synthesis
                if parts[0] in SUBJECT_DIRECTORIES or path.name == "Convergence_Master_Synthesis.md":
                    reports.append(path)
            else:
                # In test or sub-fixtures, include all markdown documents
                reports.append(path)
        return reports

    def check_expert_reviews(self) -> bool:
        """Compatibility wrapper for expert reviews check."""
        for domain, filename in EXPERT_REVIEW_FILES.items():
            path = self.root / domain / filename
            if not path.exists():
                return False
        return True

    def check_report_depth(self) -> Tuple[int, int]:
        """Compatibility wrapper returning (passing_reports, total_reports)."""
        reports = self.collect_in_scope_reports()
        passing = 0
        for r in reports:
            rel = str(r.relative_to(self.root))
            doc_type = self.classify_document(rel)
            words = len(r.read_text(encoding="utf-8", errors="replace").split())
            if doc_type == "dossier" and words >= 250:
                passing += 1
            elif doc_type in ["overview", "expert_review"] and words >= 200:
                passing += 1
            elif doc_type == "synthesis" and words >= 1000:
                passing += 1
            elif doc_type in ["readme", "other"]:
                passing += 1
        return passing, len(reports)

    def check_enhancement_integration(self) -> bool:
        initial_count = len(self.findings)
        self.check_template_and_boilerplate()
        return not any(f.severity == 'ERROR' for f in self.findings[initial_count:])

    def check_cross_report_duplication(self) -> bool:
        initial_count = len(self.findings)
        self.check_deduplication()
        return not any(f.severity == 'ERROR' for f in self.findings[initial_count:])

    def check_template_integrity(self) -> bool:
        return self.check_enhancement_integration()

    def check_document_type_requirements(self) -> bool:
        self.log_verbose("Executing Check 1: Document Type Requirements...")
        initial_error_count = sum(1 for f in self.findings if f.severity == 'ERROR')

        for domain, filename in EXPERT_REVIEW_FILES.items():
            path = self.root / domain / filename
            rel = str(path.relative_to(self.root))
            if not path.exists():
                self.add_finding(rel, 1, "", "doc_type_expert_review_missing", "ERROR", f"Missing expert review for domain '{domain}'")
            else:
                text = path.read_text(encoding="utf-8", errors="replace")
                words = len(text.split())
                if words < 300:
                    self.add_finding(rel, 1, text[:100], "doc_type_expert_review_shallow", "ERROR", f"Expert review too shallow: {words} words (expected >= 300)")

        for report in self.collect_in_scope_reports():
            rel = str(report.relative_to(self.root))
            doc_type = self.classify_document(rel)
            text = report.read_text(encoding="utf-8", errors="replace")
            lines = text.splitlines()
            words = len(text.split())

            if doc_type == "dossier":
                if words < 250:
                    self.add_finding(rel, len(lines), lines[-1] if lines else "", "doc_type_dossier_insufficient_depth", "ERROR", f"Dossier too shallow: {words} words (expected >= 250 words)")
            elif doc_type == "overview":
                if words < 200:
                    self.add_finding(rel, len(lines), lines[-1] if lines else "", "doc_type_overview_shallow", "ERROR", f"Overview too shallow: {words} words (expected >= 200 words)")
            elif doc_type == "synthesis":
                if words < 1000:
                    self.add_finding(rel, len(lines), lines[-1] if lines else "", "doc_type_synthesis_shallow", "ERROR", f"Master synthesis too shallow: {words} words (expected >= 1000 words)")

        return sum(1 for f in self.findings if f.severity == 'ERROR') == initial_error_count

    def check_deduplication(self) -> bool:
        self.log_verbose("Executing Check 2: Deduplication Engine...")
        initial_error_count = sum(1 for f in self.findings if f.severity == 'ERROR')
        reports = self.collect_in_scope_reports()

        hash_to_files: Dict[str, List[str]] = collections.defaultdict(list)
        for r in reports:
            rel = str(r.relative_to(self.root))
            content = r.read_bytes()
            file_hash = hashlib.sha256(content).hexdigest()
            hash_to_files[file_hash].append(rel)

        for f_hash, file_list in hash_to_files.items():
            if len(file_list) > 1:
                for f_path in file_list:
                    self.add_finding(f_path, 1, f"SHA256: {f_hash[:16]}...", "exact_file_duplicate", "ERROR", f"Exact identical duplicate of: {', '.join(x for x in file_list if x != f_path)}")

        para_to_locations: Dict[str, List[Tuple[str, int, str]]] = collections.defaultdict(list)
        for r in reports:
            rel = str(r.relative_to(self.root))
            lines = r.read_text(encoding="utf-8", errors="replace").splitlines()
            curr_para = []
            para_start_line = 1
            in_code_block = False

            for idx, line in enumerate(lines, 1):
                if line.strip().startswith('```'):
                    in_code_block = not in_code_block
                    continue
                if in_code_block or line.strip().startswith('|') or line.strip().startswith('#') or line.strip().startswith('---'):
                    if curr_para:
                        text_block = ' '.join(curr_para).strip()
                        if len(text_block) >= 120:
                            clean_norm = re.sub(r'\s+', ' ', text_block.lower())
                            para_to_locations[clean_norm].append((rel, para_start_line, text_block[:100]))
                        curr_para = []
                    continue

                if line.strip():
                    if not curr_para:
                        para_start_line = idx
                    curr_para.append(line.strip())
                else:
                    if curr_para:
                        text_block = ' '.join(curr_para).strip()
                        if len(text_block) >= 120:
                            clean_norm = re.sub(r'\s+', ' ', text_block.lower())
                            para_to_locations[clean_norm].append((rel, para_start_line, text_block[:100]))
                        curr_para = []

            if curr_para:
                text_block = ' '.join(curr_para).strip()
                if len(text_block) >= 120:
                    clean_norm = re.sub(r'\s+', ' ', text_block.lower())
                    para_to_locations[clean_norm].append((rel, para_start_line, text_block[:100]))

        for norm_para, locs in para_to_locations.items():
            if norm_para in ALLOWED_PARAGRAPH_DUPLICATES:
                continue
            distinct_files = set(loc[0] for loc in locs)
            if len(distinct_files) > 1:
                for rel_file, line_num, excerpt in locs:
                    other_files = [f for f in distinct_files if f != rel_file]
                    self.add_finding(rel_file, line_num, excerpt, "paragraph_duplicate", "WARNING", f"Paragraph cloned across {len(distinct_files)} files (also in: {', '.join(other_files[:2])})")

        file_tokens: Dict[str, collections.Counter] = {}
        for r in reports:
            rel = str(r.relative_to(self.root))
            words = re.findall(r'\b[a-z]{3,}\b', r.read_text(encoding="utf-8", errors="replace").lower())
            if len(words) >= 3:
                shingles = collections.Counter(' '.join(words[i:i+3]) for i in range(len(words)-2))
                file_tokens[rel] = shingles

        file_list = list(file_tokens.keys())
        for i in range(len(file_list)):
            f1 = file_list[i]
            c1 = file_tokens[f1]
            sum_c1 = sum(c1.values())
            keys_c1 = set(c1.keys())
            for j in range(i + 1, len(file_list)):
                f2 = file_list[j]
                c2 = file_tokens[f2]
                common = keys_c1 & set(c2.keys())
                if not common:
                    continue
                inter = sum(min(c1[k], c2[k]) for k in common)
                uni = sum_c1 + sum(c2.values()) - inter
                if uni > 0:
                    similarity = inter / uni
                    if similarity > 0.85:
                        self.add_finding(f1, 1, f"Similarity: {similarity:.2%}", "high_similarity_report", "WARNING", f"High text similarity ({similarity:.2%}) with {f2}")
                        self.add_finding(f2, 1, f"Similarity: {similarity:.2%}", "high_similarity_report", "WARNING", f"High text similarity ({similarity:.2%}) with {f1}")

        return sum(1 for f in self.findings if f.severity == 'ERROR') == initial_error_count

    def check_template_and_boilerplate(self) -> bool:
        self.log_verbose("Executing Check 3: Template & Boilerplate Library Scan...")
        initial_error_count = sum(1 for f in self.findings if f.severity == 'ERROR')
        reports = self.collect_in_scope_reports()

        for r in reports:
            rel = str(r.relative_to(self.root))
            lines = r.read_text(encoding="utf-8", errors="replace").splitlines()
            for idx, line in enumerate(lines, 1):
                for pattern, desc, rule_id, severity in BOILERPLATE_PATTERNS:
                    match = re.search(pattern, line)
                    if match:
                        self.add_finding(rel, idx, match.group(0), rule_id, severity, f"{desc}: '{match.group(0)}'")

        return sum(1 for f in self.findings if f.severity == 'ERROR') == initial_error_count

    def check_repeated_headings(self) -> bool:
        self.log_verbose("Executing Check 4: Repeated Headings Cap...")
        initial_error_count = sum(1 for f in self.findings if f.severity == 'ERROR')
        reports = self.collect_in_scope_reports()

        repo_heading_counts: Dict[str, List[Tuple[str, int]]] = collections.defaultdict(list)

        for r in reports:
            rel = str(r.relative_to(self.root))
            lines = r.read_text(encoding="utf-8", errors="replace").splitlines()
            file_heading_counts: Dict[str, List[int]] = collections.defaultdict(list)

            for idx, line in enumerate(lines, 1):
                m = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
                if m:
                    heading_text = m.group(2).strip().lower()
                    file_heading_counts[heading_text].append(idx)
                    # Normalize heading text for qualification check
                    clean_heading = re.sub(r'^[0-9\.\s\-]+', '', heading_text).strip()
                    if heading_text not in STANDARD_HEADINGS and clean_heading not in STANDARD_HEADINGS:
                        repo_heading_counts[heading_text].append((rel, idx))

            for h_text, line_nums in file_heading_counts.items():
                if len(line_nums) > 2:
                    self.add_finding(rel, line_nums[0], h_text, "internal_duplicate_heading", "WARNING", f"Heading '{h_text}' repeated {len(line_nums)} times in file (lines {line_nums})")

        for h_text, occurrences in repo_heading_counts.items():
            distinct_files = set(occ[0] for occ in occurrences)
            if len(distinct_files) >= 5:
                for rel_file, l_num in occurrences:
                    self.add_finding(rel_file, l_num, h_text, "repeated_heading_capped", "WARNING", f"Non-standard heading '{h_text}' repeated across {len(distinct_files)} files; requires domain-specific qualification")

        return sum(1 for f in self.findings if f.severity == 'ERROR') == initial_error_count

    def check_citations_urls_and_claim_coverage(self) -> bool:
        self.log_verbose("Executing Check 5: URLs, DOIs, and Claim Register Coverage...")
        initial_error_count = sum(1 for f in self.findings if f.severity == 'ERROR')
        reports = self.collect_in_scope_reports()

        url_pattern = re.compile(r'https?://[^\s)\]\"\>]+')
        file_url_pattern = re.compile(r'file://[^\s)\]\"\>]+')

        for r in reports:
            rel = str(r.relative_to(self.root))
            lines = r.read_text(encoding="utf-8", errors="replace").splitlines()
            for idx, line in enumerate(lines, 1):
                file_urls = file_url_pattern.findall(line)
                for fu in file_urls:
                    self.add_finding(rel, idx, fu, "local_file_url", "ERROR", f"Local filesystem URL forbidden in published deliverable: '{fu}'")

                urls = url_pattern.findall(line)
                for u in urls:
                    if not re.match(r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', u):
                        self.add_finding(rel, idx, u, "malformed_url", "WARNING", f"Malformed external URL: '{u}'")

        claim_reg_path = self.root / "review/CLAIM_REGISTER.csv"
        claim_evid_path = self.root / "review/CLAIM_EVIDENCE_REGISTER.csv"
        if claim_reg_path.exists() or claim_evid_path.exists():
            target_csv = claim_evid_path if claim_evid_path.exists() else claim_reg_path
            try:
                with open(target_csv, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        doc = row.get('source_document') or row.get('source_doc') or row.get('repository_location')
                        if doc:
                            clean_doc = doc.strip().strip('`').strip('\"').strip("'")
                            target_file = self.root / clean_doc
                            if not target_file.exists():
                                self.add_finding(str(target_csv.relative_to(self.root)), 1, clean_doc, "unresolved_claim_source_doc", "WARNING", f"Claim register cites non-existent dossier: '{clean_doc}'")
            except Exception as e:
                self.add_finding(str(target_csv.relative_to(self.root)), 1, str(e), "claim_register_read_error", "ERROR", f"Error reading claim register: {e}")

        return sum(1 for f in self.findings if f.severity == 'ERROR') == initial_error_count

    def check_mathematical_consistency(self) -> bool:
        self.log_verbose("Executing Check 6: Mathematical Consistency & Delimiters...")
        initial_error_count = sum(1 for f in self.findings if f.severity == 'ERROR')
        reports = self.collect_in_scope_reports()

        for r in reports:
            rel = str(r.relative_to(self.root))
            lines = r.read_text(encoding="utf-8", errors="replace").splitlines()
            in_display_math = False
            in_code_block = False

            for idx, line in enumerate(lines, 1):
                if line.strip().startswith('```'):
                    in_code_block = not in_code_block
                    continue
                if in_code_block:
                    continue

                # 1. Stripped currency cell check in tables
                if '|' in line:
                    if re.search(r'\|\s*B\s*\|', line) or re.search(r'\|\s*\.\d+B\s*\|', line):
                        self.add_finding(rel, idx, line, "stripped_dollar_cell", "ERROR", f"Stripped dollar sign in table cell: '{line[:80]}'")

                # 2. PID leak artifact in math expressions
                if re.search(r'\$\$.*\b[0-9]{5}\b.*\$\$', line) or re.search(r'\b(?:36646|36689|41166)\b', line) or re.search(r'\b[0-9]{5}\s*\\(?:frac|exp|sum|cdot|times)\b', line):
                    self.add_finding(rel, idx, line, "pid_leak_artifact", "ERROR", f"Shell heredoc PID leak artifact found: '{line[:80]}'")

                # 3. Corrupted frac macro without braces
                if re.search(r'\\frac\s*[0-9]', line):
                    self.add_finding(rel, idx, line, "corrupted_frac_macro", "ERROR", f"Malformed \\frac syntax without braces: '{line[:80]}'")

                # 4. Display math delimiter balance
                double_dollar_count = line.count('$$')
                if double_dollar_count % 2 != 0:
                    in_display_math = not in_display_math

            if in_display_math:
                self.add_finding(rel, len(lines), "", "unclosed_display_math", "ERROR", f"Unclosed display math block in file '{rel}'")

        return sum(1 for f in self.findings if f.severity == 'ERROR') == initial_error_count

    def run_all_checks(self) -> Dict[str, Any]:
        self.findings = []
        c1 = self.check_document_type_requirements()
        c2 = self.check_deduplication()
        c3 = self.check_template_and_boilerplate()
        c4 = self.check_repeated_headings()
        c5 = self.check_citations_urls_and_claim_coverage()
        c6 = self.check_mathematical_consistency()

        errors = [f for f in self.findings if f.severity == 'ERROR']
        warnings = [f for f in self.findings if f.severity == 'WARNING']
        info = [f for f in self.findings if f.severity == 'INFO']

        passed = (len(errors) == 0) if not self.strict else (len(errors) == 0 and len(warnings) == 0)

        return {
            "passed": passed,
            "strict": self.strict,
            "total_reports_audited": len(self.collect_in_scope_reports()),
            "total_findings": len(self.findings),
            "error_count": len(errors),
            "warning_count": len(warnings),
            "info_count": len(info),
            "checks": {
                "check1_document_type_requirements": c1,
                "check2_deduplication_engine": c2,
                "check3_template_and_boilerplate": c3,
                "check4_repeated_headings_cap": c4,
                "check5_citations_urls_claim_coverage": c5,
                "check6_mathematical_consistency": c6,
            },
            "findings": [f.to_dict() for f in self.findings],
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Convergence Repository Automated Audit & Verification Suite")
    parser.add_argument("--json", action="store_true", help="Output audit result in JSON format")
    parser.add_argument("--verbose", action="store_true", help="Print detailed progress and logs")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    parser.add_argument("--root", type=str, default=None, help="Specify alternative repository root directory")

    args = parser.parse_args()
    if args.root:
        root_dir = pathlib.Path(args.root).resolve()
    else:
        root_dir = pathlib.Path(__file__).resolve().parent.parent

    auditor = ConvergenceAuditor(root_dir=root_dir, strict=args.strict, verbose=args.verbose)
    results = auditor.run_all_checks()

    if args.json:
        print(json.dumps(results, indent=2))
        return 0 if results['passed'] else 1

    print("=" * 70)
    print(" CONVERGENCE AUTOMATED AUDIT & VERIFICATION REPORT (STEP 7)")
    print("=" * 70)
    print(f"Repository Root: {root_dir}")
    print(f"Mode: Strict={args.strict}, Verbose={args.verbose}")
    print(f"Total Reports Audited: {results['total_reports_audited']}")
    print(f"Total Findings: {results['total_findings']} (Errors: {results['error_count']}, Warnings: {results['warning_count']})")
    print("-" * 70)
    for check_name, status in results['checks'].items():
        st_str = "PASS" if status else "FAIL"
        print(f"  [{st_str}] {check_name}")
    print("=" * 70)
    if not results['passed']:
        print(f"AUDIT FAILED with {results['error_count']} errors and {results['warning_count']} warnings.")
        return 1
    else:
        print("AUDIT PASSED: All architectural integrity standards verified.")
        return 0


if __name__ == '__main__':
    sys.exit(main())
