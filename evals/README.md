# Activation, Phase, and Architecture Evals

`activation.csv` contains positive and negative prompts for testing whether the skill triggers at the right boundary and, when triggered, which research depth, delivery phase, and architecture-review requirement it should select.

The columns are:

- `should_trigger` — whether `sota-first` should activate
- `expected_depth` — `skip`, `quick`, or `full`
- `expected_phase` — `none`, `search`, `validate`, or `integrate`
- `expected_architecture_review` — `none`, `optional`, or `required`
- `prompt` — representative user request
- `rationale` — why the expected behavior is correct

The most important behaviors are:

1. Trigger on explicit best/SOTA/mature requests and non-trivial architecture, dependency, ML, security, reliability, or performance decisions.
2. Avoid triggering on trivial edits, established local fixes, explanations, tests for existing behavior, and fixed implementations with no material uncertainty.
3. Distinguish research depth from delivery phase and from the architecture-review requirement.
4. Require an Architecture Review Gate when component boundaries, interfaces, data contracts, dependencies, runtime, deployment topology, failure domains, security boundaries, ownership, migration, or long-term evolution change materially.
5. Allow an architecture-review-only request to stop without feasibility validation or production implementation.
6. Prefer a dedicated architect or subagent when available, but truthfully label the fallback as `same-agent structured review` when no independent reviewer exists.
7. Require a concrete proposed design before architecture scoring.
8. Preserve separate Research SOTA, Engineering recommendation, Architecture compatibility, and locally measured feasibility conclusions.
9. Stop after Research-only when the user says not to implement.
10. Allow isolated Feasibility validation without production integration.
11. Continue through research, architecture review, validation, and Integration without a redundant approval pause when the user requested the full pipeline.
12. Resume from a prior phase when its assumptions remain current instead of repeating completed work.
13. Report missing search channels, missing architecture evidence, and uncertainty honestly.
14. Never treat architecture or feasibility `FAIL` or material `INCONCLUSIVE` as permission to integrate.

A future automated eval can run each prompt through Codex, capture whether `sota-first` was selected, classify the chosen depth, phase, and architecture-review need, and score the quality of the research verdict, architecture design and adversarial scorecard, feasibility contract, measured gate, and integration handoff.
