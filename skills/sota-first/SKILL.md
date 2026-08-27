---
name: sota-first
description: Research and compare current state-of-the-art and production-mature approaches before implementing a non-trivial feature, algorithm, dependency, integration, or architecture change. Trigger for best/SOTA requests, unfamiliar domains, new dependencies, ML/CV/agent methods, performance- or security-sensitive work, and tasks where established alternatives likely exist. Do not trigger for trivial edits, local bug fixes with a known cause, pure refactors, or implementation of an explicitly fixed method unless compatibility is uncertain.
---

# SOTA First

Choose an evidence-backed approach that fits the current repository before writing substantial implementation code. Keep these two questions separate:

1. **Research SOTA:** What approach has the strongest credible results for the defined task?
2. **Engineering recommendation:** What approach is the best fit for this project’s constraints today?

They may have different answers.

## Operating rule

For **Full mode**, do not edit production code, manifests, lockfiles, infrastructure, or persistent configuration until a research verdict exists. Read-only inspection, external research, and disposable experiments are allowed.

When the user requested implementation, continue into implementation immediately after the verdict. Do not turn the verdict into an unnecessary approval checkpoint. Ask only when a genuinely unresolved choice would materially change the result or when the action itself requires confirmation.

## Decide the mode

### Skip

Do not run this workflow for:

- Typos, copy changes, formatting, or mechanical renames
- A localized bug whose cause and correction are already established
- Pure refactoring with no behavior, dependency, or architecture choice
- Tests or documentation for an already-selected implementation
- A user-mandated method with no material compatibility uncertainty

### Quick mode

Use a compact repository check and a short verdict when the choice is common, low-risk, reversible, and limited in scope. Examples include a small utility, a narrow development dependency, or a standard integration with no architecture impact.

### Full mode

Use the complete workflow when any of these apply:

- The user asks for the best, latest, mature, established, benchmark-leading, or SOTA method
- The task adds a major dependency, service, data store, protocol, model, or framework
- The task involves ML, computer vision, agents, retrieval, optimization, security, privacy, distributed systems, or performance-critical behavior
- The decision changes architecture, data contracts, deployment, hardware needs, or long-term maintenance
- The domain is unfamiliar or several credible approaches likely exist
- A wrong choice would be expensive to reverse

When uncertain between Quick and Full, use Full.

## Workflow

### 1. Inspect the repository first

Before external research:

1. Read applicable `AGENTS.md` files and repository instructions.
2. Inspect README files, architecture docs, manifests, lockfiles, configuration, tests, and deployment files.
3. Search for existing implementations, abstractions, dependencies, experiments, and abandoned attempts related to the task.
4. Identify the current language, framework, runtime, package manager, deployment target, hardware, data flow, and testing conventions.
5. Extract explicit and implicit constraints: latency, throughput, quality, memory, compute, privacy, offline behavior, license, budget, maintainability, and delivery scope.

Prefer **KEEP** when the repository already contains a suitable maintained solution. Do not introduce an external dependency merely because it is newer.

### 2. Frame the decision

Write down, at least internally:

- The exact capability being selected
- Success metrics and acceptance criteria
- Hard constraints and soft preferences
- The evidence cutoff or research date
- What would disqualify a candidate
- Whether the task is engineering selection, research-method selection, architecture selection, or a combination

Do not compare methods against a vague task. For benchmark claims, ensure the task, dataset, metric, split, and operating conditions are comparable.

### 3. Research through available channels

Use the most authoritative current sources available. Search in this order when relevant:

1. Existing repository code and history
2. Official specifications, documentation, release notes, security advisories, and package registries
3. Original papers, official project pages, official repositories, benchmark or leaderboard maintainers
4. Independent reproductions, reputable engineering reports, and issue trackers
5. Community discussions only for operational caveats, not as the sole basis for core claims

For Full mode, inspect the detailed playbook in `references/search-playbook.md`.

Search enough to identify the serious candidate classes, then verify the strongest two to four candidates. Do not collect a long list of near-duplicates.

### 4. Check evidence and freshness

For every finalist, verify the relevant subset of:

- Current version, release date, maintenance activity, and API stability
- Original source for performance or quality claims
- Official implementation or a credible reproduction
- Runtime, hardware, memory, data, calibration, and deployment requirements
- License, model/data terms, security posture, and known critical issues
- Compatibility with the repository’s stack and constraints
- Migration, rollback, observability, and operational burden

Record exact dates or versions for time-sensitive claims. Never call something “current SOTA” based on a single secondary article, incomparable benchmark, repository stars, or an undated result.

If a search channel is unavailable, say so in the verdict and reduce confidence. Do not imply exhaustive coverage.

### 5. Evaluate candidates on two axes

Use `references/scoring-rubric.md` for Full mode.

Evaluate separately:

- **Research strength:** result quality, benchmark comparability, evidence quality, reproducibility, and freshness
- **Project fit:** constraint fit, maturity, maintainability, integration cost, runtime/operations, security/license, and reversibility

Do not hide uncertainty behind a numeric total. A score must be supported by concrete evidence. Omit a total when evidence is not comparable.

Apply hard disqualifiers before ranking. Typical disqualifiers include incompatible licensing, impossible compute or latency requirements, known unresolved critical vulnerabilities, abandoned maintenance with no safe fork, or a benchmark that does not represent the actual task.

### 6. Produce the research verdict

Use one of these decisions:

- **KEEP** — the existing project solution is already the best fit
- **ADOPT** — use an established solution substantially as-is
- **EXTEND** — use an established foundation with a thin project-specific layer
- **COMPOSE** — combine a small number of complementary mature components
- **BUILD** — implement a focused custom solution because no candidate satisfies the constraints

The verdict must distinguish the research winner from the engineering recommendation, explain rejected finalists, state confidence and missing evidence, and define the smallest sensible implementation boundary.

Use the Full or Quick template in `references/verdict-template.md`.

### 7. Implement minimally and verify locally

After the verdict:

1. Implement the selected decision with the smallest maintainable surface area.
2. Avoid speculative wrappers, dependency duplication, and unrelated refactors.
3. Follow repository conventions for versioning and dependency pinning.
4. Add tests, benchmarks, or evaluation cases that validate the reason the candidate was selected.
5. Verify locally that integration assumptions hold. Do not repeat external performance claims as project results without measurement.
6. Preserve a reasonable rollback path for high-impact changes.

If the selected candidate fails a local spike, update the verdict and move to the next viable candidate rather than forcing the original choice.

## Evidence rules

- Cite or link every material external claim when the host supports citations or URLs.
- Prefer primary sources; use secondary sources to corroborate or expose caveats.
- Label peer-reviewed, preprint, vendor-reported, and community-reported evidence accurately.
- Treat popularity as weak supporting evidence, never proof of quality or maturity.
- State assumptions and unknowns instead of inventing missing project facts.
- Respect an explicitly selected method. Flag incompatibilities, but do not silently replace it.

## Stop conditions

Stop researching when:

- The meaningful candidate classes have been covered
- The leading recommendation is supported by primary evidence and fits all hard constraints
- Additional searching is unlikely to change the decision

Three well-verified candidates are better than fifteen shallow candidates. When no mature option passes the constraints, choose **BUILD** and use the research to define the custom implementation boundary.

## Anti-patterns

- Starting implementation before understanding the repository
- Treating “highest benchmark number” as “best production choice”
- Calling a method SOTA across different datasets, metrics, or latency regimes
- Selecting by GitHub stars, citations, or brand recognition alone
- Ignoring licenses, data terms, model weights, security, or deployment requirements
- Adding a large dependency for a tiny capability
- Researching indefinitely instead of making a falsifiable decision
- Claiming “nothing exists” after only one search channel
