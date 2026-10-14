# Project: Convergence Repository Multi-Agent Research Review, Enhancement & Verification

## Architecture
- **Subject Domains**: 5 core research directories (`4th Turning`, `Changing World Orders`, `Kondratiev Waves`, `LoAR`, `Technological Singularity`) containing 143 subject reports plus 1 master synthesis file (`Convergence_Master_Synthesis.md`).
- **Domain Expert Reviews**: 5 specialized expert review files (`4th_Turning_Expert_Review.md`, `Changing_World_Orders_Expert_Review.md`, `Kondratiev_Waves_Expert_Review.md`, `LoAR_Expert_Review.md`, `Technological_Singularity_Expert_Review.md`).
- **Automated Verification**: Zero-dependency Python verification suite (`scripts/audit_verification.py`) enforcing presence of expert review files, >50 lines depth standard across all 144+ reports, citation density, and zero placeholder text.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | 4th Turning Expert Review | Generational Theory domain expert deep audit and critique (`4th_Turning_Expert_Review.md`) | M1 | ORIGINAL_REQUEST §R1 |
| 2 | Changing World Orders Expert Review | Geopolitics & Hegemony domain expert deep audit and critique (`Changing_World_Orders_Expert_Review.md`) | M1 | ORIGINAL_REQUEST §R1 |
| 3 | Kondratiev Waves Expert Review | Long-Wave Economics domain expert deep audit and critique (`Kondratiev_Waves_Expert_Review.md`) | M1 | ORIGINAL_REQUEST §R1 |
| 4 | LoAR Expert Review | Exponential Tech & Compute domain expert deep audit and critique (`LoAR_Expert_Review.md`) | M1 | ORIGINAL_REQUEST §R1 |
| 5 | Technological Singularity Expert Review | AGI/ASI Alignment domain expert deep audit and critique (`Technological_Singularity_Expert_Review.md`) | M1 | ORIGINAL_REQUEST §R1 |
| 6 | 4th Turning Report Enhancements | Integrate recommendations, citations, and expand line depth (>50 lines) across 54 reports | M2 | ORIGINAL_REQUEST §R2 |
| 7 | Changing World Orders Enhancements | Integrate recommendations, citations, and expand line depth (>50 lines) across 15 reports | M2 | ORIGINAL_REQUEST §R2 |
| 8 | Kondratiev Waves Enhancements | Integrate recommendations, citations, and expand line depth (>50 lines) across 34 reports | M2 | ORIGINAL_REQUEST §R2 |
| 9 | LoAR Enhancements | Integrate recommendations, citations, and expand line depth (>50 lines) across 19 reports | M2 | ORIGINAL_REQUEST §R2 |
| 10 | Technological Singularity Enhancements | Integrate recommendations, citations, and expand line depth (>50 lines) across 21 reports | M2 | ORIGINAL_REQUEST §R2 |
| 11 | Master Synthesis Enhancement | Integrate cross-domain expert findings into `Convergence_Master_Synthesis.md` | M2 | ORIGINAL_REQUEST §R2 |
| 12 | Automated Verification Script | Zero-dependency Python verification tool at `scripts/audit_verification.py` verifying all criteria | M3 | ORIGINAL_REQUEST §R3 |
| 13 | Verification Test Harness | Python unit test suite executing automated verification across 100% of workspace reports | M3 | DUAL_TRACK_E2E |
| 14 | Final Gate Approval | 100% pass across all 144+ reports, 5 expert review files, and 0 audit errors | M4 | ORIGINAL_REQUEST §Criteria |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Domain Expert Audits (R1) | Generate all 5 dedicated domain expert review files | None | DONE |
| M2 | Report Enhancement & Integration (R2) | Apply expert recommendations across all 143 subject reports + 1 synthesis file | M1 | DONE |
| M3 | Automated Audit Suite (R3) | Implement `scripts/audit_verification.py` and test runner | None (Parallel Track) | DONE |
| M4 | Final E2E Gate & Verification | Run full verification suite against enhanced codebase and verify zero errors | M2, M3 | DONE |

## Interface Contracts

### Expert Review Files Contract
- Each review file must be located in its subject root directory or workspace root:
  - `4th Turning/4th_Turning_Expert_Review.md`
  - `Changing World Orders/Changing_World_Orders_Expert_Review.md`
  - `Kondratiev_Waves/Kondratiev_Waves_Expert_Review.md` (or `Kondratiev Waves/Kondratiev_Waves_Expert_Review.md`)
  - `LoAR/LoAR_Expert_Review.md`
  - `Technological Singularity/Technological_Singularity_Expert_Review.md`
- Each file must contain >50 lines of substantive critique, academic references, data tables, and enhancement specifications.

### Report Enhancement Contract
- Every subfolder report inside the 5 subject directories must meet:
  1. `line_count > 50` (at least 51 lines).
  2. Substantive domain additions (citations, datasets, historical context).
  3. Zero placeholder strings (`TODO`, `TBD`, `FIXME`, `[INSERT`).
  4. Parenthetical citations or section reference entries.

### Automated Verification Script Contract (`scripts/audit_verification.py`)
- Executable via standard Python: `python3 scripts/audit_verification.py`
- Exit Code: `0` on success (all checks pass), non-zero on failure.
- Returns structured JSON/text output listing total files checked, passed count, failed count, and detailed error messages per file.

## Code Layout
```
Convergence/
├── 4th Turning/                       # 54 reports + 4th_Turning_Expert_Review.md
├── Changing World Orders/             # 15 reports + Changing_World_Orders_Expert_Review.md
├── Kondratiev Waves/                  # 34 reports + Kondratiev_Waves_Expert_Review.md
├── LoAR/                              # 19 reports + LoAR_Expert_Review.md
├── Technological Singularity/         # 21 reports + Technological_Singularity_Expert_Review.md
├── Convergence_Master_Synthesis.md    # Master cross-domain synthesis (105+ lines)
├── scripts/
│   └── audit_verification.py          # Programmatic verification script (R3)
├── tests/
│   └── test_audit_verification.py     # Unit test runner for verification script
└── PROJECT.md                         # Project Master Plan & Feature Inventory
```