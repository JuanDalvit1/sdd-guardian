# Document contract

Use this reference to keep the pack consistent.

## PROJECT.md

- Purpose: fast project map
- Include: purpose, stack, structure, commands, integrations, constraints
- Keep short enough to read first

## STATE.md

- Purpose: live working state
- Include: current status, active risks, pending work, recent important changes, next actions
- Update when the state actually changes

## Architecture docs

- `overview.md`: top-level system shape
- `components.md`: responsibilities and boundaries
- `flows.md`: critical runtime and data flows

## Ops docs

- `deploy.md`: release flow, rollback, CI/CD notes
- `environments.md`: environment boundaries and config conventions
- `runbook.md`: common procedures and incident actions

## Domain docs

- `invariants.md`: rules that must remain true regardless of refactors

## ADRs

- Use when a meaningful technical decision is made, reversed, or clarified

