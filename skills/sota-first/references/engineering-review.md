# Engineering Readiness Expert Review

Use this reference after candidate architectures are concrete enough to select actual implementation bundles.

Architecture review asks whether the system shape is coherent. Engineering review asks whether the exact combination can be built, deployed, operated, and sustained with the project's real stack and resource envelope.

## 1. Reviewer role

Prefer a dedicated engineering reviewer, implementation specialist, platform engineer, or separate reviewer context.

Provide:

- Repository constraint brief
- Candidate architecture options and architecture gate results
- Candidate dossiers
- Exact implementation candidates
- Project runtime, deployment, hardware, and operational constraints
- Architecture conditions
- Evidence ledger

When no separate reviewer exists, label the result `same-agent structured engineering review`.

## 2. Pin the implementation bundle

Do not review abstract labels such as “use a vector database” or “run the model.”

Specify the relevant subset of:

- Library, framework, SDK, model, checkpoint, service, protocol, and version or commit
- Language, compiler, runtime, operating system, container, browser, device, and architecture
- CUDA, driver, accelerator, precision, and serving engine
- Database, schema, client, protocol, and migration tool
- Cloud service tier, quota, region, SLA, and API version
- Build system, package manager, deployment target, and CI path
- Data format, serialization, transport, tensor layout, coordinate frame, and encoding

Unknown exact versions lower confidence and may yield **INCONCLUSIVE**.

## 3. Pairwise compatibility matrix

Check every important component pair.

```markdown
| Producer / dependency | Consumer / dependent | Contract | Runtime/version | Resource interaction | License/security | Status | Required adapter |
|---|---|---|---|---|---|---|---|
| IMPL-A | IMPL-B | ... | ... | ... | ... | Green/Yellow/Red/Unknown | ... |
```

Check:

- API and schema compatibility
- Language, runtime, ABI, compiler, and framework compatibility
- Driver, CUDA, accelerator, and operating-system compatibility
- Package and transitive dependency conflicts
- Data format, tensor layout, coordinate frame, tokenization, and serialization
- Batch, stream, cadence, ordering, synchronization, and state assumptions
- Threading, process, async, cancellation, and backpressure behavior
- Shared GPU, CPU, memory, storage, network, ports, and file-system requirements
- License, model terms, data terms, and supply-chain risk
- Authentication, credentials, secrets, network, and trust boundaries

A large undocumented adapter is a new subsystem, not a “thin integration.”

## 4. Resource and performance budget

Build an end-to-end budget.

```markdown
| Stage | Implementation | p50 budget | p95 budget | CPU | GPU | VRAM | RAM | Network | Storage | Concurrency | Evidence type |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
```

Include:

- Preprocessing and postprocessing
- Serialization and transport
- Queueing and scheduling
- Model or service execution
- Persistence and indexing
- Startup and warm-up
- Cache behavior
- Peak and steady-state use
- Shared-resource contention
- Failure and retry amplification
- Explicit project-defined headroom

Label each value:

- Locally measured
- Primary-source reported
- Independently reproduced
- Analytically estimated
- Unknown

Do not sum incomparable vendor numbers as though they were end-to-end measurements.

## 5. Resource placement

For each component, state:

- Process or service boundary
- Client, edge, device, server, cloud, or worker placement
- CPU and accelerator placement
- Memory and storage ownership
- Network path and bandwidth sensitivity
- Scaling unit
- Affinity and isolation
- Shared-resource contention
- Failure domain
- Operational owner

Check whether the proposed placement creates unnecessary transfer, serialization, or synchronization cost.

## 6. Build and deployment review

Check:

- Installation and reproducible build path
- Lockfile and dependency strategy
- Container or package availability
- Supported platform and architecture
- CI runner requirements
- Artifact, checkpoint, dataset, or model distribution
- Secret and credential management
- Configuration and feature flags
- Observability and debugging
- Upgrade, migration, and rollback
- External service quotas, rate limits, regions, cost, and availability
- Supply-chain and security advisories
- Ownership and on-call implications

## 7. Testability and operations

Require a credible plan for:

- Unit and contract tests
- Integration tests
- Representative benchmarks or evals
- Failure injection and degraded-mode tests
- Telemetry, logs, metrics, traces, and health checks
- Capacity and resource alerts
- Version and schema compatibility checks
- Rollout, canary, shadow, or feature-flag strategy
- Rollback and data recovery

An implementation that cannot be observed or safely rolled out is not production-ready.

## 8. Hard blockers

Typical blockers:

- Irreconcilable runtime, driver, ABI, dependency, or platform conflict
- Missing or inaccessible required model, checkpoint, service, data, or artifact
- Incompatible license, data terms, or service terms
- Resource or latency budget structurally exceeds available capacity
- No viable build, packaging, or deployment path
- Interface mismatch requiring an unbounded or high-risk custom subsystem
- Unsupported security or credential model
- External quota, region, availability, or cost that violates a hard requirement
- Unowned operational burden
- Destructive migration or state transition without rollback
- Evidence too incomplete to determine a material compatibility claim

A blocker yields **FAIL**. Missing evidence needed to rule out a blocker yields **INCONCLUSIVE**.

## 9. Engineering readiness dimensions

Score 1–5.

| Dimension | Weight | 1 | 3 | 5 |
|---|---:|---|---|---|
| Implementation availability and maturity | 10% | Missing, abandoned, or unstable | Usable with gaps | Maintained, available, and production-ready |
| Dependency, version, runtime, and platform compatibility | 20% | Irreconcilable conflict | Compatible with bounded constraints | Directly compatible and reproducible |
| Interface and data-representation compatibility | 15% | Pervasive mismatch | Bounded adapters | Native contracts or thin adapters |
| Resource and performance budget | 20% | Exceeds hard capacity | Plausible with explicit conditions | Fits budgets with measured or strong evidence and headroom |
| Build, deploy, and operational path | 10% | No viable path | Viable with material work | Fits existing build and deployment model |
| Reliability, observability, and testability | 10% | Unsafe or opaque | Acceptable with added controls | Strong failure handling and project-native verification |
| Security, license, and supply chain | 5% | Material unresolved risk | Acceptable with mitigation | Clear compatible terms and posture |
| Migration, rollback, ownership, and maintainability | 10% | Unsafe transition or unclear owner | Bounded plan | Incremental rollout, clear owner, sustainable maintenance |

Calculate:

```text
Engineering readiness = sum((dimension score / 5) * dimension weight)
```

Default gate:

- **PASS** — at least 80, no hard blocker, no dimension below 3, and resource budget has explicit headroom
- **CONDITIONAL PASS** — 65–79 or a non-blocking score of 2 with bounded conditions and a validation plan
- **FAIL** — below 65, any hard blocker, or a critical dimension scored 1
- **INCONCLUSIVE** — material implementation, compatibility, or budget evidence is missing

## 10. Comparative output

```markdown
## Engineering Readiness Gate

**Reviewer mode:** ...
**Repository revision:** ...
**Architectures and bundles reviewed:** ...

### Implementation bundles
- ARCH-01 / BUNDLE-01:
- ARCH-02 / BUNDLE-02:

### Compatibility matrix
<required table>

### Resource and latency budgets
<required table>

### Hard blockers
- BUNDLE-01:
- BUNDLE-02:

### Scorecards
| Dimension | Weight | BUNDLE-01 | Evidence | BUNDLE-02 | Evidence |
|---|---:|---:|---|---:|---|

### Comparative result
| Bundle | Score | Gate | Main implementation advantage | Main engineering risk | Estimated integration effort |
|---|---:|---|---|---|---|

### Preferred bundle
- Bundle:
- Reason:
- Conditions:
- Validation needs:
- Ownership:
- Rollback:
- Remaining unknowns:
```

## 11. Architecture feedback loop

The Engineering Reviewer may ask the Solution Architect to revise:

- Component choice
- Interface boundary
- Process or service boundary
- Edge/server placement
- Queue or concurrency model
- Data representation
- Resource allocation
- Fallback path
- Deployment strategy

Explain the delta and rerun affected dimensions only. Normal workflow allows one bounded revision round.

## 12. Relationship to feasibility

Engineering review is predictive.

It can use repository facts, official compatibility documentation, released benchmarks, and analytical budgets. It cannot produce a local feasibility **PASS** unless representative local measurement has already occurred.

Transfer uncertain high-impact claims into the feasibility contract, including:

- End-to-end p95 latency
- Peak VRAM and RAM
- Throughput and concurrency
- Startup and warm-up
- Streaming behavior
- Dependency installation
- Contract adapter size
- Failure recovery
- Service quotas and cost
- Deployment compatibility

A high Engineering Readiness score cannot override a local feasibility **FAIL**.
