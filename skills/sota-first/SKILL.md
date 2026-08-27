---
name: sota-first
description: Use an evidence-backed expert-council workflow to investigate how leading companies, recognized practitioners, open-source ecosystems, standards bodies, and current academic work solve a non-trivial capability; decompose the problem, build and deeply analyze candidate methods, synthesize multiple end-to-end architectures, review architecture and system compatibility, review concrete implementation and resource feasibility, validate the selected design locally, and optionally integrate it. Trigger for research-only comparisons, best/SOTA requests, unfamiliar domains, architecture choices, major dependencies, ML/CV/agent methods, distributed systems, and performance-, reliability-, privacy-, or security-sensitive work. Do not trigger for trivial edits, established local fixes, pure refactors, or an explicitly fixed implementation with no material compatibility uncertainty.
---

# SOTA First

Use a staged expert council to decide how a non-trivial capability should be built before substantial production code is written.

Keep these conclusions separate:

1. **Research SOTA** — the strongest credible current method under a comparable task and evaluation setting.
2. **Industry practice** — publicly disclosed methods used by relevant leading companies, category leaders, open-source maintainers, standards groups, or recognized practitioners.
3. **Domain analysis** — the real operating assumptions, mechanisms, tradeoffs, and implementation variants of each serious candidate.
4. **Architecture compatibility** — which end-to-end system shape best fits this repository's boundaries, contracts, topology, failure model, security model, ownership, and evolution path.
5. **Engineering readiness** — whether the concrete implementation bundle is buildable, version-compatible, deployable, operable, and plausible within latency, compute, memory, storage, network, budget, and team constraints.
6. **Local feasibility** — whether the reviewed design measurably satisfies representative project thresholds.

A winner in one category is not automatically the winner in another.

## Operating model

This skill separates **research depth** from **delivery endpoint**.

### Research depth

- **Skip** — no external selection or compatibility work is needed.
- **Quick mode** — compact repository inspection, focused search, one or two serious candidates, and a lightweight engineering sanity check.
- **Full mode** — broad landscape investigation, domain-specialist analysis, multiple candidate architectures, architecture review, engineering review, and explicit gates.

### Delivery endpoint

- **Research-only** — investigate, analyze, synthesize, review, and recommend; do not run a feasibility spike or modify production state.
- **Feasibility validation** — continue through architecture and engineering review, then run an isolated representative spike; do not integrate production code.
- **Integration** — continue through every required gate and promote the validated design into the real feature.

Stop exactly at the endpoint requested by the user. When the user requests the full pipeline, continue through passing gates without an unnecessary approval pause.

## Expert council

For Full mode, use the role graph in `references/expert-orchestration.md`.

Core roles:

- **Research Director** — frames the decision, decomposes the capability, assigns roles, manages evidence and stop conditions, and reconciles conflicts.
- **Repository Cartographer** — maps the existing architecture, constraints, interfaces, data contracts, runtime, deployment, resources, ownership, and prior attempts.
- **Industry Practice Investigator** — finds publicly disclosed production methods from relevant leading companies, category leaders, startups, maintainers, conferences, and practitioners.
- **Academic Frontier Investigator** — finds current papers, surveys, benchmarks, leaderboards, official implementations, datasets, and reproductions.
- **Ecosystem and Standards Investigator** — finds mature open-source projects, frameworks, protocols, standards, registries, vendor offerings, advisories, and reference architectures.
- **Domain Specialists** — deeply analyze each shortlisted method family or capability, including mechanism, assumptions, inputs, outputs, state, quality, latency, failure modes, maturity, and implementation variants.
- **Solution Architect** — composes compatible capabilities into two to four distinct end-to-end candidate architectures.
- **Architecture Reviewer** — independently compares candidate architectures and runs the Architecture Review Gate.
- **Engineering Reviewer** — evaluates exact implementation bundles, pairwise compatibility, dependency and version constraints, resource allocation, latency budgets, deployment, operability, and integration cost through the Engineering Readiness Gate.
- **Evidence Auditor and Decision Chair** — challenges unsupported claims, resolves contradictions, preserves uncertainty, and selects the recommended architecture without hiding hard blockers behind averages.
- **Feasibility Experimenter** — executes the smallest isolated representative experiment that can falsify the recommendation.
- **Integration Engineer** — implements only the reviewed and validated production boundary.

Prefer distinct subagents or reviewer contexts when the harness provides them. When it does not, run clearly separated role passes and label the mode, such as `same-agent structured review`. Never claim that a human expert or independent subagent participated when one did not.

## Dynamic routing

Do not invoke the full council mechanically for every task.

### Quick mode panel

Normally use:

1. Repository Cartographer
2. One focused Investigator
3. A compact Domain and Engineering sanity check
4. Research Director decision

Escalate to Full mode when architecture, resource, security, or compatibility uncertainty emerges.

### Full mode panel

Normally use:

1. Repository Cartographer
2. Industry, Academic, and Ecosystem Investigators in parallel when possible
3. Domain Specialists for serious solution families
4. Solution Architect
5. Architecture Reviewer and Engineering Reviewer, preferably as independent parallel reviewers
6. Evidence Auditor and Decision Chair
7. Feasibility Experimenter and Integration Engineer only when requested

Add security, privacy, operations, cost, hardware, or data specialists only when the risk justifies them.

## Boundaries

### Research-only boundary

Allowed:

- Read-only repository inspection
- External search
- Candidate analysis
- Architecture sketches and scorecards
- Engineering estimates and compatibility matrices
- A proposed validation contract

Not allowed:

- Production code edits
- Persistent dependency installation
- Manifest, lockfile, migration, infrastructure, or persistent configuration changes
- A feasibility spike unless separately requested

### Feasibility boundary

A spike may execute code and create temporary artifacts, but keep it isolated from production behavior and persistent project state whenever practical. Prefer a temporary directory, worktree, throwaway branch, untracked experiment, or shadow path. Record versions, commands, results, and cleanup.

A successful install, import, toy demo, architecture score, or published benchmark is not a local feasibility pass.

### Integration boundary

Production integration requires every applicable gate to permit it:

- Architecture Review Gate: **PASS** or an accepted **CONDITIONAL PASS**
- Engineering Readiness Gate: **PASS** or an accepted **CONDITIONAL PASS**
- Feasibility Gate when material uncertainty remains: **PASS** or an accepted **CONDITIONAL PASS**

A **FAIL** blocks the candidate. Material **INCONCLUSIVE** blocks Integration until resolved or explicitly shown to be non-material.

## Full workflow

# Phase 0: Frame the decision

## 1. Inspect the repository

Read applicable instructions and inspect the relevant subset of:

- `AGENTS.md`, README files, ADRs, design documents, manifests, lockfiles, schemas, tests, deployment files, operational docs, and history
- Existing implementations, abstractions, dependencies, experiments, TODOs, and abandoned attempts
- Languages, frameworks, runtimes, package managers, services, models, data stores, protocols, drivers, hardware, and deployment targets
- Component boundaries, interfaces, data contracts, state ownership, data and control flow, failure domains, security boundaries, observability, and ownership
- Latency, throughput, quality, memory, compute, storage, network, availability, privacy, license, budget, maintenance, migration, rollback, and delivery constraints

Prefer **KEEP** when the repository already contains a suitable maintained solution.

## 2. Decompose the capability

Create a capability graph before searching for implementations.

Identify:

- User-visible outcome
- Functional sub-capabilities
- Cross-cutting requirements
- Inputs, outputs, state, and contracts
- End-to-end success metrics
- Hard constraints and disqualifiers
- Which decisions are algorithmic, architectural, engineering, operational, or policy-related
- Which unknowns require external evidence, expert analysis, architecture review, engineering review, or local measurement

Do not search against a vague feature name.

# Phase A: Broad investigation

## 3. Search the solution landscape

Use `references/search-playbook.md`.

Search broadly before narrowing:

- How relevant leading companies and category leaders publicly describe similar systems
- Public engineering blogs, conference talks, system papers, open-source repositories, reference architectures, case studies, and postmortems
- Current academic surveys, papers, benchmarks, leaderboards, official code, datasets, and independent reproductions
- Mature open-source ecosystems, package registries, standards, protocols, vendor products, advisories, and migration reports
- Negative evidence, failed approaches, operational pain, abandoned projects, and known limitations

Do not infer a private company architecture from marketing, hiring posts, or indirect stack signals. Label vendor-reported, company-reported, peer-reviewed, independently reproduced, community-reported, and locally measured evidence accurately.

The broad phase should produce a **solution landscape**, not merely a list of repositories.

## 4. Cluster candidates

Use `references/scoring-rubric.md` to shortlist families without collapsing research strength, public practice, ecosystem maturity, and predicted project fit into one opaque score.

Group findings into distinct solution families and implementation variants.

Aim to cover the meaningful families, then shortlist two to four serious candidates or candidate families for deep analysis. Explain when the landscape genuinely contains fewer.

# Phase A2: Domain-specialist analysis

## 5. Produce candidate dossiers

Use `references/domain-analysis.md`.

Assign a Domain Specialist to each serious family or capability when practical. Each dossier must cover:

- Problem formulation and mechanism
- Required inputs, outputs, state, calibration, data, services, and assumptions
- Quality and performance evidence under comparable conditions
- Failure modes and operating envelope
- Publicly disclosed adopters or expert endorsements, with source quality labels
- Academic evidence and reproducibility
- Concrete implementations, versions, checkpoints, licenses, and maintenance
- Runtime, hardware, dependency, and deployment implications
- Interface and composition requirements
- Unknowns and falsifiable risks

The Domain Specialist analyzes detail; it does not choose the final system architecture alone.

## 6. Audit the evidence

The Evidence Auditor checks:

- Source authority and freshness
- Benchmark comparability
- Whether public company claims are actually disclosed and technically specific
- Whether implementation and paper behavior match
- Conflicting evidence and missing negative evidence
- Claims that are estimates rather than local facts

Lower confidence rather than filling gaps with plausible-sounding assumptions.

# Phase A3: Architecture synthesis

## 7. Build candidate architectures

Use `references/architecture-synthesis.md`.

The Solution Architect composes compatible capabilities and implementations into two to four end-to-end architectures. Each option must specify:

- Components and exact candidate implementations where known
- Responsibilities and ownership
- APIs, schemas, events, protocols, data formats, and state
- Data and control flow
- Process, service, edge, cloud, GPU, and storage placement
- Concurrency, queues, caching, retries, timeouts, cancellation, and backpressure
- Failure isolation and degraded behavior
- Security and privacy boundaries
- Observability and operational ownership
- Preliminary latency and resource budgets
- Migration, rollout, and rollback
- Which capabilities are reused, extended, composed, or built

Do not create a “best-of-every-benchmark” Frankenstein design whose interfaces, runtimes, budgets, or operating assumptions conflict.

# Phase A4: Comparative architecture review

## 8. Run the Architecture Review Gate

Use `references/architecture-review.md`.

Prefer a dedicated Architecture Reviewer that did not author the options. Compare the candidate architectures, not just a single favored design.

The review must produce:

- Reviewer mode
- Hard blockers for each option
- Per-dimension 1–5 scores and a weighted 0–100 compatibility score
- Strongest compatibility argument and strongest objection
- **PASS**, **CONDITIONAL PASS**, **FAIL**, or **INCONCLUSIVE**
- Required redesign or conditions
- The architecture option that should proceed to engineering review, or a request for another synthesis round

A score cannot override a hard blocker.

# Phase A5: Engineering readiness review

## 9. Select concrete implementation bundles

For each architecture still under consideration, identify the concrete implementation bundle:

- Libraries, frameworks, models, checkpoints, services, protocols, and versions
- Language, runtime, compiler, driver, CUDA, operating-system, and hardware requirements
- Data formats, tensor layouts, schemas, serialization, and transport
- Build, packaging, deployment, configuration, observability, and testing path

## 10. Run the Engineering Readiness Gate

Use `references/engineering-review.md`.

The Engineering Reviewer must produce:

- Pairwise component compatibility matrix
- Dependency, version, runtime, ABI, driver, and platform analysis
- End-to-end latency budget and critical path
- CPU, GPU, VRAM, RAM, storage, network, startup, and concurrency budget with explicit headroom
- Resource placement and contention analysis
- Build, deploy, test, monitor, migrate, and rollback plan
- Supply-chain, license, service, and operational constraints
- Integration effort and ownership
- Hard blockers, per-dimension scores, and **PASS**, **CONDITIONAL PASS**, **FAIL**, or **INCONCLUSIVE**

Engineering review predicts buildability. It does not replace representative local validation.

## 11. Iterate once when useful

If the Architecture Reviewer or Engineering Reviewer finds bounded problems, the Solution Architect may revise the options once and rerun only the affected review dimensions. Avoid endless design loops. If no option passes, revisit the shortlist or choose **BUILD** with a narrowly defined custom boundary.

# Phase A6: Decision

## 12. Produce the decision record

Use the relevant templates in `references/verdict-template.md`.

Keep separate:

- Research SOTA
- Public industry practice
- Domain-specialist conclusions
- Architecture comparison
- Engineering readiness
- Recommended end-to-end architecture
- Exact implementation bundle
- Rejected options and reasons
- Confidence and missing evidence
- Conditions to validate
- Smallest production boundary

Use one implementation strategy:

- **KEEP**
- **ADOPT**
- **EXTEND**
- **COMPOSE**
- **BUILD**

Do not collapse research, architecture, and engineering scores into one opaque average. Hard blockers and gate outcomes remain authoritative.

If the endpoint is Research-only, stop here.

# Phase B: Feasibility validation

## 13. Define a falsifiable validation contract

Use `references/feasibility-playbook.md`.

Transfer architecture and engineering conditions into measurable acceptance criteria. Specify:

- Candidate architecture and exact implementation bundle
- Repository revision and environment
- Highest-risk assumptions
- Representative inputs, traffic, hardware, runtime, and deployment conditions
- Quality, latency, throughput, resource, compatibility, failure, security, and integration thresholds
- Hard failure conditions
- Isolation and cleanup plan
- The smallest experiment that can reverse the decision

## 14. Run the isolated spike

Test the highest-risk unknown first. Record raw measurements and distinguish them from external claims.

Assign exactly one feasibility status:

- **PASS**
- **CONDITIONAL PASS**
- **FAIL**
- **INCONCLUSIVE**

If the spike changes boundaries, contracts, implementations, topology, ownership, or resource assumptions, rerun affected architecture and engineering review dimensions.

If the endpoint is Feasibility validation, stop here.

# Phase C: Integration

## 15. Promote cleanly

Enter Integration only when requested and allowed by every required gate.

- Recreate the smallest maintainable production implementation; do not blindly copy spike code.
- Preserve reviewed boundaries, contracts, resource budgets, failure isolation, security conditions, ownership, and rollback.
- Reuse mature delegated capability instead of rebuilding it.
- Avoid speculative wrappers, duplicate dependencies, hard-coded experiment settings, and unrelated refactors.
- Add contract checks, architecture tests, benchmarks, resource guards, integration tests, and observability that preserve the reasons the design passed.
- Verify the final integrated path under representative conditions.
- Re-review any material deviation.

## Phase continuity

Each phase leaves a compact handoff:

- Repository brief
- Solution landscape
- Candidate dossiers
- Candidate architecture set
- Architecture review
- Engineering readiness review
- Decision record
- Feasibility verdict
- Integration result

Reuse prior handoffs when their repository revision, versions, constraints, evidence date, and assumptions remain current. Refresh only invalidated parts.

## Evidence rules

- Cite or link material external claims when the host supports it.
- Prefer primary and authoritative sources.
- Search for contrary and negative evidence.
- Treat popularity, citations, company size, and brand recognition as weak signals, not proof.
- Do not claim that a company uses an undisclosed internal method.
- Do not treat academic SOTA as production maturity.
- Do not treat public production adoption as task-optimal for this repository.
- Separate external claims, expert analysis, engineering estimates, and local measurements.
- State unavailable channels and unresolved uncertainty.

## Stop conditions

Stop research when:

- The meaningful solution families have been covered
- Serious candidates have primary evidence
- Domain assumptions and cross-component constraints are understood
- Candidate architectures are sufficiently distinct
- Architecture and engineering reviews can discriminate among them
- Additional searching is unlikely to change the shortlist or validation plan

Three deeply verified families are better than fifteen shallow links. Two coherent end-to-end architectures are better than a pile of individually strong but incompatible components.

## Anti-patterns

- Searching only for “best library” or “latest paper”
- Choosing a candidate before mapping the solution landscape
- Treating a major-company implementation as universally optimal
- Inventing private implementation details
- Letting one generic agent summarize every domain without deep analysis
- Asking an architect to score an undefined integration
- Reviewing only the favored architecture
- Combining individually strong components without checking contracts, runtimes, and budgets
- Ignoring version, driver, ABI, license, resource, or deployment conflicts
- Averaging away a hard blocker
- Treating engineering estimates as local measurements
- Treating a toy demo as a feasibility pass
- Continuing beyond the user-requested endpoint
