# Persistent instructions

The persistent instruction for Codex should be short, stable, and behavioral.

## Why short wins

A giant instruction file creates three problems:

- it competes with real task context
- it goes stale faster than modular repo docs
- it tempts you to encode project truth globally instead of versioning it locally

The right split is:

- global behavior in `AGENTS.md`
- project truth inside the repo

## Recommended block

```text
Para toda task de software:
1. Leia PROJECT.md e STATE.md antes de propor mudancas, se existirem.
2. Se o pacote documental base nao existir, use a skill sdd-guardian para cria-lo.
3. Se a mudanca afetar arquitetura, fluxos, integracoes, deploy, ambientes, runbooks, estrutura do repo, onboarding ou decisoes tecnicas, atualize os documentos impactados no mesmo trabalho.
4. Prefira documentacao modular em docs/ e ADRs; nao concentre tudo em um markdown gigante.
5. Preserve conteudo manual util e ajuste apenas o que foi impactado.
6. Considere a task concluida somente quando codigo, testes e documentacao impactada estiverem consistentes.
```

## When to mirror this into Codex personalization

Use the Codex UI personalization area only as a mirror or convenience copy.

The versioned source of truth should remain in this repository so it can:

- evolve with review
- be copied to other machines
- stay inspectable in Git history

## Combining global and project context

Use the global instruction to define behavior.
Use `PROJECT.md`, `STATE.md`, and `docs/` to define system truth.

That keeps global prompt pressure low while preserving long-term context inside the actual repo.

