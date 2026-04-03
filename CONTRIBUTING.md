# Contributing

Thanks for improving `sdd-guardian`.

## Principles

- Keep the persistent instruction short and durable
- Prefer modular docs over one giant markdown file
- Preserve human-written project context whenever possible
- Treat templates as scaffolding, not as fiction generators
- Keep scripts deterministic and easy to inspect

## Development flow

1. Open an issue or describe the problem clearly
2. Change the minimum set of files needed
3. Update templates and docs together when behavior changes
4. Run the local validation commands
5. Open a pull request with before/after context

## Local validation

```powershell
python .\skill\sdd-guardian\scripts\scan_project.py --root .
python .\skill\sdd-guardian\scripts\check_doc_drift.py --root . --changed README.md
python "$env:CODEX_HOME\\skills\\.system\\skill-creator\\scripts\\quick_validate.py" .\skill\sdd-guardian
```

## Contribution boundaries

- Do not enlarge the persistent instruction block without a strong reason
- Do not add heavy dependencies to the bootstrap path
- Do not make the skill rewrite all docs by default
- Do not add repo-specific assumptions into generic templates
