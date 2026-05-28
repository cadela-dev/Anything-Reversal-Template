#!/usr/bin/env python3
"""Print a compact-safe resume reminder for Claude Code."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def latest(folder, pat):
    xs=sorted((ROOT/folder).glob(pat))
    xs=[p for p in xs if 'TEMPLATE' not in p.name]
    return xs[-1].relative_to(ROOT).as_posix() if xs else 'none'

print('Anything Reversal resume context:')
print('- Re-read CLAUDE.md before continuing.')
print('- Do not start a new batch unless previous verification is PASS.')
print(f'- Latest assignment: {latest("assignments", "BATCH_*.md")}')
print(f'- Latest worker report: {latest("worker_reports", "BATCH_*_WORKER.md")}')
print(f'- Latest verification report: {latest("verification_reports", "BATCH_*_VERIFICATION.md")}')
print('- Required invariant: every assigned src file has docs/_file_docs/<same-relative-path>.md')
