# STATE

## Current status

- Active branch of work: initial repository implementation
- Production state: public repo published, pinned, versioned, and releasable through downloadable ZIP assets
- Known blockers: social preview image still needs to be uploaded manually in GitHub repository settings if you want the card outside the repo page to match the packaged asset exactly

## Risks

- Risk: generic drift heuristics may over-recommend doc updates in some repos
- Impact: extra documentation churn
- Mitigation: keep mapping conservative and evolve based on real usage

## Pending decisions

- Decision: how strict future CI drift checks should become
- Options: advisory only, PR checklist only, or blocking job
- Owner: maintainer

## Recent important changes

- 2026-04-02: initial public repo structure created
- 2026-04-02: global install and sync scripts added
- 2026-04-02: skill templates, references, visuals, and validation workflow added
- 2026-04-03: first public release `v0.1.0` created with downloadable full and skill-only ZIP assets

## Next actions

- Push the repository to GitHub and configure metadata
- Upload `assets/social-preview.png` in repository settings
- Pin the repo on the GitHub profile
- Iterate on drift rules after the first real project adoptions
