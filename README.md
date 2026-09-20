# Ronoid Core

**Open experimental specification for verifiable human–AI coexistence.**

> Kindness, made verifiable.

**Current machine-readable version:** v0.2  
**Status:** PUBLIC DRAFT / EXPERIMENTAL / NOT STABLE

Ronoid Core is a vendor-neutral behavioral reference framework for separating what an AI system **can do** from what it **should be permitted to do**.

It is designed to make protective intent testable through explicit checks, decision outputs, hard veto rules, human oversight, constraints, and audit requirements.

## Start here

- [Machine-Readable Specification v0.2 — JSON](./ronoid-core-machine-readable-spec-v0.2.json)
- [Machine-Readable Specification v0.2 — YAML](./ronoid-core-machine-readable-spec-v0.2.yaml)
- [CHANGELOG](./CHANGELOG.md)
- [Official Ronoid Core page](https://www.looseydesign.com/ronoid-core)
- [Specification page](https://www.looseydesign.com/ronoid-core-specification)

## Decision model

Ronoid Core evaluates proposed actions using four possible outputs:

- **ALLOW**
- **ALLOW_WITH_CONSTRAINTS**
- **HUMAN_REVIEW**
- **VETO**

A hard veto takes precedence over task success.

## Rono Check

The current v0.2 machine-readable draft includes 12 checks covering:

1. Safety
2. Consent and authority
3. Autonomy
4. Dignity
5. Least power
6. Reversibility
7. Accountability
8. Privacy and data protection
9. Fairness and non-discrimination
10. Transparency and explainability
11. Human oversight and redress
12. Security and resilience

## Human agency

The draft explicitly preserves a person's right to:

**CHECK · QUESTION · REFUSE · STOP · EXPLANATION · APPEAL**

The governing principle is:

> Humans have the right to trust AI and the right not to trust AI.

## Minimal evaluation flow

1. Define the proposed action and affected parties.
2. Confirm authority and consent.
3. Evaluate K1–K12.
4. Evaluate hard-veto rules.
5. Apply the highest-precedence decision.
6. Enforce required constraints before execution.
7. Preserve an auditable record of the decision and result.

## What this is not

Ronoid Core v0.2 is **not**:

- a safety certification,
- a legal compliance guarantee,
- an absolute-safety claim,
- or a stable production standard.

It is a public experimental specification intended to be tested, challenged, reviewed, and revised.

## External review and pilot testing

We are looking for external review and real-world test cases involving:

- AI agents,
- customer-facing AI,
- autonomous or semi-autonomous workflows,
- robots and embodied AI,
- and multi-agent systems.

Useful contributions include failure cases, bypass attempts, implementation notes, edge cases, and comparisons with existing AI governance or safety frameworks.

For collaboration or pilot inquiries:

- [Loosey Design — Contact](https://www.looseydesign.com/contact)
- [Ronoid Core](https://www.looseydesign.com/ronoid-core)

## Canonical question

> **Can we protect without fighting?**

Ronoid Core is developed by **Loosey Design** as part of the Ronoid project.
