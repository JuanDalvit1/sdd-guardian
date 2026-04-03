# Adoption playbook

Use this checklist when adopting `sdd-guardian` in a real repository.

## Step 1: Bootstrap the pack

Create or update:

- `PROJECT.md`
- `STATE.md`
- `docs/architecture/*`
- `docs/ops/*`
- `docs/domain/invariants.md`
- `docs/adr/*`

## Step 2: Define review rules

Add a pull request checklist that asks:

- Did architecture change?
- Did deploy or environment behavior change?
- Did onboarding or public usage change?
- Does an ADR need to be created or updated?

## Step 3: Make docs part of done

Do not close implementation work if code changed the system shape but the docs stayed behind.

## Step 4: Keep the entrypoint small

`PROJECT.md` and `STATE.md` should be readable fast.

- `PROJECT.md` is the map
- `STATE.md` is the living state

Do not dump every detail into them.

## Step 5: Use ADRs for decisions

When architecture changes direction, add or update an ADR instead of rewriting history into a generic summary.

