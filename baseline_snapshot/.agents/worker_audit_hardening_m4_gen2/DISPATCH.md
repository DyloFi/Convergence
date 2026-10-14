## 2026-08-11T13 — 51:56Z
You are Worker 1 (Audit Verification Script Hardening Worker) for Milestone 4 (Gen 2 Iteration 3).

Working directory: `/Users/dylanboyle/Desktop/Convergence/.agents/worker_audit_hardening_m4_gen2`
Target directory: `/Users/dylanboyle/Desktop/Convergence`

Mandatory context files to read:
- `/Users/dylanboyle/Desktop/Convergence/.agents/ORIGINAL_REQUEST.md`
- `/Users/dylanboyle/Desktop/Convergence/PROJECT.md`
- `/Users/dylanboyle/Desktop/Convergence/.agents/auditor_1_m4_gen2/handoff.md`
- `/Users/dylanboyle/Desktop/Convergence/.agents/explorer_1_m4_gen2/handoff.md`

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Files Owned Exclusively:
- `scripts/audit_verification.py`
- `tests/test_audit_verification.py`

Assignment:
1. Update `scripts/audit_verification.py` according to Explorer 1's specification (`.agents/explorer_1_m4_gen2/handoff.md`):
   - Add Check 4 (`check_cross_report_duplication`): Calculate duplicate non-blank line percentage across subfolder reports per domain directory. Flag any domain directory where duplicate line percentage exceeds 15.0%. Exclude `*_Expert_Review.md` files.
   - Add Check 5 / Check 3 enhancement (`check_template_integrity`): Add regex checks for broken template tags (`regarding  and`, `reveals how  evolves`, `transitions in .`, `{topic}`, empty table column headers `|  Indicator`, dangling colons/periods).
   - Integrate Check 4 and Check 5 into `main()` execution flow so `python3 scripts/audit_verification.py --strict` executes all 5 checks.
2. Update `tests/test_audit_verification.py` to add unit test classes `TestCrossReportDuplicationCheck` and `TestBrokenTemplateTagCheck` verifying that the audit script detects high duplication (>15%) and broken template slots.
3. Run `python3 -m unittest discover tests` to verify all unit tests pass.

Deliver your handoff report to `/Users/dylanboyle/Desktop/Convergence/.agents/worker_audit_hardening_m4_gen2/handoff.md` documenting your exact changes, build/test execution outputs, and verification results.