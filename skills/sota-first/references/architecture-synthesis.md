# Candidate Architecture Synthesis

Use this reference after the solution landscape and Domain Specialist dossiers are complete.

The goal is not to select the highest-scoring component for every capability. The goal is to compose coherent end-to-end systems whose contracts, operating assumptions, resources, and ownership fit together.

## 1. Build a capability graph

Represent the feature as:

- User-visible outcome
- Functional capabilities
- Cross-cutting services
- Inputs and outputs
- State and lifecycle
- Ordering and timing constraints
- Quality, latency, throughput, and resource budgets
- Failure and degraded-mode requirements
- Security, privacy, and policy boundaries
- Operations and ownership

Mark capabilities that already exist in the repository.

## 2. Normalize component contracts

For every shortlisted implementation, normalize:

- Input and output schema
- Coordinate system, units, encoding, tensor layout, or protocol
- Cadence, ordering, and synchronization
- Stateful or stateless behavior
- Batch, stream, online, offline, or asynchronous assumptions
- Error and confidence signaling
- Resource and deployment requirements
- License and data constraints

Do not compose components until their contracts are explicit.

## 3. Create distinct architecture options

Produce two to four options that are materially different.

Useful diversity axes:

- Edge-heavy versus server-heavy
- Monolithic versus service-separated
- Learned versus deterministic or hybrid
- Online map-free versus mapped or indexed
- Single-model versus staged pipeline
- Synchronous versus event-driven
- Managed service versus self-hosted
- Fast-path plus fallback versus one universal path
- High-accuracy versus low-latency Pareto points

Do not create cosmetic variants that differ only by library name.

## 4. Avoid Frankenstein architectures

A “best component per benchmark” composition is invalid when:

- Inputs and outputs do not align
- Components assume different coordinate frames, tokenization, timing, or state
- Runtime, driver, or dependency versions conflict
- End-to-end latency exceeds the budget even though each component is fast alone
- GPU, memory, network, storage, or process placement conflicts
- Failure handling and backpressure are incompatible
- Security or data boundaries conflict
- Licenses or service terms conflict
- Operational ownership becomes fragmented or unclear
- The integration adapter becomes a new complex subsystem

Prefer a slightly weaker component that yields a coherent system.

## 5. Architecture option template

Use stable IDs.

```markdown
## Architecture option: ARCH-XX

### Objective and strategy
- Target outcome:
- Core architecture pattern:
- Why this option is materially distinct:

### Components
| Capability | Component or implementation | Reuse/Adopt/Extend/Compose/Build | Responsibility | Owner |
|---|---|---|---|---|

### Contracts
- External APIs:
- Internal APIs:
- Schemas and data formats:
- Events and ordering:
- State ownership:
- Versioning strategy:

### Flow
```text
<input>
   │
   ▼
<component>
   │
   ▼
<output>
```

### Runtime and topology
- Processes and services:
- Edge, client, server, GPU, and storage placement:
- Network paths:
- Concurrency model:
- Queues, backpressure, retries, timeouts, and cancellation:

### Preliminary budgets
| Stage | Quality role | p50/p95 latency allocation | CPU | GPU/VRAM | RAM | Network | Storage |
|---|---|---:|---:|---:|---:|---:|---:|

- Startup and warm-up:
- Throughput:
- Headroom assumption:
- Critical path:

### Reliability and safety
- Failure domains:
- Degraded mode:
- Recovery:
- Data retention:
- Security and privacy boundaries:
- Compliance considerations:

### Operations
- Observability:
- Deployment and rollout:
- Migration:
- Rollback:
- Operational ownership:

### Evidence and uncertainty
- Supporting candidate dossiers:
- Public industry precedent:
- Academic support:
- Mature implementation support:
- Main assumptions:
- Highest-risk unknowns:

### Preliminary assessment
- Advantages:
- Disadvantages:
- Hard blockers:
- Conditions:
```

## 6. Preliminary budgets are estimates

Architecture synthesis may allocate budgets, but label them as estimates.

A preliminary budget should:

- Allocate the full end-to-end critical path
- Include preprocessing, serialization, transport, queueing, postprocessing, and persistence
- Include startup and warm-up where relevant
- Account for shared resource contention
- Reserve explicit project-defined headroom
- Identify which values are externally reported, analytically estimated, or unknown

The Engineering Reviewer turns this into a concrete implementation budget.

## 7. Use public architectures carefully

When borrowing from a leading company or public system:

- Reuse the pattern, not the brand name
- Record the disclosed operating context
- Identify infrastructure or organizational assumptions that do not transfer
- Replace unavailable internal services with concrete alternatives
- Explain where the target project intentionally diverges

## 8. Hybrid design

Hybrid architectures are valid when the combination resolves real tradeoffs.

Examples:

- Fast local path plus accurate remote fallback
- Deterministic state estimation plus learned semantic correction
- Mature managed service for one capability plus self-hosted sensitive data path
- Batch preprocessing plus online incremental updates

For every hybrid, define:

- Routing criteria
- Consistency between paths
- Shared state
- Failure and fallback behavior
- Cost and resource implications
- How quality is measured across paths

Do not use “hybrid” as a label for an undefined mixture.

## 9. Architecture revision loop

After Architecture and Engineering review:

1. Collect hard blockers and bounded conditions
2. Revise only affected components, contracts, placement, or budgets
3. Explain the delta
4. Rerun affected review dimensions
5. Limit normal synthesis to two rounds

If every architecture fails for the same fundamental reason, revisit the capability decomposition or candidate families instead of producing superficial variants.

## 10. Selection handoff

The architecture set should allow independent reviewers to answer:

- Which option fits repository boundaries best?
- Which option has the cleanest contracts?
- Which option is implementable with available runtimes and resources?
- Which option isolates failure and risk?
- Which option is easiest to migrate and roll back?
- Which option has the lowest long-term ownership burden?
- Which assumptions require local validation?

Do not declare the final recommendation inside the synthesis document.
