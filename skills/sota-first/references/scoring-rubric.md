# Research Candidate Scoring Rubric

Use this rubric during candidate-family and implementation shortlisting. It makes reasoning inspectable without pretending that research evidence proves architecture, engineering, or local feasibility.

Score only dimensions supported by evidence. Use 1–5 with a short justification.

## Hard disqualifiers

Remove a candidate before ranking when it violates a non-negotiable constraint, including:

- Incompatible license, model terms, data terms, privacy, or policy
- Unsupported runtime, platform, framework, hardware, or deployment environment
- Impossible quality, latency, memory, throughput, availability, or offline requirement
- Unavailable model, checkpoint, service, dataset, artifact, or dependency
- Known unresolved critical security issue without a safe mitigation
- Abandoned maintenance when the project cannot safely own a fork
- Evidence measured on a materially different task
- A required private company component that is not publicly available

Architecture, engineering, or feasibility review may discover a later blocker that overrides this score.

## Axis A: Research strength

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Task and result quality | Weak or irrelevant | Competitive on a relevant task | Leading credible result under comparable conditions |
| Benchmark comparability | Different task or setup | Partially comparable with caveats | Same task, dataset, metric, split, and protocol |
| Evidence quality | Informal or promotional | Primary source with limited corroboration | Primary source plus credible independent corroboration |
| Reproducibility | No usable artifacts | Partial or difficult reproduction | Maintained code, artifacts, instructions, and credible reproduction |
| Freshness | Superseded or stale | Still relevant | Current and checked against recent work |

Suggested research-oriented weighting:

- Task and result quality: 30%
- Benchmark comparability: 20%
- Evidence quality: 20%
- Reproducibility: 15%
- Freshness: 15%

## Axis B: Public practice and ecosystem evidence

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Production disclosure quality | Marketing or indirect signal | Technically useful company report | Detailed public architecture, implementation, or postmortem |
| Context transferability | Very different scale or constraints | Partially transferable | Closely comparable context |
| Ecosystem maturity | Fragmented or abandoned | Active with gaps | Stable, maintained, documented ecosystem |
| Standards and interoperability | Proprietary and isolated | Some adapters or standards | Strong standard or protocol fit |
| Operational evidence | No production evidence | Limited case study | Multiple credible operational reports |

Do not interpret absence of public disclosure as proof that a method is unused.

## Axis C: Predicted project fit

Before local validation, label these as predictions.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Constraint fit | Violates major constraints | Fits with tradeoffs | Fits hard constraints and key preferences |
| Integration surface | Major rewrite or high coupling | Moderate adapter or migration | Native fit or thin boundary |
| Runtime and operations | Difficult to deploy or observe | Manageable with work | Fits current operating model |
| Security and license | Material unresolved risk | Acceptable with mitigation | Clear compatible terms and posture |
| Reversibility and ownership | High lock-in or unclear owner | Bounded plan | Easy rollback and clear ownership |

These predictions help decide what should reach architecture synthesis. They do not replace:

- `architecture-review.md`
- `engineering-review.md`
- `feasibility-playbook.md`

## Separate conclusions

Report separately:

- Research SOTA
- Strongest public industry precedent
- Most mature ecosystem implementation
- Best predicted project fit

Do not average these into one universal score when tradeoffs are meaningful.

## Confidence

- **High** — current primary evidence, comparable conditions, credible corroboration, known repository constraints
- **Medium** — supported conclusion with one important evidence or compatibility gap
- **Low** — limited search coverage, indirect company evidence, incomparable results, missing project constraints, or material conflict

Architecture and Engineering gates have their own confidence and statuses. Local feasibility depends on representative measurement.
