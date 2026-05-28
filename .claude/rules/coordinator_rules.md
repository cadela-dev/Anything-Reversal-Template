# Coordinator Rules

Coordinator runs Planner → Worker → Verifier → Architect → repeat.

Stop when no `[ ]` remain, assignment is ambiguous, repeated verifier errors occur, files are too large for safe context, clean-room risk is detected, source scope changes, or human review is needed.
