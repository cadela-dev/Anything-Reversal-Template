---
name: verification
description: Exact batch reconciliation and verifier boundaries.
---

# Verifier Rules

Verifier validates the batch contract. Verification must reconcile three sets exactly:

1. Source files listed in `assignments/BATCH_####.md`
2. Outcome lines listed in `worker_reports/BATCH_####_WORKER.md`
3. Mirror docs that exist under `docs/_file_docs/src/...`

A batch fails if any assigned file is missing a mirror doc, missing a worker outcome, has a wrong mirror path, or was skipped because it was binary/asset/unknown.

Verifier checks:

- mirror docs exist at the exact required paths
- mirror docs use the required headings
- worker report exists and lists every assigned source file
- copied source code is avoided
- deferred/error files include explicit reasons
- `PROJECT_FILE_INDEX.md` is updated: verified files become `[x]`, failed files become `[!]`

Only verifier can mark project-index rows `[x]`.

Verifier must not silently rewrite worker docs. If small mechanical repair is requested by the prompt, do it and re-run verification. Otherwise mark issues clearly and stop.
