# Project charter

## Project

**Name:** Agentic Procurement Contestability Lab  
**Phase:** 0 — project foundation  
**Status:** Foundation controls only  
**Scenario:** A fictional UAE infrastructure authority considering routine, low-risk maintenance supplies

## Purpose

Establish a controlled research environment for studying whether a bounded, recommendation-only agent could support procurement contestability without displacing rules, evidence, auditability, or human authority.

Phase 0 creates the repository structure, scope controls, synthetic-data policy, backlog, and CI baseline required before any functional prototype work may begin.

## Problem statement

Routine, low-risk supply requests can involve repetitive validation and comparison work. A future prototype may explore whether structured assistance improves consistency and exposes contestability risks. Automation also creates risks: opaque ranking, hidden exclusions, concentration, conflicts, fabricated certainty, and accidental execution. The lab therefore treats bounded authority and reviewable evidence as design requirements.

## Objectives

1. Define the permitted recommendation boundary and explicit prohibited actions.
2. Establish synthetic-data, non-claims, and non-endorsement controls.
3. Create a minimal, maintainable Python repository scaffold.
4. Make future work phase-gated, testable, auditable, and reviewable.
5. Preserve human approval as a mandatory control.

## In scope for Phase 0

- project and repository documentation;
- empty folders for future source, tests, configuration, and synthetic data;
- development dependencies; and
- basic Python lint and syntax CI.

## Out of scope for Phase 0

- synthetic data or policy-rule content;
- request validation or supplier eligibility logic;
- consideration-set or ranking logic;
- risk detection and audit-record implementation;
- user interfaces or dashboards;
- governance matrices;
- evaluation or impact reports;
- valuation or financial models;
- executive memos;
- slide decks; and
- demos or deployments.

## Future capability ceiling

A separately approved prototype may validate requests, retrieve synthetic policy rules, construct a supplier consideration set, check eligibility, rank compliant suppliers, flag concentration or conflict risks, create an audit record, and require human approval.

It may never award contracts, issue purchase orders, make payments, change ranking weights, override eligibility rules, or act without human approval.

## Principles

- **Human authority:** recommendations are non-binding and require explicit review.
- **Eligibility before ranking:** an ineligible supplier cannot be rescued by a score.
- **Contestability:** material inputs, rules, exclusions, scores, and flags must be explainable and challengeable.
- **Least authority:** no production credentials, transactional integrations, or execution permissions.
- **Synthetic by design:** no real procurement, supplier, personal, or confidential records.
- **Fail closed:** missing mandatory evidence or approval prevents a recommendation from progressing.
- **Auditability:** material events and versions must be traceable.

## Deliverables and acceptance criteria

Phase 0 is complete when:

- required root documentation exists and uses consistent scope language;
- the charter, policy, backlog, and repository structure are documented;
- future implementation directories exist but contain no functional features or dataset;
- CI installs declared tooling, runs lint checks, and compiles Python paths;
- all changes pass review against `AGENTS.md`; and
- one unmerged draft pull request presents the foundation for review.

## Governance

The repository owner authorises phase transitions. Contributors implement only the authorised phase. A human reviewer must approve scope changes, rule changes, future ranking-weight changes, and any move toward demonstration or deployment. The agent itself may not modify these controls or approve its own output.

## Assumptions and constraints

- The scenario and every scenario entity are fictional.
- UAE references are contextual and do not assert sponsorship or legal compliance.
- Phase 0 makes no empirical, performance, savings, fairness, or valuation claim.
- No connection to a live procurement, ordering, payment, identity, or supplier system is permitted.

## Initial risks

| Risk | Phase 0 control |
| --- | --- |
| Scope expansion | Explicit exclusions and phase-gated backlog |
| Apparent government endorsement | Prominent disclaimer and non-claims policy |
| Real or personal data entering the lab | Synthetic-only policy |
| Autonomous procurement action | Capability ceiling and prohibited-action list |
| Opaque future decisions | Contestability and auditability requirements |
| Controls weakening over time | Repository-wide instructions and review checklist |
