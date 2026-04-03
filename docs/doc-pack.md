# Documentation pack

The default `sdd-guardian` pack is optimized for agent readability and long-term maintenance.

## Core files

- `PROJECT.md`: fast system map
- `STATE.md`: current operational and delivery state
- `docs/architecture/overview.md`: system shape
- `docs/architecture/components.md`: responsibilities and boundaries
- `docs/architecture/flows.md`: critical flows and data movement
- `docs/ops/deploy.md`: release and rollback flow
- `docs/ops/environments.md`: environment boundaries and variables
- `docs/ops/runbook.md`: operational procedures and incident steps
- `docs/domain/invariants.md`: rules that must not be broken
- `docs/adr/*`: durable decision log

## Update rules

- Architecture, integration, flows: update architecture docs and ADRs
- CI/CD, runtime, env, deploy, observability: update ops docs and `STATE.md`
- Domain rules: update invariants
- Onboarding or external usage changes: update `README.md`

## What not to do

- Do not turn `PROJECT.md` into a novel
- Do not duplicate the same explanation in every markdown file
- Do not store critical context only in chat or only in a personal note

