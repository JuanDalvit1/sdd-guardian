# Runbook

## Common procedures

- Install globally: run `bootstrap\\install.ps1`
- Resync after updates: run `bootstrap\\sync.ps1`
- Validate scripts: run the local Python commands from `CONTRIBUTING.md`
- Inspect managed instruction: open `%USERPROFILE%\\.codex\\AGENTS.md`

## Incident handling

- If the install script fails, confirm the resolved Codex home and validator path
- If the managed block duplicates, inspect the start and end markers in `AGENTS.md`
- If the skill drifts across machines, pull the repo and rerun `bootstrap\\sync.ps1`

