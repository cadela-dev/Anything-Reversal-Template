# Anything Reversal Project

A clean-room documentation workflow for reversing any source tree into safe rebuild notes without copying source code.

Main source folder: `src/`  
Mirrored docs folder: `docs/_file_docs/`

## The big rule

Every source file assigned in a batch must have one mirror doc:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

That includes fonts, images, config files, lock files, empty files, and unknown binaries.

## Prompts

- `prompts/01_index_fresh_project.md` — first setup/index pass
- `prompts/continue_cycle.md` — run one batch
- `prompts/repair_batch_consistency.md` — repair missing mirrored docs/reports
- `prompts/04_final_verify_project.md` — final pass to verify all source files, mirror docs, reports, and statuses
- `prompts/05_create_rebuild_plan.md` — optional generic clean-room rebuild planning prompt after final verification passes

## Helper scripts

```bash
# Optional bootstrap/index helper
python scripts/inventory_src.py --write --print-summary

# Batch/report consistency checks
python scripts/check_batch_consistency.py --latest

# Compact/resume helper summary
python scripts/compact_resume_summary.py
```

## HOW TO USE THE PROMPTS AND RUN THE REVERSAL PROJECT
- `HOW_TO_USE_THIS_AND_PROMPT.md` - copy/paste prompts for running the workflow in Claude Code