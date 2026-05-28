# Anything Reversal Project Rules

This project documents one arbitrary source tree in `src/` into clean-room, rebuild-oriented reference docs. It is not tied to any specific product type, framework, language, or codebase.

## Permanent laws

1. Source files live under `src/`.
2. Documentation lives under `docs/`.
3. `docs/_project_index/PROJECT_FILE_INDEX.md` is the living tracker. Do not regenerate it after indexing unless preserving all statuses and notes.
4. Every assigned file must produce exactly one mirrored documentation file.
5. Clean-room docs only: describe behavior, responsibilities, inputs, outputs, dependencies, and rebuild guidance. Do not copy source code into docs.
6. Run exactly one batch per continue cycle, then stop.
7. Do not compact during a batch. Compact only between completed/verified batches.

## Mirror path invariant

For every assigned source file, compute the mirror path from the project-root relative path:

`src/path/to/file.ext` -> `docs/_file_docs/src/path/to/file.ext.md`

A batch is incomplete until every assigned file has one of these explicit outcomes:

- mirrored doc created and listed in the worker report
- `[D]` deferred with a reason
- `[!]` failed/needs repair with a reason

Silent omission is forbidden, including for images, fonts, configs, lock files, binaries, unknown assets, and empty files.

## Batch sizing rule

Choose batch size by the largest file in the proposed batch and by total readable line count. Stay under roughly 4,000 readable lines per batch.

- `> 2000` lines: 1 file only
- `1501-2000` lines: 1-2 files
- `901-1500` lines: 2-3 files
- `301-900` lines: 4-8 files
- `100-300` lines: 8-20 files
- `0-99` lines: 20-30 files

For mixed batches, the largest file wins. If files are dense, minified, generated, or architecturally risky, use the low end.

## Asset handling

Non-code files still get mirrored docs. Identify what they appear to be using extension, filename, directory, MIME/type clues, and safe metadata where available. If not confident, say so plainly:

`Type could not be determined confidently from available metadata.`

## Normal continue-cycle context

For a normal batch, do not reread the whole project history. Read only `CLAUDE.md`, `NEXT_ASSIGNMENT.md`, `status/WORKFLOW_STATUS.md`, `docs/_project_index/PROJECT_FILE_INDEX.md`, the current/latest assignment/report/verification needed to confirm previous PASS, and the source files assigned to this batch. Older reports are for repair cycles only.
