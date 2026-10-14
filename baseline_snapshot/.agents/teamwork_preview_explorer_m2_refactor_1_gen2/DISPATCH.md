## 2026-08-11T18 — 41:18Z
You are assigned to investigate and create a detailed content refactoring specification for the reports in `Changing World Orders` (15 reports) and `Kondratiev Waves` (34 reports) under `/Users/dylanboyle/Desktop/Convergence`.

Context and Requirements:
- Read `/Users/dylanboyle/Desktop/Convergence/.agents/ORIGINAL_REQUEST.md` and `/Users/dylanboyle/Desktop/Convergence/PROJECT.md`.
- Read your working directory: `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_explorer_m2_refactor_1_gen2`.
- Run `python3 scripts/audit_verification.py --strict` to measure the current duplicate line percentage for `Changing World Orders` and `Kondratiev Waves`.
- Analyze all report files in `Changing World Orders/` and `Kondratiev Waves/` to identify shared boilerplates, copy-pasted blocks, or template tags.
- For each report file in these two directories, detail:
  1. Current line count and duplicate line percentage.
  2. Concrete topic-tailored replacement sections and analytical text to eliminate shared lines and bring duplicate overlap well below 15.0%.
- Write your investigation findings and step-by-step refactoring instructions to `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_explorer_m2_refactor_1_gen2/handoff.md` and update `progress.md`.