# Indexing Scope

This workflow indexes one project source tree: `src/`.

Everything inside `src/` must be indexed, including code, configs, data, docs, images, fonts, audio/video, archives, lock files, empty files, and unknown binaries.

The initial index creates `docs/_project_index/PROJECT_FILE_INDEX.md` with every file under `src/`.

After initial indexing, `PROJECT_FILE_INDEX.md` becomes a living tracker. Do not regenerate it in a way that loses `[ ]`, `[~]`, `[x]`, `[D]`, `[!]`, notes, or ordering.

Do not compare against a second source tree. This project is one-source-tree documentation/reversal only.
