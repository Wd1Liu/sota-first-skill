# Verdict Templates

Use the template for the phase being completed. Keep the report proportional to the decision and preserve enough information for a later phase to resume without repeating all prior work.

## Phase A: Full research verdict

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

- Repository: <files, areas, and history inspected>
- External: <official docs, registries, papers, benchmarks, repositories, advisories>
- Unavailable or skipped: <channel and impact on confidence>

### Candidate comparison

| Candidate | Primary evidence | Research strength | Project fit | Main limitation | Status |
|---|---|---:|---:|---|---|
| A | <source> | 1–5 | 1–5 | <limitation> | Finalist/Rejected |
| B | <source> | 1–5 | 1–5 | <limitation> | Finalist/Rejected |
| C | <source> | 1–5 | 1–5 | <limitation> | Finalist/Rejected |

### Conclusions

- **Research SOTA:** <candidate or “not established”>, because <evidence and comparison boundary>.
- **Engineering recommendation:** <candidate>, because <fit to constraints>.
- **Why they differ:** <state explicitly, or “They are the same.”>
- **Rejected finalists:** <candidate → concrete reason>.

### Proposed implementation boundary

- Reuse: <library, model, service, protocol, or standard>
- Custom code: <small project-specific layer only>
- Do not build: <capability delegated to the mature component>
- Rollback: <how to reverse safely when relevant>

### Feasibility handoff

- Candidate to validate: <candidate and exact version/checkpoint/commit>
- Critical assumptions: <project-specific claims not proven by external research>
- Highest-risk unknown: <unknown most likely to change the decision>
- Representative environment: <hardware, runtime, data, traffic, or deployment conditions>
- Proposed thresholds: <measurable acceptance criteria>
- Suggested smallest spike: <falsifiable experiment>

### Unknowns and assumptions

- <remaining uncertainty>
- <assumption that could change the decision>
```

When the requested endpoint is Research-only, stop after this verdict.

## Phase A: Quick research verdict

```markdown
**SOTA-first research (Quick):** <KEEP/ADOPT/EXTEND/COMPOSE/BUILD> `<candidate>`.

- Requested endpoint: Research-only | Feasibility validation | Integration
- Repository check: <existing solution or relevant constraint>
- Evidence checked: <official source/version and one corroborating signal when available>
- Why this choice: <one or two concrete reasons>
- Main caveat: <risk or unknown>
- Feasibility need: <none, or the exact assumption to test>
- Proposed boundary: <what will be reused versus written>
```

## Phase B: Feasibility verdict

```markdown
## SOTA-first feasibility verdict

**Validation date:** YYYY-MM-DD  
**Repository revision:** <commit or working-tree state>  
**Candidate:** <name and exact version/checkpoint/commit>  
**Status:** PASS | CONDITIONAL PASS | FAIL | INCONCLUSIVE  
**Requested endpoint:** Feasibility validation | Integration

### Validation contract

- Hypothesis: <falsifiable project-specific claim>
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
| <criterion> | <threshold> | <measurement> | Pass/Fail/Unresolved |

### Findings

- Locally measured: <results produced by this validation>
- External claim comparison: <where the setup or result differs from published/vendor conditions>
- Integration assumption: <verified, disproved, or unresolved>
- Failure modes observed: <details>

### Transition decision

- Next action: Integrate | Validate next finalist | Revise research verdict | Stop
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
**Feasibility status:** PASS | CONDITIONAL PASS  
**Decision:** KEEP | ADOPT | EXTEND | COMPOSE | BUILD  
**Integrated candidate:** <name and exact version/checkpoint/commit>

### Production changes

- Reused component: <mature capability adopted>
- Project-specific code: <minimal adapter or custom boundary>
- Configuration/dependencies: <material changes>
- Intentionally excluded: <experimental or delegated capability not promoted>

### Verification

| Acceptance criterion | Integrated result | Outcome |
|---|---:|---|
| <criterion preserved from feasibility> | <measurement> | Pass/Fail |
| <criterion> | <measurement> | Pass/Fail |

### Differences from the spike

- <difference and impact, or “None”>

### Rollback and follow-up

- Rollback path: <how to reverse>
- Remaining condition or risk: <details>
```

## Rules for using the templates

- Do not create a long Full-mode report for a narrow Quick-mode choice.
- Include source links or host-native citations for material external claims.
- Use exact dates and versions for time-sensitive information.
- Do not claim a research winner where evidence is not comparable; say “not established” and explain why.
- Separate external claims from locally measured feasibility and integration results.
- Research-only means no feasibility spike or implementation unless separately requested.
- Feasibility validation means no production integration unless separately requested.
- When the user requested research, validation, and implementation in one task, continue through each passing gate without an unnecessary approval pause.
- After FAIL or material INCONCLUSIVE status, do not integrate the candidate as though it passed.
