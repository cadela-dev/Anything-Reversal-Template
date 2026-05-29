Read and follow this prompt exactly.

You are regenerating a MODIFIED clean rebuild plan from the approved modified master plan.

Do not read `src/`.

Use only:

`clean_rebuild_plan_modified/MODIFIED_MASTER_REBUILD_PLAN_DRAFT.md`

The modified master plan has been manually reviewed and edited.

Treat it as the only source of truth.

Important:

Do not overwrite the original planning files in:

`clean_rebuild_plan/`

The original generated plan must remain untouched.

Create this folder at the project root if it does not already exist:

`clean_rebuild_plan_modified/`

Then regenerate the customized planning files inside that folder only:

* `clean_rebuild_plan_modified/00_README.md`
* `clean_rebuild_plan_modified/01_REBUILD_SCOPE.md`
* `clean_rebuild_plan_modified/02_TECH_STACK.md`
* `clean_rebuild_plan_modified/03_PROJECT_STRUCTURE_PLAN.md`
* `clean_rebuild_plan_modified/04_DATA_AND_STATE_PLAN.md`
* `clean_rebuild_plan_modified/05_CORE_BOOTSTRAP_PLAN.md`
* `clean_rebuild_plan_modified/06_MODULE_AND_FEATURE_PLAN.md`
* `clean_rebuild_plan_modified/07_INTEGRATION_AND_FLOW_PLAN.md`
* `clean_rebuild_plan_modified/08_INTERFACE_OR_UI_PLAN.md`
* `clean_rebuild_plan_modified/09_SUBSYSTEM_ORDER.md`
* `clean_rebuild_plan_modified/10_TESTING_AND_VALIDATION_PLAN.md`
* `clean_rebuild_plan_modified/11_OPEN_QUESTIONS.md`
* `clean_rebuild_plan_modified/12_IMPLEMENTATION_ROADMAP.md`

The customized files must be based only on:

`clean_rebuild_plan_modified/MODIFIED_MASTER_REBUILD_PLAN_DRAFT.md`

Do not use:

* `src/`
* original `clean_rebuild_plan/00–12` files
* original `clean_rebuild_plan/MASTER_REBUILD_PLAN_DRAFT.md`

The original planning files are historical/generated originals only.

Important rules:

* Do not create implementation code.
* Do not read `src/`.
* Do not overwrite original files in `clean_rebuild_plan/`.
* Use only the edited `clean_rebuild_plan_modified/MODIFIED_MASTER_REBUILD_PLAN_DRAFT.md`.
* Keep each regenerated file focused and consistent.
* Remove anything the modified master plan removed.
* Add anything the modified master plan added.
* Preserve the clean-room boundary.
* If something is unclear in the modified master plan, add it to `clean_rebuild_plan_modified/11_OPEN_QUESTIONS.md` instead of inventing details.
* Do not invent a project type, UI layer, database, command system, event system, or web layer unless the modified master plan supports it.

After creating the customized plan files, create:

`clean_rebuild_plan_modified/REGENERATION_SUMMARY.md`

Include:

* files created in `clean_rebuild_plan_modified/`
* confirmation that original `clean_rebuild_plan/` files were not overwritten
* confirmation that the modified master plan was used as the only source of truth
* major changes reflected from the modified master plan
* unresolved questions
* whether the customized plan is ready for implementation
* which folder should be used for the actual build planning going forward

Final decision wording:

If ready, write:

`Use clean_rebuild_plan_modified/ as the source of truth for the changed project build.`

Stop after regeneration.

Do not start building code.
