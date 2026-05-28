# Start Here: Anything Reversal

This folder is a ready-to-use clean-room documentation workflow for any source code project.

## How to use

1. Put the target project files inside `src/`.
2. In Claude Code / VS Code, run the initial indexing prompt:
   - Paste `prompts/01_index_fresh_project.md`, or
   - Use the project skill `.claude/skills/index-anything-reversal/SKILL.md` if your Claude Code setup exposes skills.
3. After indexing finishes, compact if you want.
4. Run the continue prompt:
   - Paste `prompts/02_continue_cycle.md`, or
   - Use `.claude/skills/continue-anything-reversal/SKILL.md`.
5. Compact between batches as needed.
6. If anything gets weird, run `prompts/03_repair_batch_consistency.md`.

## Main fix in this version

Every batch must include a table mapping each assigned source file to the exact mirrored doc path. The worker must create all mirror docs first as stubs, then fill them in. The verifier must reject the batch if any mirror doc is missing.

## Optional helper scripts

Run these from the project root:

```bash
python scripts/inventory_src.py --write --print-summary
python scripts/check_batch_consistency.py --latest
python scripts/compact_resume_summary.py
```
Use the inventory script only before the first indexing pass, or later only if you understand that PROJECT_FILE_INDEX.md is a living tracker. The script preserves statuses by default, but Claude should normally manage batch status updates.

The scripts help keep the workflow deterministic so Claude does not forget mirrored docs during a long batch.
