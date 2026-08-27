# Verdict Templates

## Full mode

```markdown
## SOTA-first verdict

**Research date:** YYYY-MM-DD  
**Task:** <precise capability>  
**Mode:** Full  
**Decision:** KEEP | ADOPT | EXTEND | COMPOSE | BUILD  
**Confidence:** High | Medium | Low

### Project constraints

- <hard constraint>
- <hard constraint>
- <important preference>

### Search coverage

- Repository: <files/areas/history inspected>
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

### Implementation boundary

- Reuse: <library/model/service/standard already selected>
- Custom code: <small project-specific layer only>
- Do not build: <capability delegated to mature component>
- Validation: <tests, benchmark, spike, acceptance criteria>
- Rollback: <how to reverse safely when relevant>

### Unknowns and assumptions

- <remaining uncertainty>
- <assumption that could change the decision>
```

## Quick mode

```markdown
**SOTA-first (Quick):** <KEEP/ADOPT/EXTEND/COMPOSE/BUILD> `<candidate>`.

- Repository check: <existing solution or relevant constraint>
- Evidence checked: <official source/version and one corroborating signal when available>
- Why this choice: <one or two concrete reasons>
- Main caveat: <risk or unknown>
- Implementation boundary: <what will be reused versus written>
```

## Rules for using the templates

- Keep the report proportional to the decision. Do not create a long report for a narrow Quick-mode choice.
- Include source links or host-native citations for material external claims.
- Use exact dates and versions for time-sensitive information.
- Do not claim a winner where evidence is not comparable; say “not established” and explain why.
- When the user asked for implementation, continue after the verdict in the same task.
