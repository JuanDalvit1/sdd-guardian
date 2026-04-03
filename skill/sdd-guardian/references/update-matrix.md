# Update matrix

Map repo changes to documentation updates.

## Architecture changes

Examples:

- component boundaries
- service integration
- data flow changes
- major folder or module reorganization

Update:

- `PROJECT.md`
- `docs/architecture/overview.md`
- `docs/architecture/components.md`
- `docs/architecture/flows.md`
- relevant ADR

## Ops changes

Examples:

- CI/CD
- Docker
- systemd
- deployment scripts
- runtime ports
- environment handling
- monitoring or runbook changes

Update:

- `STATE.md`
- `docs/ops/deploy.md`
- `docs/ops/environments.md`
- `docs/ops/runbook.md`

## Domain rule changes

Examples:

- business invariants
- validation rules
- permission rules
- lifecycle constraints

Update:

- `docs/domain/invariants.md`
- relevant ADR when the rule changed by design

## Onboarding or public usage changes

Examples:

- setup flow
- required tools
- exposed commands
- public API usage summary

Update:

- `README.md`
- `PROJECT.md` if the project map changed too

