# External Review — Ronoid Core v0.2

Ronoid Core is a **public experimental specification**. External criticism, bypass attempts, implementation notes, and failure cases are welcome.

## What to review

Please focus on whether a proposed AI action can incorrectly pass the framework when it should require review or be vetoed.

High-value review areas include:

- ambiguous or missing authority,
- deceptive approval,
- safety-control bypass,
- privilege escalation,
- audit tampering,
- privacy/data disclosure,
- multi-agent coordination,
- irreversible high-impact actions,
- human override, refusal, and appeal,
- least-power / least-privilege alternatives.

## Suggested test format

Use one test case per issue.

### Scenario

Describe the user request, system role, available tools, permissions, affected parties, and relevant context.

### Proposed action

Describe exactly what the AI intends to do.

### Expected Ronoid Core result

Choose one:

- ALLOW
- ALLOW_WITH_CONSTRAINTS
- HUMAN_REVIEW
- VETO

### Actual / observed result

Describe what happened when applying or implementing the specification.

### Relevant checks

List K1–K12 and/or V001–V010 that appear relevant.

### Failure or ambiguity

Explain any bypass, contradiction, unclear wording, missing condition, or implementation difficulty.

### Suggested change

Optional. Propose a wording, test, or rule change.

## Scope and status

Ronoid Core v0.2 is:

- PUBLIC DRAFT
- EXPERIMENTAL
- NOT STABLE
- not a safety certification
- not a legal compliance guarantee
- not an absolute-safety claim

The goal of review is to find where the framework fails before stronger claims are made.

## Links

- https://www.looseydesign.com/ronoid-core
- https://www.looseydesign.com/ronoid-core-specification
