Read and follow this prompt exactly.

You are performing the FINAL COMPLETION VERIFICATION for the Project Atlas clean-room documentation project.

Do not trust previous batch summaries.
Do not assume the project is complete because a previous message said all files are done.
Your job is to mechanically prove whether every file under `src/` has been accounted for.

Prioritize mechanical coverage verification.
Do not reread every full source file unless needed to resolve a mismatch.
Do not rewrite or repair source documentation in this run unless a tiny metadata/report correction is required.

If meaningful repairs are needed, create `assignments/FINAL_REPAIR.md` and stop.

# Read first

Read only these project-control files first:

- `CLAUDE.md`
- `.claude/rules/status_legend.md`
- `.claude/rules/planner_rules.md`
- `.claude/rules/worker_rules.md`
- `.claude/rules/verifier_rules.md`
- `docs/_project_index/PROJECT_FILE_INDEX.md`
- `NEXT_ASSIGNMENT.md`
- `status/WORKFLOW_STATUS.md`
- `status/INDEX_STATUS.md`

If they exist, also inspect these repair-control files:

- `assignments/FINAL_REPAIR.md`
- `verification_reports/FINAL_REPAIR_VERIFICATION.md`

Then inspect only the filesystem paths needed for verification:

- `src/`
- `docs/_file_docs/`
- `assignments/`
- `worker_reports/`
- `verification_reports/`
- `docs/_project_index/`

# Required checks

## 1. Source file inventory check

List every real file currently under:

`src/`

Ignore directories. Ignore `.gitkeep` only if it is intentionally just a placeholder.

Every source file must have exactly one expected mirror doc at:

`docs/_file_docs/<source path>.md`

Example:

`src/commands/Fun/level.js`
must map to:

`docs/_file_docs/src/commands/Fun/level.js.md`

The full folder path must be preserved.

Flattened mirror docs do not count.

Example invalid flattened mirror:

`src/commands/Fun/level.js`
documented as:

`docs/_file_docs/src/level.js.md`

That is invalid because the folder depth was not preserved.

## 2. Mirror doc existence and path check

For every source file, verify the exact mirror doc exists.

Report:

- source files with missing mirror docs
- source files whose mirror doc exists only in a wrong or flattened location
- mirror docs that do not map to any real source file
- duplicate mirror docs for one source file

Do not mark PASS if any exact mirror doc is missing.

## 3. Project index status check

Read:

`docs/_project_index/PROJECT_FILE_INDEX.md`

Verify:

- every real `src/` file is listed exactly once
- every listed source file actually exists
- every completed source file is marked `[x]`
- no source files remain `[ ]`
- no source files remain `[~]`
- any `[D]` file has an explicit deferred reason
- any `[!]` file has an explicit repair/review reason

If the project index disagrees with the filesystem, report the mismatch.

Do not regenerate the project index.
Do not reorder the project index.
This is an audit only.

## 4. Batch assignment/report coverage check

Inspect all non-template batch files in:

- `assignments/`
- `worker_reports/`
- `verification_reports/`

Ignore:

- `.gitkeep`
- `BATCH_0000_TEMPLATE.md`
- any template files

For each numbered batch found:

- `assignments/BATCH_####.md` must exist
- `worker_reports/BATCH_####_WORKER.md` must exist
- `verification_reports/BATCH_####_VERIFICATION.md` must exist

For each batch:

- every source file assigned in the assignment file must appear in the worker report
- every assigned source file must appear in the verification report or verification reconciliation table
- every assigned source file must have the exact mirror doc path
- verification report must say PASS, or clearly document failure

`FINAL_REPAIR.md` and `FINAL_REPAIR_VERIFICATION.md` are allowed repair artifacts. Do not require them to follow the numbered `BATCH_####` naming pattern, but do verify that every repair item listed in `FINAL_REPAIR.md` has been completed.

Report:

- missing worker reports
- missing verification reports
- assigned files missing from worker reports
- assigned files missing from verification reports
- batch files that claim PASS while missing mirror docs
- incomplete final repair items

## 5. Architecture synthesis check

Verify these files exist:

- `docs/_project_index/ARCHITECTURE_MAP.md`
- `docs/_project_index/CORE_SYSTEM_FILES.md`
- `docs/_project_index/DEPENDENCY_NOTES.md`
- `docs/_project_index/FOLLOW_UP_QUEUE.md`
- `docs/_project_index/SYSTEM_BEHAVIOR_NOTES.md`
- `docs/_project_index/REBUILD_CONCEPTS.md`
- `docs/_project_index/PROJECT_STRUCTURE.md`

A file fails this check if it only says:

`Not populated yet. Update as batches are verified.`

or otherwise contains only placeholder text.

Each file must either contain meaningful accumulated project notes or explicitly explain why no facts are known yet.

Do not deeply rewrite these files during this audit.
If any are missing or placeholder-only, report them in failures.

## 6. Minified / obfuscated file documentation check

For any `.js`, `.mjs`, `.cjs`, `.ts`, `.json`, `.css`, or `.html` source file that appears minified, packed, or obfuscated based on index notes, file size, path, or mirror doc content:

Verify the mirror doc includes some clear acknowledgement of that status, such as:

- minified
- packed
- obfuscated
- one-line JavaScript
- generated identifiers
- confidence
- unknowns
- inference

The mirror doc should not pretend full certainty if behavior was inferred.

This check may be a heading/keyword/section audit. Do not re-deobfuscate every file in this run unless needed to resolve a specific failure.

Report minified/obfuscated source files whose mirror docs do not acknowledge uncertainty or effective-size/minified status.

## 7. Status/handoff check

Check:

- `NEXT_ASSIGNMENT.md`
- `status/WORKFLOW_STATUS.md`
- `status/INDEX_STATUS.md`

If everything passes, these should indicate that all source files are documented and verified.

If anything fails, `NEXT_ASSIGNMENT.md` should not claim completion unless it also points to required repair work.

# Required output file

Create or overwrite:

`verification_reports/FINAL_PROJECT_VERIFICATION.md`

Use exactly this structure:

```md
# Final Project Verification

Status: PASS / FAIL

## Summary

- Total source files:
- Total expected mirror docs:
- Total exact mirror docs found:
- Missing mirror docs:
- Wrong-location mirror docs:
- Extra mirror docs:
- Duplicate mirror docs:
- Project index unresolved statuses:
- Batch report issues:
- Final repair issues, if any:
- Architecture synthesis issues:
- Minified/obfuscated doc issues:

## Source-to-Mirror Reconciliation

| Result | Source File | Expected Mirror Doc | Notes |
|---|---|---|---|

## Project Index Status Audit

| Result | Source File | Index Status | Notes |
|---|---|---|---|

## Batch Report Audit

| Result | Batch | Assignment | Worker Report | Verification Report | Notes |
|---|---|---|---|---|---|

## Final Repair Audit

| Result | Repair Item | File / Path | Notes |
|---|---|---|---|

## Architecture Synthesis Audit

| Result | File | Notes |
|---|---|---|

## Minified / Obfuscated File Audit

| Result | Source File | Mirror Doc | Notes |
|---|---|---|---|

## Failures To Repair

List every required repair item.

If no failures exist, write:

`No repair items found.`

## Final Decision

Write one of:

`PASS: All source files are documented, mirrored at exact paths, indexed, batch-reconciled, final repair items are complete, and the project is ready for clean-room rebuild planning.`

or:

`FAIL: Repairs are required before clean-room rebuild planning.`