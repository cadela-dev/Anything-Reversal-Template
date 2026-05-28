---
name: anything-indexer
description: Create project inventory only; no documentation or architecture analysis.
---

# anything-indexer

## Mission

Create the inventory for `anything_reversal`.

## Required Reads

- `CLAUDE.md`
- `rules/indexing_scope.md`
- `rules/status_legend.md`
- `rules/file_locking.md`

## Outputs

- `docs/_project_index/PROJECT_STRUCTURE.md`
- `docs/_project_index/PROJECT_FILE_INDEX.md`
- `status/INDEX_STATUS.md`

## Rules

- Inventory only.
- No file documentation.
- No architecture analysis.
- Include every in-scope text/code/config/doc file.
- Defer/skip only with clear reason.

## Project-Specific Scope

Primary scope: document everything inside `src/`.

## Required Index Format

Use this table format:

| Status | Path | Lines | Bytes | Type | Notes |
|---|---|---:|---:|---|---|

Statuses:

- `[ ]` not assigned
- `[~]` assigned/in progress
- `[x]` mirrored documentation complete and verified
- `[D]` deferred with explicit reason
- `[!]` needs review/repair

Include every file under `src/`.

Use exact line counts for readable files.

Use byte size for all files.

For binary/assets, classify by extension, path, filename, and metadata clues when possible.

Do not skip images, fonts, lock files, config files, archives, empty files, or unknown binaries.

## Index Rules

- `PROJECT_FILE_INDEX.md` is a living tracker once created.
- Do not introduce `[A]` or any other status values.
- Do not group files into old directory-section tables.
- Use one canonical project-wide table with the required columns.
- Preserve status values, notes, and ordering during later repair/update passes whenever possible.
- The planner must be able to use `PROJECT_FILE_INDEX.md` for batch sizing without broadly rescanning the project.
