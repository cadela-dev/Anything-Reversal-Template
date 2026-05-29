Read and follow this prompt exactly.

You are consolidating the existing clean rebuild planning docs into one editable master planning document.

Do not read `src/`.

Use only the files in:

`clean_rebuild_plan/`

The planning files should have been created by:

`prompts/05_create_rebuild_plan.md`

Read the generic clean rebuild planning files that exist in `clean_rebuild_plan/`.

Expected files usually include:

* `clean_rebuild_plan/00_README.md`
* `clean_rebuild_plan/01_REBUILD_SCOPE.md`
* `clean_rebuild_plan/02_TECH_STACK.md`
* `clean_rebuild_plan/03_PROJECT_STRUCTURE_PLAN.md`
* `clean_rebuild_plan/04_DATA_AND_STATE_PLAN.md`
* `clean_rebuild_plan/05_CORE_BOOTSTRAP_PLAN.md`
* `clean_rebuild_plan/06_MODULE_AND_FEATURE_PLAN.md`
* `clean_rebuild_plan/07_INTEGRATION_AND_FLOW_PLAN.md`
* `clean_rebuild_plan/08_INTERFACE_OR_UI_PLAN.md`
* `clean_rebuild_plan/09_SUBSYSTEM_ORDER.md`
* `clean_rebuild_plan/10_TESTING_AND_VALIDATION_PLAN.md`
* `clean_rebuild_plan/11_OPEN_QUESTIONS.md`
* `clean_rebuild_plan/12_IMPLEMENTATION_ROADMAP.md`

If an expected file is missing, continue with the files that exist and record the missing file in the master plan under open questions.

Create one new file:

`clean_rebuild_plan/MASTER_REBUILD_PLAN_DRAFT.md`

Purpose:

This file should combine and summarize the clean rebuild planning docs into one coherent, editable master plan.

Important:

* Do not delete or overwrite the original planning files.
* Do not create implementation code.
* Do not read `src/`.
* Do not blindly copy every line from the planning files.
* Summarize and consolidate.
* Keep enough detail that this master file can later be used to regenerate the planning docs.
* Mark uncertain or optional items clearly.
* Remove duplicate information.
* Preserve important implementation order, architecture decisions, dependencies, risks, and testing requirements.
* Do not assume the project type. Use only what the planning docs prove.

Use this structure:

# Master Rebuild Plan Draft

## 1. Project Identity

* Current project name:
* Proposed/rebranded project name:
* One-line purpose:
* Clean-room boundary:
* Primary use case:
* Secondary use cases:
* Project type:
* Known interfaces:

## 2. Clean-Room Rules

Summarize the rules for rebuilding from docs only.

Must include:

* do not read `src/`
* use docs, mirror docs, and generated planning docs only
* recreate behavior, not copied implementation
* no pasted source code
* assumptions must be labeled
* unclear items must become open questions instead of invented facts

## 3. Rebuild Scope

Summarize:

* what will be rebuilt
* what will not be rebuilt yet
* compatibility goals
* risk areas
* assumptions
* known versus inferred behavior

## 4. Recommended Tech Stack

Summarize:

* runtime/language
* package manager/build tools
* frameworks/libraries
* database/storage if any
* UI/web/game/CLI dependencies if any
* asset/binary dependencies
* testing/linting tools
* optional alternatives
* external services/APIs if any

Do not invent technologies not supported by the plan.

## 5. Proposed Project Structure

Create a clean folder/file structure for the rebuilt project.

Keep this practical.

Mark anything optional.

Only include folders that make sense for the project.

Possible folders may include:

* `core/`
* `config/`
* `models/`
* `services/`
* `controllers/`
* `commands/`
* `events/`
* `routes/`
* `ui/`
* `web/`
* `assets/`
* `tests/`
* `utils/`
* `scripts/`

Do not include irrelevant folders just because they are common.

## 6. Data and State Plan

Summarize all persistent data, runtime state, config files, cache files, local storage, database models, schemas, serialized data, indexes, and important relationships.

If there are many data/state items, group them by priority.

If the project has no persistent data, explicitly say so and describe runtime state only.

## 7. Core Startup / Bootstrap Plan

Summarize startup order.

Include only relevant items:

* environment loading
* config loading
* dependency initialization
* database/storage connection if applicable
* main app/service/client creation
* module loading
* plugin loading if applicable
* route/command/event registration if applicable
* schedulers/background jobs if applicable
* asset loading if applicable
* logging/errors/shutdown

## 8. Major Modules and Features

Summarize each major module/subsystem.

For each include:

* responsibility
* inputs
* outputs
* dependencies
* data/state used
* important behavior
* rebuild priority
* docs to consult first
* known unknowns

Do not assume command systems, event systems, web dashboards, game systems, or database systems unless the planning docs prove them.

## 9. Integration and Behavior Flows

Summarize major flows such as:

* startup flow
* user/action flow
* request/response flow
* command/event flow
* data processing flow
* file processing flow
* background job flow
* network/API flow
* error/retry flow
* plugin/addon flow

Only include flows proven by the existing plan docs.

## 10. Interface / UI / API Plan

Summarize user-facing interfaces.

Examples:

* CLI
* web UI
* API endpoints
* bot commands
* desktop GUI
* game UI
* plugin API
* library public API
* config files as interface
* generated reports/output files

If the project has no dedicated UI, say so.

Do not invent interfaces not supported by the plan.

## 11. Subsystem Build Order

Summarize the safest implementation order.

For each phase include:

* goal
* dependencies
* docs to read
* validation method
* risk level
* stop condition

The order should minimize broken imports, context overload, and rebuild risk.

## 12. Testing and Validation Plan

Summarize:

* static checks
* lint/format checks
* type checks if applicable
* config validation
* startup checks
* unit tests
* integration tests
* subsystem dry-runs
* compatibility checks
* final acceptance criteria

Only include relevant test categories.

## 13. Open Questions

Classify open questions as:

* must resolve before coding
* resolve during implementation
* optional polish
* obsolete/already answered

If an answer can be found in existing mirror docs later, note which docs should be checked.

Do not read `src/`.

## 14. Implementation Roadmap

Summarize the implementation rounds.

For each round include:

* round number
* goal
* docs to read
* files/folders to create
* expected output
* validation/checklist
* stop condition
* risk level

Keep rounds small enough for Claude Code to handle without context overload.

## 15. Items To Edit Before Regenerating Plans

Create a checklist of things a human should review/edit in this master file before regenerating the plan docs.

Examples:

* project name
* repo name
* stack choices
* folders to include/remove
* scope cuts
* risky/legal wording
* optional features
* first implementation round
* compatibility targets
* features to postpone or remove

## 16. Regeneration Notes

Explain that after this master draft is manually edited, Claude should regenerate the planning files from the edited master plan.

Do not regenerate them yet.

Stop after creating:

`clean_rebuild_plan/MASTER_REBUILD_PLAN_DRAFT.md`
