---
name: sota-first
description: Research, compare, validate feasibility, and optionally integrate current state-of-the-art and production-mature approaches for a non-trivial feature, algorithm, dependency, integration, or architecture change. Trigger for research-only comparisons, feasibility spikes, research-then-implement requests, best/SOTA requests, unfamiliar domains, new dependencies, ML/CV/agent methods, and performance- or security-sensitive work. Do not trigger for trivial edits, local bug fixes with a known cause, pure refactors, or implementation of an explicitly fixed method unless compatibility or prior feasibility remains uncertain.
---

# SOTA First

Choose and validate an evidence-backed approach that fits the current repository before writing substantial production code. Keep these two questions separate:

1. **Research SOTA:** What approach has the strongest credible results for the defined task?
2. **Engineering recommendation:** What approach is the best fit for this project's constraints today?

They may have different answers. A research winner is not automatically feasible in the target project, and a successful search is not the same as a successful validation.

## Core model: two independent choices

This skill separates **research depth** from **delivery phase**.

### Research depth

- **Skip** — no external selection work is needed
- **Quick mode** — compact repository check and targeted evidence review
- **Full mode** — complete repository, evidence, comparison, and risk analysis

### Delivery phase

- **Research-only** — search, compare, and recommend without implementing or running a feasibility spike
- **Feasibility validation** — test the selected candidate in an isolated, disposable way without integrating it into production
- **Integration** — promote a validated approach into the real feature, with tests and rollback awareness

These axes are independent. A narrow task can use Quick mode and stop at Research-only. A high-risk ML task can use Full mode, continue through Feasibility validation, and then enter Integration.

## Respect the requested endpoint

Infer the endpoint from the user's request and stop exactly there.

| User intent | Required endpoint | Production writes |
|---|---|---|
| “Research/compare/recommend only” or “do not implement” | Research-only | No |
| “Check feasibility,” “run a spike/prototype,” or “do not integrate yet” | Feasibility validation | Only isolated disposable experiment artifacts |
| “Research, validate, and implement if viable” | Integration after a passing gate | Yes, only after validation |
| “Implement the best/mature option” | Research and validation proportional to risk, then Integration | Yes, after the required gate |

When the user already requested the full pipeline, continue from research to validation to integration without an unnecessary approval checkpoint. When the user requested only research or validation, do not silently continue into the next phase.

A later request may resume from a prior phase. Reuse an earlier verdict or feasibility result when its repository assumptions, versions, constraints, and evidence are still current; otherwise refresh only what may have changed.

## Operating boundaries

### Research-only boundary

Do not edit production code, manifests, lockfiles, infrastructure, migrations, or persistent configuration. Use read-only repository inspection and external research. Do not install dependencies persistently merely to support a search-only conclusion.

### Feasibility validation boundary

A feasibility spike may execute code, install temporary dependencies, or create disposable artifacts, but it must remain isolated from production behavior and persistent project state whenever practical. Prefer a temporary directory, worktree, throwaway branch, untracked spike, or clearly isolated experiment path. Record and clean up temporary changes.

Do not present a toy demo, successful import, or paper benchmark as proof that the candidate meets the project's constraints.

### Integration boundary

Enter production integration only after the selected candidate receives one of these statuses:

- **PASS** — continue when integration was requested
- **CONDITIONAL PASS** — continue only if the explicit conditions fit the stated constraints and requested scope
- **FAIL** — do not integrate; test the next justified finalist or revise the recommendation
- **INCONCLUSIVE** — do not treat uncertainty as success; resolve the material unknown or explain why it remains

For **Full mode**, do not edit production code, manifests, lockfiles, infrastructure, migrations, or persistent configuration until a research verdict exists. If material feasibility risk remains, do not integrate until a feasibility verdict also exists.

## Decide the research depth

### Skip

Do not run this workflow for:

- Typos, copy changes, formatting, or mechanical renames
- A localized bug whose cause and correction are already established
- Pure refactoring with no behavior, dependency, or architecture choice
- Tests or documentation for an already-selected implementation
- A user-mandated method with no material compatibility or feasibility uncertainty

### Quick mode

Use a compact repository check and a short verdict when the choice is common, low-risk, reversible, and limited in scope. Examples include a small utility, a narrow development dependency, or a standard integration with no architecture impact.

Quick mode can still stop at Research-only, run a small Feasibility validation, or continue to Integration depending on the requested endpoint.

### Full mode

Use the complete workflow when any of these apply:

- The user asks for the best, latest, mature, established, benchmark-leading, or SOTA method
- The task adds a major dependency, service, data store, protocol, model, or framework
- The task involves ML, computer vision, agents, retrieval, optimization, security, privacy, distributed systems, or performance-critical behavior
- The decision changes architecture, data contracts, deployment, hardware needs, or long-term maintenance
- The domain is unfamiliar or several credible approaches likely exist
- A wrong choice would be expensive to reverse

When uncertain between Quick and Full, use Full.

# Phase A: Research and selection

## 1. Inspect the repository first

Before external research:

1. Read applicable `AGENTS.md` files and repository instructions.
2. Inspect README files, architecture docs, manifests, lockfiles, configuration, tests, and deployment files.
3. Search for existing implementations, abstractions, dependencies, experiments, and abandoned attempts related to the task.
4. Identify the current language, framework, runtime, package manager, deployment target, hardware, data flow, and testing conventions.
5. Extract explicit and implicit constraints: latency, throughput, quality, memory, compute, privacy, offline behavior, license, budget, maintainability, and delivery scope.

Prefer **KEEP** when the repository already contains a suitable maintained solution. Do not introduce an external dependency merely because it is newer.

## 2. Frame the decision

Write down, at least internally:

- The exact capability being selected
- Success metrics and acceptance criteria
- Hard constraints and soft preferences
- The evidence cutoff or research date
- What would disqualify a candidate
- Whether the task is engineering selection, research-method selection, architecture selection, or a combination
- Which unknowns require local feasibility evidence rather than literature or documentation alone

Do not compare methods against a vague task. For benchmark claims, ensure the task, dataset, metric, split, and operating conditions are comparable.

## 3. Research through available channels

Use the most authoritative current sources available. Search in this order when relevant:

1. Existing repository code and history
2. Official specifications, documentation, release notes, security advisories, and package registries
3. Original papers, official project pages, official repositories, benchmark or leaderboard maintainers
4. Independent reproductions, reputable engineering reports, and issue trackers
5. Community discussions only for operational caveats, not as the sole basis for core claims

For Full mode, inspect `references/search-playbook.md`.

Search enough to identify the serious candidate classes, then verify the strongest two to four candidates. Do not collect a long list of near-duplicates.

## 4. Check evidence and freshness

For every finalist, verify the relevant subset of:

- Current version, release date, maintenance activity, and API stability
- Original source for performance or quality claims
- Official implementation or a credible reproduction
- Runtime, hardware, memory, data, calibration, and deployment requirements
- License, model/data terms, security posture, and known critical issues
- Compatibility with the repository's stack and constraints
- Migration, rollback, observability, and operational burden

Record exact dates or versions for time-sensitive claims. Never call something “current SOTA” based on a single secondary article, incomparable benchmark, repository stars, or an undated result.

If a search channel is unavailable, say so in the verdict and reduce confidence. Do not imply exhaustive coverage.

## 5. Evaluate candidates on two axes

Use `references/scoring-rubric.md` for Full mode.

Evaluate separately:

- **Research strength:** result quality, benchmark comparability, evidence quality, reproducibility, and freshness
- **Project fit:** constraint fit, maturity, maintainability, integration cost, runtime/operations, security/license, and reversibility

Do not hide uncertainty behind a numeric total. A score must be supported by concrete evidence. Omit a total when evidence is not comparable.

Apply hard disqualifiers before ranking. Typical disqualifiers include incompatible licensing, impossible compute or latency requirements, known unresolved critical vulnerabilities, abandoned maintenance with no safe fork, or a benchmark that does not represent the actual task.

## 6. Produce the research verdict

Use one of these decisions:

- **KEEP** — the existing project solution is already the best fit
- **ADOPT** — use an established solution substantially as-is
- **EXTEND** — use an established foundation with a thin project-specific layer
- **COMPOSE** — combine a small number of complementary mature components
- **BUILD** — implement a focused custom solution because no candidate satisfies the constraints

The verdict must distinguish the research winner from the engineering recommendation, explain rejected finalists, state confidence and missing evidence, define the smallest sensible implementation boundary, and list the assumptions that still require feasibility validation.

Use the relevant template in `references/verdict-template.md`.

If the requested endpoint is Research-only, stop here and do not implement.

# Phase B: Feasibility validation

Use `references/feasibility-playbook.md` whenever material project-specific uncertainty remains or the user explicitly requests a feasibility check, spike, prototype, benchmark, or proof of concept.

## 7. Define a falsifiable validation contract

Before building the spike, specify:

- The selected candidate and exact version, checkpoint, service tier, or commit
- The assumptions and highest-risk unknowns being tested
- Representative data, traffic, hardware, runtime, and operating conditions
- Measurable acceptance thresholds
- Hard failure conditions
- The smallest experiment capable of changing the decision
- The isolation and cleanup plan

Test the highest-risk unknown first. Do not spend effort polishing a candidate that has already failed a hard constraint.

## 8. Run an isolated representative spike

Prefer read-only capability probes first, then a temporary script or environment, then an isolated worktree or experiment path only when needed.

Measure the relevant subset of:

- Quality or task success on representative project inputs
- End-to-end latency, throughput, warm-up, startup, and streaming behavior
- Peak and steady-state CPU, GPU memory, RAM, storage, and network use
- Runtime, framework, API, data contract, and deployment compatibility
- Failure handling, retries, cancellation, observability, migration, and rollback
- Dependency, licensing, security, privacy, service, or checkpoint constraints
- The actual size and coupling of the required project-specific adapter

Record the repository revision, environment, versions, configuration, commands, raw results, and differences from published conditions. Keep external claims separate from locally measured results.

## 9. Produce the feasibility verdict

Assign exactly one status:

- **PASS** — hard thresholds and critical integration assumptions were verified
- **CONDITIONAL PASS** — viable only under explicit bounded conditions
- **FAIL** — a hard threshold or non-negotiable constraint was violated
- **INCONCLUSIVE** — a material uncertainty could not be resolved with the available data, access, tooling, or environment

Use the feasibility template in `references/verdict-template.md`.

If the candidate fails, update the research verdict and test the next justified finalist when that is within the requested scope. Do not force the original recommendation.

If the requested endpoint is Feasibility validation, stop here and do not integrate production code.

# Phase C: Integration

Enter this phase only when integration was requested and the feasibility gate allows it.

## 10. Promote the validated approach cleanly

1. Recreate the smallest maintainable production implementation; do not blindly copy experimental code.
2. Reuse the selected library, model, service, protocol, or standard instead of rebuilding delegated capability.
3. Avoid speculative wrappers, dependency duplication, hard-coded experiment settings, and unrelated refactors.
4. Follow repository conventions for versioning, dependency pinning, configuration, observability, and data contracts.
5. Preserve a reasonable rollback path for high-impact changes.

## 11. Preserve the evidence as project validation

1. Add tests, benchmarks, or evaluation cases that cover the thresholds that established feasibility.
2. Verify the integrated path under representative conditions, not only the isolated spike.
3. Report any difference between the spike and final implementation.
4. Do not repeat external performance claims as project results without local measurement.
5. Update the verdict when the integrated result materially differs from the validated assumption.

If the final integration fails a validated threshold, roll back or move to the next viable candidate rather than forcing the original choice.

## Phase continuity

Each phase should leave a compact handoff for the next phase:

- Research-only handoff: selected candidate, rejected alternatives, constraints, unknowns, and proposed validation contract
- Feasibility validation handoff: environment, measurements, status, conditions, cleanup state, and integration boundary
- Integration handoff: production changes, preserved tests, measured results, deviations, and rollback path

Do not repeat completed work merely because the task resumed later. Recheck freshness and changed constraints, then continue from the earliest invalidated assumption.

## Evidence rules

- Cite or link every material external claim when the host supports citations or URLs.
- Prefer primary sources; use secondary sources to corroborate or expose caveats.
- Label peer-reviewed, preprint, vendor-reported, independently reproduced, and locally measured evidence accurately.
- Treat popularity as weak supporting evidence, never proof of quality or maturity.
- State assumptions and unknowns instead of inventing missing project facts.
- Respect an explicitly selected method. Flag incompatibilities, but do not silently replace it.

## Stop conditions by phase

### Research-only

Stop when:

- The meaningful candidate classes have been covered
- The recommendation is supported by primary evidence and checked against hard constraints
- The remaining unknowns are clearly identified as feasibility questions
- Additional searching is unlikely to change the shortlist or validation plan

### Feasibility validation

Stop when:

- A hard disqualifier is confirmed, or
- The acceptance thresholds and critical integration assumptions have been resolved, or
- The result is demonstrably inconclusive and the missing evidence is identified

### Integration

Stop when:

- The validated approach is integrated with the smallest sensible surface area
- The relevant project tests or benchmarks pass
- Deviations from the spike are measured and documented
- A rollback path exists where warranted

Three well-verified candidates are better than fifteen shallow candidates. One representative falsifiable spike is better than a polished toy demo.

## Anti-patterns

- Starting implementation before understanding the repository
- Continuing to implementation after the user explicitly requested research-only or validation-only work
- Treating a research verdict as proof of local feasibility
- Treating successful installation, import, or toy output as a feasibility pass
- Letting disposable prototype code silently become production code
- Validating on unrepresentative data, hardware, traffic, or settings
- Treating “highest benchmark number” as “best production choice”
- Calling a method SOTA across different datasets, metrics, or latency regimes
- Selecting by GitHub stars, citations, or brand recognition alone
- Ignoring licenses, data terms, model weights, security, or deployment requirements
- Adding a large dependency for a tiny capability
- Researching indefinitely instead of making a falsifiable decision
- Claiming “nothing exists” after only one search channel
