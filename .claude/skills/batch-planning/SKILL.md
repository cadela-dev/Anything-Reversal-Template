---
name: batch-planning
description: Batch sizing, ordering, living tracker checkout, and human override handling.
---

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

Use the largest readable file in the proposed batch as the ceiling, then check total readable lines.

- `> 2000` lines: 1 file only
- `1501-2000` lines: 1-2 files
- `901-1500` lines: 2-3 files
- `301-900` lines: 4-8 files
- `100-300` lines: 8-20 files
- `0-99` lines: 20-30 files

Stay under roughly 4,000 readable lines total. These are ceilings, not targets. Reduce the batch for dense, minified, generated, or architecturally risky files.

## Assignment table

Every assignment must include exact source-to-mirror mapping:

| Status | Source File | Lines | Type | Required Mirror Doc |
|---|---|---:|---|---|

Mirror path format:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

## Index metadata rule

Use the Lines column in `PROJECT_FILE_INDEX.md` for batch sizing. If a file is missing line metadata, stop and request index repair instead of guessing or broadly rescanning the project.
