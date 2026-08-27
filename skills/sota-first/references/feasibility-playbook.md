# Feasibility Validation Playbook

Use this reference after a recommended architecture and concrete implementation bundle have passed or conditionally passed the required Architecture and Engineering gates.

Research selects candidates. Architecture review checks system coherence. Engineering review predicts buildability. Feasibility validation measures the highest-risk project-specific claims under representative conditions.

A paper result, public deployment, architecture score, engineering score, successful installation, working import, or toy demo is not sufficient proof.

## 1. Required handoff

Record:

- Repository revision
- Architecture ID and Architecture gate status
- Implementation bundle and exact versions
- Engineering gate status
- Every condition from Architecture or Engineering `CONDITIONAL PASS`
- Resource and latency budget
- Highest-risk assumptions
- Proposed production boundary
- Requested endpoint

If material information is missing, return **INCONCLUSIVE** or refresh the relevant earlier phase.

## 2. Validation contract

Before running a spike, specify:

- Falsifiable hypothesis
- Representative inputs, traffic, data, hardware, runtime, topology, and operating conditions
- Quality thresholds
- Latency and throughput thresholds
- CPU, GPU, VRAM, RAM, storage, and network thresholds
- Interface and compatibility thresholds
- Reliability and failure thresholds
- Policy, service, license, and cost constraints
- Maximum acceptable adapter and integration surface
- Hard failure conditions
- Smallest experiment that can reverse the decision
- Isolation and cleanup plan

Transfer material Architecture and Engineering conditions into measurable checks.

## 3. Test the highest-risk unknown first

Typical high-risk unknowns:

- Exact dependency, runtime, driver, or platform compatibility
- End-to-end p95 latency
- Peak and steady-state resource use
- Quality on representative project data
- Streaming, online, offline, edge, startup, and warm-up behavior
- Throughput and concurrency
- Queueing, cancellation, backpressure, retry, and recovery
- Schema, data-format, coordinate, or tensor-layout adapters
- Required service quota, region, price, or availability
- Model, checkpoint, data, or artifact availability
- Actual adapter size and coupling
- Deployment and observability path

Stop early when a hard blocker is confirmed.

## 4. Isolation

Prefer:

1. Read-only compatibility probes
2. Temporary environment or directory
3. Disposable script outside production paths
4. Temporary worktree or throwaway branch
5. Isolated experiment directory
6. Shadow path that does not affect production traffic or persistent data

Do not let experiment code silently become production code. Record temporary changes and clean up or list exactly what remains.

## 5. Representative conditions

### Software or service integration

Check exact runtime and framework compatibility, installation impact, API and schema behavior, cancellation and concurrency, external limits, observability, migration, rollback, testability, and adapter spread.

### ML, CV, retrieval, or agent method

Check quality on representative samples; end-to-end latency; throughput; p50/p95; startup; warm-up; streaming; CPU, GPU, VRAM, RAM, storage, and network use; hardware and precision settings; model and data availability; robustness; and error signaling.

### Architecture or infrastructure

Check expected load, scaling unit, availability, consistency, durability, recovery, failure isolation, backpressure, degraded mode, observability, backup, migration, rollback, cost drivers, and service limits.

### Security or privacy

Check trust boundaries, data flow, retention, safe defaults, supported versions, failure behavior, isolation, compliance, and auditability. A disposable test does not replace a formal review where one is required.

## 6. Reproducible evidence

Capture:

- Date and repository revision
- Architecture and implementation bundle IDs
- Exact versions and commits
- Hardware, operating system, runtime, framework, drivers, and services
- Dataset, sample, traffic shape, or workload
- Configuration and material settings
- Commands and procedure
- Raw measurements
- Failure modes
- Differences from public, paper, vendor, architecture-review, or engineering-review conditions
- Cleanup state

Label results as **locally measured**.

## 7. Status

Use exactly one:

- **PASS** — all hard thresholds and critical assumptions were verified
- **CONDITIONAL PASS** — viable only under explicit bounded conditions that fit the project
- **FAIL** — a hard threshold or non-negotiable constraint was violated
- **INCONCLUSIVE** — a material uncertainty could not be resolved with available data, access, tooling, or environment

Do not convert **INCONCLUSIVE** to **PASS** because a candidate appears promising.

## 8. Feasibility Gate output

```markdown
## Feasibility Gate

**Validation date:** ...
**Repository revision:** ...
**Architecture:** ARCH-XX
**Implementation bundle:** BUNDLE-XX
**Architecture gate status:** ...
**Engineering gate status:** ...
**Status:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE

### Results
| Criterion | Threshold | Measured result | Outcome | Evidence |
|---|---:|---:|---|---|

### Findings
- Locally measured:
- Architecture conditions:
- Engineering conditions:
- Failure modes:
- Differences from external claims:

### Transition
- Next action:
- Conditions:
- Production boundary:
- Preserved acceptance test:
- Cleanup:
- Remaining uncertainty:
```

## 9. Transitions

- Research-only: do not run validation
- Validation-only: stop after the gate
- Full pipeline after **PASS**: continue to Integration
- **CONDITIONAL PASS**: continue only when conditions are accepted and enforceable
- **FAIL**: test the next justified option or revise the decision
- **INCONCLUSIVE**: identify the smallest missing evidence
- If the spike changes components, contracts, placement, resource assumptions, failure model, or ownership, rerun affected Architecture and Engineering dimensions

## 10. Promotion

After a passing gate, recreate the production implementation cleanly, preserve the tests and measurements that established feasibility, measure the integrated path again, and roll back when the final path violates a gate condition.
