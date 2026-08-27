# Architecture Expert Review Playbook

Use this reference when a candidate changes component boundaries, interfaces, data contracts, dependencies, deployment topology, resource placement, security boundaries, operational ownership, or long-term evolution.

Research identifies a promising approach. The architecture review determines whether the proposed integration is structurally compatible with the current system before feasibility work or production changes proceed.

## 1. Reviewer role and independence

Prefer a dedicated architect agent, architecture-review subagent, or a separate reviewer context when the active harness provides one. Ask the reviewer to challenge the recommendation rather than merely endorse it.

Provide the reviewer with:

- The current repository architecture and applicable instructions
- The selected candidate and serious alternatives
- Hard constraints and known invariants
- The proposed integration sketch
- Evidence collected during research
- Unknowns intended for feasibility validation

Do not hide material limitations, but avoid anchoring the reviewer with a prewritten conclusion when an independent comparison is practical.

When no separate reviewer is available, perform a distinct second-pass architecture review and label the reviewer mode as `same-agent structured review`. Never claim that an independent architecture expert reviewed the design when that did not occur.

The architecture reviewer does not rerun broad SOTA research by default. The reviewer evaluates how the candidate fits this system and may request targeted evidence when a compatibility claim is unsupported.

## 2. Require an integration architecture sketch

Before scoring, describe the smallest plausible production design. Include the relevant subset of:

- Existing components and ownership boundaries affected
- New or changed components and their responsibilities
- Request, event, data, and control flow
- Public and internal APIs, schemas, data contracts, and versioning
- State ownership, persistence, consistency, and lifecycle
- New dependencies, runtimes, services, protocols, models, or hardware
- Deployment topology, process boundaries, network paths, and resource placement
- Concurrency, backpressure, caching, retries, timeouts, cancellation, and failure isolation
- Security, privacy, trust, tenancy, and compliance boundaries
- Observability, operational ownership, rollout, migration, and rollback

Use a compact text diagram or structured description when no diagram tool is available. Score the proposed design, not an undefined intention such as “integrate library X.”

## 3. Check architecture hard blockers first

An overall score cannot override a hard blocker. Typical blockers include:

- Violation of a repository invariant, ownership boundary, or required architectural rule
- Incompatible API, schema, protocol, runtime, platform, driver, or deployment environment
- A circular dependency or cross-layer coupling that the project cannot reasonably own
- Unbounded failure propagation, missing isolation, or an unacceptable single point of failure
- Security, privacy, tenancy, compliance, or data-residency boundary violations
- Destructive state or data migration with no credible compatibility and rollback strategy
- A consistency, durability, or availability model that conflicts with the product requirement
- A resource or scaling envelope that is structurally impossible on the target topology
- Operational responsibility that no team or service boundary can sustainably own
- A proposal too underspecified to evaluate a material compatibility risk

When a blocker is confirmed, assign `FAIL`. When the evidence needed to determine whether a blocker exists is unavailable, assign `INCONCLUSIVE` rather than guessing.

## 4. Score architecture compatibility

Score each dimension from 1 to 5 and justify it with repository evidence, primary documentation, or a clearly labeled assumption.

| Dimension | Weight | 1 | 3 | 5 |
|---|---:|---|---|---|
| Boundary and responsibility fit | 15% | Breaks layering or ownership | Fits with bounded restructuring | Fits existing boundaries naturally |
| Interface and data-contract fit | 15% | Incompatible or pervasive contract changes | Versioned adapters or moderate changes | Native interface fit or thin adapter |
| Dependency, runtime, and platform fit | 15% | Conflicting or unsupported stack | Compatible with bounded conditions | Directly supported by the current stack |
| Deployment, topology, and resource fit | 10% | Requires an impractical topology | Deployable with material additions | Fits current deployment and resource model |
| Reliability and failure isolation | 10% | Creates uncontrolled failure propagation | Risks are mitigable with explicit controls | Clear isolation, degradation, and recovery behavior |
| Security, privacy, and compliance fit | 10% | Violates a trust or policy boundary | Acceptable with explicit mitigations | Preserves or improves required boundaries |
| Observability and operability | 10% | Difficult to monitor, debug, or operate | Operable with additional instrumentation | Fits current telemetry and operating model |
| Migration, compatibility, and rollback | 5% | No credible safe transition | Bounded migration with conditions | Incremental rollout and simple rollback |
| Maintainability, ownership, and evolution | 10% | High coupling or unclear ownership | Sustainable with documented tradeoffs | Clear ownership and low-cost future evolution |

Calculate the weighted compatibility score as:

```text
Architecture compatibility = sum((dimension score / 5) * dimension weight)
```

Report the result on a 0–100 scale. The number summarizes the review; the evidence and blockers remain authoritative.

Default gate interpretation:

- **PASS** — score at least 80, no hard blocker, and no dimension below 3
- **CONDITIONAL PASS** — score 65–79, or a score of 2 in a non-blocking dimension with explicit bounded remediation
- **FAIL** — score below 65, any hard blocker, or a critical dimension scored 1
- **INCONCLUSIVE** — material architecture evidence or the integration sketch is missing

Weights and thresholds may be adapted for a project only when the change is disclosed and justified before scoring.

## 5. Require an adversarial review

The reviewer should explicitly answer:

1. Which existing invariant is most likely to be broken?
2. Where does coupling increase, and who owns it?
3. Which interface or data contract is hardest to evolve or roll back?
4. What is the largest new failure domain or operational burden?
5. Which compatibility assumption is inferred rather than demonstrated?
6. What simpler architecture or alternative candidate would reduce risk?
7. Which architecture conditions must become feasibility acceptance criteria?

A review that lists only benefits is incomplete.

## 6. Produce the Architecture Review Gate

Use exactly one status:

- **PASS** — the design is structurally compatible and may proceed to the requested next phase
- **CONDITIONAL PASS** — it may proceed only with explicit architectural conditions and validation criteria
- **FAIL** — redesign the integration or select another candidate before feasibility or production integration
- **INCONCLUSIVE** — obtain the missing repository, interface, topology, or ownership evidence before proceeding

The review must contain:

- Reviewer mode: dedicated architect/subagent or same-agent structured review
- Proposed architecture summary
- Hard blockers checked
- Dimension scores, weighted score, and evidence
- Strongest compatibility argument
- Strongest architecture objection
- Required conditions or redesign
- Impact on the engineering recommendation
- Conditions transferred into the feasibility contract

## 7. Phase transition rules

- A Research-only request may include the architecture review and stop without a spike or implementation.
- A candidate with architecture `FAIL` must not enter production feasibility as though the design were acceptable. Redesign it or evaluate the next finalist.
- A candidate with material architecture `INCONCLUSIVE` must not enter Integration.
- Architecture `CONDITIONAL PASS` conditions must become explicit feasibility thresholds or production acceptance criteria.
- Before Integration, recheck the architecture gate if the spike changed component boundaries, dependencies, contracts, topology, resource assumptions, or operational behavior.
- If the final implementation materially differs from the reviewed design, rerun the affected architecture dimensions before declaring completion.

Architecture review complements local feasibility. A structurally clean design can still fail performance or quality validation, and a fast prototype can still be architecturally unacceptable.
