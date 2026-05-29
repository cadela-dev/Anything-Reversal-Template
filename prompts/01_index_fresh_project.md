# Initial Prompt: Index Fresh Project Atlas Project

You are starting an Project Atlas clean-room documentation project.

## Read first

Read:

- `CLAUDE.md`
- `.claude/rules/indexing_scope.md`
- `.claude/rules/status_legend.md`
- `.claude/rules/planner_rules.md`
- `START_HERE.md`

## Goal

Inspect `src/` and create/update `docs/_project_index/PROJECT_FILE_INDEX.md` with every file found under `src/`.

Do not document source files yet. This step is only inventory and planning prep.

## Required index columns

Use this table format:

| Status | Path | Lines | Bytes | Type | Notes |
|---|---|---:|---:|---|---|

Statuses:

- `[ ]` not assigned
- `[~]` assigned/in progress
- `[x]` mirrored documentation complete and verified
- `[D]` deferred with explicit reason
- `[!]` needs review/repair

## Type labeling

Classify files as best as possible:

- code
- config
- data
- doc
- image asset
- font asset
- audio/video asset
- archive/binary asset
- unknown binary asset
- empty file

For binary assets, use extension, path, filename, and MIME/type clues if available. If not confident, say so in Notes.

## Required output updates

After indexing:

1. Update `docs/_project_index/PROJECT_FILE_INDEX.md`.
2. Update `docs/_project_index/PROJECT_STRUCTURE.md` with the directory tree overview.
3. Update `status/INDEX_STATUS.md`.
4. Update `NEXT_ASSIGNMENT.md` with the first recommended batch, including exact source -> mirror doc mapping.

When creating starter project-index files such as:

- `ARCHITECTURE_MAP.md`
- `CORE_SYSTEM_FILES.md`
- `DEPENDENCY_NOTES.md`
- `FOLLOW_UP_QUEUE.md`
- `SYSTEM_BEHAVIOR_NOTES.md`
- `REBUILD_CONCEPTS.md`

use placeholder text only before the first batch is processed.

After BATCH_0001 is verified, the continue prompt must replace placeholder text with real notes or an explicit reason why no facts are known yet.

## First batch sizing

Use the batch thresholds and effective-size rules in `.claude/rules/planner_rules.md`.

Choose conservatively to avoid compaction during the batch.

The first assignment must use mirror paths in this form:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

## Important

Do not skip assets. Every file under `src/` must eventually get exactly one mirror doc.


## Do not use destructive inventory rewrites

Do not run `scripts/inventory_src.py --write` after manual edits unless preserving status and notes. The project index is a living tracker once created.
