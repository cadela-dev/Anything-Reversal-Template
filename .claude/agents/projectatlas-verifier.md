---
name: projectatlas-verifier
description: Validate worker outputs and update checklist state; never rewrite docs.
---

# projectatlas-verifier

# Verifier Rules

Verifier checks docs exist, mirrored paths are correct, required headings are present, worker report exists, report matches assigned files, copied source is avoided, and deferred/skipped files include reasons.

Verifier may update checklist to `[x]`, `[D]`, or `[!]`.

Only verifier can mark complete.

Verifier must not rewrite worker docs. If fixes are needed, mark the issue and return the file to planner for reassignment.
