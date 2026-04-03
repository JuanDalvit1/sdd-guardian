# Why agent-legible docs matter

AI agents work best when the repository itself exposes stable context.

## The failure mode

Teams often try to fix missing context by adding:

- bigger prompts
- more chat background
- more ad-hoc instructions copied into each task

That approach scales poorly because session context is temporary and expensive.

## The better pattern

Put the durable truth in the repo:

- short global behavior instruction
- small repo entrypoint files
- modular docs with clear ownership
- ADRs for decisions

This gives both humans and agents the same durable source of truth.

## Practical effect

When context is stored well:

- onboarding is faster
- handoffs are cleaner
- changes are safer
- AI assistance becomes more consistent
- long-running projects stop losing their architectural memory

