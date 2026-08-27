# Expert Council Output Templates

Use only the sections needed for the requested endpoint. Keep stable IDs so a later phase can resume without repeating valid work.

## 1. Research and landscape brief

```markdown
# SOTA-first decision record

**Research date:** YYYY-MM-DD
**Repository revision:** ...
**Task:** ...
**Research depth:** Quick | Full
**Requested endpoint:** Research-only | Feasibility validation | Integration
**Council mode:** separate subagents | mixed | same-agent role-separated passes
**Decision strategy:** KEEP | ADOPT | EXTEND | COMPOSE | BUILD
**Confidence:** High | Medium | Low

## Repository constraint brief

- Existing architecture:
- Components and ownership:
- Interfaces and data contracts:
- Runtime, deployment, and hardware:
- Quality, latency, throughput, and resource constraints:
- Security, privacy, reliability, and compliance:
- Migration and rollback:
- Existing or abandoned related work:
- Unknowns:

## Capability graph

| Capability ID | Outcome | Inputs | Outputs | State | Hard constraints | Cross-cutting concerns |
|---|---|---|---|---|---|---|

## Investigation coverage

| Lane | Reviewer mode | Sources and areas searched | Evidence cutoff | Missing coverage | Confidence |
|---|---|---|---|---|---|
| Industry practice | ... | ... | ... | ... | ... |
| Academic frontier | ... | ... | ... | ... | ... |
| Ecosystem and standards | ... | ... | ... | ... | ... |

## Solution landscape

| Family ID | Core idea | Public industry evidence | Academic evidence | Mature implementations | Main constraints | Status |
|---|---|---|---|---|---|---|

## Candidate dossier summary

| Candidate ID | Domain specialist | Mechanism | Strongest evidence | Main assumption | Main failure mode | Concrete implementations | Status |
|---|---|---|---|---|---|---|---|

## Evidence audit

- Weakest material claim:
- Incomparable evidence:
- Indirect or vendor-reported adoption:
- Missing negative evidence:
- Contradictions:
- Facts that are estimates:
- Evidence that could reverse the shortlist:
```

## 2. Candidate architecture set

```markdown
## Candidate architectures

### ARCH-01 — <name>

- Strategy:
- Components and implementations:
- Responsibilities and ownership:
- Interfaces, schemas, events, and state:
- Data and control flow:
- Runtime and topology:
- Concurrency, queues, retries, cancellation, and backpressure:
- Failure isolation and degraded mode:
- Security and privacy:
- Observability and operations:
- Preliminary latency and resource budget:
- Migration and rollback:
- Supporting evidence:
- Main assumptions:
- Main objection:

### ARCH-02 — <name>

...
```

Use `architecture-synthesis.md` for the full option schema.

## 3. Comparative Architecture Review Gate

```markdown
## Architecture Review Gate

**Reviewer mode:** dedicated architect | separate reviewer context | same-agent structured review
**Options reviewed:** ARCH-01, ARCH-02, ...

### Hard blockers

- ARCH-01:
- ARCH-02:

### Scorecards

| Dimension | Weight | ARCH-01 | Evidence | ARCH-02 | Evidence |
|---|---:|---:|---|---:|---|
| Boundary and responsibility fit | 15% | ... | ... | ... | ... |
| Interface and data-contract fit | 15% | ... | ... | ... | ... |
| Dependency, runtime, and platform fit | 15% | ... | ... | ... | ... |
| Deployment, topology, and resource fit | 10% | ... | ... | ... | ... |
| Reliability and failure isolation | 10% | ... | ... | ... | ... |
| Security, privacy, and compliance fit | 10% | ... | ... | ... | ... |
| Observability and operability | 10% | ... | ... | ... | ... |
| Migration, compatibility, and rollback | 5% | ... | ... | ... | ... |
| Maintainability, ownership, and evolution | 10% | ... | ... | ... | ... |

### Result

| Architecture | Score | Gate | Strongest compatibility argument | Strongest objection | Required conditions |
|---|---:|---|---|---|---|

### Architecture recommendation

- Preferred option:
- Why alternatives lost:
- Required redesign:
- Conditions transferred to engineering review:
- Minority objection:
- Remaining uncertainty:
```

## 4. Engineering Readiness Gate

```markdown
## Engineering Readiness Gate

**Reviewer mode:** dedicated engineering reviewer | separate reviewer context | same-agent structured engineering review
**Architectures reviewed:** ...
**Implementation bundles:** BUNDLE-01, BUNDLE-02, ...

### Concrete bundles

- BUNDLE-01:
  - Libraries/frameworks/models/services:
  - Exact versions or commits:
  - Runtime, OS, drivers, hardware:
  - Build and deployment path:

### Pairwise compatibility matrix

| Producer/dependency | Consumer/dependent | Contract | Runtime/version | Resource interaction | License/security | Status | Adapter |
|---|---|---|---|---|---|---|---|

### Resource and latency budget

| Stage | Implementation | p50 budget | p95 budget | CPU | GPU/VRAM | RAM | Network | Storage | Concurrency | Evidence type |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|

### Hard blockers

- BUNDLE-01:
- BUNDLE-02:

### Scorecards

| Dimension | Weight | BUNDLE-01 | Evidence | BUNDLE-02 | Evidence |
|---|---:|---:|---|---:|---|
| Implementation availability and maturity | 10% | ... | ... | ... | ... |
| Dependency, version, runtime, and platform compatibility | 20% | ... | ... | ... | ... |
| Interface and data-representation compatibility | 15% | ... | ... | ... | ... |
| Resource and performance budget | 20% | ... | ... | ... | ... |
| Build, deploy, and operational path | 10% | ... | ... | ... | ... |
| Reliability, observability, and testability | 10% | ... | ... | ... | ... |
| Security, license, and supply chain | 5% | ... | ... | ... | ... |
| Migration, rollback, ownership, and maintainability | 10% | ... | ... | ... | ... |

### Result

| Bundle | Score | Gate | Main advantage | Main engineering risk | Estimated effort | Conditions |
|---|---:|---|---|---|---|---|

### Engineering recommendation

- Preferred bundle:
- Resource placement:
- Headroom:
- Build/deploy plan:
- Ownership:
- Conditions transferred to feasibility:
- Remaining unknowns:
```

## 5. Final Research-only decision

```markdown
## Final decision

- **Research SOTA:** ...
- **Public industry practice:** ...
- **Most mature ecosystem path:** ...
- **Domain-specialist conclusion:** ...
- **Preferred architecture:** ARCH-XX
- **Architecture gate:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE
- **Preferred implementation bundle:** BUNDLE-XX
- **Engineering gate:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE
- **Engineering recommendation:** ...
- **Why these conclusions differ:** ...
- **Rejected families, architectures, and bundles:** ...
- **Decision strategy:** KEEP | ADOPT | EXTEND | COMPOSE | BUILD
- **Smallest production boundary:** ...
- **Confidence:** ...
- **Missing evidence:** ...
- **Proposed feasibility contract:** ...
```

For Research-only, stop here.

## 6. Feasibility Gate

```markdown
## Feasibility Gate

**Validation date:** ...
**Repository revision:** ...
**Architecture:** ARCH-XX
**Implementation bundle:** BUNDLE-XX
**Status:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE

### Contract

- Hypothesis:
- Representative setup:
- Hard thresholds:
- Architecture conditions:
- Engineering conditions:
- Isolation and cleanup:

### Environment

- Hardware/OS:
- Runtime/framework/drivers:
- Versions:
- Data or traffic:
- Commands and configuration:

### Results

| Criterion | Threshold | Measured result | Outcome | Evidence |
|---|---:|---:|---|---|

### Findings

- Locally measured:
- Differences from external claims:
- Compatibility findings:
- Resource findings:
- Failure modes:
- Adapter and integration surface:

### Transition

- Next action:
- Conditions:
- Production boundary:
- Preserved acceptance test:
- Cleanup:
- Remaining uncertainty:
```

For validation-only, stop here.

## 7. Integration result

```markdown
## Integration result

**Source decision record:** ...
**Architecture gate:** PASS | CONDITIONAL PASS
**Engineering gate:** PASS | CONDITIONAL PASS
**Feasibility gate:** PASS | CONDITIONAL PASS
**Integrated architecture:** ARCH-XX
**Implementation bundle:** BUNDLE-XX
**Decision strategy:** KEEP | ADOPT | EXTEND | COMPOSE | BUILD

### Production changes

- Reused components:
- Project-specific code:
- Interfaces and contracts:
- Dependencies and configuration:
- Resource placement:
- Observability and ownership:
- Intentionally excluded experiment artifacts:

### Verification

| Preserved condition | Integrated result | Outcome |
|---|---:|---|

### Deviations

- Architecture delta:
- Engineering-bundle delta:
- Feasibility delta:
- Re-review performed:

### Rollout and rollback

- Rollout:
- Rollback:
- Remaining conditions:
- Follow-up:
```

## Rules

- Include source links or host-native citations for material external claims
- Label evidence type
- Use exact versions and dates for time-sensitive facts
- Do not claim a public company implementation that was not disclosed
- Do not claim consensus when roles disagree materially
- Do not average away hard blockers
- Separate estimates from local measurements
- Keep output proportional to the task
- Stop at the user's requested endpoint
