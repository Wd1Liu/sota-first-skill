# Activation and Phase Evals

`activation.csv` contains positive and negative prompts for testing whether the skill triggers at the right boundary and, when triggered, which research depth and delivery phase it should select.

The columns are:

- `should_trigger` — whether `sota-first` should activate
- `expected_depth` — `skip`, `quick`, or `full`
- `expected_phase` — `none`, `search`, `validate`, or `integrate`
- `prompt` — representative user request
- `rationale` — why the expected behavior is correct

The most important behaviors are:

1. Trigger on explicit best/SOTA/mature requests and non-trivial architecture, dependency, ML, security, or performance decisions.
2. Avoid triggering on trivial edits, established local fixes, explanations, tests for existing behavior, and explicitly fixed implementations with no material uncertainty.
3. Distinguish research depth from delivery phase.
4. Stop after Research-only when the user says not to implement.
5. Allow isolated Feasibility validation without production integration.
6. Continue from research through validation to Integration without a redundant approval pause when the user requested the full pipeline.
7. Resume from a prior phase when its assumptions remain current instead of repeating all completed work.
8. Keep Research SOTA, Engineering recommendation, and locally measured feasibility separate.
9. Report missing search channels and uncertainty honestly.
10. Never treat `FAIL` or material `INCONCLUSIVE` validation as permission to integrate.

A future automated eval can run each prompt through Codex, capture whether `sota-first` was selected, classify the chosen depth and phase, and score the quality of the research verdict, feasibility contract, measured gate, and integration handoff.
