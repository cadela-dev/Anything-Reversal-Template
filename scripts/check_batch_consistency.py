#!/usr/bin/env python3
"""Check latest Project Atlas batch for required mirror docs."""
from __future__ import annotations
from pathlib import Path
import argparse, re, sys

ROOT=Path(__file__).resolve().parents[1]
ASSIGN=ROOT/'assignments'
VERIFY=ROOT/'verification_reports'
WORKERS=ROOT/'worker_reports'

def latest_assignment():
    files=sorted(ASSIGN.glob('BATCH_*.md'))
    files=[p for p in files if 'TEMPLATE' not in p.name]
    return files[-1] if files else None

def parse_rows(text):
    rows=[]
    for line in text.splitlines():
        if not line.strip().startswith('|') or '`src/' not in line:
            continue
        ticks=re.findall(r'`([^`]+)`', line)
        if len(ticks)>=2:
            rows.append((ticks[0], ticks[-1]))
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--latest', action='store_true')
    args=ap.parse_args()
    a=latest_assignment()
    if not a:
        print('No non-template assignment found.')
        return 0
    batch=re.search(r'(BATCH_\d+)', a.name)
    batch_id=batch.group(1) if batch else a.stem
    rows=parse_rows(a.read_text(encoding='utf-8', errors='replace'))
    missing=[]
    for src, mirror in rows:
        if not (ROOT/mirror).exists():
            missing.append((src, mirror))
    worker=WORKERS/f'{batch_id}_WORKER.md'
    verification=VERIFY/f'{batch_id}_VERIFICATION.md'
    print(f'Assignment: {a.relative_to(ROOT)}')
    print(f'Rows: {len(rows)}')
    print(f'Worker report exists: {worker.exists()}')
    print(f'Verification report exists: {verification.exists()}')
    if missing:
        print('FAIL: missing mirror docs:')
        for s,m in missing:
            print(f'  {s} -> {m}')
        return 2
    print('PASS: all assigned mirror docs exist.')
    return 0

if __name__=='__main__':
    sys.exit(main())
