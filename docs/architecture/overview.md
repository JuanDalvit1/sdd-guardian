# Architecture Overview

## System shape

`sdd-guardian` is a repo-centered distribution for a global Codex skill. The repository stores four core layers:

- a public-facing product layer in `README.md`, `docs/`, community files, and visuals
- a distributable skill layer in `skill/sdd-guardian/`
- an installation layer in `bootstrap/`
- a persistent behavior layer in `codex/AGENTS.snippet.md`

## Runtime model

The repo itself is the source of truth. Installation copies the skill into the active Codex home and injects a managed block into `%USERPROFILE%\\.codex\\AGENTS.md`.

## Design principle

Global behavior stays short. Project truth stays versioned inside each project repo.

