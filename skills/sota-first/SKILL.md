---
name: sota-first
description: Research, compare, architecture-review, validate feasibility, and optionally integrate current state-of-the-art and production-mature approaches for a non-trivial feature, algorithm, dependency, integration, or architecture change. Trigger for research-only comparisons, architecture and system-compatibility reviews, feasibility spikes, research-then-implement requests, best/SOTA requests, unfamiliar domains, new dependencies, ML/CV/agent methods, and performance-, reliability-, privacy-, or security-sensitive work. Do not trigger for trivial edits, local bug fixes with a known cause, pure refactors, or implementation of an explicitly fixed method unless architecture compatibility or prior feasibility remains uncertain.
---

# SOTA First

Choose, architecture-review, and validate an evidence-backed approach that fits the current repository before writing substantial production code. Keep these questions separate:

1. **Research SOTA:** What approach has the strongest credible results for the defined task?
2. **Engineering recommendation:** What approach is the best practical fit for this project's constraints today?
3. **Architecture compatibility:** Can the candidate fit the existing component boundaries, interfaces, data contracts, runtime, deployment topology, failure model, security boundaries, ownership, and evolution path?
4. **Local feasibility:** Does the reviewed candidate measurably work under representative project conditions?

These may have different answers. A research winner is not automatically the best engineering choice, a promising engineering choice can fail architecture review, and a clean architecture can still fail local feasibility.

## Core model

This skill separates **research depth** from **delivery phase** and applies an **Architecture Review Gate** when system structure is materially affected.

### Research depth

- **Skip** — no external selection work is needed
- **Quick mode** — compact repository check and targeted evidence review
- **Full mode** — complete repository, evidence, comparison, architecture, and risk analysis

### Delivery phase

- **Research-only** — search, compare, architecture-review when relevant, and recommend without running a feasibility spike or implementing
- **Feasibility validation** — test an architecture-reviewed candidate in an isolated, disposable way without integrating it into production
- **Integration** — promote a reviewed and validated approach into the real feature, with tests and rollback awareness

These axes are independent. A narrow task can use Quick mode and stop at Research-only. A high-risk ML or infrastructure task can use Full mode, pass the Architecture Review Gate, continue through Feasibility validation, and then enter Integration.

### When architecture review is required

Run an Architecture Review Gate when the candidate materially changes any of these:

- Component, module, service, process, or ownership boundaries
- APIs, schemas, protocols, events, state ownership, or data contracts
- A major dependency, runtime, framework, service, data store, model-serving path, or hardware requirement
- Deployment topology, network paths, scaling, consistency, availability, or failure domains
- Security, privacy, tenancy, compliance, or data-residency boundaries
- Migration, rollback, observability, operational ownership, or long-term maintainability

Architecture review is normally required for Full-mode Integration and for architecture-sensitive Research-only or Feasibility validation requests. It may be a compact precheck for low-risk Quick-mode work.

## Respect the requested endpoint

Infer the endpoint from the user's request and stop exactly there.

| User intent | Required endpoint | Production writes |
|---|---|---|
| “Research/compare/recommend only,” “architecture-review only,” or “do not implement” | Research-only, including the Architecture Review Gate when relevant | No |
| “Check feasibility,” “run a spike/prototype,” or “do not integrate yet” | Architecture review plus Feasibility validation | Only isolated disposable experiment artifacts |
| “Research, validate, and implement if viable” | Architecture review, validation, then Integration after passing gates | Yes, only after the required gates |
| “Implement the best/mature option” | Research and review proportional to risk, validation where material, then Integration | Yes, after the required gates |

When the user already requested the full pipeline, continue through research, architecture review, validation, and integration without an unnecessary approval checkpoint. When the user requested only research, architecture review, or validation, do not silently continue into the next phase.

A later request may resume from a prior phase. Reuse an earlier research verdict, architecture review, or feasibility result when its repository assumptions, architecture, versions, constraints, and evidence are still current; otherwise refresh only the invalidated parts.

## Operating boundaries

### Research-only boundary

Do not edit production code, manifests, lockfiles, infrastructure, migrations, or persistent configuration. Use read-only repository inspection and external research. Do not install dependencies persistently merely to support a search-only or architecture-review-only conclusion.

### Architecture review boundary

Architecture review may inspect code, dependency graphs, interfaces, schemas, deployment files, ADRs, and history. It may produce a proposed integration sketch and scorecard, but it does not authorize production changes by itself.

Prefer a dedicated architect agent, architecture subagent, or separate reviewer context when available. Otherwise perform a distinct second-pass review and label it `same-agent structured review`. Never claim independent expert review when no separate reviewer was used.

### Feasibility validation boundary

A feasibility spike may execute code, install temporary dependencies, or create disposable artifacts, but it must remain isolated from production behavior and persistent project state whenever practical. Prefer a temporary directory, worktree, throwaway branch, untracked spike, or clearly isolated experiment path. Record and clean up temporary changes.

Do not present a toy demo, successful import, paper benchmark, or architecture score as proof that the candidate meets the project's runtime constraints.

### Integration boundary

Enter production integration only when every required gate permits it.

Architecture gate statuses:

- **PASS** — architecture-compatible; continue when the requested endpoint allows it
- **CONDITIONAL PASS** — continue only with explicit architectural conditions transferred into validation and implementation
- **FAIL** — redesign or select another candidate
- **INCONCLUSIVE** — obtain the missing architecture evidence before Integration

Feasibility gate statuses:

- **PASS** — continue when Integration was requested
- **CONDITIONAL PASS** — continue only if the explicit conditions fit the stated constraints and requested scope
- **FAIL** — do not integrate; test the next justified finalist or revise the recommendation
- **INCONCLUSIVE** — do not treat uncertainty as success; resolve the material unknown or explain why it remains

For **Full mode**, do not edit production code, manifests, lockfiles, infrastructure, migrations, or persistent configuration until a research verdict and any required Architecture Review Gate exist. If material feasibility risk remains, do not integrate until a feasibility verdict also exists.

## Decide the research depth

### Skip

Do not run this workflow for:

- Typos, copy changes, formatting, or mechanical renames
- A localized bug whose cause and correction are already established
- Pure refactoring with no behavior, dependency, architecture, or compatibility choice
- Tests or documentation for an already-selected implementation
- A user-mandated method with no material architecture or feasibility uncertainty

### Quick mode

Use a compact repository check and a short verdict when the choice is common, low-risk, reversible, and limited in scope. Examples include a small utility, a narrow development dependency, or a standard integration with no architecture impact.

Quick mode can stop at Research-only, run a compact architecture precheck, run a small Feasibility validation, or continue to Integration depending on the requested endpoint and impact.

### Full mode

Use the complete workflow when any of these apply:

- The user asks for the best, latest, mature, established, benchmark-leading, or SOTA method
- The task adds a major dependency, service, data store, protocol, model, framework, runtime, or deployment component
- The task involves ML, computer vision, agents, retrieval, optimization, security, privacy, distributed systems, reliability, or performance-critical behavior
- The decision changes architecture, interfaces, data contracts, deployment, hardware needs, failure domains, or long-term maintenance
- The domain is unfamiliar or several credible approaches likely exist
- A wrong choice would be expensive to reverse

When uncertain between Quick and Full, use Full.

# Phase A: Research and selection

## 1. Inspect the repository first

Before external research:

1. Read applicable `AGENTS.md` files and repository instructions.
2. Inspect README files, architecture docs, ADRs, manifests, lockfiles, configuration, tests, deployment files, schemas, and operational docs.
3. Search for existing implementations, abstractions, dependencies, experiments, and abandoned attempts related to the task.
4. Identify the current language, framework, runtime, package manager, deployment target, hardware, data flow, component boundaries, and testing conventions.
5. Extract explicit and implicit constraints: latency, throughput, quality, memory, compute, privacy, offline behavior, license, budget, reliability, maintainability, ownership, migration, and delivery scope.

Prefer **KEEP** when the repository already contains a suitable maintained solution. Do not introduce an external dependency merely because it is newer.

## 2. Frame the decision

Write down, at least internally:

- The exact capability being selected
- Success metrics and acceptance criteria
- Hard constraints and soft preferences
- The evidence cutoff or research date
- What would disqualify a candidate
- Whether the task is engineering selection, research-method selection, architecture selection, or a combination
- Which compatibility claims require architecture review
- Which unknowns require local feasibility evidence rather than literature or documentation alone

Do not compare methods against a vague task. For benchmark claims, ensure the task, dataset, metric, split, and operating conditions are comparable.

## 3. Research through available channels

Use the most authoritative current sources available. Search in this order when relevant:

1. Existing repository code and history
2. Official specifications, documentation, release notes, security advisories, and package registries
3. Original papers, official project pages, official repositories, benchmark or leaderboard maintainers
4. Independent reproductions, reputable engineering reports, architecture case studies, and issue trackers
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
- Compatibility with the repository's stack, interfaces, deployment, and constraints
- Migration, rollback, observability, operational ownership, and failure behavior

Record exact dates or versions for time-sensitive claims. Never call something “current SOTA” based on a single secondary article, incomparable benchmark, repository stars, or an undated result.

If a search channel is unavailable, say so in the verdict and reduce confidence. Do not imply exhaustive coverage.

## 5. Evaluate candidates without collapsing distinct concerns

Use `references/scoring-rubric.md` for Full mode.

Evaluate separately:

- **Research strength:** result quality, benchmark comparability, evidence quality, reproducibility, and freshness
- **Predicted project fit:** constraint fit, maturity, integration cost, runtime/operations, security/license, and reversibility
- **Architecture compatibility:** a separate expert score and gate based on the proposed integration design

Do not hide uncertainty behind a single numeric total. A score must be supported by concrete evidence. Apply hard disqualifiers before ranking.

## 6. Produce the research verdict

Use one of these decisions:

- **KEEP** — the existing project solution is already the best fit
- **ADOPT** — use an established solution substantially as-is
- **EXTEND** — use an established foundation with a thin project-specific layer
- **COMPOSE** — combine a small number of complementary mature components
- **BUILD** — implement a focused custom solution because no candidate satisfies the constraints

The verdict must distinguish the research winner from the engineering recommendation, explain rejected finalists, state confidence and missing evidence, define the smallest sensible implementation boundary, and list the assumptions that require architecture review or feasibility validation.

Use the relevant template in `references/verdict-template.md`.

# Phase A2: Architecture expert review

## 7. Prepare the proposed integration architecture

Before scoring, describe the smallest plausible production design for the recommended candidate. Include the relevant component boundaries, responsibilities, interfaces, schemas, state ownership, dependencies, runtime, data and control flow, deployment topology, failure domains, trust boundaries, observability, migration, and rollback.

Do not ask an architect to score an undefined statement such as “use candidate X.”

## 8. Run the Architecture Review Gate

Use `references/architecture-review.md`.

When the host supports it, invoke a dedicated architect agent or subagent as an adversarial reviewer. Give it repository evidence, constraints, candidate facts, and the proposed design, and ask it to identify broken invariants, coupling, ownership gaps, compatibility risks, and a simpler alternative. When no separate reviewer exists, perform the same checklist as a clearly labeled second pass.

The review must produce:

- Reviewer mode
- A 0–100 weighted architecture compatibility score with per-dimension 1–5 ratings
- Hard blockers checked
- Strongest compatibility argument and strongest objection
- **PASS**, **CONDITIONAL PASS**, **FAIL**, or **INCONCLUSIVE**
- Conditions that must enter the feasibility contract or production acceptance criteria
- Any change to the engineering recommendation

If the candidate receives **FAIL**, redesign it or review the next justified finalist. If material **INCONCLUSIVE** remains, do not enter Integration. A **CONDITIONAL PASS** may proceed only with explicit bounded conditions.

If the requested endpoint is Research-only, stop after the research verdict and any required architecture review. Do not run a spike or implement.

# Phase B: Feasibility validation

Use `references/feasibility-playbook.md` whenever material project-specific uncertainty remains or the user explicitly requests a feasibility check, spike, prototype, benchmark, or proof of concept.

## 9. Define a falsifiable validation contract

Before building the spike, specify:

- The selected candidate and exact version, checkpoint, service tier, or commit
- The architecture gate status and conditions
- The assumptions and highest-risk unknowns being tested
- Representative data, traffic, hardware, runtime, and operating conditions
- Measurable acceptance thresholds
- Hard failure conditions
- The smallest experiment capable of changing the decision
- The isolation and cleanup plan

Transfer architecture conditions into measurable tests whenever possible. Test the highest-risk unknown first.

## 10. Run an isolated representative spike

Prefer read-only capability probes first, then a temporary script or environment, then an isolated worktree or experiment path only when needed.

Measure the relevant subset of:

- Quality or task success on representative project inputs
- End-to-end latency, throughput, warm-up, startup, and streaming behavior
- Peak and steady-state CPU, GPU memory, RAM, storage, and network use
- Runtime, framework, API, schema, data-contract, dependency, and deployment compatibility
- Failure handling, retries, cancellation, backpressure, observability, migration, and rollback
- Security, privacy, service, license, checkpoint, and operational constraints
- The actual size, coupling, and ownership of the required project-specific adapter

Record the repository revision, environment, versions, configuration, commands, raw results, and differences from published conditions. Keep external claims separate from locally measured results.

## 11. Produce the feasibility verdict

Assign exactly one status:

- **PASS** — hard thresholds and critical integration assumptions were verified
- **CONDITIONAL PASS** — viable only under explicit bounded conditions
- **FAIL** — a hard threshold or non-negotiable constraint was violated
- **INCONCLUSIVE** — a material uncertainty could not be resolved with the available data, access, tooling, or environment

Use the feasibility template in `references/verdict-template.md`.

If validation changes the proposed boundaries, contracts, dependencies, topology, failure model, or ownership, rerun the affected architecture-review dimensions before Integration.

If the candidate fails, update the research verdict and test the next justified finalist when that is within the requested scope. If the requested endpoint is Feasibility validation, stop here and do not integrate production code.

# Phase C: Integration

Enter this phase only when Integration was requested and every required gate allows it.

## 12. Promote the reviewed and validated approach cleanly

1. Recreate the smallest maintainable production implementation; do not blindly copy experimental code.
2. Preserve the reviewed component boundaries, interfaces, contracts, failure isolation, security boundaries, and ownership model.
3. Reuse the selected library, model, service, protocol, or standard instead of rebuilding delegated capability.
4. Avoid speculative wrappers, dependency duplication, hard-coded experiment settings, and unrelated refactors.
5. Follow repository conventions for versioning, dependency pinning, configuration, observability, deployment, and data contracts.
6. Preserve a reasonable rollout and rollback path for high-impact changes.

## 13. Preserve both architecture and feasibility evidence

1. Add tests, contract checks, architecture tests, benchmarks, or evaluation cases that cover the conditions that established compatibility and feasibility.
2. Verify the integrated path under representative conditions, not only the isolated spike.
3. Report any difference between the reviewed architecture, the spike, and the final implementation.
4. Do not repeat external performance claims as project results without local measurement.
5. Rerun affected architecture dimensions when the final implementation materially differs from the reviewed design.
6. Roll back or move to the next viable candidate when the integrated result violates a gate condition.

## Phase continuity

Each phase should leave a compact handoff for the next phase:

- Research handoff: selected candidate, rejected alternatives, constraints, proposed integration boundary, and unknowns
- Architecture handoff: reviewer mode, proposed design, dimension scores, gate status, blockers, conditions, and validation implications
- Feasibility handoff: environment, measurements, status, conditions, cleanup state, and production boundary
- Integration handoff: production changes, preserved architecture and acceptance tests, measured results, deviations, ownership, and rollback path

Do not repeat completed work merely because the task resumed later. Recheck freshness, repository revision, changed architecture, versions, and constraints, then continue from the earliest invalidated assumption.

## Evidence rules

- Cite or link every material external claim when the host supports citations or URLs.
- Prefer primary sources; use secondary sources to corroborate or expose caveats.
- Label peer-reviewed, preprint, vendor-reported, independently reproduced, architecture-inferred, and locally measured evidence accurately.
- Treat popularity as weak supporting evidence, never proof of quality, maturity, or compatibility.
- State assumptions and unknowns instead of inventing missing project facts.
- Respect an explicitly selected method. Flag incompatibilities, but do not silently replace it.

## Stop conditions by phase

### Research-only

Stop when the meaningful candidate classes are covered, the recommendation is supported by primary evidence, the required Architecture Review Gate is complete, and remaining unknowns are identified as feasibility questions.

### Feasibility validation

Stop when a hard disqualifier is confirmed, the acceptance thresholds and critical assumptions are resolved, or the result is demonstrably inconclusive with the missing evidence identified.

### Integration

Stop when the reviewed design is integrated with the smallest sensible surface area, architecture and feasibility conditions are preserved by tests or checks, representative verification passes, deviations are documented, and a rollback path exists where warranted.

Three well-verified candidates are better than fifteen shallow candidates. One adversarial architecture review and one representative falsifiable spike are better than a polished toy demo.

## Anti-patterns

- Starting implementation before understanding the repository
- Claiming an architecture expert reviewed the design when only the implementing agent did
- Scoring an undefined architecture without component, interface, data-flow, deployment, and ownership details
- Averaging away a hard architecture blocker with a high research score
- Continuing after the user explicitly requested research-only, architecture-review-only, or validation-only work
- Treating a research verdict or architecture score as proof of local feasibility
- Treating successful installation, import, or toy output as a feasibility pass
- Letting disposable prototype code silently become production code
- Validating on unrepresentative data, hardware, traffic, or settings
- Treating “highest benchmark number” as “best production choice”
- Selecting by GitHub stars, citations, or brand recognition alone
- Ignoring interfaces, contracts, ownership, failure domains, licenses, data terms, security, or deployment requirements
- Adding a large dependency for a tiny capability
- Researching indefinitely instead of making a falsifiable decision
- Claiming “nothing exists” after only one search channel
