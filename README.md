# Agentic Procurement Contestability Lab

> FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY.  
> NOT A REAL PROCUREMENT RECORD OR DECISION.  
> NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT.

This branch contains Phase 1 synthetic scenario data for a bounded procurement-research prototype concerning routine, low-risk maintenance supplies.

## Phase 1 contents

- 100 fictional suppliers across five maintenance-supply categories;
- 200 fictional procurement requests;
- five category-matched offers per request;
- synthetic policy fixtures that are not applied by code;
- a complete data dictionary and scenario-design document;
- a deterministic generator using seed `20260827`; and
- validation and reproducibility tests.

## Scope boundary

This phase contains no ranking engine, eligibility engine, supplier recommendation, ground-truth ranking, award decision, scoring weight, competition result, dashboard, governance control matrix, evaluation report, valuation model, memo, slide deck, demo, external integration, API call, or real-data retrieval.

All entities, records, assumptions, and outputs are invented for research and demonstration. They do not describe a real authority, supplier, person, procurement, transaction, policy, or outcome.

## Regenerate and test

Python 3.12 is used in CI. The generator and tests use only the Python standard library.

```bash
python scripts/generate_synthetic_data.py
python -m unittest discover -s tests -v
```
