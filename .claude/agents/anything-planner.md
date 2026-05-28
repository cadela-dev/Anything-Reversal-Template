---
name: anything-planner
description: Create the next safe assignment batch from unprocessed index entries.
---

# anything-planner

# Planner Rules

Planner creates `NEXT_ASSIGNMENT.md` and `assignments/BATCH_####.md`.

Only select `[ ]` items. Never select `[~]`, `[x]`, `[D]`, or `[!]`.
Use strict top-to-bottom order unless a documented human override exists.

## Batch Size

Use the thresholds in `CLAUDE.md` and `.claude/rules/planner_rules.md`:

- `> 2000` lines: 1 file only
- `1501-2000` lines: 1-2 files
- `901-1500` lines: 2-3 files
- `301-900` lines: 4-8 files
- `100-300` lines: 8-20 files
- `0-99` lines: 20-30 files

Stay under roughly 4,000 readable lines total. Human overrides must be documented in `NEXT_ASSIGNMENT.md` and the batch file.

## Index Metadata Rule

Planner must use the Lines, Bytes, Type, and Notes columns in PROJECT_FILE_INDEX.md for batch sizing.

Planner must not rescan the whole source tree for line counts during normal planning.

If the next eligible file is missing Lines/Size metadata, stop and request index repair instead of guessing or scanning broadly.