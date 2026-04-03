# Environments

## Environment inventory

- Local development: Windows workstation with Codex profile
- Distribution: GitHub repository
- Automation: GitHub Actions runner for validation

## Configuration

- Codex home resolves from `$env:CODEX_HOME` or `%USERPROFILE%\\.codex`
- Install path writes into the global skills directory and `AGENTS.md`
- No secrets are required for local install itself

