# Repository instructions

These instructions apply to the entire repository.

## Project boundary

This repository is an independent, fictional, synthetic research lab. Do not imply that the UAE Government, a UAE public authority, or any real organisation commissioned, approved, sponsored, adopted, or endorsed it.

Current authorised scope is Phase 1: project controls plus deterministic synthetic scenario data and inert policy fixtures. Do not implement Phase 2 or later work: ranking or eligibility logic, recommendations, scoring weights, competition results, dashboard, governance matrix, evaluation report, valuation model, memo, slide deck, demo, external integrations, API calls, real-data retrieval, or procurement execution.

## Non-negotiable agent constraints

Any future prototype must remain recommendation-only. It may be designed to validate requests, retrieve synthetic policy rules, construct a consideration set, check eligibility, rank compliant suppliers, flag concentration or conflict risks, create an audit record, and request human approval.

It must never be designed or described as able to:

- award contracts;
- issue purchase orders;
- make or initiate payments;
- change its own ranking weights;
- override eligibility rules;
- bypass or fabricate human approval; or
- take autonomous procurement action.

## Data and claims

Follow `docs/policies/SYNTHETIC_DATA_AND_NON_CLAIMS.md`.

- Use only clearly labelled fictional and synthetic organisations, people, transactions, policies, and results.
- Do not add personal data, confidential data, live procurement records, or scraped supplier data.
- Do not present synthetic results as measured public-sector outcomes.
- Keep provenance, assumptions, seeds, and transformations reviewable when data work is later authorised.
- Put a visible synthetic/non-endorsement notice on future user-facing outputs.

## Engineering controls

- Keep business rules explicit, deterministic, versioned, and testable.
- Preserve immutable audit evidence; never silently rewrite past decisions or approvals.
- Separate recommendation generation from human approval and from any external execution system.
- Fail closed when required inputs, rules, eligibility evidence, or approval are missing.
- Do not add credentials, secrets, production endpoints, or write-capable procurement integrations.
- Keep changes within the currently authorised backlog phase.
- Add or update tests and documentation with future executable changes.
- Do not weaken these controls without explicit owner approval and a documented rationale.

## Review checklist

Before proposing a change, confirm that it:

1. stays within the authorised phase;
2. uses only synthetic inputs and claims;
3. preserves human approval and contestability;
4. introduces no pathway to contract award, purchasing, or payment;
5. leaves an auditable explanation of material decisions; and
6. passes the repository CI checks.
