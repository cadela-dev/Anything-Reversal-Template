#!/usr/bin/env python3
"""Inventory src/ for Anything Reversal."""
from __future__ import annotations
from pathlib import Path
import argparse, mimetypes

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
INDEX = ROOT / 'docs' / '_project_index' / 'PROJECT_FILE_INDEX.md'

TEXT_EXTS = {'.js','.jsx','.ts','.tsx','.py','.json','.md','.txt','.yml','.yaml','.toml','.ini','.cfg','.env','.html','.css','.scss','.sql','.sh','.bat','.ps1','.xml','.csv','.lock'}
IMAGE_EXTS = {'.png','.jpg','.jpeg','.gif','.webp','.svg','.ico','.bmp','.tif','.tiff'}
FONT_EXTS = {'.ttf','.otf','.woff','.woff2','.eot'}
AUDIO_VIDEO_EXTS = {'.mp3','.wav','.ogg','.flac','.mp4','.mov','.webm','.avi'}
ARCHIVE_EXTS = {'.zip','.rar','.7z','.tar','.gz','.tgz','.bz2','.xz'}

def is_probably_text(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTS:
        return True
    try:
        chunk = path.read_bytes()[:4096]
    except Exception:
        return False
    if b'\x00' in chunk:
        return False
    try:
        chunk.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

def line_count(path: Path) -> int:
    if not is_probably_text(path):
        return 0
    try:
        return len(path.read_text(encoding='utf-8', errors='replace').splitlines())
    except Exception:
        return 0

def classify(path: Path) -> str:
    ext = path.suffix.lower()
    mt, _ = mimetypes.guess_type(str(path))
    if path.stat().st_size == 0:
        return 'empty file'
    if ext in IMAGE_EXTS or (mt or '').startswith('image/'):
        return 'image asset'
    if ext in FONT_EXTS or (mt or '').startswith('font/'):
        return 'font asset'
    if ext in AUDIO_VIDEO_EXTS or (mt or '').startswith(('audio/','video/')):
        return 'audio/video asset'
    if ext in ARCHIVE_EXTS:
        return 'archive/binary asset'
    if is_probably_text(path):
        if ext in {'.json','.yml','.yaml','.toml','.ini','.cfg','.env','.lock'}:
            return 'config/data'
        if ext in {'.md','.txt'}:
            return 'doc'
        return 'code/text'
    return 'unknown binary asset'

def rows():
    if not SRC.exists():
        return []
    out=[]
    for p in sorted(x for x in SRC.rglob('*') if x.is_file()):
        rel = p.relative_to(ROOT).as_posix()
        out.append((rel, line_count(p), p.stat().st_size, classify(p)))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--reset-index', action='store_true', help='Overwrite statuses/notes instead of preserving existing index rows.')
    ap.add_argument('--print-summary', action='store_true')
    args=ap.parse_args()
    data=rows()
    if args.write:
        INDEX.parent.mkdir(parents=True, exist_ok=True)
        existing = {}
        if INDEX.exists() and not args.reset_index:
            for line in INDEX.read_text(encoding='utf-8', errors='replace').splitlines():
                if not line.startswith('|') or '`src/' not in line:
                    continue
                parts=[x.strip() for x in line.strip().strip('|').split('|')]
                if len(parts) >= 6:
                    existing[parts[1].strip('`')] = (parts[0], parts[5])
        lines=['# Project File Index','','Generated from `src/`. Preserve this file as the living tracker after initial indexing.','','Status legend:','','- `[ ]` not assigned','- `[~]` assigned/in progress','- `[x]` mirrored documentation complete and verified','- `[D]` deferred with explicit reason','- `[!]` needs repair or review','','| Status | Path | Lines | Bytes | Type | Notes |','|---|---|---:|---:|---|---|']
        for rel, lc, size, typ in data:
            default_note = '' if typ not in {'unknown binary asset','archive/binary asset'} else 'Best-effort type only; mirror doc must state uncertainty.'
            status, old_note = existing.get(rel, ('[ ]', default_note))
            note = old_note or default_note
            lines.append(f'| {status} | `{rel}` | {lc} | {size} | {typ} | {note} |')
        INDEX.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    if args.print_summary:
        print(f'Files: {len(data)}')
        print(f'Readable lines: {sum(r[1] for r in data)}')
        for typ in sorted(set(r[3] for r in data)):
            print(f'{typ}: {sum(1 for r in data if r[3]==typ)}')

if __name__ == '__main__':
    main()
