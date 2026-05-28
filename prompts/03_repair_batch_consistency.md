# Repair Prompt: Batch Consistency and Mirror Recovery

Use this when a batch is incomplete, inconsistent, or after compaction if you are not sure whether the last batch finished correctly.

## Read first

Read:

- `CLAUDE.md`
- `NEXT_ASSIGNMENT.md`
- `docs/_project_index/PROJECT_FILE_INDEX.md`
- latest `assignments/BATCH_####.md`
- matching `worker_reports/BATCH_####_WORKER.md` if present
- matching `verification_reports/BATCH_####_VERIFICATION.md` if present

## Repair target

Repair the latest incomplete batch. Do not create a new batch unless the latest batch is verified PASS.

## Required checks

For every row in the assignment source -> mirror map:

1. Confirm source file exists or mark it missing.
2. Confirm required mirror doc exists.
3. If missing, create the mirror doc immediately.
4. If the file is binary/asset/unknown, create an asset mirror doc with best-effort identification and explicit uncertainty.
5. Confirm worker report exists and includes every assigned file.
6. Confirm verification report exists and has a PASS/FAIL table.

## Output

Create or update `verification_reports/BATCH_####_VERIFICATION.md`.

Update `status/WORKFLOW_STATUS.md` and `NEXT_ASSIGNMENT.md` to say whether it is safe to continue.

Do not skip mirrored docs. Missing mirrored docs are the main repair target.


## Mirror repair priority

For the latest batch, compare assignment rows, worker report outcome rows, and mirror docs on disk. Create any missing mirror docs before doing architecture updates. Preserve `PROJECT_FILE_INDEX.md` as a living tracker: `[~]` for active repair, `[x]` only after verification, `[!]` for unresolved failures.
