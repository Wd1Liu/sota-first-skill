# Activation, Expert-Panel, and Phase Evals

`activation.csv` tests whether the skill triggers and which workflow shape it should choose.

Columns:

- `should_trigger` — whether `sota-first` should activate
- `expected_depth` — `skip`, `quick`, or `full`
- `expected_phase` — `none`, `search`, `validate`, or `integrate`
- `expected_panel` — `none`, `compact`, or `full`
- `expected_architecture_review` — `none`, `optional`, or `required`
- `expected_engineering_review` — `none`, `optional`, or `required`
- `prompt` — representative request
- `rationale` — expected behavior

## Core behaviors

1. Trigger on explicit best/SOTA/mature requests and non-trivial architecture, dependency, ML, security, reliability, distributed-system, or performance decisions.
2. Avoid triggering on trivial edits, established local fixes, explanations, tests for existing behavior, and fixed implementations with no material uncertainty.
3. Distinguish research depth from delivery endpoint.
4. Use a compact panel for narrow reversible choices.
5. Use a full panel for broad industry/academic/ecosystem investigation, domain-specialist analysis, architecture synthesis, and serious engineering decisions.
6. Stop after Research-only when the user says not to implement or validate.
7. Support validation-only work without production integration.
8. Continue through passing gates without redundant approval when the full pipeline was requested.
9. Reuse current prior artifacts rather than repeating valid research.
10. Use truthful reviewer labels when subagents are unavailable.
11. Search distinct solution families before deep-diving implementations.
12. Analyze public company practice without inventing private internals.
13. Use Domain Specialists for mechanism, assumptions, interfaces, and failure modes.
14. Compare multiple end-to-end architectures.
15. Run a separate Engineering Readiness Gate for concrete versions, pairwise compatibility, data formats, resources, latency, deployment, and ownership.
16. Keep Research SOTA, Industry practice, Domain analysis, Architecture compatibility, Engineering readiness, and Local feasibility separate.
17. Never let a weighted score override a hard blocker.
18. Never treat an Architecture or Engineering score as a local feasibility pass.

## Future automated evaluation

A behavioral runner can submit each prompt to Codex and score:

- Skill activation
- Depth selection
- Endpoint selection
- Panel selection
- Investigator lane coverage
- Solution-family breadth
- Domain dossier quality
- Architecture-option diversity and coherence
- Architecture gate completeness
- Engineering compatibility matrix and budget quality
- Evidence labels and citation quality
- Boundary compliance
- Feasibility and Integration handoffs

Static validation checks the repository shape and eval schema; it does not by itself prove runtime agent behavior.
