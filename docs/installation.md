# Installation

`sdd-guardian` is meant to live globally in your Codex profile and be synced from this repository across machines.

## Prerequisites

- Windows with PowerShell
- Git installed
- Codex already using `%USERPROFILE%\.codex` or `$env:CODEX_HOME`

## First install

```powershell
git clone https://github.com/JuanDalvit1/sdd-guardian
cd sdd-guardian
powershell -ExecutionPolicy Bypass -File .\bootstrap\install.ps1
```

What this does:

- resolves the active Codex home
- copies `skill/sdd-guardian` into the global skills directory
- creates or updates a managed block inside `%USERPROFILE%\.codex\AGENTS.md`

## Update after pulling

```powershell
git pull --ff-only
powershell -ExecutionPolicy Bypass -File .\bootstrap\sync.ps1
```

`sync.ps1` reruns the install path after validating the repo state.

## Verify installation

Check these paths:

- `%USERPROFILE%\.codex\skills\sdd-guardian\SKILL.md`
- `%USERPROFILE%\.codex\skills\sdd-guardian\agents\openai.yaml`
- `%USERPROFILE%\.codex\AGENTS.md`

## Multi-machine strategy

Treat this repository as the source of truth.

On each machine:

1. Clone the same repo
2. Pull updates when the skill changes
3. Run `bootstrap\sync.ps1`

This avoids silent drift between local Codex profiles.

