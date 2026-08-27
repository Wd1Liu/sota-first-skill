# Expert Council Orchestration

Use this reference in Full mode and whenever the user explicitly asks for multiple expert perspectives.

The council is a set of logical roles. Prefer separate subagents or reviewer contexts when available, but preserve the same role boundaries in a single-agent environment. Report the actual reviewer mode honestly.

## 1. Research Director

The Research Director owns the decision process, not the technical conclusion.

Responsibilities:

- Translate the user request into a precise decision and delivery endpoint
- Build the capability graph and identify cross-cutting concerns
- Assign investigator and specialist roles
- Prevent duplicated search and uncontrolled agent proliferation
- Maintain the evidence ledger, open questions, hard constraints, and stop conditions
- Reconcile conflicting reports without erasing disagreement
- Decide which candidate families reach architecture synthesis
- Enforce Research-only, Feasibility validation, and Integration boundaries

The Research Director must not silently choose a favorite before the evidence and reviews exist.

## 2. Repository Cartographer

The Repository Cartographer produces the internal system brief.

Minimum output:

```markdown
## Repository constraint brief

- Revision and scope:
- Existing architecture:
- Components and ownership:
- Interfaces and data contracts:
- State and persistence:
- Runtime, dependencies, and versions:
- Deployment topology:
- Hardware and resource constraints:
- Failure, security, privacy, and compliance boundaries:
- Observability and operations:
- Migration and rollback constraints:
- Relevant existing implementations and abandoned attempts:
- Unknowns:
```

Repository evidence overrides generic assumptions about how a project “usually” works.

## 3. Investigator lanes

Run these lanes in parallel when possible.

### Industry Practice Investigator

Goal: identify publicly disclosed production methods used by relevant leading companies, category leaders, high-signal startups, maintainers, conference speakers, and recognized practitioners.

Strong evidence includes:

- Official engineering blogs and architecture documentation
- Conference talks and system-design presentations
- Company-authored or jointly authored system papers
- Official open-source repositories and reference implementations
- Public postmortems, migration reports, and operational case studies
- Primary interviews or technical writeups with enough implementation detail

Rules:

- Record the company or practitioner, source, date, system scale, and disclosed method
- Label company-reported and vendor-sponsored evidence
- Do not infer private internals from product marketing, job listings, package telemetry, or indirect stack signals
- Explain when a production design is optimized for a scale, organization, or infrastructure unlike this project

### Academic Frontier Investigator

Goal: map the current research frontier and the evidence behind it.

Strong evidence includes:

- Recent surveys and taxonomies
- Original peer-reviewed papers and clearly labeled preprints
- Official project pages, code, checkpoints, model cards, and dataset cards
- Benchmark and leaderboard maintainers
- Independent reproductions and ablations
- Failure analyses and follow-up work

Rules:

- Preserve task, dataset, split, metric, hardware, batch size, precision, and protocol
- Separate paper claims from released implementation behavior
- Record publication and last-update dates
- Do not call a result SOTA across incomparable settings

### Ecosystem and Standards Investigator

Goal: identify mature, reusable implementation paths.

Strong evidence includes:

- Official specifications and standards
- Maintained open-source projects and release histories
- Package registries and compatibility tables
- Protocols, SDKs, frameworks, and reference architectures
- Security advisories and migration guides
- Vendor products and service limits
- Maintainer issue discussions and ecosystem integration reports

Rules:

- Check license, maintenance, support window, API stability, and transitive dependencies
- Distinguish standards from one vendor's implementation
- Treat repository popularity as discovery evidence, not quality proof

## 4. Domain Specialists

Spawn specialists after broad discovery, not before. Assign them to serious capability areas or solution families.

Examples:

- Visual localization specialist
- Streaming systems specialist
- Retrieval specialist
- Model-serving specialist
- Distributed state specialist
- Security or privacy specialist
- Human-computer interaction specialist
- Hardware and edge-compute specialist

Each specialist produces a candidate dossier using `domain-analysis.md`. A specialist may reject its assigned family when evidence or constraints justify rejection.

Avoid one specialist per repository. Group near-identical implementations into a method family and analyze meaningful variants.

## 5. Solution Architect

The Solution Architect receives:

- Repository constraint brief
- Solution landscape
- Candidate dossiers
- Hard constraints
- Cross-capability interface requirements

It produces two to four coherent end-to-end architecture options using `architecture-synthesis.md`.

The architect should optimize for coherent system behavior, not the sum of individual component rankings.

## 6. Architecture Reviewer

The Architecture Reviewer should be independent from the Solution Architect when possible.

It:

- Checks hard blockers
- Compares all serious architecture options
- Challenges boundaries, contracts, topology, failure domains, security, operations, migration, and ownership
- Runs the Architecture Review Gate
- Requests bounded redesign or another synthesis round when justified

It must not merely approve the option preferred by the Research Director.

## 7. Engineering Reviewer

The Engineering Reviewer evaluates actual implementation bundles rather than abstract boxes.

It:

- Pins candidate versions, runtimes, drivers, services, and deployment assumptions
- Builds pairwise compatibility and dependency matrices
- Allocates end-to-end latency and resources
- Checks build, packaging, deployment, test, observability, migration, rollback, and ownership
- Runs the Engineering Readiness Gate
- Identifies the smallest experiment needed to resolve uncertain estimates

The Engineering Reviewer may conclude that an architecturally clean design is not currently implementable.

## 8. Evidence Auditor and Decision Chair

Prefer an auditor that did not author the investigation reports.

The auditor asks:

1. Which important claim has only one source?
2. Which company-use claim is indirect or vendor-sponsored?
3. Which benchmark comparison is not truly comparable?
4. Which candidate received less negative-evidence search than the leader?
5. Which implementation detail is inferred?
6. Which resource or compatibility claim is only an estimate?
7. What evidence would reverse the recommendation?

The Decision Chair then records:

- Research SOTA
- Public industry practice
- Domain conclusions
- Architecture gate outcomes
- Engineering gate outcomes
- Recommended architecture and exact implementation bundle
- Rejected options
- Conditions and confidence

Do not manufacture consensus. Preserve a minority objection when it exposes material risk.

## 9. Feasibility Experimenter

The experimenter receives a validation contract, not a vague instruction to “try it.”

It must:

- Test the highest-decision-value unknown first
- Use representative conditions
- Keep the experiment isolated
- Record reproducible commands and raw measurements
- Separate local results from published claims
- Return PASS, CONDITIONAL PASS, FAIL, or INCONCLUSIVE

## 10. Integration Engineer

The Integration Engineer receives:

- Reviewed architecture
- Concrete implementation bundle
- Architecture and engineering conditions
- Feasibility evidence
- Production boundary
- Tests and rollback requirements

It must rebuild the production path cleanly instead of copying experimental scaffolding.

## 11. Parallelism and sequencing

Recommended Full-mode graph:

```text
Repository Cartographer
          │
          ▼
Research Director capability plan
          │
   ┌──────┼──────────┐
   ▼      ▼          ▼
Industry  Academic   Ecosystem
Invest.   Invest.    Invest.
   └──────┼──────────┘
          ▼
Solution landscape
          │
   ┌──────┼──────────┐
   ▼      ▼          ▼
Domain Specialist A  B  C
   └──────┼──────────┘
          ▼
Candidate dossiers
          │
          ▼
Solution Architect
          │
          ▼
Candidate architecture set
          │
    ┌─────┴─────┐
    ▼           ▼
Architecture   Engineering
Reviewer       Reviewer
    └─────┬─────┘
          ▼
Evidence Auditor / Decision Chair
          │
          ▼
Feasibility Experimenter
          │
          ▼
Integration Engineer
```

Architecture and engineering review can run in parallel only after each has enough concrete design and implementation detail. Otherwise run architecture review first, then engineering review.

## 12. Handoff contracts

Every role should return:

- Scope and role
- Evidence or repository areas inspected
- Findings
- Assumptions
- Hard blockers
- Confidence
- Open questions
- Recommended next role or stop condition

Use stable candidate and architecture IDs across handoffs.

Example IDs:

```text
FAMILY-01
IMPL-01A
ARCH-01
GATE-ARCH-01
GATE-ENG-01
```

## 13. Conflict resolution

When roles disagree:

1. Identify whether the disagreement is factual, evaluative, or constraint-based
2. Resolve factual disputes with targeted primary-source or repository evidence
3. Preserve evaluative disagreement when tradeoffs are real
4. Give hard project constraints priority over generic preference
5. Give hard blockers priority over weighted scores
6. Convert unresolved material disagreement into INCONCLUSIVE or a validation experiment

Do not resolve conflict by asking the original author to restate its conclusion more confidently.

## 14. Cost and scope control

Avoid an agent swarm.

- Quick mode should normally use one investigator and a compact review
- Full mode should normally use three investigator lanes and two to five domain-specialist dossiers
- Do not create specialists for near-duplicate candidates
- Stop a lane when additional sources are unlikely to change the candidate family map
- Limit architecture synthesis to two rounds unless the user requests broader exploration
- Deeply verify a few coherent architectures rather than shallowly scoring many

## 15. Truthful fallback

When the harness lacks subagents:

- Run role-separated passes
- Clear the working conclusion before adversarial review when practical
- Label reviews as `same-agent structured review`
- Do not say “expert panel consensus” or “independent review”
- Still preserve the same artifacts and gates
