# File Locking Rule

Before editing shared workflow files, create or update a lock entry in `status/LOCKS.md`.

Do not create random temporary lock files.

Shared files include:

- `docs/_project_index/PROJECT_FILE_INDEX.md`
- `NEXT_ASSIGNMENT.md`
- `docs/_project_index/ARCHITECTURE_MAP.md`
- `docs/_project_index/FOLLOW_UP_QUEUE.md`
- `docs/_project_index/CORE_SYSTEM_FILES.md`

Lock entry should include agent name, file, batch number if applicable, timestamp, and current action.
If another active agent is working on the same shared file, stop and report.
