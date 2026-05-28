# Documentation Depth Rules

Documentation depth is based on architectural importance, not file size.

Deeply document anything affecting orchestration, execution, permissions, prompts, memory, tools, state, model routing, agent behavior, control flow, lifecycle, background processing, command routing, file operations, subprocesses, bridge/IPC, MCP, user safety, or rebuild-critical behavior.

Use medium detail for adapters, handlers, providers, renderers, transport layers, API wrappers, integrations, support modules, CLI helpers, and behavior-revealing test utilities.

Use compact detail only for clearly simple constants, wrappers, aliases, formatting helpers, passthrough exports, one-function utilities, and static metadata with no behavioral effect.

A single file may contain deep, medium, and compact sections. If uncertain, document more, not less.
