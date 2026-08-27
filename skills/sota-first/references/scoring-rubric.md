# Candidate Scoring Rubric

Use this rubric to make research-stage reasoning inspectable, not to create false precision. Score only dimensions supported by evidence. Use a 1–5 scale and add a short justification for each rating.

Candidate scoring ranks what should be validated next. It does **not** produce a feasibility `PASS`. Only representative local validation against explicit thresholds can produce `PASS`, `CONDITIONAL PASS`, `FAIL`, or `INCONCLUSIVE`.

## Hard disqualifiers

Remove a candidate before ranking when it fails a non-negotiable constraint, for example:

- Incompatible license, model terms, or data terms
- Unsupported runtime, platform, framework, or hardware
- Impossible latency, memory, throughput, availability, or offline requirements
- Known unresolved critical security issue without a safe mitigation
- Unavailable checkpoint, service, dataset, or dependency required for the intended use
- Abandoned maintenance when the project cannot safely own a fork
- Evidence measured on a task that is materially different from the actual requirement

A hard disqualifier discovered during feasibility validation overrides the earlier score.

## Axis A: Research strength

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Task/result quality | Weak or irrelevant result | Competitive result on a relevant task | Leading credible result under comparable conditions |
| Benchmark comparability | Different task, metric, or setup | Partially comparable with caveats | Same task, dataset, metric, split, and protocol |
| Evidence quality | Informal or vendor claim only | Primary source with limited corroboration | Primary source plus credible independent corroboration |
| Reproducibility | No usable code/artifacts | Partial implementation or difficult reproduction | Maintained code, artifacts, instructions, and credible reproduction |
| Freshness | Superseded or stale | Still relevant but not current | Current and checked against recent work/releases |

## Axis B: Project fit

Before local validation, label these ratings as **predicted project fit** when they rely on documentation, external reports, or repository inspection rather than measurements in the target environment.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Constraint fit | Violates major constraints | Fits with tradeoffs | Fits all hard constraints and key preferences |
| Maturity/maintenance | Abandoned or unstable | Active but with gaps | Stable releases, responsive maintenance, clear roadmap |
| Integration cost | Major rewrite or high coupling | Moderate adapter/migration | Native fit or thin integration layer |
| Runtime/operations | Difficult to deploy or observe | Manageable with added work | Fits current deployment, monitoring, scaling, and rollback |
| Security/license | Material unresolved risk | Acceptable with mitigations | Clear compatible terms and strong security posture |
| Reversibility/ecosystem | High lock-in and weak ecosystem | Some portability | Easy rollback/migration and healthy ecosystem |

After a feasibility spike, update the relevant justifications with locally measured evidence. Do not silently convert an external estimate into a local fact.

## Optional weighting

Use weighting only when it clarifies the research-stage decision. Adjust weights to the task and disclose the change.

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

## Feasibility is a gate, not a score

A candidate's feasibility status must be based on the validation contract in `feasibility-playbook.md`:

- **PASS** — all hard thresholds and critical assumptions were verified
- **CONDITIONAL PASS** — viable under explicit bounded conditions
- **FAIL** — a hard threshold or non-negotiable constraint was violated
- **INCONCLUSIVE** — a material uncertainty remains unresolved

A high research or project-fit score cannot override `FAIL` or material `INCONCLUSIVE` status.

## Confidence

Use:

- **High:** Primary evidence is current, comparable, independently corroborated where practical, project constraints are known, and any material feasibility claim is locally measured.
- **Medium:** The recommendation is supported, but evidence, compatibility, feasibility, or one important constraint remains partially uncertain.
- **Low:** Search coverage is limited, claims are not independently verified, project constraints are missing, validation is unrepresentative, or evidence conflicts materially.
