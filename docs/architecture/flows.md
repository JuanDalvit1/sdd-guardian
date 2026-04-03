# Critical Flows

## Install flow

1. User clones the repository
2. `bootstrap/install.ps1` resolves Codex home
3. The skill is copied into the global skills directory
4. The managed `AGENTS.md` block is inserted or replaced
5. The installed skill is validated when the validator is available

## Documentation update flow

1. Codex reads `PROJECT.md` and `STATE.md`
2. The skill scans the repo
3. Drift mapping decides whether this is bootstrap or targeted update
4. Impacted docs are created or updated
5. Code and docs ship together

