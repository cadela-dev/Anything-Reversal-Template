# Anything Reversal Project

A Claude Code clean-room documentation workflow for turning any source tree into behavior-focused mirror docs, batch reports, verification reports, and optional clean-room rebuild planning.

This project is meant to help you understand how a codebase works without copying the original implementation. You put a source tree into `src/`, run the Claude Code prompts in order, and the workflow creates structured documentation under `docs/`.

> **Important:** This template is for documentation, analysis, and clean-room rebuild planning. Do not use it to publish private source code, purchased source code, secrets, generated private mirror docs, or proprietary project files.

---

## What This Does

Anything Reversal helps Claude Code work through a source tree in controlled batches.

It will:

- inventory every file under `src/`
- create a project file index
- assign files into batches
- create one mirror doc for every source file
- preserve the original folder depth in the mirror docs
- document readable code, config files, assets, binaries, minified files, and unknown files
- create worker and verification reports for each batch
- update architecture/rebuild notes as behavior is discovered
- repair incomplete batches if a run stops halfway
- run a final verification pass to make sure nothing was missed
- optionally create a generic clean-room rebuild plan from the docs

The main idea is:

```text
src/path/file.ext
-> docs/_file_docs/src/path/file.ext.md
```

Every source file gets a matching documentation file.

---

## What This Does Not Do

This project does **not**:

- copy source code into the docs
- make a perfect decompiler
- guarantee legal permission to reverse anything
- automatically rebuild the project
- replace human review
- safely publish someone else’s private/proprietary source

Use it only on projects you have the right to inspect and document.

---

## Project Layout

```text
anything-reversal-template/
├── .claude/
│   ├── agents/
│   ├── rules/
│   └── skills/
├── assignments/
│   └── .gitkeep
├── docs/
│   ├── _file_docs/
│   │   └── .gitkeep
│   └── _project_index/
│       └── .gitkeep
├── prompts/
│   ├── 01_index_fresh_project.md
│   ├── 02_continue_cycle.md
│   ├── 03_repair_batch_consistency.md
│   ├── 04_final_verify_project.md
│   └── 05_create_rebuild_plan.md
├── scripts/
├── src/
│   └── .gitkeep
├── status/
│   └── .gitkeep
├── verification_reports/
│   └── .gitkeep
├── worker_reports/
│   └── .gitkeep
├── CLAUDE.md
├── README.md
└── START_HERE.md
```

---

## The Big Rule

Every source file assigned in a batch must have one mirror doc:

```text
src/path/file.ext -> docs/_file_docs/src/path/file.ext.md
```

That includes:

- source code
- config files
- lock files
- JSON/YAML/XML
- images
- fonts
- archives
- empty files
- unknown binaries
- minified or obfuscated files

Nested paths must be preserved. Do not flatten mirror docs.

Correct:

```text
src/commands/admin/ban.js
-> docs/_file_docs/src/commands/admin/ban.js.md
```

Wrong:

```text
src/commands/admin/ban.js
-> docs/_file_docs/src/ban.js.md
```

---

## Status Legend

`PROJECT_FILE_INDEX.md` is the living tracker.

```text
[ ] not assigned
[~] assigned/in progress
[x] mirrored documentation complete and verified
[D] deferred with explicit reason
[!] needs repair or review
```

Only verified files should be marked `[x]`.

---

## Prompt Files

The detailed workflow prompts live in `prompts/`.

| Prompt | Purpose |
|---|---|
| `prompts/01_index_fresh_project.md` | First setup/index pass |
| `prompts/02_continue_cycle.md` | Run one batch |
| `prompts/03_repair_batch_consistency.md` | Repair missing mirror docs/reports after a bad run |
| `prompts/04_final_verify_project.md` | Final pass to verify all source files, mirror docs, reports, and statuses |
| `prompts/05_create_rebuild_plan.md` | Optional generic clean-room rebuild planning prompt after final verification passes |

---

## Helper Scripts

```bash
# Optional bootstrap/index helper
python scripts/inventory_src.py --write --print-summary

# Batch/report consistency checks
python scripts/check_batch_consistency.py --latest

# Compact/resume helper summary
python scripts/compact_resume_summary.py
```

`PROJECT_FILE_INDEX.md` is a living tracker after indexing starts. Do not blindly regenerate it during batching unless the script preserves statuses and notes.

---

# Quick Start

1. Click **Use this template** or clone the repo.
2. Put the source tree you want documented into `src/`.
3. Open the project in VS Code with Claude Code.
4. Run the initial indexing prompt.
5. Compact if needed.
6. Run the continue prompt repeatedly, one batch at a time.
7. Use the repair prompt only if a batch breaks.
8. Run final verification when Claude says all files are done.
9. Optionally run the rebuild planning prompt after final verification passes.

---

# Copy/Paste Prompts for Claude Code

This project is designed so you do **not** need to paste huge instructions every time.

Use the short prompts below to tell Claude Code which workflow prompt to run.

---

## 0. Before You Start

Put the source code you want documented into:

```text
src/
```

Open this project folder in VS Code / Claude Code.

Run Claude Code from the project root.

The project root should contain:

```text
CLAUDE.md
START_HERE.md
README.md
prompts/
docs/
src/
assignments/
worker_reports/
verification_reports/
status/
.claude/
```

---

## 1. Initial Project Index Prompt

Use this once at the beginning of a fresh source tree.

Paste this into Claude Code:

```text
Read `prompts/01_index_fresh_project.md` and execute it exactly.

This is a fresh Anything Reversal project.

Use `src/` as the only source tree.

Index every file under `src/`.

Do not document source files yet.

Create or update:
- `docs/_project_index/PROJECT_FILE_INDEX.md`
- `docs/_project_index/PROJECT_STRUCTURE.md`
- `status/INDEX_STATUS.md`
- `NEXT_ASSIGNMENT.md`
- the first real assignment file, usually `assignments/BATCH_0001.md`

Follow `.claude/rules/planner_rules.md` for batch sizing, including effective-size rules for minified, packed, binary, asset, or unusually dense files.

The first assignment handoff is not complete unless both `NEXT_ASSIGNMENT.md` and the matching `assignments/BATCH_####.md` file exist.
```

After it finishes, check that these exist:

```text
docs/_project_index/PROJECT_FILE_INDEX.md
docs/_project_index/PROJECT_STRUCTURE.md
NEXT_ASSIGNMENT.md
assignments/BATCH_0001.md
```

Then compact if needed.

---

## 2. Continue Batch Prompt

Use this repeatedly until all files are documented.

Paste this into Claude Code:

```text
Read `prompts/02_continue_cycle.md` and execute exactly one batch.

Process the batch pointed to by `NEXT_ASSIGNMENT.md`.

Do not process more than one batch.

Do not reload the whole project history.

Create every required mirror doc at the exact path:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

Every assigned source file must have one of:
- a completed mirror doc
- an explicit deferred reason
- an explicit error/repair reason

After verification passes, do not stop until the next handoff is complete:
- `NEXT_ASSIGNMENT.md` points to the next batch
- the real next `assignments/BATCH_####.md` file exists
- `PROJECT_FILE_INDEX.md` has current batch files marked `[x]`
- `PROJECT_FILE_INDEX.md` has next batch files marked `[~]`

Stop after one batch.
```

After it finishes, check:

```text
worker_reports/BATCH_####_WORKER.md
verification_reports/BATCH_####_VERIFICATION.md
docs/_file_docs/src/
NEXT_ASSIGNMENT.md
assignments/BATCH_####.md
```

Then compact if needed and run the same continue prompt again.

---

## 3. Normal Repeat Loop

The normal workflow is:

```text
1. Run initial project index prompt once.
2. Compact if needed.
3. Run continue batch prompt.
4. Compact if needed.
5. Repeat continue batch prompt until no `[ ]` or `[~]` files remain.
6. Run final verification prompt.
```

---

## 4. Repair Prompt

Use this only if a batch crashes, compacts mid-batch, stops halfway, misses mirror docs, or leaves reports inconsistent.

Paste this into Claude Code:

```text
Read `prompts/03_repair_batch_consistency.md` and execute it exactly.

Repair the latest incomplete or inconsistent batch.

Do not start a new batch.

Reconcile:
- the latest `assignments/BATCH_####.md`
- the matching `worker_reports/BATCH_####_WORKER.md`
- the matching `verification_reports/BATCH_####_VERIFICATION.md`
- the required mirror docs under `docs/_file_docs/src/`
- `docs/_project_index/PROJECT_FILE_INDEX.md`
- `NEXT_ASSIGNMENT.md`

Every assigned source file must have exactly one outcome:
- mirror doc created and verified
- deferred with explicit reason
- failed with explicit repair reason

If a mirror doc is missing, create or repair it at the exact required path:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

After repair, update statuses:
- verified files: `[x]`
- still broken files: `[!]`
- deferred files: `[D]`

Stop after the repair. Do not start the next batch.
```

After repair, either rerun the continue prompt or rerun final verification if you were already done.

---

## 5. Final Verification Prompt

Use this after Claude claims all batches are done.

Paste this into Claude Code:

```text
Read `prompts/04_final_verify_project.md` and execute it exactly.

This is the final completion verification.

Do not trust previous batch summaries.

Mechanically verify:
- every real file under `src/` is listed in `PROJECT_FILE_INDEX.md`
- every real file under `src/` has exactly one mirror doc
- every mirror doc is at the exact depth-preserved path:
  `docs/_file_docs/src/path/file.ext.md`
- no source files remain `[ ]`
- no source files remain `[~]`
- any `[D]` or `[!]` files have explicit reasons
- every batch has an assignment file, worker report, and verification report
- architecture synthesis files are populated
- minified/packed/obfuscated files are acknowledged as such in their mirror docs

Create or overwrite:

`verification_reports/FINAL_PROJECT_VERIFICATION.md`

If everything passes:
- update `NEXT_ASSIGNMENT.md` to say `ALL FILES DOCUMENTED AND VERIFIED`
- update `status/WORKFLOW_STATUS.md`
- update `status/INDEX_STATUS.md`

If anything fails:
- create `assignments/FINAL_REPAIR.md`
- list exact repair tasks
- update `NEXT_ASSIGNMENT.md` to point to `assignments/FINAL_REPAIR.md`
- do not perform the repairs unless explicitly asked

Stop after final verification.
```

Expected pass result:

```text
verification_reports/FINAL_PROJECT_VERIFICATION.md
Status: PASS
```

If it fails, run the repair prompt or ask Claude to execute `assignments/FINAL_REPAIR.md`.

---

## 6. Final Repair Prompt

Use this only if final verification creates `assignments/FINAL_REPAIR.md`.

Paste this into Claude Code:

```text
Read `assignments/FINAL_REPAIR.md` and execute the repair exactly.

This is a final repair pass, not a normal batch.

Do not process unrelated files.

For each repair item:
- create missing mirror docs
- fix wrong mirror paths
- update incorrect project index statuses
- repair missing report references
- update architecture synthesis docs only if the repaired file adds new verified behavior

After repairs, create:

`verification_reports/FINAL_REPAIR_VERIFICATION.md`

Verify:
- all listed repair items were completed
- all repaired mirror docs exist at exact paths
- `PROJECT_FILE_INDEX.md` has correct statuses
- `NEXT_ASSIGNMENT.md` no longer points to unresolved repair work if all repairs passed

If repair succeeds, update:

`NEXT_ASSIGNMENT.md`

to say:

`ALL FILES DOCUMENTED AND VERIFIED`

Then stop.
```

After final repair, rerun the final verification prompt.

---

## 7. Optional Rebuild Planning Prompt

Use this only after final verification passes.

Paste this into Claude Code:

```text
Read `prompts/05_create_rebuild_plan.md` and execute it exactly.

Final verification has passed.

Do not read `src/`.

Create a generic clean-room rebuild plan using only:
- `docs/_project_index/`
- `docs/_file_docs/`
- `verification_reports/FINAL_PROJECT_VERIFICATION.md`

Do not write implementation code yet.

Stop after creating `clean_rebuild_plan/`.
```

---

## Recommended Claude Code Rhythm

Use this rhythm:

```text
Initial prompt
Compact
Continue prompt
Compact
Continue prompt
Compact
Continue prompt
Compact
Repair prompt only if needed
Final verification prompt
Final repair if needed
Final verification again
```

Do not let Claude start a new batch until the current batch has:

```text
assignment file
mirror docs
worker report
verification report
PROJECT_FILE_INDEX.md updates
NEXT_ASSIGNMENT.md handoff
```

---

## Minified, Packed, and Obfuscated Files

Do not trust line count alone.

Some files may show `0` or `1` line but still be large because they are minified, packed, or obfuscated.

For these files, Claude should use:

- byte size
- file extension
- file path
- import/require clues
- visible strings
- exports/module shape
- config references
- model references
- side effects
- uncertainty notes

Mirror docs for these files should clearly say when behavior is inferred.

---

## What Not To Do

Do not tell Claude to:

```text
Document everything in one pass.
Read the whole project history every batch.
Skip assets.
Skip binaries.
Flatten mirror docs.
Trust line count for minified files.
Start a new batch before the previous batch is verified.
Declare completion without final verification.
```

Use the prompt files and this guide instead.

---

## Contributing

Contributions are welcome.

Good contribution types:

- clearer prompts
- safer clean-room rules
- better batching logic
- stronger final verification
- better repair handling
- improved helper scripts
- better README/docs

Please do not submit private source code, purchased source code, generated mirror docs from private projects, secrets, tokens, or credentials.

---

## License

MIT
