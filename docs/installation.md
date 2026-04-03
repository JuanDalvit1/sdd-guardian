# Installation

`sdd-guardian` is meant to live globally in your Codex profile and be synced from this repository across machines.

## Prerequisites

- Windows with PowerShell
- Git installed
- Codex already using `%USERPROFILE%\.codex` or `$env:CODEX_HOME`

## First install

### Option A: download the latest release

1. Open [the latest release](https://github.com/JuanDalvit1/sdd-guardian/releases/latest)
2. Download `sdd-guardian-<version>.zip`
3. Extract it
4. Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\bootstrap\install.ps1
```

### Option B: clone the repository

```powershell
git clone https://github.com/JuanDalvit1/sdd-guardian
cd sdd-guardian
powershell -ExecutionPolicy Bypass -File .\bootstrap\install.ps1
```

What this does:

- resolves the active Codex home
- copies `skill/sdd-guardian` into the global skills directory
- creates or updates a managed block inside `%USERPROFILE%\.codex\AGENTS.md`

## Release assets

- `sdd-guardian-<version>.zip`: full repo snapshot ready to extract and install
- `sdd-guardian-skill-<version>.zip`: skill-only payload for manual placement into `.codex\skills`

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

## Building release archives

Maintainers can generate both ZIP assets locally with:

```powershell
powershell -ExecutionPolicy Bypass -File .\bootstrap\package-release.ps1 -Version v0.1.0
```
