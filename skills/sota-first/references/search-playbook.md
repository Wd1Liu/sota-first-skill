# Landscape Investigation Playbook

Use this reference for Full-mode investigation. The purpose is to discover the meaningful solution landscape before selecting implementations.

Broad discovery and narrow verification are separate activities:

```text
Discover broadly
      ↓
Cluster solution families
      ↓
Prune with hard constraints
      ↓
Deeply verify serious finalists
```

Do not begin with a favored library or paper and search only for confirming evidence.

## 1. Start from the capability graph

For every sub-capability and cross-cutting requirement, generate:

- Exact terms and synonyms
- Adjacent fields that solve an equivalent problem
- Architecture and systems terminology
- Real-time, streaming, online, offline, edge, cloud, mobile, or embedded variants
- Hardware, latency, quality, privacy, license, and deployment constraints
- Evidence-type modifiers such as paper, benchmark, official code, production architecture, engineering blog, postmortem, migration, failure mode, or security advisory

Search for methods, system shapes, and implementation ecosystems.

## 2. Industry Practice lane

Investigate how relevant leading organizations publicly implement similar capabilities.

Potential targets:

- Large technology companies with comparable systems
- Category-leading product companies
- High-signal startups or “star companies” in the exact field
- Open-source maintainers and standards bodies
- Recognized practitioners, conference speakers, and system authors
- Vendors that publish sufficiently detailed reference architectures

Priority sources:

1. Official engineering blogs and architecture documentation
2. Conference talks, technical presentations, and system papers
3. Official open-source repositories and reference implementations
4. Public postmortems, migration reports, and operational case studies
5. Primary interviews or detailed practitioner writeups
6. Vendor case studies, clearly labeled as vendor-reported

For every public adoption claim, record:

```markdown
- Organization:
- Product or system:
- Public source and date:
- Disclosed method or architecture:
- Scale and operating context:
- Evidence label:
- Relevance to this repository:
- Missing details:
```

Rules:

- Never claim a company uses an undisclosed method
- Do not treat a marketing page, job listing, package telemetry, or technology-detection site as proof
- Use indirect signals only to discover better primary sources
- Explain when the organization's scale, team, data, hardware, or regulatory context makes its design non-transferable
- “Used by a famous company” is not a quality score

## 3. Academic Frontier lane

Investigate the research frontier and its implementation reality.

Priority sources:

1. Recent surveys, taxonomies, and benchmark papers
2. Original peer-reviewed papers and clearly labeled preprints
3. Official project pages, repositories, checkpoints, model cards, and dataset cards
4. Benchmark and leaderboard maintainers
5. Independent reproductions, ablations, follow-up papers, and failure analyses
6. Reputable research-engineering reports with disclosed conditions

For every result, preserve:

- Task definition
- Dataset and split
- Metric
- Evaluation protocol
- Input resolution, sequence length, or context
- Hardware, precision, batch size, and latency definition
- Training or external data
- Publication and last-update date
- Peer-reviewed, preprint, vendor-reported, or independent-reproduction status
- Availability of code, weights, data, and license

Do not compare headline numbers across materially different settings.

## 4. Ecosystem and Standards lane

Investigate reusable and production-mature implementation paths.

Priority sources:

1. Official standards and specifications
2. Maintained open-source projects
3. Package registries and compatibility tables
4. Reference architectures and SDKs
5. Security advisories, release notes, and migration guides
6. Maintainer issue discussions
7. Vendor products, quotas, service limits, and support windows

Check:

- Current release and maintenance activity
- API stability and support lifecycle
- Runtime, framework, compiler, operating-system, and platform compatibility
- Transitive dependencies
- License and commercial-use terms
- Security posture and advisories
- Observability and testability
- Failure behavior
- Migration and rollback
- Ecosystem integrations and lock-in

Repository stars, downloads, and citations are supporting signals only.

## 5. Architecture search

Search explicitly for system design, not only methods.

Useful query classes:

```text
<capability> reference architecture
<capability> production architecture
<capability> system design
<capability> engineering blog
<capability> conference talk
<capability> deployment architecture
<capability> edge architecture
<capability> real-time pipeline
<capability> scaling
<capability> migration
<capability> postmortem
<capability> failure modes
<capability> alternative approaches
```

For research-heavy systems:

```text
<capability> survey
<capability> benchmark
<capability> official implementation
<method family> inference latency
<method family> memory benchmark
<method family> independent reproduction
<method family> streaming
<method family> limitations
```

## 6. Negative-evidence search

For every serious family, search for:

- Limitations and failure modes
- Unmaintained or abandoned implementations
- Security advisories
- Migration pain
- Production incidents and postmortems
- Incompatible versions or drivers
- Dataset leakage or benchmark caveats
- Missing weights, services, data, calibration, or licenses
- Real-time or resource failures
- Community reports that point to primary evidence

A candidate with only positive evidence is under-investigated.

## 7. Source labels

Use these labels consistently:

- **Primary official** — specification, official documentation, original paper, official repository, official release, official postmortem
- **Peer-reviewed**
- **Preprint**
- **Company-reported**
- **Vendor-reported**
- **Independent reproduction**
- **Maintainer-reported**
- **Community-reported**
- **Locally measured**

Do not blend them into a single confidence category.

## 8. Landscape map

The broad phase should produce:

```markdown
## Solution landscape

### Capability graph
- <capability>
- <capability>

### Solution families
| Family ID | Core idea | Public industry evidence | Academic evidence | Mature implementations | Main constraints | Status |
|---|---|---|---|---|---|---|
| FAMILY-01 | ... | ... | ... | ... | ... | Shortlist/Watch/Reject |

### Cross-family observations
- Common architecture patterns:
- Important disagreements:
- Missing evidence:
- Negative evidence:
- Families excluded by hard constraints:

### Shortlist for domain analysis
- FAMILY-01:
- FAMILY-02:
- FAMILY-03:
```

The table should represent distinct solution families, not near-identical repositories.

## 9. Minimum Full-mode coverage

Aim for:

- The meaningful industry, academic, and ecosystem lanes
- At least three distinct solution families when the field genuinely offers them
- Primary evidence for every shortlisted family
- Current version, license, and implementation availability checks
- At least one negative-evidence search for every finalist
- Public industry evidence when available, or an explicit statement that no technically specific disclosure was found
- Recent academic evidence when relevant
- Architecture-level evidence, not only component benchmarks

When a lane is unavailable or irrelevant, state why and lower confidence appropriately.

## 10. Search log

Keep a compact ledger:

- Search date and evidence cutoff
- Repository revision
- Investigator lane
- Queries or categories
- Sources and labels
- Candidate IDs affected
- Contradictions
- Unavailable channels
- Unresolved facts

The user-facing report may summarize the ledger, but the decision must remain traceable.

## 11. Stop conditions

Stop broad discovery when:

- New sources mostly map to existing families
- Major adjacent solution classes have been checked
- Serious families have primary evidence
- Hard constraints can eliminate unsuitable families
- Domain Specialists can meaningfully distinguish the shortlist
- Additional searching is unlikely to change the family map

Do not stop merely because three popular repositories were found.
