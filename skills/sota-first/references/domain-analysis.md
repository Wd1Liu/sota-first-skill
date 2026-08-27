# Domain Specialist Analysis

Use this reference after broad landscape discovery. Domain Specialists explain how serious method families actually work and what they require before the Solution Architect composes them.

## 1. Assign specialists by meaningful expertise

Assign a specialist to:

- A capability that materially affects the system
- A distinct solution family
- A cross-cutting domain such as security, privacy, streaming, distributed state, hardware, or human factors

Do not create one specialist per repository. Group near-identical implementations into a family and analyze important variants.

A specialist may cover multiple families when the underlying mechanism and evidence are tightly related.

## 2. Specialist role

The specialist should behave as a technical critic, not an advocate.

It must:

- Explain the mechanism at the level needed for architecture and implementation decisions
- Distinguish the method family from individual implementations
- Identify assumptions and operating envelope
- Preserve benchmark and source context
- Compare serious variants
- Expose hidden prerequisites and failure modes
- Identify interfaces needed for composition
- Mark externally inferred facts and local unknowns
- Reject the family when it violates a hard constraint

## 3. Candidate dossier

Use stable IDs.

```markdown
## Candidate dossier: FAMILY-XX / IMPL-XX

### Scope
- Capability:
- Method family:
- Concrete implementations:
- Specialist role and reviewer mode:

### Mechanism
- Core idea:
- Processing stages:
- State or memory:
- Training, mapping, calibration, or setup:
- Online versus offline behavior:

### Contract
- Inputs:
- Outputs:
- Data types, schemas, coordinate systems, tensor layouts, or protocols:
- State ownership:
- Timing, ordering, and synchronization assumptions:
- Error and confidence signaling:

### Evidence
- Academic evidence:
- Public industry evidence:
- Mature ecosystem evidence:
- Independent reproduction:
- Negative evidence:
- Evidence date and confidence:

### Operating envelope
- Quality or task-success conditions:
- Latency and throughput conditions:
- CPU, GPU, VRAM, RAM, storage, and network implications:
- Startup, warm-up, batch, precision, resolution, or context assumptions:
- Scaling behavior:
- Edge, mobile, cloud, streaming, or offline constraints:

### Failure modes
- Known failure cases:
- Degraded behavior:
- Recovery requirements:
- Safety, security, privacy, or compliance risks:
- Observability requirements:

### Implementation variants
| Implementation ID | Version or commit | Runtime and dependencies | License | Maturity | Main advantage | Main limitation |
|---|---|---|---|---|---|---|
| IMPL-XXA | ... | ... | ... | ... | ... | ... |

### Composition requirements
- Required upstream capability:
- Required downstream capability:
- Interface adapters:
- Incompatible assumptions:
- Shared resources:
- Coupling risks:
- Alternatives or fallbacks:

### Repository fit
- Existing components reused:
- Required changes:
- Predicted integration effort:
- Predicted project fit:
- Hard blockers:
- Unknowns requiring architecture or engineering review:
- Unknowns requiring local validation:

### Specialist conclusion
- Status: Shortlist | Conditional | Reject | Inconclusive
- Strongest argument:
- Strongest objection:
- Conditions:
```

## 4. Analyze mechanism, not branding

A product, model, framework, or company name is not a method description.

For each candidate, explain:

- What transformation it performs
- What information it assumes
- What persistent or temporal state it maintains
- What parts are learned, configured, mapped, indexed, or hand-authored
- What happens online
- What happens during setup, training, or deployment
- How uncertainty and failure are represented

This prevents the architect from treating incompatible black boxes as interchangeable.

## 5. Preserve comparability

For empirical claims, retain the relevant subset of:

- Task and workload
- Dataset, split, and sample composition
- Metric and threshold
- Input resolution or sequence length
- Hardware and driver
- Precision and batch size
- End-to-end versus kernel-only latency
- Warm versus cold performance
- Streaming versus offline evaluation
- External data or services
- Publication and implementation version

When conditions differ, compare qualitatively or normalize transparently rather than fabricating a precise ranking.

## 6. Public industry evidence

When a company or practitioner is cited:

- Name the publicly disclosed system and source
- Record what was actually disclosed
- Record scale and context
- Distinguish direct implementation details from high-level claims
- Explain transferability limits
- Label vendor-sponsored or company-reported evidence

Do not convert an association such as “partner,” “customer,” or “uses AI” into an implementation claim.

## 7. Implementation detail

A specialist should inspect concrete implementations deeply enough to expose:

- Exact maintained version, release, or commit
- Runtime and framework requirements
- Model, checkpoint, service, or data availability
- API shape
- Build and packaging path
- Supported platforms and hardware
- Known issues and migration constraints
- License and usage terms
- Gaps between paper and code
- Likely adapter boundary

The specialist does not need to run the implementation unless the task has entered Feasibility validation.

## 8. Composition analysis

Before recommending a family for synthesis, identify:

- Required input cadence and ordering
- Coordinate frames, schemas, encodings, or tokenization
- Stateful versus stateless behavior
- Synchronous versus asynchronous assumptions
- Batch versus stream assumptions
- Backpressure and cancellation behavior
- Shared GPU, CPU, memory, storage, or network needs
- Error propagation
- Confidence calibration
- Data retention and privacy
- Licensing interactions

A strong standalone method may be a poor component in the target architecture.

## 9. Cross-specialist reconciliation

After dossiers exist, the Research Director should build a cross-capability matrix:

| Capability | Candidate family | Input contract | Output contract | State | Critical resource | Failure behavior | Main incompatibility |
|---|---|---|---|---|---|---|---|

Resolve factual conflicts with targeted evidence. Preserve real tradeoffs.

## 10. Stop conditions

A dossier is sufficient when:

- The mechanism and assumptions are understandable
- Serious variants are covered
- Important evidence and negative evidence are present
- Interfaces and composition constraints are explicit
- Hard blockers and unknowns are separated
- The Solution Architect can use the dossier without guessing the candidate's behavior

Do not spend time documenting every minor implementation option.
