Read and follow this prompt exactly.

You are starting the CLEAN-ROOM REBUILD PLANNING phase for the Project Atlas project.

The documentation/mapping phase is complete.
Final verification should already be complete or nearly complete.

Important clean-room boundary:

Do not open, read, inspect, copy, summarize, or reference files under `src/`.

Use only:

* `verification_reports/FINAL_PROJECT_VERIFICATION.md`
* `docs/_project_index/REBUILD_CONCEPTS.md`
* `docs/_project_index/ARCHITECTURE_MAP.md`
* `docs/_project_index/CORE_SYSTEM_FILES.md`
* `docs/_project_index/DEPENDENCY_NOTES.md`
* `docs/_project_index/SYSTEM_BEHAVIOR_NOTES.md`
* `docs/_project_index/FOLLOW_UP_QUEUE.md`
* `docs/_project_index/PROJECT_STRUCTURE.md`
* selected mirror docs under `docs/_file_docs/` only when needed

If `verification_reports/SMART_REBUILD_READINESS_AUDIT.md` exists, read it too.

Do not write implementation code yet.

Your job is to create a clean-room rebuild plan for whatever project was documented .

Do not assume the project is a Discord bot, web app, game, CLI tool, library, plugin, or service unless the documentation proves it.

# Goal

Create a new rebuild planning folder:

`clean_rebuild_plan/`

Inside it, create these files:

* `00_README.md`
* `01_REBUILD_SCOPE.md`
* `02_TECH_STACK.md`
* `03_PROJECT_STRUCTURE_PLAN.md`
* `04_DATA_AND_STATE_PLAN.md`
* `05_CORE_BOOTSTRAP_PLAN.md`
* `06_MODULE_AND_FEATURE_PLAN.md`
* `07_INTEGRATION_AND_FLOW_PLAN.md`
* `08_INTERFACE_OR_UI_PLAN.md`
* `09_SUBSYSTEM_ORDER.md`
* `10_TESTING_AND_VALIDATION_PLAN.md`
* `11_OPEN_QUESTIONS.md`
* `12_IMPLEMENTATION_ROADMAP.md`

# Required planning behavior

Use the verified ProjectAtlas documentation to infer the safest clean rebuild strategy.

Do not blindly mirror the original structure if a cleaner structure would be better.

Preserve behavior and compatibility where useful.

Create a plan that fits the actual project type discovered from the docs.

Examples:

* If the project is a web app, plan routes, controllers, middleware, templates/assets, API endpoints, sessions/auth.
* If the project is a bot, plan command/event handling, permissions, state, external API integrations.
* If the project is a game, plan engine setup, gameplay systems, assets, input, networking, save data.
* If the project is a CLI/tool, plan commands, config, file IO, output formats, packaging.
* If the project is a library, plan public API, modules, tests, examples, package exports.
* If the project uses a database, plan schemas/models/migrations.
* If the project has no database, do not invent one unless needed for clean rebuild behavior.
* If the project has no UI/web layer, do not create a web/UI plan beyond saying none is needed.

# Required contents

## `00_README.md`

Explain:

* this is a clean-room rebuild plan
* original `src/` must not be used during rebuild
* rebuild must use docs only
* behavior should be recreated, not source code copied
* the plan is based on verified mirror docs and project-index synthesis docs

## `01_REBUILD_SCOPE.md`

Define:

* what will be rebuilt
* what will not be rebuilt yet
* compatibility goals
* risk areas
* assumptions
* what parts are known versus inferred

Use the documented project notes to determine scope.

Do not assume any specific technology or product type.

## `02_TECH_STACK.md`

List the recommended stack based on the documented project.

Include:

* runtime/language
* package manager/build tools
* frameworks/libraries
* database/storage tools if applicable
* UI/web/game/rendering libraries if applicable
* testing tools
* linting/formatting tools
* external services or APIs
* assets or binary dependencies

Use `DEPENDENCY_NOTES.md` as the main source.

If the original stack is outdated, recommend a modern equivalent while preserving behavior.

## `03_PROJECT_STRUCTURE_PLAN.md`

Propose a clean folder structure under:

`clean_rebuild/`

Use modern organization based on the actual project.

Include only folders that make sense for this project.

Possible examples:

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

Do not include irrelevant folders just because they appeared in an example.

## `04_DATA_AND_STATE_PLAN.md`

Plan all persistent data, runtime state, config files, cache files, local storage, database models, schemas, or serialized data.

For each data/state item:

* purpose
* key fields or structure
* relationships
* persistence method
* indexes or lookup keys if known
* rebuild priority
* compatibility concerns

If the project has no persistent data, explicitly say so and describe runtime state only.

## `05_CORE_BOOTSTRAP_PLAN.md`

Plan how the rebuilt project starts.

Include only relevant items:

* environment loading
* config loading
* dependency initialization
* database/storage connection if applicable
* main app/service/client creation
* module loading
* plugin loading if applicable
* route/command/event registration if applicable
* scheduler/background job startup if applicable
* asset loading if applicable
* error handling/logging
* shutdown behavior

## `06_MODULE_AND_FEATURE_PLAN.md`

Plan the major modules and features discovered in the ProjectAtlas docs.

For each module/feature:

* responsibility
* inputs
* outputs
* dependencies
* data/state used
* important behavior
* rebuild priority
* docs/mirror docs to consult first

Do not assume command systems, event systems, or web systems unless the project actually has them.

## `07_INTEGRATION_AND_FLOW_PLAN.md`

Plan how the system pieces interact.

Include relevant flows such as:

* startup flow
* request/response flow
* command/action flow
* event/message flow
* user interaction flow
* data processing flow
* file processing flow
* network/API flow
* background job flow
* error/retry flow
* plugin/addon flow

Use `SYSTEM_BEHAVIOR_NOTES.md` and `ARCHITECTURE_MAP.md`.

## `08_INTERFACE_OR_UI_PLAN.md`

Plan any user-facing interface found in the project.

This may include:

* web UI
* API endpoints
* command-line interface
* bot commands
* desktop GUI
* game UI
* plugin API
* library public API
* config files as interface
* generated reports/output files

If the project has no UI, write:

`No dedicated UI layer was identified. The primary interface appears to be: ...`

Do not invent a web dashboard, CLI, GUI, or API if the docs do not support it.

## `09_SUBSYSTEM_ORDER.md`

Create the safest build order.

For each subsystem or phase:

* dependencies
* docs to read first
* implementation goal
* validation method
* risk level
* stop condition

The order should minimize broken imports and context overload.

Start with the smallest foundation that can run, then add features in batches.

## `10_TESTING_AND_VALIDATION_PLAN.md`

Plan tests and validation.

Include relevant checks:

* static checks
* lint/format checks
* type checks if applicable
* config validation
* startup checks
* unit tests
* integration tests
* data/model tests
* API/route tests if applicable
* UI tests if applicable
* CLI tests if applicable
* game/simulation tests if applicable
* file processing tests if applicable
* regression/compatibility checks

Do not include irrelevant test categories.

## `11_OPEN_QUESTIONS.md`

Classify follow-ups from `FOLLOW_UP_QUEUE.md` as:

* resolve before coding
* resolve during implementation
* optional polish
* obsolete/already answered

Do not block rebuild on low-risk questions.

If a question can be resolved from existing mirror docs, note which docs should be checked.

Do not open `src/`.

## `12_IMPLEMENTATION_ROADMAP.md`

Break the rebuild into numbered implementation rounds.

For each round include:

* goal
* docs to read
* files/folders to create
* expected output
* validation/checklist
* stop condition
* risk level

Aim for small Claude Code rounds that avoid context overflow.

Do not make a single giant rebuild round.

# Output rules

Do not create `clean_rebuild/` implementation files yet.

Only create planning files inside:

`clean_rebuild_plan/`

Do not read `src/`.

If you need source behavior, use the mirror docs under:

`docs/_file_docs/`

If required docs are missing, create the planning files anyway and mark gaps clearly in `11_OPEN_QUESTIONS.md`.

Stop after creating the planning files and give a concise summary.
