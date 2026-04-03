---
name: sdd-guardian
description: Bootstrap and maintain agent-legible project documentation packs built around PROJECT.md, STATE.md, modular docs, and ADRs. Use when Codex needs to create the first SDD for a repo, audit documentation drift, update architecture or ops docs after a change, improve README and onboarding context, or prepare a project for long-running AI-assisted work without losing system context.
---

# SDD Guardian

# Goal

Turn documentation into part of delivery quality. Create a durable context system for humans and agents, then keep it aligned as the project evolves.

## Always start with the repo, not with imagination

- Read `PROJECT.md` and `STATE.md` first when they exist.
- Scan the repo before proposing documentation changes.
- Prefer updating the minimum affected docs over rewriting the whole pack.
- Preserve useful human-written context whenever possible.

Use `scripts/scan_project.py` to inventory the repo and `scripts/check_doc_drift.py` to map changes to impacted documentation.

## Workflow

### 1. Inventory the current state

- Identify manifests, CI files, runtime files, docs, tests, entrypoints, and env hints.
- Detect whether the base pack exists:
  - `PROJECT.md`
  - `STATE.md`
  - `docs/architecture/*`
  - `docs/ops/*`
  - `docs/domain/invariants.md`
  - `docs/adr/*`

### 2. Decide whether this is bootstrap or update

- If the pack is missing or fragmented, bootstrap it from the templates in `assets/templates`.
- If the pack exists, update only the impacted modules.
- Do not invent stable architecture claims without evidence from the repo.

### 3. Map change type to docs

- Architecture, boundaries, integrations, flows: update `docs/architecture/*` and ADRs.
- CI/CD, runtime, deploy, env, observability, runbooks: update `docs/ops/*` and `STATE.md`.
- Domain rules or invariants: update `docs/domain/invariants.md`.
- Public onboarding or usage changes: update `README.md`.

Use `references/update-matrix.md` when in doubt.

### 4. Keep the entrypoint small

- `PROJECT.md` is the fast map.
- `STATE.md` is the current state.
- Detailed truth belongs in modular docs under `docs/`.
- Do not turn `AGENTS.md` into a giant system encyclopedia.

### 5. Treat documentation as done criteria

- Code is not done if the system shape changed and the affected docs stayed stale.
- Ship code and impacted docs in the same task when possible.
- Keep the README focused on onboarding and public usage, not as the only source of system truth.

## Templates and references

- Use `assets/templates/` for the initial pack.
- Read `references/doc-contract.md` for the purpose of each document.
- Read `references/update-matrix.md` for change-to-doc mapping.

## Outputs this skill should aim for

- A repo with a clear and readable entrypoint
- Modular docs that reflect the current system
- ADRs that preserve important decisions
- Minimal documentation drift after delivery work

## Avoid

- rewriting every markdown file for a small fix
- duplicating the same explanation in every doc
- storing long-term project truth only in chat history
- replacing evidence with generic architecture boilerplate
