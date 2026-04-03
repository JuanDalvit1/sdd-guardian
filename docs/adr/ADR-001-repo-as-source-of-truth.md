# ADR-001: Use the GitHub repository as the source of truth

## Status

Accepted

## Context

The same Codex user can work from multiple machines. Keeping the skill only inside one local `.codex` directory makes drift inevitable and weakens long-term maintainability.

## Decision

Version the skill, templates, visuals, and persistent instruction snippet in the public `sdd-guardian` repository, then install from that repository into the active Codex profile.

## Consequences

- Cross-machine sync becomes simple and auditable
- Git history explains why the skill changed
- The repo doubles as public product documentation
- GitHub settings still need one-time manual or authenticated configuration outside plain Git pushes

