# Verdict Templates

Use the template for the phase being completed. Keep the report proportional to the decision and preserve enough information for a later phase to resume without repeating all prior work.

## Phase A: Full research and architecture verdict

```markdown
## SOTA-first research verdict

**Research date:** YYYY-MM-DD  
**Task:** <precise capability>  
**Research depth:** Full  
**Requested endpoint:** Research-only | Feasibility validation | Integration  
**Decision:** KEEP | ADOPT | EXTEND | COMPOSE | BUILD  
**Confidence:** High | Medium | Low

### Project constraints

- <hard constraint>
- <hard constraint>
- <important preference>

### Search coverage

- Repository: <files, areas, architecture, and history inspected>
- External: <official docs, registries, papers, benchmarks, repositories, advisories, architecture reports>
- Unavailable or skipped: <channel and impact on confidence>

### Candidate comparison

| Candidate | Primary evidence | Research strength | Predicted project fit | Architecture review need | Main limitation | Status |
|---|---|---:|---:|---|---|---|
| A | <source> | 1–5 | 1–5 | Required/Optional/None | <limitation> | Finalist/Rejected |
| B | <source> | 1–5 | 1–5 | Required/Optional/None | <limitation> | Finalist/Rejected |
| C | <source> | 1–5 | 1–5 | Required/Optional/None | <limitation> | Finalist/Rejected |

### Research conclusions

- **Research SOTA:** <candidate or “not established”>, because <evidence and comparison boundary>.
- **Engineering recommendation:** <candidate>, because <fit to constraints>.
- **Why they differ:** <state explicitly, or “They are the same.”>
- **Rejected finalists:** <candidate → concrete reason>.

### Proposed integration architecture

- Existing boundaries affected: <components, services, modules, owners>
- New or changed responsibilities: <summary>
- Interfaces and data contracts: <APIs, schemas, events, state>
- Data and control flow: <compact description or text diagram>
- Dependencies/runtime/platform: <changes>
- Deployment and resource topology: <processes, services, hardware, network paths>
- Failure, security, and privacy boundaries: <summary>
- Migration, rollout, and rollback: <summary>

### Architecture Expert Review

- **Reviewer mode:** Dedicated architect/subagent | Same-agent structured review
- **Architecture gate:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE
- **Architecture compatibility score:** <0–100>
- **Hard blocker:** None | <blocker>

| Architecture dimension | Weight | Score (1–5) | Evidence and risk |
|---|---:|---:|---|
| Boundary and responsibility fit | 15% | <score> | <evidence/risk> |
| Interface and data-contract fit | 15% | <score> | <evidence/risk> |
| Dependency, runtime, and platform fit | 15% | <score> | <evidence/risk> |
| Deployment, topology, and resource fit | 10% | <score> | <evidence/risk> |
| Reliability and failure isolation | 10% | <score> | <evidence/risk> |
| Security, privacy, and compliance fit | 10% | <score> | <evidence/risk> |
| Observability and operability | 10% | <score> | <evidence/risk> |
| Migration, compatibility, and rollback | 5% | <score> | <evidence/risk> |
| Maintainability, ownership, and evolution | 10% | <score> | <evidence/risk> |

- **Strongest compatibility argument:** <argument>
- **Strongest architecture objection:** <objection>
- **Simpler alternative considered:** <alternative or “None identified”>
- **Required conditions/redesign:** <conditions>
- **Impact on engineering recommendation:** Unchanged | Changed to <candidate/design>, because <reason>

### Proposed production boundary

- Reuse: <library, model, service, protocol, or standard>
- Custom code: <small project-specific layer only>
- Do not build: <capability delegated to the mature component>
- Architecture invariants to preserve: <boundaries/contracts/failure model>
- Rollback: <how to reverse safely when relevant>

### Feasibility handoff

- Candidate to validate: <candidate and exact version/checkpoint/commit>
- Architecture conditions to test: <conditions inherited from review>
- Critical assumptions: <project-specific claims not proven by research or architecture review>
- Highest-risk unknown: <unknown most likely to change the decision>
- Representative environment: <hardware, runtime, data, traffic, or deployment conditions>
- Proposed thresholds: <measurable acceptance criteria>
- Suggested smallest spike: <falsifiable experiment>

### Unknowns and assumptions

- <remaining uncertainty>
- <assumption that could change the decision>
```

When the requested endpoint is Research-only, stop after this verdict and any required Architecture Expert Review.

## Phase A: Quick research verdict

```markdown
**SOTA-first research (Quick):** <KEEP/ADOPT/EXTEND/COMPOSE/BUILD> `<candidate>`.

- Requested endpoint: Research-only | Feasibility validation | Integration
- Repository check: <existing solution or relevant constraint>
- Evidence checked: <official source/version and one corroborating signal when available>
- Why this choice: <one or two concrete reasons>
- Main caveat: <risk or unknown>
- Architecture precheck: None | Optional | Required, because <reason>
- Feasibility need: <none, or the exact assumption to test>
- Proposed boundary: <what will be reused versus written>
```

## Architecture Review Gate only

```markdown
## SOTA-first architecture review

**Review date:** YYYY-MM-DD  
**Repository revision:** <commit or working-tree state>  
**Candidate/design:** <name, version, and integration design reference>  
**Reviewer mode:** Dedicated architect/subagent | Same-agent structured review  
**Status:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE  
**Architecture compatibility score:** <0–100>

### Proposed architecture

- Boundaries and responsibilities: <summary>
- Interfaces/data contracts: <summary>
- Runtime/dependencies/platform: <summary>
- Deployment/resource topology: <summary>
- Failure/security/privacy model: <summary>
- Ownership/migration/rollback: <summary>

### Scorecard

| Dimension | Weight | Score (1–5) | Evidence and risk |
|---|---:|---:|---|
| Boundary and responsibility fit | 15% | <score> | <evidence/risk> |
| Interface and data-contract fit | 15% | <score> | <evidence/risk> |
| Dependency, runtime, and platform fit | 15% | <score> | <evidence/risk> |
| Deployment, topology, and resource fit | 10% | <score> | <evidence/risk> |
| Reliability and failure isolation | 10% | <score> | <evidence/risk> |
| Security, privacy, and compliance fit | 10% | <score> | <evidence/risk> |
| Observability and operability | 10% | <score> | <evidence/risk> |
| Migration, compatibility, and rollback | 5% | <score> | <evidence/risk> |
| Maintainability, ownership, and evolution | 10% | <score> | <evidence/risk> |

### Adversarial findings

- Hard blocker: None | <blocker>
- Most likely invariant to break: <finding>
- Largest coupling/ownership risk: <finding>
- Hardest contract or rollback problem: <finding>
- Largest new failure domain: <finding>
- Strongest objection: <finding>
- Simpler alternative: <alternative>

### Gate decision

- Conditions/redesign: <details>
- Recommendation impact: Unchanged | Changed to <candidate/design>
- Feasibility criteria inherited from architecture: <measurable conditions>
- Next action: Stop | Feasibility validation | Review next finalist | Redesign
```

## Phase B: Feasibility verdict

```markdown
## SOTA-first feasibility verdict

**Validation date:** YYYY-MM-DD  
**Repository revision:** <commit or working-tree state>  
**Candidate:** <name and exact version/checkpoint/commit>  
**Architecture gate:** PASS | CONDITIONAL PASS  
**Architecture score:** <0–100>  
**Status:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE  
**Requested endpoint:** Feasibility validation | Integration

### Validation contract

- Hypothesis: <falsifiable project-specific claim>
- Architecture conditions inherited: <conditions>
- Representative setup: <data, traffic, hardware, runtime, deployment conditions>
- Hard thresholds: <non-negotiable acceptance criteria>
- Isolation method: <temporary directory, worktree, branch, shadow path, or other>

### Environment

- Hardware/OS: <details>
- Runtime/framework/drivers: <details>
- Candidate configuration: <precision, batch size, resolution, service tier, or other material settings>
- Commands/procedure: <reproducible summary>

### Results

| Criterion | Threshold | Measured result | Outcome |
|---|---:|---:|---|
| <criterion> | <threshold> | <measurement> | Pass/Fail/Unresolved |
| <architecture-derived criterion> | <threshold> | <measurement> | Pass/Fail/Unresolved |

### Findings

- Locally measured: <results produced by this validation>
- External claim comparison: <where the setup or result differs from published/vendor conditions>
- Architecture assumptions: <verified, disproved, or unresolved>
- Integration assumption: <verified, disproved, or unresolved>
- Failure modes observed: <details>

### Transition decision

- Architecture re-review needed: Yes/No, because <boundary, contract, topology, dependency, or ownership change>
- Next action: Integrate | Validate next finalist | Revise research verdict | Redesign | Stop
- Conditions: <requirements for a conditional pass, or “None”>
- Production boundary: <clean implementation surface if integration is allowed>
- Preserved acceptance test: <test or benchmark to carry into integration>
- Cleanup state: <removed artifacts, or exact artifacts that remain>

### Remaining uncertainty

- <unknown that still matters>
```

For a validation-only request, stop after this verdict. Do not integrate production code.

## Phase C: Integration completion

```markdown
## SOTA-first integration result

**Source research verdict:** <date or reference>  
**Architecture gate:** PASS | CONDITIONAL PASS  
**Architecture compatibility score:** <0–100>  
**Feasibility status:** PASS | CONDITIONAL PASS  
**Decision:** KEEP | ADOPT | EXTEND | COMPOSE | BUILD  
**Integrated candidate:** <name and exact version/checkpoint/commit>

### Production architecture

- Preserved component boundaries: <details>
- Interfaces and contracts: <details>
- Runtime/dependencies/deployment: <details>
- Failure/security/privacy boundaries: <details>
- Ownership and operations: <details>
- Migration/rollout/rollback: <details>

### Production changes

- Reused component: <mature capability adopted>
- Project-specific code: <minimal adapter or custom boundary>
- Configuration/dependencies: <material changes>
- Intentionally excluded: <experimental or delegated capability not promoted>

### Verification

| Architecture or feasibility criterion | Integrated result | Outcome |
|---|---:|---|
| <architecture condition> | <result> | Pass/Fail |
| <criterion preserved from feasibility> | <measurement> | Pass/Fail |

### Differences from reviewed design and spike

- <difference and impact, or “None”>
- Architecture dimensions re-reviewed: <dimensions or “None”>

### Rollback and follow-up

- Rollback path: <how to reverse>
- Operational owner: <team/component owner>
- Remaining condition or risk: <details>
```

## Rules for using the templates

- Do not create a long Full-mode report for a narrow Quick-mode choice.
- Include source links or host-native citations for material external claims.
- Use exact dates and versions for time-sensitive information.
- Do not claim a research winner where evidence is not comparable; say “not established” and explain why.
- Do not claim a dedicated architecture expert or subagent was used when the review was performed by the same agent.
- Score a concrete proposed architecture, not an undefined intention.
- Hard architecture blockers override the weighted score.
- Keep Research strength, Predicted project fit, Architecture compatibility, and locally measured feasibility separate.
- Research-only means no feasibility spike or implementation unless separately requested.
- Feasibility validation means no production integration unless separately requested.
- When the user requested the full pipeline, continue through each passing gate without an unnecessary approval pause.
- After architecture or feasibility `FAIL`, or material `INCONCLUSIVE`, do not integrate the candidate as though it passed.
