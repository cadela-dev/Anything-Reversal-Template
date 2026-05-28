# Documentation Worker Rules

Worker reads only assigned files plus the assignment and required rules.

## Mirror-first rule

Before deep documentation, create every required mirrored doc path listed in the assignment table.

For each assigned source file:

`src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`

Every assigned file must have exactly one explicit outcome in the worker report:

- `[x]` mirror doc created
- `[D]` deferred with reason
- `[!]` error/needs repair with reason

Silent omission is forbidden.

## Worker outputs

Create:

- `docs/_file_docs/src/<same relative path>.md`
- `worker_reports/BATCH_####_WORKER.md`

Worker may temporarily use `[~]` in the project index while files are in progress. Worker must not mark `[x]` in the project index; only verifier marks complete.

## Documentation boundaries

Document behavior and architecture, not copied implementation. Do not paste source code except tiny identifiers, public names, file names, or very short phrases needed for clarity.

Images, fonts, archives, binaries, lock files, and unknown assets still receive mirror docs. For unreadable assets, document safe metadata, likely role, path clues, references, and confidence limits.
