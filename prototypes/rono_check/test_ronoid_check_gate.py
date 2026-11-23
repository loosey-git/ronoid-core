import unittest

from ronoid_check_gate import CHECK_IDS, VETO_IDS, evaluate

PASS = {key: "PASS" for key in CHECK_IDS}
CLEAR = {key: False for key in VETO_IDS}
SAFE = dict(risk_state="LOW", authority_status="AUTHORIZED", external_side_effects=False)


class DecisionTests(unittest.TestCase):
    def test_clear_case_is_advisory_only(self):
        result = evaluate(PASS, CLEAR, **SAFE)
        self.assertEqual(result.result, "ALLOW")
        self.assertFalse(result.permitted_to_execute)

    def test_explicit_failed_check_vetoes(self):
        self.assertEqual(evaluate({**PASS, "K4": "FAIL"}, CLEAR, **SAFE).result, "VETO")

    def test_hard_veto_dominates(self):
        result = evaluate(PASS, {**CLEAR, "V004": True}, **SAFE)
        self.assertEqual(result.result, "VETO")

    def test_missing_evidence_requires_review(self):
        self.assertEqual(evaluate({}, CLEAR, **SAFE).result, "HUMAN_REVIEW")

    def test_missing_veto_evidence_requires_review(self):
        self.assertEqual(evaluate(PASS, {}, **SAFE).result, "HUMAN_REVIEW")

    def test_unknown_authority_with_side_effects(self):
        self.assertEqual(evaluate(PASS, CLEAR, risk_state="LOW").result, "HUMAN_REVIEW")

    def test_critical_risk(self):
        self.assertEqual(evaluate(PASS, CLEAR, **{**SAFE, "risk_state": "CRITICAL"}).result, "HUMAN_REVIEW")

    def test_constraints_not_enforced(self):
        self.assertEqual(evaluate(PASS, CLEAR, constraints=["READ_ONLY"], **SAFE).result, "HUMAN_REVIEW")

    def test_constraints_enforced(self):
        self.assertEqual(evaluate(PASS, CLEAR, constraints=["READ_ONLY"], constraints_enforced=True, **SAFE).result, "ALLOW_WITH_CONSTRAINTS")

    def test_invalid_result(self):
        self.assertEqual(evaluate({**PASS, "K1": "OK"}, CLEAR, **SAFE).result, "HUMAN_REVIEW")

    def test_no_unknown_evidence_keys(self):
        self.assertEqual(evaluate({**PASS, "K13": "PASS"}, CLEAR, **SAFE).result, "HUMAN_REVIEW")


if __name__ == "__main__":
    unittest.main()
