# Development backlog

This backlog is a scope-control document, not authorisation to implement deferred work. Only Phase 0 is authorised in the current branch.

## Phase 0 — project foundation

| ID | Item | Acceptance signal | Status |
| --- | --- | --- | --- |
| P0-001 | Core repository documentation | README, instructions, and disclaimer use consistent boundaries | Complete in this PR |
| P0-002 | Project charter | Purpose, scope, capability ceiling, governance, and risks documented | Complete in this PR |
| P0-003 | Synthetic-data and non-claims policy | Synthetic-only, provenance, labelling, and non-endorsement rules documented | Complete in this PR |
| P0-004 | Approved structure | Future directories are documented and empty of features/data | Complete in this PR |
| P0-005 | Development backlog | Later work is visible but explicitly deferred | Complete in this PR |
| P0-006 | Basic Python CI | Dependency install, lint, and syntax compilation configured | Complete in this PR |

## Deferred phases

No deferred item may start until the repository owner explicitly authorises its phase and the pull request records the scope decision.

### Phase 1 — synthetic scenario and policy fixtures

- Define schemas and validation constraints.
- Generate clearly labelled, reproducible synthetic records.
- Add synthetic policy-rule fixtures and leakage checks.

### Phase 2 — bounded recommendation engine

- Validate requests.
- Retrieve versioned synthetic policy rules.
- Construct supplier consideration sets.
- Apply eligibility before scoring.
- Rank only compliant suppliers using owner-approved, immutable weights.
- Flag concentration and conflict risks.
- Produce a versioned audit record.
- Block progression pending explicit human approval.

### Phase 3 — review interface

- Build a dashboard that exposes evidence, exclusions, scores, flags, limitations, and the approval gate.
- Ensure the interface cannot award, order, pay, override rules, or silently change weights.

### Phase 4 — governance and evaluation

- Create the governance matrix.
- Define synthetic evaluation protocols and failure tests.
- Prepare an evaluation report that makes no real-world or government-endorsed claims.

### Phase 5 — decision-support materials

- Prepare a valuation model with explicit hypothetical assumptions.
- Draft a non-claims-compliant memo and slide deck.
- Prepare a bounded demo using synthetic inputs only.

## Cross-cutting engineering backlog

- Threat modelling and misuse cases.
- Rule, model, data, and configuration versioning.
- Deterministic tests for eligibility and scoring.
- Fairness and contestability tests.
- Audit-record integrity and retention design.
- Human-approval authentication and separation-of-duties design.
- Accessibility, security, privacy, and documentation review.

## Definition of ready for a future phase

A phase is ready only when its owner, inputs, outputs, prohibited actions, acceptance criteria, test plan, and human-review points are documented and explicitly approved.

## Definition of done

A future item is done only when implementation, tests, documentation, limitations, synthetic labels, audit evidence, and human-review controls are complete and reviewed. Passing synthetic tests is not evidence of production readiness or real-world impact.
