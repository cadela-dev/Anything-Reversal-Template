# Planner Rules

Planner creates or updates `NEXT_ASSIGNMENT.md` and creates `assignments/BATCH_####.md`.

## Living tracker rule

`docs/_project_index/PROJECT_FILE_INDEX.md` is the planner source of truth and a living tracker.

- Only select `[ ]` items for normal batches.
- Never select `[~]`, `[x]`, `[D]`, or `[!]` unless the user explicitly starts a repair cycle.
- When assigning a batch, update selected rows from `[ ]` to `[~]`.
- Preserve existing `[x]`, `[!]`, `[D]`, notes, ordering, and formatting where possible.
- Do not regenerate the entire index during normal planning.

## Batch size

Use effective file size, not just physical line count.

- `> 2000` lines: 1 file only
- `1501-2000` lines: 1-2 files
- `901-1500` lines: 2-3 files
- `301-900` lines: 4-8 files
- `100-300` lines: 8-20 files
- `0-99` lines: 20-30 files

Stay under roughly 4,000 readable lines total. These are ceilings, not targets. Reduce the batch for dense, minified, generated, or architecturally risky files.

Effective size overrides line count.

If line count says small but byte size/token estimate says medium or large, use the larger category.

## Effective File Size Rule

Do not rely only on physical line count.

Some JavaScript, JSON, CSS, and HTML files may be minified or packed into one very long line. These files may show as 0-1 readable lines but still be large in tokens/context.

For every readable file, estimate effective size using:

- physical line count
- byte size
- character count if available
- whether the file appears minified/packed
- architectural importance

Use the largest effective size signal when choosing batch size.

## Minified / Packed File Rule

A file is probably minified or packed if:

- it has fewer than 20 physical lines, AND
- it is larger than 8KB, AND
- it is `.js`, `.json`, `.css`, `.html`, `.mjs`, `.cjs`, `.ts`, or similar text code/data

Never treat a minified/packed file as tiny just because it has 0-1 physical lines.

For minified/packed files:

- 1KB-5KB: small
- 5KB-15KB: medium
- 15KB-50KB: large
- 50KB+: very large

Batch limits for minified/packed files:

- mostly 1KB-5KB files: up to 20 files
- mostly 5KB-15KB files: 8-12 files
- mostly 15KB-50KB files: 2-5 files
- any file over 50KB: 1 file, or only with closely related tiny files

If a planned batch contains mixed minified files from 1KB-15KB, prefer 8-12 files, not 20-30.

Never write "0 readable lines" as the reason for assigning 20-30 minified JavaScript files.

## Assignment table

Every assignment must include exact source-to-mirror mapping:

| Status | Source File | Lines | Bytes | Type | Effective Size | Required Mirror Doc |
|---|---|---:|---:|---|---|---|

Mirror path format:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

## Index metadata rule

Use `PROJECT_FILE_INDEX.md` as the source of truth for available files and tracker status.

For batch sizing, use the Lines column plus any available Bytes, Type, and Notes data.

If the Lines column says `0`, `1`, or a very small number, do not assume the file is tiny. Check Bytes, Type, Notes, and path context.

If a `.js`, `.json`, `.css`, `.html`, `.mjs`, `.cjs`, or `.ts` file has very few lines but appears large by bytes or context, treat it as minified/packed and use the Minified / Packed File Rule.

If important metadata is missing, do not broadly rescan the whole project. Inspect only the candidate files needed for the next batch and update their metadata.
