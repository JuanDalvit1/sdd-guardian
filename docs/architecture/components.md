# Components

## Main components

- `skill/sdd-guardian/SKILL.md`: tells Codex when to use the skill and how to behave
- `scripts/scan_project.py`: inventories repo signals relevant to documentation
- `scripts/check_doc_drift.py`: maps repo changes to impacted docs
- `assets/templates/`: scaffolds the base documentation pack
- `bootstrap/install.ps1`: installs the skill globally and manages `AGENTS.md`
- `bootstrap/sync.ps1`: updates a local clone and reapplies installation

## Boundaries

- The skill does not own project-specific truth; it bootstraps and maintains the structure for it
- The bootstrap scripts only touch the Codex profile and the installed skill target
- Public documentation explains usage and rationale but is not the persistent instruction itself

