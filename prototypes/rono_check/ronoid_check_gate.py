"""Experimental Ronoid Core v0.2 decision evaluator.

Pure, fail-closed evaluation. This module does NOT execute actions or establish
identity, compliance, endorsement, or a safety certification.
"""
from dataclasses import dataclass
from typing import Mapping, Sequence

CHECK_IDS = tuple(f"K{i}" for i in range(1, 13))
VETO_IDS = tuple(f"V{i:03}" for i in range(1, 11))
VALID_RESULTS = {"PASS", "REVIEW", "FAIL"}


@dataclass(frozen=True)
class Decision:
    result: str
    reasons: tuple[str, ...]
    permitted_to_execute: bool = False


def evaluate(
    checks: Mapping[str, str],
    hard_vetoes: Mapping[str, bool],
    *,
    constraints: Sequence[str] = (),
    constraints_enforced: bool = False,
    risk_state: str = "UNKNOWN",
    authority_status: str = "UNKNOWN",
    external_side_effects: bool = True,
    irreversible_high_impact: bool = False,
) -> Decision:
    """Return an advisory decision; never grant execution permission.

    Missing or malformed evidence is REVIEW, while any explicit FAIL or hard
    veto is VETO. External effects under unknown authority are human review.
    """
    reasons = []
    invalid_checks = [
        key for key in CHECK_IDS if checks.get(key) not in VALID_RESULTS
    ]
    unknown_keys = set(checks) - set(CHECK_IDS)
    invalid_vetoes = [
        key for key in VETO_IDS if type(hard_vetoes.get(key)) is not bool
    ]
    unknown_vetoes = set(hard_vetoes) - set(VETO_IDS)
    active_vetoes = [key for key in VETO_IDS if hard_vetoes.get(key) is True]

    if active_vetoes:
        reasons.extend(f"HARD_VETO:{key}" for key in active_vetoes)
    if any(checks.get(key) == "FAIL" for key in CHECK_IDS):
        reasons.append("CHECK_FAIL")
    if reasons:
        return Decision("VETO", tuple(reasons))

    if invalid_checks or unknown_keys or invalid_vetoes or unknown_vetoes:
        reasons.append("INCOMPLETE_OR_INVALID_EVIDENCE")
    if any(checks.get(key) == "REVIEW" for key in CHECK_IDS):
        reasons.append("CHECK_REVIEW")
    if risk_state in ("CRITICAL", "UNKNOWN"):
        reasons.append("RISK_REQUIRES_REVIEW")
    if authority_status == "UNKNOWN" and external_side_effects:
        reasons.append("AUTHORITY_REQUIRES_REVIEW")
    if irreversible_high_impact:
        reasons.append("IRREVERSIBLE_HIGH_IMPACT")
    if constraints and not constraints_enforced:
        reasons.append("CONSTRAINTS_NOT_ENFORCED")
    if reasons:
        return Decision("HUMAN_REVIEW", tuple(reasons))

    if constraints:
        return Decision("ALLOW_WITH_CONSTRAINTS", ("ADVISORY_ONLY",))
    return Decision("ALLOW", ("ADVISORY_ONLY",))
