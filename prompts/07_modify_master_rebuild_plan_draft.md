Read and follow this prompt exactly.

You are preparing a separate editable modified rebuild master plan.

This is used when the user wants to change the generated rebuild plan before creating the final customized plan docs.

Do not read `src/`.

Use only:

`clean_rebuild_plan/MASTER_REBUILD_PLAN_DRAFT.md`

Create this folder at the project root, next to `clean_rebuild_plan/`:

`clean_rebuild_plan_modified/`

Copy:

`clean_rebuild_plan/MASTER_REBUILD_PLAN_DRAFT.md`

to:

`clean_rebuild_plan_modified/MODIFIED_MASTER_REBUILD_PLAN_DRAFT.md`

Important:

* Do not overwrite `clean_rebuild_plan/MASTER_REBUILD_PLAN_DRAFT.md`.
* Do not overwrite any original files in `clean_rebuild_plan/`.
* Do not create modified planning files yet.
* Do not create implementation code.
* Do not read `src/`.

After copying the file, add this note near the top of `clean_rebuild_plan_modified/MODIFIED_MASTER_REBUILD_PLAN_DRAFT.md`:

`NOTE: This is the editable modified master plan. Make all project changes here first. After editing, regenerate the modified planning files from this file only.`

Then create:

`clean_rebuild_plan_modified/README.md`

with a short explanation:

# Modified Clean Rebuild Plan

This folder is for a customized version of the rebuild plan.

Edit this file first:

`MODIFIED_MASTER_REBUILD_PLAN_DRAFT.md`

Do not edit the original generated plan in:

`clean_rebuild_plan/`

After editing the modified master plan, run the regeneration prompt to create the customized planning files in this folder.

The customized planning files should be generated from the modified master only.

Do not use `src/` during this process.

Stop after creating the modified master copy and README.

Do not generate the modified planning files yet.
