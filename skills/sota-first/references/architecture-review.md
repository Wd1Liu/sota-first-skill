# Comparative Architecture Expert Review

Use this reference after the Solution Architect has produced concrete end-to-end options.

The reviewer evaluates architecture and system compatibility. It should compare serious options rather than merely approve a preselected candidate.

## 1. Reviewer role and independence

Prefer a dedicated architect agent, architecture-review subagent, or separate reviewer context that did not author the options.

Provide:

- Repository constraint brief
- Capability graph
- Solution landscape
- Candidate dossiers
- Candidate architecture set
- Hard constraints
- Evidence ledger
- Unknowns intended for engineering review or feasibility validation

Ask the reviewer to challenge the options.

When no separate reviewer exists, perform a distinct second pass and label it `same-agent structured review`. Never claim independent expert review when that did not occur.

## 2. Review the design, not the product name

Each option must specify enough of:

- Components and responsibilities
- Interfaces, schemas, protocols, events, and state
- Data and control flow
- Runtime and deployment topology
- Resource placement
- Concurrency, queues, backpressure, retries, timeouts, and cancellation
- Failure isolation and degraded modes
- Security, privacy, tenancy, and compliance boundaries
- Observability and operational ownership
- Migration, rollout, and rollback
- Long-term evolution

An undefined statement such as “use model X” is **INCONCLUSIVE**, not a reviewable architecture.

## 3. Hard blockers

An overall score cannot override a hard blocker.

Typical blockers:

- Violation of a repository invariant, ownership boundary, or required architectural rule
- Incompatible API, schema, protocol, consistency, state, or lifecycle model
- Circular dependency or unacceptable cross-layer coupling
- Unsupported runtime, platform, deployment environment, or resource topology
- Unbounded failure propagation or unacceptable single point of failure
- Security, privacy, tenancy, compliance, or data-residency violation
- Destructive migration without credible compatibility and rollback
- Availability, durability, or consistency behavior that conflicts with the product
- Operational responsibility that no component or team can sustainably own
- A design too underspecified to resolve a material compatibility risk

A confirmed blocker yields **FAIL**. Missing evidence needed to determine a blocker yields **INCONCLUSIVE**.

## 4. Architecture compatibility dimensions

Score each dimension from 1 to 5 and justify it with repository evidence, primary documentation, or a clearly labeled assumption.

| Dimension | Weight | 1 | 3 | 5 |
|---|---:|---|---|---|
| Boundary and responsibility fit | 15% | Breaks layering or ownership | Fits with bounded restructuring | Fits existing boundaries naturally |
| Interface and data-contract fit | 15% | Incompatible or pervasive contract changes | Versioned adapters or moderate changes | Native fit or thin adapter |
| Dependency, runtime, and platform fit | 15% | Structurally unsupported stack | Compatible with bounded conditions | Directly supported by the current stack |
| Deployment, topology, and resource fit | 10% | Requires impractical placement or topology | Deployable with material additions | Fits current deployment and resource model |
| Reliability and failure isolation | 10% | Uncontrolled propagation or no degraded mode | Risks mitigable with explicit controls | Clear isolation, degradation, and recovery |
| Security, privacy, and compliance fit | 10% | Violates a required boundary | Acceptable with explicit mitigations | Preserves or improves required boundaries |
| Observability and operability | 10% | Difficult to monitor, debug, or operate | Operable with added instrumentation | Fits current telemetry and operating model |
| Migration, compatibility, and rollback | 5% | No credible safe transition | Bounded migration with conditions | Incremental rollout and simple rollback |
| Maintainability, ownership, and evolution | 10% | High coupling or unclear ownership | Sustainable with documented tradeoffs | Clear ownership and low-cost evolution |

Calculate:

```text
Architecture compatibility = sum((dimension score / 5) * dimension weight)
```

Report 0–100.

Default gate:

- **PASS** — score at least 80, no hard blocker, and no dimension below 3
- **CONDITIONAL PASS** — score 65–79, or a score of 2 in a non-blocking dimension with explicit bounded remediation
- **FAIL** — score below 65, any hard blocker, or a critical dimension scored 1
- **INCONCLUSIVE** — material design or repository evidence is missing

Adapt weights only when disclosed and justified before scoring.

## 5. Comparative review

For every option, produce:

| Architecture ID | Hard blocker | Weighted score | Gate | Strongest advantage | Strongest objection | Required condition |
|---|---|---:|---|---|---|---|

Then compare:

- Which option best preserves repository invariants?
- Which option introduces the fewest and cleanest boundaries?
- Which option has the most evolvable contracts?
- Which option minimizes new failure domains?
- Which option has the simplest migration and rollback?
- Which option creates the clearest operational ownership?
- Which option depends on the fewest unsupported assumptions?
- Which option is likely to remain coherent after the Engineering Reviewer selects concrete implementations?

Do not let a familiar architecture win by default.

## 6. Adversarial questions

The reviewer must answer:

1. Which existing invariant is most likely to be broken?
2. Where does coupling increase, and who owns it?
3. Which interface or state contract is hardest to evolve?
4. What is the largest new failure domain?
5. Which trust, privacy, or compliance boundary becomes weaker?
6. Which compatibility claim is inferred rather than demonstrated?
7. Which public reference architecture depends on non-transferable scale or infrastructure?
8. What simpler option would reduce risk?
9. Which conditions must enter engineering review and feasibility validation?
10. What evidence would reverse the preferred architecture?

A review that lists only benefits is incomplete.

## 7. Output template

```markdown
## Architecture Review Gate

**Reviewer mode:** dedicated architect | separate reviewer context | same-agent structured review
**Repository revision:** ...
**Options reviewed:** ARCH-01, ARCH-02, ...

### Hard blockers
- ARCH-01:
- ARCH-02:

### Scorecards
| Dimension | Weight | ARCH-01 score | Evidence | ARCH-02 score | Evidence |
|---|---:|---:|---|---:|---|
| Boundary and responsibility fit | 15% | ... | ... | ... | ... |

### Comparative result
| Architecture | Score | Gate | Strongest compatibility argument | Strongest objection |
|---|---:|---|---|---|

### Preferred architecture
- Architecture:
- Reason:
- Why alternatives lost:
- Required conditions:
- Remaining uncertainty:
- Engineering-review handoff:

### Minority objection
- <material disagreement, or “None”>
```

## 8. Transition rules

- A Research-only request may stop after this review
- **FAIL** requires redesign or another candidate architecture
- Material **INCONCLUSIVE** blocks Integration
- **CONDITIONAL PASS** conditions enter the Engineering Readiness Gate and feasibility contract
- The Engineering Reviewer may invalidate the preferred option when concrete implementations conflict
- Re-run affected dimensions when engineering review or feasibility changes boundaries, contracts, topology, ownership, or failure behavior
- Re-review the final implementation when it materially differs from the reviewed option

Architecture review and engineering review are separate. A clean system shape may still be impossible to build with the selected implementations and resources.
