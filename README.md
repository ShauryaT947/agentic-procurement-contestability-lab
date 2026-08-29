# Agentic Procurement Contestability Lab

> **FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY.**  
> **NOT A REAL PROCUREMENT RECORD OR DECISION.**  
> **NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT.**

The Agentic Procurement Contestability Lab is an independent research prototype for a fictional UAE infrastructure authority considering routine, low-risk maintenance supplies. It explores how a tightly bounded recommendation agent might support contestability, auditability, and human review without taking procurement action.

## Repository status

This repository now retains:

- **Phase 0 — project controls:** scope boundaries, governance instructions, disclaimer, project charter, phase-gated backlog, approved structure, synthetic-data/non-claims policy, development requirements, and empty future source/configuration scaffolds.
- **Phase 1 — synthetic scenario data:** deterministic fictional suppliers, procurement requests, relational offers, inert policy fixtures, data documentation, a fixed-seed generator, and validation tests.

No ranking engine, eligibility engine, supplier recommendation, ground-truth ranking, award decision, scoring weight, competition result, dashboard, governance control matrix, evaluation report, valuation model, memo, slide deck, demo, external integration, API call, or real-data retrieval is implemented.

## Phase 0 controls

- [Repository working instructions](AGENTS.md)
- [Disclaimer](DISCLAIMER.md)
- [Project charter](docs/PROJECT_CHARTER.md)
- [Development backlog](docs/DEVELOPMENT_BACKLOG.md)
- [Approved repository structure](docs/REPOSITORY_STRUCTURE.md)
- [Synthetic-data and non-claims policy](docs/policies/SYNTHETIC_DATA_AND_NON_CLAIMS.md)
- [Development requirements](requirements.txt)

These controls define the recommendation-only capability ceiling, prohibited autonomous actions, synthetic-only boundary, human-approval requirement, and phase-gated development process.

## Phase 1 synthetic fixtures

- [Data dictionary](docs/DATA_DICTIONARY.md)
- [Synthetic scenario design](docs/SYNTHETIC_SCENARIO_DESIGN.md)
- [Suppliers](data/synthetic/suppliers.csv)
- [Procurement requests](data/synthetic/procurement_requests.csv)
- [Offers](data/synthetic/offers.csv)
- [Inert policy fixtures](data/synthetic/policy_rules.json)
- [Deterministic generator](scripts/generate_synthetic_data.py)
- [Validation tests](tests/test_synthetic_data.py)

Phase 1 uses seed `20260827` to generate exactly 100 fictional suppliers, 200 fictional requests, and 1,000 offers across five maintenance-supply categories. Every generated record/file is explicitly marked synthetic. The policy JSON is an inert fixture; no code applies it.

## Capability boundary

Subject to a separately approved future phase, a prototype may validate requests, retrieve synthetic policy rules, construct a supplier consideration set, check eligibility, rank compliant suppliers, flag concentration or conflict risks, create an audit record, and present a recommendation for human approval.

It must never award contracts, issue purchase orders, make payments, change ranking weights, override eligibility rules, or act without explicit human approval.

## Install, regenerate, and test

Python 3.12 is the reference CI runtime.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install --requirement requirements.txt
ruff check .
python -m compileall -q src scripts tests
python -m unittest discover -s tests -v
python scripts/generate_synthetic_data.py
git diff --exit-code -- data/synthetic
```

The generator and tests perform no network, API, or real-data access.
