# Contributing

Thanks for helping improve Anything Reversal Template.

This project is a Claude Code clean-room documentation workflow. It should remain generic and safe to use with many kinds of source trees.

## Important rules

Do not submit:

- proprietary source code
- purchased source code
- private customer code
- secrets, API keys, tokens, passwords, or credentials
- generated mirror docs from a private project
- content copied from source code that should not be public

This repository should contain only the reusable template, prompts, rules, skills, helper scripts, and documentation.

## How to contribute

1. Fork the repository.
2. Create a branch.
3. Make your changes.
4. Test the workflow on a disposable/sample source tree.
5. Open a pull request.

## Good contribution types

- clearer prompts
- better batching rules
- better final verification rules
- improved clean-room documentation templates
- safer `.gitignore` rules
- helper scripts that do not expose private source
- bug fixes in workflow instructions

## Before opening a pull request

Check that:

- no private source files are included
- `src/` contains only `.gitkeep`
- generated docs/reports are not included
- prompt filenames and README references match
- status values use only `[ ]`, `[~]`, `[x]`, `[D]`, and `[!]`