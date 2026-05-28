---
name: mirrored-file-docs
description: Preserve source path structure under docs/_file_docs and require one mirror doc per assigned file.
---

# Mirrored File Docs

Every assigned file must produce exactly one mirrored doc unless explicitly marked `[D]` deferred or `[!]` failed with a reason.

Mirror path format:

```text
src/tools/Tool.ts
-> docs/_file_docs/src/tools/Tool.ts.md

src/assets/logo.png
-> docs/_file_docs/src/assets/logo.png.md
```

Never flatten file docs. Never skip binary, image, font, archive, unknown, or empty files.
