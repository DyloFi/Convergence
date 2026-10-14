## 2026-08-11T18 — 42:54Z

You are assigned to refactor all markdown reports across the 4 domain directories (`Changing World Orders`, `Kondratiev Waves`, `LoAR`, `Technological Singularity`) in `/Users/dylanboyle/Desktop/Convergence`.

Context & Mandatory Files:
- Read `/Users/dylanboyle/Desktop/Convergence/.agents/ORIGINAL_REQUEST.md` and `/Users/dylanboyle/Desktop/Convergence/PROJECT.md`.
- Read Explorer handoffs:
  - `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_explorer_m2_refactor_1_gen2/handoff.md` (Changing World Orders & Kondratiev Waves specs)
  - `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_explorer_m2_refactor_2_gen2/handoff.md` (LoAR & Technological Singularity specs)
  - `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_explorer_m2_refactor_3_gen2/handoff.md` (Double-pipe `||` table syntax and robotic header suffix list)
- Working directory: `/Users/dylanboyle/Desktop/Convergence/.agents/teamwork_preview_worker_m2_refactor_gen2`.

Write Ownership:
- You have EXCLUSIVE write ownership of markdown files in `Changing World Orders/`, `Kondratiev Waves/`, `LoAR/`, and `Technological Singularity/`. Do NOT touch `scripts/` or `tests/`.

Tasks:
1. Fix all 35 files containing corrupted `||` double-pipe markdown table syntax by replacing `||` with valid `|` column delimiters.
2. Remove robotic header suffixes (e.g. `: [Document Title]` or `: Topic Name`) across all 39 flagged files, replacing them with natural, topic-tailored section titles.
3. Refactor high-duplication files (`JSON Deep Dive.md` in Kondratiev Waves and `00_Research_Plan.md` in Changing World Orders) to eliminate repeated schema keys/closing braces and table borders, bringing single-file duplicate line rates below 5.0%.
4. Refactor shared ASCII diagrams, repeated table headers, LaTeX equations, and verbatim sentences across all 89 reports in the 4 domain directories, replacing them with unique, topic-tailored analytical text.
5. Run `python3 scripts/audit_verification.py --strict` and `python3 -m unittest discover tests` to verify exit code 0 and 0 errors across all 5 checks.