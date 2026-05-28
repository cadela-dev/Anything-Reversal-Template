---
name: anything-doc-worker
description: Document assigned files using mirrored paths and clean-room descriptions.
---

# anything-doc-worker

# Documentation Worker Rules

Worker reads only assigned files.

Creates:

- `docs/_file_docs/<same relative path>.md`
- `worker_reports/BATCH_####.md`

Worker may temporarily use `[~]`.
Worker must not mark `[x]`.
Worker documents behavior and architecture, not copied implementation.
Every doc must preserve mirrored path structure: `src/path/file.ext` -> `docs/_file_docs/src/path/file.ext.md`. Every assigned file must have a mirror doc or an explicit `[D]`/`[!]` outcome with reason.


# File Documentation Template

# `<relative/source/path>`

Project: `<anything_reversal>`  
Batch: `BATCH_####`  
Status: `Draft | Needs Verification | Verified | Needs Rework`

## Purpose

## Main Responsibilities

## Key Exports

## Inputs / Outputs

## Imports / Dependencies

## Referenced Modules

## Relationships

## Architectural Role

## Clean-Room Rebuild Notes

## Unknowns / Follow-up

---

Optional sections when helpful:

## Important Types / Interfaces
## Important Functions / Methods
## State Mutations
## Permission / Safety Behavior
## Tool Calls / External Effects
## Execution Flow
## Error Handling
## Test Coverage / Fixtures
## Comparison Notes


# Documentation Depth Rules

Documentation depth is based on architectural importance, not file size.

Deeply document anything affecting orchestration, execution, permissions, prompts, memory, tools, state, model routing, agent behavior, control flow, lifecycle, background processing, command routing, file operations, subprocesses, bridge/IPC, MCP, user safety, or rebuild-critical behavior.

Use medium detail for adapters, handlers, providers, renderers, transport layers, API wrappers, integrations, support modules, CLI helpers, and behavior-revealing test utilities.

Use compact detail only for clearly simple constants, wrappers, aliases, formatting helpers, passthrough exports, one-function utilities, and static metadata with no behavioral effect.

A single file may contain deep, medium, and compact sections. If uncertain, document more, not less.
