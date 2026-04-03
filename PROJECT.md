# PROJECT

## Summary

- Product or system purpose: publish a global Codex skill that bootstraps and maintains agent-legible SDD packs
- Primary audience: developers using Codex across multiple repositories and machines
- Current maturity: v1 foundation with install, sync, templates, validation, and public documentation

## Stack

- Languages: PowerShell, Python, Markdown, YAML, SVG
- Runtime: local Codex profile on Windows, GitHub repository, GitHub Actions
- Data layer: none

## Repository map

- `skill/sdd-guardian/`: shipped skill, templates, scripts, and references
- `bootstrap/`: global install and sync scripts
- `codex/AGENTS.snippet.md`: persistent instruction block
- `docs/`: public docs plus internal project architecture and ops notes
- `assets/`: social preview and README visuals

## Integrations

- Codex global profile at `%USERPROFILE%\\.codex` or `$env:CODEX_HOME`
- GitHub repository for sync across machines
- GitHub Actions for structural validation

## Commands

- Install globally: `powershell -ExecutionPolicy Bypass -File .\\bootstrap\\install.ps1`
- Sync after pull: `powershell -ExecutionPolicy Bypass -File .\\bootstrap\\sync.ps1`
- Package release: `powershell -ExecutionPolicy Bypass -File .\\bootstrap\\package-release.ps1 -Version v0.1.0`
- Scan repo: `python .\\skill\\sdd-guardian\\scripts\\scan_project.py --root . --pretty`
- Check doc drift: `python .\\skill\\sdd-guardian\\scripts\\check_doc_drift.py --root . --changed README.md --pretty`

## Constraints

- Global instruction must stay short and durable
- Templates must remain generic enough for many stacks
- Install path must be idempotent and safe inside Codex home
- The repo should explain the system clearly without turning into a giant manual
