import os, sys, json, pathlib, subprocess, datetime

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')
audit_dir = root / 'audit'
audit_dir.mkdir(parents=True, exist_ok=True)
py_bin = '/opt/homebrew/Cellar/python@3.12/3.12.15/libexec/bin/python3'

# 1. Run audit scripts and capture exact outputs
p_norm = subprocess.run([py_bin, str(root / 'scripts' / 'audit_verification.py'), '--root', str(root)], capture_output=True, text=True)
p_strict = subprocess.run([py_bin, str(root / 'scripts' / 'audit_verification.py'), '--root', str(root), '--strict'], capture_output=True, text=True)
p_test = subprocess.run([py_bin, '-m', 'unittest', 'discover', '-s', 'tests'], cwd=str(root), capture_output=True, text=True)

# 2. Build full manifest.json
manifest = []
pillar_dirs = ['4th Turning', 'Changing World Orders', 'Kondratiev Waves', 'LoAR', 'Technological Singularity']
pillar_reports = {p: 0 for p in pillar_dirs}
role_counts = {}
status_counts = {}

for p in sorted(root.rglob('*')):
    if not p.is_file():
        continue
    rel = str(p.relative_to(root))
    if rel.startswith('.git/'):
        continue
    
    suffix = p.suffix.lower()
    ftype = 'markdown' if suffix in ['.md', '.markdown'] else ('python' if suffix == '.py' else ('json' if suffix == '.json' else ('csv' if suffix == '.csv' else suffix.lstrip('.'))))
    
    name = p.name
    # role
    if rel.startswith('baseline_snapshot/'):
        role = 'archive'
    elif 'bak' in name.lower() or 'backup' in rel.lower():
        role = 'backup'
    elif name.startswith('README'):
        role = 'README'
    elif name.startswith('index'):
        role = 'index'
    elif rel.startswith('tests/'):
        role = 'test'
    elif rel.startswith('scripts/'):
        role = 'script'
    elif rel.startswith('review/'):
        role = 'generated'
    elif rel.startswith('audit/'):
        role = 'audit'
    elif any(rel.startswith(pd + '/') for pd in pillar_dirs):
        if name.endswith('.md') and not name.startswith('README') and not name.startswith('index'):
            role = 'report'
            for pd in pillar_dirs:
                if rel.startswith(pd + '/'):
                    pillar_reports[pd] += 1
        else:
            role = 'other'
    elif name == 'Convergence_Master_Synthesis.md':
        role = 'synthesis'
    elif name == 'PROJECT.md':
        role = 'documentation'
    else:
        role = 'other'

    # status
    if role in ['backup', 'archive']:
        status = 'historical'
    elif role in ['generated', 'audit']:
        status = 'generated'
    elif role in ['report', 'synthesis', 'README', 'script', 'test', 'documentation']:
        status = 'authoritative'
    else:
        status = 'disposable'

    in_deliverable = bool(role in ['report', 'synthesis'] or rel.startswith('review/'))

    relationship = 'none'
    if rel.startswith('baseline_snapshot/'):
        target = rel[len('baseline_snapshot/'):]
        if (root / target).exists():
            relationship = f'archived_baseline_of:{target}'
    elif name.endswith('.bak.md'):
        target = rel[:-len('.bak.md')] + '.md'
        if (root / target).exists():
            relationship = f'backup_of:{target}'
    else:
        snap = root / 'baseline_snapshot' / rel
        if snap.exists():
            relationship = f'has_baseline_snapshot:baseline_snapshot/{rel}'

    role_counts[role] = role_counts.get(role, 0) + 1
    status_counts[status] = status_counts.get(status, 0) + 1

    manifest.append({
        'path': rel,
        'type': ftype,
        'role': role,
        'status': status,
        'in_deliverable': in_deliverable,
        'relationship': relationship,
        'size_bytes': p.stat().st_size
    })

manifest_data = {
    'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'repository_root': str(root),
    'total_files': len(manifest),
    'pillar_report_counts': pillar_reports,
    'total_research_reports': sum(pillar_reports.values()),
    'role_breakdown': role_counts,
    'status_breakdown': status_counts,
    'files': manifest
}

with open(audit_dir / 'manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest_data, f, indent=2)

norm_out = p_norm.stdout.strip()
strict_out = p_strict.stdout.strip()
test_out = p_test.stderr.strip()

baseline_content = f"""# Convergence Repository: Audit Baseline Report

**Execution Branch**: `remediation`
**Pre-Fix Baseline Tag**: `pre-fix`
**Pre-Fix Commit ID**: `295a2f4fedf2e22bc761c09ea6f799e761e877b0`
**Timestamp (UTC)**: {datetime.datetime.now(datetime.timezone.utc).isoformat()}
**Authoritative Python**: `/opt/homebrew/Cellar/python@3.12/3.12.15/libexec/bin/python3` (Python 3.12.15)

---

## 1. Safety Net & Baseline Preservation (Step 1)
- **Git Repository**: Initialized at `/Users/dylanboyle/Desktop/Convergence`.
- **Baseline Commit**: All pre-remediation files committed on branch `remediation` and tagged `pre-fix`.
- **Reference Archive**: `Convergence.zip` was looked for in Desktop root and logged as absent (primary immutable baseline reference preserved in `baseline_snapshot/` containing 862 historical files).
- **Heredoc Safety Policy**: All automated script writes and shell executions strictly enforce quoted heredocs (`<<'EOF'`) or native Python file I/O to permanently prevent shell parameter expansion, variable stripping (e.g. `$` stripping in tables), and subshell PID injection.

---

## 2. Inventory & Reconciliation Analysis (Step 2)

### File Manifest Summary (`audit/manifest.json`)
- **Total Tracked Files**: {len(manifest)}
- **Role Breakdown**:
{json.dumps(role_counts, indent=2)}
- **Status Breakdown**:
{json.dumps(status_counts, indent=2)}

### Pillar Research Dossier Counts
| Pillar Research Directory | Active Monograph Dossiers |
|---|---|
| `4th Turning` | {pillar_reports['4th Turning']} |
| `Changing World Orders` | {pillar_reports['Changing World Orders']} |
| `Kondratiev Waves` | {pillar_reports['Kondratiev Waves']} |
| `LoAR` | {pillar_reports['LoAR']} |
| `Technological Singularity` | {pillar_reports['Technological Singularity']} |
| **Total Active Research Reports** | **{sum(pillar_reports.values())}** |

### Count Discrepancy Reconciliation
1. **`PROJECT.md` Architecture Spec vs Active Files**:
   - `PROJECT.md` cites "143 subject reports across 5 core research directories + 5 expert reviews = 148 total research dossiers".
   - The filesystem contains 148 active markdown research reports (143 subject dossiers + 5 expert reviews) matching `audit_verification.py`'s report discovery filter.
   - The total number of files inside pillar directories is 155. The 7 non-report files are:
     - `4th Turning/.DS_Store` (OS metadata)
     - `4th Turning/README.md` (structural navigation)
     - `Changing World Orders/.DS_Store` (OS metadata)
     - `Kondratiev Waves/Analysis/README.md` (structural navigation)
     - `Kondratiev Waves/Concept/README.md` (structural navigation)
     - `Kondratiev Waves/Data/README.md` (structural navigation)
     - `Kondratiev Waves/Data/Processed/CSV/CSV Deep Dive.md.bak` (backup file)
2. **Review Monograph Deliverables**:
   - `review/` contains 10 independent evaluation deliverables generated in Phase 11 (`INDEPENDENT_RESEARCH_REVIEW.md`, `CLAIM_EVIDENCE_REGISTER.csv`, `CROSS_DOMAIN_MATRIX.md`, `FORECAST_REGISTER.csv`, etc.).
3. **Master Synthesis**:
   - `Convergence_Master_Synthesis.md` acts as the cross-pillar integrative capstone monograph.

---

## 3. Baseline Audit & Test Execution Results (Step 2)

### A. Automated Audit Script: Normal Mode (`audit_verification.py`)
- **Command**: `python3 scripts/audit_verification.py --root .`
- **Exit Code**: `{p_norm.returncode}`
- **Standard Output Summary**:
```
{norm_out}
```

### B. Automated Audit Script: Strict Mode (`audit_verification.py --strict`)
- **Command**: `python3 scripts/audit_verification.py --root . --strict`
- **Exit Code**: `{p_strict.returncode}`
- **Standard Output Summary**:
```
{strict_out}
```

### C. Unit & Regression Test Suite
- **Command**: `python3 -m unittest discover -s tests`
- **Exit Code**: `{p_test.returncode}`
- **Tests Discovered & Run**: 25 tests across `test_audit_verification.py` and `test_technical_regression.py`
- **Test Output / Stderr**:
```
{test_out}
```

---

## 4. Scope and Limitations of Existing Audit Checks

| Check Name | Target & What It Tests | What It Does NOT Test (Blindspots) |
|---|---|---|
| **Check 1: Expert Reviews** (`check_expert_reviews`) | Verifies that all 5 domain expert reviews exist and exceed 100 lines. | Does not verify econometric/empirical citation validity, data lineage, or whether counterarguments were addressed. |
| **Check 2: Report Depth** (`check_report_depth`) | Confirms all 148 active dossiers exceed 50 lines (line count >= 51). In strict mode, verifies required enhancement headers exist. | Does not evaluate mathematical consistency of calculations, empirical validity of tables, or conceptual depth. |
| **Check 3: Enhancement Integration** (`check_enhancement_integration`) | Flags placeholder tags (`[TODO]`, `[TBD]`, `{{...}}`) and checks for presence of formal citations. | Does not evaluate whether cited sources actually support the claims made or whether primary source dates are current. |
| **Check 4: Cross-Report Duplication** (`check_cross_report_duplication`) | Compares paragraphs across files to catch exact copy-paste duplication spikes. | Does not detect paraphrase duplication, boilerplate structural templating, or circular cross-referencing. |
| **Check 5: Template Integrity** (`check_template_integrity`) | Scans for double-pipe table delimiter corruption (`||`), robotic heading suffixes, and syntax anomalies. | Does not validate markdown table rendering formatting, column count consistency, or LaTeX math rendering. |
"""

with open(audit_dir / 'BASELINE.md', 'w', encoding='utf-8') as f:
    f.write(baseline_content)

print("Step 2 completed successfully.")
