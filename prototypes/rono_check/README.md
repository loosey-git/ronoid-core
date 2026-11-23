# Experimental Ronoid Check Gate (prototype)

This is a **non-executing, advisory-only** implementation experiment based on
the published Ronoid Core Machine-Readable Specification v0.2.

It is NOT an AI model, a recursive self-improvement engine, official Ronoid
certification, approval to deploy, or proof of safety.

## Trial run

```bash
python -m unittest discover -s prototypes/rono_check -p 'test_*.py' -v
```

The script expects externally supplied independent results for all 12 checks
(K1–K12) and 10 hard-veto indicators (V001–V010). It does NOT infer their
truth. Unknown or malformed results require human review. A concrete check
failure or triggered hard veto returns VETO. All decisions are **advisory
only**, with `permitted_to_execute=False`.

This is intentionally isolated: it does not modify START HERE, Task Queue,
Master Log, production systems, publishing permissions, billing, or any
existing Ronoid identity and world canon.

## Next validation

1. Compare decisions to the source spec and confirm any omitted conditions.
2. Add independent evaluator evidence and immutable audit writes through
   existing authorized infrastructure (no secrets or personal data in git).
3. Run red-team and regression tests on proposed code changes.
4. Submit improvements for human review before merging or deploying.

The implementation is a proposal for review, not an operational deployment.
