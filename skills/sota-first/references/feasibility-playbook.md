# Feasibility Validation Playbook

Use this reference when the delivery phase includes feasibility validation. Research identifies a promising candidate, the Architecture Review Gate establishes whether its proposed system design is structurally acceptable, and validation determines whether the reviewed candidate actually works under this repository's representative conditions.

A paper result, architecture score, successful installation, working import, or toy demo is not sufficient proof of feasibility.

## 1. Require the architecture handoff

Before running a spike for an architecture-sensitive candidate, record:

- Architecture reviewer mode
- Architecture gate status and weighted score
- The reviewed component, interface, data, deployment, failure, security, ownership, migration, and rollback boundaries
- Every condition attached to an architecture `CONDITIONAL PASS`
- Architecture assumptions that remain inferred rather than demonstrated

Do not validate a candidate with architecture `FAIL` as though the design were acceptable. Redesign it or select another finalist. Resolve material architecture `INCONCLUSIVE` before Integration.

## 2. Define a validation contract

Before running a spike, state:

- The candidate and exact version, checkpoint, service tier, or commit being tested
- The project assumption or risk being tested
- Architecture conditions converted into measurable acceptance criteria
- Representative inputs, traffic, data, hardware, runtime, topology, and operating conditions
- Measurable acceptance thresholds
- Hard failure conditions
- The smallest experiment that can falsify the recommendation
- Which changes are disposable and how they will be cleaned up

Use concrete thresholds whenever possible. Examples include latency percentiles, throughput, memory, task quality, failure recovery, schema compatibility, startup time, dependency size, adapter surface, or integration effort.

## 3. Test the highest-risk unknown first

Order experiments by decision value, not implementation convenience.

Typical high-risk unknowns include:

- A required API, schema, protocol, runtime, driver, or platform is incompatible with the repository
- Real latency, memory, storage, network, or compute exceeds the deployment budget
- Quality drops materially on representative project data
- Streaming, online, offline, edge, concurrency, or cancellation behavior differs from the published setup
- A checkpoint, license, model term, dataset, or service capability is unavailable
- Integration requires an architectural rewrite rather than the reviewed thin boundary
- Failure isolation, backpressure, observability, rollback, security, privacy, or operational ownership is inadequate
- A migration or data-contract condition cannot be satisfied safely

Stop early when a hard disqualifier is confirmed. Do not build a polished prototype for a candidate that has already failed a non-negotiable constraint.

## 4. Isolate the experiment

Prefer, in order:

1. Read-only compatibility checks and documented capability probes
2. A temporary directory or disposable script outside production paths
3. A temporary worktree, throwaway branch, or clearly isolated experiment directory
4. A shadow path that does not affect production traffic or persistent data

During validation:

- Do not treat experimental code as production integration
- Avoid persistent manifest, lockfile, migration, infrastructure, or configuration changes unless isolated and necessary
- Record every temporary dependency and environment change
- Do not commit secrets, credentials, model weights, datasets, or generated artifacts
- Preserve the reviewed architecture boundary instead of creating an easier but unrepresentative toy path
- Clean up disposable artifacts, or list exactly what remains and why

## 5. Use representative conditions

A validation result is useful only when its setup covers the constraint being tested.

### Software library or integration

Check:

- Exact runtime, framework, platform, and dependency compatibility
- Installation and transitive dependency impact
- API shape, schema/data-contract behavior, retries, cancellation, concurrency, and failure semantics
- Required configuration, credentials, external services, and deployment paths
- Testability, observability, migration, rollback, and ownership
- Whether the integration remains within the reviewed boundary or spreads through the codebase

### ML, CV, agent, retrieval, or research method

Check the relevant subset of:

- Quality on representative project samples, not only published datasets
- End-to-end latency, including preprocessing, model serving, transport, and postprocessing
- Throughput, p50/p95 latency, warm-up, startup, streaming, batching, and concurrency behavior
- Peak and steady-state CPU, GPU memory, RAM, storage, and network use
- Hardware, precision, resolution, batch size, sequence length, and context settings
- Checkpoint access, model/data terms, calibration, prompts, sensors, maps, and external services
- Robustness to expected edge cases, degraded modes, and failure domains
- Whether the required adapter and service topology match the reviewed architecture

### System architecture or infrastructure

Check:

- Expected load and scaling envelope
- Availability, consistency, durability, ordering, and recovery behavior
- Failure isolation, backpressure, degraded mode, and incident recovery
- Operational complexity, observability, backup, migration, rollback, and ownership
- Cost drivers, external service limits, and resource placement
- Contract compatibility and rollout behavior across versions
- Failure injection when practical

### Security- or privacy-sensitive capability

Check:

- Threat model and trust boundaries
- Safe defaults and configuration requirements
- Data flow, retention, encryption, key or credential management
- Current advisories and supported versions
- Failure behavior, tenancy isolation, compliance, and auditability

A disposable security test does not replace a proper security review when one is required.

## 6. Record the environment and results

Capture enough detail to reproduce the decision:

- Date and repository revision
- Architecture review reference, status, and conditions
- Candidate version or commit
- Hardware, operating system, runtime, framework, topology, and relevant drivers
- Dataset, sample, traffic shape, or workload
- Configuration, precision, batch size, resolution, and other material settings
- Commands or test procedure
- Raw measurements and observed failure modes
- Differences from published, vendor-reported, or architecture-reviewed conditions

Separate external claims, architecture inferences, and locally measured results.

## 7. Assign a feasibility status

Use exactly one status:

- **PASS** — All hard thresholds, architecture conditions, and critical integration assumptions were verified, and no new disqualifier appeared.
- **CONDITIONAL PASS** — The candidate is viable only under explicit conditions or with bounded follow-up work that still fits the project constraints and architecture.
- **FAIL** — A hard threshold, architecture condition, or non-negotiable constraint was violated.
- **INCONCLUSIVE** — The test could not resolve a material uncertainty because data, access, tooling, environment, or evidence was insufficient.

Do not convert an inconclusive result into a pass because the candidate appears promising.

## 8. Decide whether architecture must be reviewed again

Rerun the affected architecture dimensions when the spike changes or disproves any reviewed assumption about:

- Component or ownership boundaries
- Interfaces, schemas, protocols, state, or data contracts
- Dependencies, runtime, platform, service, model-serving, or hardware requirements
- Deployment topology, resource placement, scaling, or network paths
- Failure isolation, security, privacy, observability, migration, or rollback

A feasibility `PASS` against a materially different design does not validate the original Architecture Review Gate.

## 9. Decide the transition

- For a research-only request, do not enter validation unless the user requested it.
- For a validation-only request, stop after the feasibility verdict and do not integrate production code.
- For a research-review-validate-integrate request, continue directly after architecture and feasibility **PASS**.
- After either **CONDITIONAL PASS**, continue only when all conditions can be satisfied within the stated constraints and requested scope.
- After **FAIL**, test the next justified finalist, redesign, or revise the research verdict. Do not force the failed candidate into production.
- After **INCONCLUSIVE**, identify the smallest missing test or evidence needed. Do not integrate while a material uncertainty remains.

## 10. Promote cleanly, not by accident

When Integration is authorized after the required gates:

- Recreate the minimal production implementation cleanly
- Preserve reviewed boundaries, interfaces, data contracts, failure isolation, security boundaries, and ownership
- Do not blindly copy temporary scripts, hard-coded paths, debug logging, test credentials, or experimental configuration
- Preserve architecture conditions and feasibility thresholds as tests, contract checks, architecture checks, or benchmarks
- Document differences between the reviewed design, spike, and final integration
- Keep a rollout and rollback path for high-impact changes
