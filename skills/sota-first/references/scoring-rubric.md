# Candidate Scoring Rubric

Use this rubric to make reasoning inspectable, not to create false precision. Score only dimensions supported by evidence. Use a 1–5 scale and add a short justification for each rating.

## Hard disqualifiers

Remove a candidate before ranking when it fails a non-negotiable constraint, for example:

- Incompatible license, model terms, or data terms
- Unsupported runtime, platform, framework, or hardware
- Impossible latency, memory, throughput, availability, or offline requirements
- Known unresolved critical security issue without a safe mitigation
- Unavailable checkpoint, service, dataset, or dependency required for the intended use
- Abandoned maintenance when the project cannot safely own a fork
- Evidence measured on a task that is materially different from the actual requirement

## Axis A: Research strength

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Task/result quality | Weak or irrelevant result | Competitive result on a relevant task | Leading credible result under comparable conditions |
| Benchmark comparability | Different task, metric, or setup | Partially comparable with caveats | Same task, dataset, metric, split, and protocol |
| Evidence quality | Informal or vendor claim only | Primary source with limited corroboration | Primary source plus credible independent corroboration |
| Reproducibility | No usable code/artifacts | Partial implementation or difficult reproduction | Maintained code, artifacts, instructions, and credible reproduction |
| Freshness | Superseded or stale | Still relevant but not current | Current and checked against recent work/releases |

## Axis B: Project fit

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Constraint fit | Violates major constraints | Fits with tradeoffs | Fits all hard constraints and key preferences |
| Maturity/maintenance | Abandoned or unstable | Active but with gaps | Stable releases, responsive maintenance, clear roadmap |
| Integration cost | Major rewrite or high coupling | Moderate adapter/migration | Native fit or thin integration layer |
| Runtime/operations | Difficult to deploy or observe | Manageable with added work | Fits current deployment, monitoring, scaling, and rollback |
| Security/license | Material unresolved risk | Acceptable with mitigations | Clear compatible terms and strong security posture |
| Reversibility/ecosystem | High lock-in and weak ecosystem | Some portability | Easy rollback/migration and healthy ecosystem |

## Optional weighting

Use weighting only when it clarifies the decision. Adjust weights to the task and disclose the change.

### Research-oriented selection

- Task/result quality: 30%
- Benchmark comparability: 20%
- Evidence quality: 20%
- Reproducibility: 15%
- Freshness: 15%

### Production-oriented selection

- Constraint fit: 25%
- Maturity/maintenance: 20%
- Integration cost: 15%
- Runtime/operations: 15%
- Security/license: 15%
- Reversibility/ecosystem: 10%

Do not average Research strength and Project fit into one number when doing so would hide a meaningful conflict. Report two separate conclusions instead.

## Confidence

Use:

- **High:** Primary evidence is current, comparable, independently corroborated where practical, and project constraints are known.
- **Medium:** The recommendation is supported, but evidence, compatibility, or one important constraint remains partially uncertain.
- **Low:** Search coverage is limited, claims are not independently verified, project constraints are missing, or evidence conflicts materially.
