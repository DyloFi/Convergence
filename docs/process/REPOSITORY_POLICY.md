# Convergence Repository Policy

## Scope and source of truth

This policy applies only to `DyloFi/Convergence`. GitHub is the source of truth for repository files, branches, commits, and provenance. Keep Step 16 changes on `remediation`; do not modify other repositories or unrelated paths. Preserve the existing domain names and case exactly.

## Canonical locations

- Research reports remain in the five existing domain directories: `4th Turning/`, `Changing World Orders/`, `Kondratiev Waves/`, `LoAR/`, and `Technological Singularity/`.
- The current master synthesis remains `Convergence_Master_Synthesis.md` at the repository root.
- Reusable scripts belong in `scripts/`. `scripts/audit_verification.py` is the canonical verification tool documented by `PROJECT.md`.
- Verification tests belong in `tests/`, including `tests/test_audit_verification.py`.
- Research review material currently in `review/` is process documentation. For Step 16, the intended destination is `docs/process/review/`, preserving all existing relative paths and contents.
- Existing `.agents/` instructions and handoff records are process material. For Step 16, the intended destination is `docs/process/.agents/`, preserving all existing relative paths and contents.
- Keep source data and evidence in their current domain-specific locations. Do not relocate source material as part of repository hygiene.

## Naming and generated artifacts

Use descriptive names for new durable files and snake_case for new Python scripts. Do not add ad hoc backup siblings to canonical source directories. Any archival copy must have a recorded original path and a manifest entry. Existing legacy names are preserved unless a separately authorized change explicitly renames them.

`.gitignore` currently excludes `__pycache__/`, `*.pyc`, `audit/tmp_*.json`, and `*.zip`. Treat these as generated or temporary artifacts, not source material. `.bak` variants are not currently ignored by `.gitignore`; do not create new `.bak` files, and do not assume a suffix alone is enough to delete an existing file without listing it in the approved Step 16 inventory.

## Review, scripts, and archive records

Keep review reports, claim and forecast registers, source audits, and triage records together under the process-review location after the authorized move. Classify scripts by file path and evidenced role, not by count or filename alone. The requested 167 one-off and 15 retained split must be reconciled against the complete current script inventory before any script is archived; retain a per-file disposition list.

Keep `archive/step13_originals/` and its `MANIFEST.csv` separate and untouched. The intended Step 16 archive location for individually classified one-off scripts is `archive/step16_one_off_scripts/`, preserving their source-relative paths and recording their dispositions. Do not mix Step 16 material into the Step 13 archive.

## Provenance, hashes, and reversible hygiene

Before any move or deletion, record every affected path, file type, GitHub blob SHA, byte size where available, source branch and commit, intended destination or deletion disposition, and the exact operation. State the hash field and algorithm explicitly; a GitHub blob SHA and a SHA-256 digest are distinct fields. For a move, record both old and new paths and verify the file content remains unchanged. Keep a before/after inventory and a disposition log for each file group.

Use only the specifically approved Step 16 categories. Do not discard source, research, review, or provenance files as generated artifacts. Complete the independent ChatGPT review gate in DYL-48 before moving or deleting any files. Keep the `pre-fix` tag as the recovery reference; as read on 2026-11-08, `pre-fix` points to commit `295a2f4fedf2e22bc761c09ea6f799e761e877b0`, whose root tree SHA is `308ff64292ddcba0dbf1320c14225e006edeaa34`. The `baseline_snapshot/` tree at the reviewed `remediation` revision `37c42d775919bcc91cb0d87f453b6ab34eb3ff99` has tree SHA `e0009670a11ad0998bc75ef74d940d1109f4af44`; this does not match the tag's root tree. The verified root-entry comparison is 17 entries at the tag root and 12 in `baseline_snapshot/`. The snapshot omits `.DS_Store`, `AUDIT_BASELINE.md`, `audit_baseline.json`, `baseline_snapshot/`, and `review/`. Of the 12 shared root paths, the Git tree/blob SHAs match for `Kondratiev Waves/`, `PROJECT.md`, and `TEST_READY.md`; these nine paths differ: `.agents/`, `4th Turning/`, `Changing World Orders/`, `Convergence_Master_Synthesis.bak.md`, `Convergence_Master_Synthesis.md`, `LoAR/`, `Technological Singularity/`, `scripts/`, and `tests/`. This is a root-entry comparison only; it does not establish descendant-level file matches, differences, or a complete inventory/disposition. Do not treat `baseline_snapshot/` as a full-tree mirror. Do not remove the snapshot until a complete descendant-level comparison and inventory establish its disposition.

No move, deletion, archive, test, commit, or push is authorized by this policy alone. Step 16 execution must follow the issue's current coordination guard and its required verification evidence.