## 2026-08-11T18 — 43:00Z
You are assigned to harden `scripts/audit_verification.py` and `tests/test_audit_verification.py` based on the Explorer findings in `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_explorer_m2_refactor_3_gen2/handoff.md`.

Context & Mandatory Files:
- Read `/Users/dylanboyle/Desktop/Convergence/.agents/ORIGINAL_REQUEST.md` and `/Users/dylanboyle/Desktop/Convergence/PROJECT.md`.
- Read `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_explorer_m2_refactor_3_gen2/handoff.md`.
- Working directory: `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_worker_m2_script_gen2`.

Write Ownership:
- You have EXCLUSIVE write ownership of `scripts/audit_verification.py` and `tests/test_audit_verification.py`.

Tasks:
1. Update `check_template_integrity` in `scripts/audit_verification.py`:
   - Fix the double-pipe table alignment check regex to `r"\|{2,}"` (or matching `|` without requiring 2+ whitespace characters between pipes) so that corrupted table alignment markers like `| :--- | :--- |` are flagged as template syntax errors.
   - Harden the robotic title suffix check to flag level 2/3 headings ending with `: [Document Title]` or `: Topic Name` patterns.
2. Update `check_cross_report_duplication` in `scripts/audit_verification.py`:
   - Enforce single-file line duplication caps (e.g. no single file may exceed 15.0% duplicate line overlap, in addition to folder averages).
3. Update `tests/test_audit_verification.py` to add test cases covering the new hardened regexes and single-file duplication caps.
4. Execute `python3 -m unittest discover tests` and `python3 scripts/audit_verification.py --strict` to verify all tests pass (100% PASS, 0 errors).

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Deliver your handoff report to `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_worker_m2_script_gen2/handoff.md` and update `progress.md`.