# Asset and Binary Rules

Every asset gets a mirror doc. Identify type with extension, path, filename, and MIME/type hints when available.

Common examples:

- `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`, `.ico` -> image asset
- `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot` -> font asset
- `.mp3`, `.wav`, `.ogg`, `.mp4`, `.webm` -> audio/video asset
- `.zip`, `.rar`, `.7z`, `.tar`, `.gz` -> archive/binary asset

Fallback:

`This appears to be an unknown binary asset. I cannot safely describe its internal contents from text inspection alone.`
