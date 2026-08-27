# Candidate Scoring Rubric

Use this rubric to make research-stage reasoning inspectable, not to create false precision. Score only dimensions supported by evidence. Use a 1–5 scale and add a short justification for each rating.

Candidate scoring ranks what should be reviewed and validated next. It does **not** produce an Architecture Review Gate or a feasibility `PASS`. Architecture compatibility requires a proposed design and expert review; local feasibility requires representative validation against explicit thresholds.

## Hard disqualifiers

Remove a candidate before ranking when it fails a non-negotiable constraint, for example:

- Incompatible license, model terms, or data terms
- Unsupported runtime, platform, framework, hardware, protocol, or deployment environment
- Impossible latency, memory, throughput, availability, consistency, or offline requirements
- Known unresolved critical security issue without a safe mitigation
- Unavailable checkpoint, service, dataset, or dependency required for the intended use
- Abandoned maintenance when the project cannot safely own a fork
- Evidence measured on a task that is materially different from the actual requirement
- A confirmed architecture blocker such as an incompatible contract, trust-boundary violation, unbounded failure propagation, or destructive migration with no rollback

A hard disqualifier discovered during architecture review or feasibility validation overrides every earlier score.

## Axis A: Research strength

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Task/result quality | Weak or irrelevant result | Competitive result on a relevant task | Leading credible result under comparable conditions |
| Benchmark comparability | Different task, metric, or setup | Partially comparable with caveats | Same task, dataset, metric, split, and protocol |
| Evidence quality | Informal or vendor claim only | Primary source with limited corroboration | Primary source plus credible independent corroboration |
| Reproducibility | No usable code/artifacts | Partial implementation or difficult reproduction | Maintained code, artifacts, instructions, and credible reproduction |
| Freshness | Superseded or stale | Still relevant but not current | Current and checked against recent work/releases |

## Axis B: Predicted project fit

Before local validation, label these ratings as **predicted project fit** when they rely on documentation, external reports, or repository inspection rather than measurements in the target environment.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Constraint fit | Violates major constraints | Fits with tradeoffs | Fits all hard constraints and key preferences |
| Maturity/maintenance | Abandoned or unstable | Active but with gaps | Stable releases, responsive maintenance, clear roadmap |
| Integration effort | Major rewrite or high coupling appears likely | Moderate adapter or migration | Native fit or thin project layer appears likely |
| Runtime/operations | Difficult to deploy or observe | Manageable with added work | Fits current deployment, monitoring, scaling, and rollback |
| Security/license | Material unresolved risk | Acceptable with mitigations | Clear compatible terms and strong security posture |
| Reversibility/ecosystem | High lock-in and weak ecosystem | Some portability | Easy rollback/migration and healthy ecosystem |

After architecture review and a feasibility spike, update the relevant justifications with reviewed or locally measured evidence. Do not silently convert an external estimate into a local fact.

## Axis C: Architecture compatibility

Architecture compatibility is a separate expert-reviewed axis. Do not infer it only from package metadata or a candidate's popularity. First define the proposed integration design, then use `architecture-review.md`.

The detailed architecture score covers:

- Boundary and responsibility fit
- Interface and data-contract fit
- Dependency, runtime, and platform fit
- Deployment, topology, and resource fit
- Reliability and failure isolation
- Security, privacy, and compliance fit
- Observability and operability
- Migration, compatibility, and rollback
- Maintainability, ownership, and evolution

Report:

- Per-dimension 1–5 ratings
- A weighted 0–100 architecture compatibility score
- Hard blockers
- `PASS`, `CONDITIONAL PASS`, `FAIL`, or `INCONCLUSIVE`
- Reviewer mode: dedicated architect/subagent or same-agent structured review

Do not average Architecture compatibility into Research strength or Predicted project fit. A high research score cannot offset an architecture `FAIL`.

## Optional weighting for research-stage ranking

Use weighting only when it clarifies which candidate should receive architecture review next. Adjust weights to the task and disclose the change.

### Research-oriented selection

- Task/result quality: 30%
- Benchmark comparability: 20%
- Evidence quality: 20%
- Reproducibility: 15%
- Freshness: 15%

### Production-oriented shortlist

- Constraint fit: 25%
- Maturity/maintenance: 20%
- Integration effort: 15%
- Runtime/operations: 15%
- Security/license: 15%
- Reversibility/ecosystem: 10%

Do not combine Research strength, Predicted project fit, and Architecture compatibility into one grand total when doing so would hide a meaningful conflict. Report three separate conclusions.

## Architecture is a gate, not only a score

Use the Architecture Review Gate from `architecture-review.md`:

- **PASS** — structurally compatible and eligible for the requested next phase
- **CONDITIONAL PASS** — structurally viable under explicit bounded conditions
- **FAIL** — redesign or select another candidate
- **INCONCLUSIVE** — material architecture evidence remains missing

A score is a summary. Hard blockers and dimension evidence are authoritative.

## Feasibility is a separate gate

A candidate's feasibility status must be based on the validation contract in `feasibility-playbook.md`:

- **PASS** — all hard thresholds and critical assumptions were verified
- **CONDITIONAL PASS** — viable under explicit bounded conditions
- **FAIL** — a hard threshold or non-negotiable constraint was violated
- **INCONCLUSIVE** — a material uncertainty remains unresolved

A high research, project-fit, or architecture score cannot override feasibility `FAIL` or material `INCONCLUSIVE` status.

## Confidence

Use:

- **High:** Primary evidence is current and comparable, the proposed architecture was reviewed against known repository constraints, and every material feasibility claim is locally measured.
- **Medium:** The recommendation is supported, but evidence, architecture compatibility, feasibility, or one important constraint remains partially uncertain.
- **Low:** Search coverage is limited, claims are not independently verified, architecture evidence is missing, project constraints are incomplete, validation is unrepresentative, or evidence conflicts materially.
