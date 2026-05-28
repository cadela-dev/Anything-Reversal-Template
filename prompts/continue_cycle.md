# Continue Prompt: Run One Anything Reversal Batch

Run exactly one batch, then stop with a concise status summary.

## Lean context rule

Do not reload the whole project history.

Read only:

- `CLAUDE.md`
- `NEXT_ASSIGNMENT.md`
- `status/WORKFLOW_STATUS.md`
- `docs/_project_index/PROJECT_FILE_INDEX.md`
- the latest non-template assignment/report/verification only if needed to confirm the previous batch passed
- the source files assigned to this batch

Do not read all previous assignments, all worker reports, all verification reports, or all architecture files during a normal continue cycle. Older reports are for repair cycles only.

If the previous batch is missing a required worker report, verification report, or mirror docs, do not start a new batch. Use `prompts/repair_batch_consistency.md` instead.

## Minified JavaScript / Packed File Warning

Before selecting, repairing, or processing a batch, check whether any `.js`, `.json`, `.css`, `.html`, `.mjs`, `.cjs`, or `.ts` files are minified/packed.

Do not treat a file as tiny just because it has `0`, `1`, or very few physical lines.

A file is probably minified/packed if:

- it has fewer than 20 physical lines, AND
- it is larger than 8KB, AND
- it is JavaScript, JSON, CSS, HTML, TypeScript, or similar text code/data.

For one-line/minified JavaScript command files:

- 1KB-5KB: small
- 5KB-15KB: medium
- 15KB-50KB: large
- 50KB+: very large

Batch limits for minified/packed files:

- mostly 1KB-5KB files: up to 20 files
- mostly 5KB-15KB files: 8-12 files
- mostly 15KB-50KB files: 2-5 files
- any file over 50KB: 1 file, or only with closely related tiny files

If most files are 5KB-15KB minified JS, use 8-12 files per batch.

Never assign 20-30 minified JavaScript files just because line count is `0`.

## Step 1: Resolve or create the current batch

`NEXT_ASSIGNMENT.md` is the handoff pointer, but it is not a replacement for an assignment file.

At the start of a continue cycle:

1. Read `NEXT_ASSIGNMENT.md`.

2. If `NEXT_ASSIGNMENT.md` points to or describes a batch such as `BATCH_0002`, check whether the matching assignment file exists:

   `assignments/BATCH_0002.md`

3. If that assignment file exists, process that exact batch.

4. If `NEXT_ASSIGNMENT.md` describes a batch but the matching assignment file does not exist, repair the handoff before processing:
   - create `assignments/BATCH_####.md` from the assignment table/details in `NEXT_ASSIGNMENT.md`
   - verify those files are marked `[~]` in `PROJECT_FILE_INDEX.md`
   - if they are still `[ ]`, change them to `[~]`
   - then process that batch

5. Only if `NEXT_ASSIGNMENT.md` does not contain a usable next batch, create a new `assignments/BATCH_####.md` from the next `[ ]` rows in `PROJECT_FILE_INDEX.md`.

When creating or repairing an assignment, preserve `[x]`, `[D]`, `[!]`, notes, order, and formatting in `PROJECT_FILE_INDEX.md`. Do not regenerate the whole index.

The assignment must include this table:

| Status | Source File | Lines | Bytes | Type | Effective Size | Required Mirror Doc |
|---|---|---:|---:|---|---|---|

Required mirror path format:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

Use the batch sizing thresholds from `.claude/rules/planner_rules.md`.

Do not rely only on line count. For minified/generated/dense files, use byte size and effective size.

## Step 2: Mirror docs first

Before detailed documentation, create every required mirrored doc path from the assignment table.

Each mirror doc must start with this metadata:

```markdown
# `<source path>`

Source file: `<source path>`
Mirror doc: `<mirror path>`
Project: `anything_reversal`
Batch: `BATCH_####`
Type: `<code/config/doc/image asset/font asset/unknown binary asset/etc>`
Status: draft / complete / needs review
```

For images, fonts, archives, and unknown binaries, do not pretend to read internals. Describe extension, likely purpose, path context, size, naming clues, references, and confidence. Use explicit fallback wording when uncertain.

## Step 3: Fill mirror docs

Document every assigned file. Do not copy source code except tiny identifiers or very short phrases. Focus on clean-room behavior, responsibilities, relationships, and rebuild guidance.

## Step 4: Worker report

Create `worker_reports/BATCH_####_WORKER.md`.

The worker report must list every assigned source file and its exact outcome:

| Outcome | Source File | Mirror Doc | Notes |
|---|---|---|---|

Every assigned file must appear once. No silent omissions.

## Step 5: Verification gate

Create `verification_reports/BATCH_####_VERIFICATION.md`.

Verify exact reconciliation between:

1. assignment source files
2. worker report outcome lines
3. mirror docs on disk

If any mirror doc is missing, immediately create/repair it and rerun the verification table before proceeding.

When verification passes, update `PROJECT_FILE_INDEX.md` rows for verified files from `[~]` to `[x]`. If any file failed, update it to `[!]` with notes.

## Step 6: Required architecture synthesis

Only after verification passes, update project notes in `docs/_project_index/`.

Do not leave architecture files in the default "Not populated yet" state if the verified batch contains any information relevant to them.

You must update these files every verified batch:

- `ARCHITECTURE_MAP.md`
- `CORE_SYSTEM_FILES.md`
- `DEPENDENCY_NOTES.md`
- `FOLLOW_UP_QUEUE.md`
- `SYSTEM_BEHAVIOR_NOTES.md`
- `REBUILD_CONCEPTS.md`

Update rules:

1. `ARCHITECTURE_MAP.md`
   - Add or update the known project structure.
   - Add discovered subsystems, entry points, data layers, command folders, config systems, or asset areas.
   - If this batch proves only a small part, add a "Known So Far" section.

2. `CORE_SYSTEM_FILES.md`
   - List important files verified in this batch.
   - Explain why they appear core.

3. `DEPENDENCY_NOTES.md`
   - Record imports, requires, packages, config references, schemas, or external services discovered in this batch.

4. `FOLLOW_UP_QUEUE.md`
   - Add unresolved questions, suspicious patterns, missing context, unknown behavior, or files that need later review.

5. `SYSTEM_BEHAVIOR_NOTES.md`
   - Record behavior proven or strongly suggested by this batch.
   - Examples: startup flow, command loading, database model usage, config loading, event handling, permission checks, cooldowns, logging, API calls.
   - If behavior is inferred but not proven, label it as `Inference`.

6. `REBUILD_CONCEPTS.md`
   - Add clean-room rebuild notes based on this batch.
   - Focus on what a future clean implementation would need to recreate behaviorally, without copying source code.
   - Include modules/classes/services that would likely exist in a rebuild.

Keep updates concise. Do not rewrite the whole files every time. Append or update sections as needed.

A batch is not fully complete until these project index files have been reviewed and updated or explicitly marked with a reason such as:

`No new behavior discovered in this batch. Existing notes remain current.`

Do not leave the placeholder text `Not populated yet. Update as batches are verified.` in any required architecture synthesis file after BATCH_0001 has verified.

## Step 7: Prepare next handoff

After the current batch is verified and architecture notes are updated, prepare the next handoff before stopping.

A valid handoff requires BOTH:

1. `NEXT_ASSIGNMENT.md` points to the next batch.
2. `assignments/BATCH_####.md` exists for that exact next batch.

Required actions:

1. Update `PROJECT_FILE_INDEX.md` for the current batch:
   - verified complete files become `[x]`
   - failed/incomplete files become `[!]`
   - deferred files become `[D]`

2. Select the next batch from remaining `[ ]` files using `.claude/rules/planner_rules.md`.

3. Use effective file size, not just line count:
   - if files are minified/packed, use byte size and the Minified JavaScript / Packed File Warning rules
   - do not assign 20-30 minified JS files just because their line count is `0`

4. Mark the selected next-batch files as `[~]` in `PROJECT_FILE_INDEX.md`.

5. Create the real next assignment file:

   `assignments/BATCH_####.md`

6. The next assignment file must contain:
   - batch number
   - source file list
   - line count
   - byte size if known
   - type
   - effective size classification
   - exact required mirror doc path for every file
   - worker report path
   - verification report path

7. Update `NEXT_ASSIGNMENT.md` to point to the same batch file and summarize the next batch.

8. Update:
   - `status/WORKFLOW_STATUS.md`
   - `status/INDEX_STATUS.md`

If no `[ ]` files remain, do not create an empty batch. Update `NEXT_ASSIGNMENT.md` to say `ALL FILES ASSIGNED`, and list any remaining `[!]` or `[D]` files.

Stop after one batch. Do not begin the next batch. Do not compact until after this batch is verified and the handoff files are updated.

A handoff is incomplete if `NEXT_ASSIGNMENT.md` describes the next batch but `assignments/BATCH_####.md` does not exist.