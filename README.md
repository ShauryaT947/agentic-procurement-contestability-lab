# Agentic Procurement Contestability Lab

> **Fictional and synthetic prototype.** This independent lab is not commissioned, sponsored, approved, or endorsed by the UAE Government or any UAE public authority. It must not be used for live procurement or purchasing decisions.

The Agentic Procurement Contestability Lab is a research prototype for a fictional UAE infrastructure authority. It explores how a tightly bounded recommendation agent might support routine, low-risk maintenance-supply procurement while preserving eligibility rules, contestability, auditability, and human decision authority.

## Current status

**Phase 0 — project foundation only.** This repository currently contains governance controls, documentation, an empty implementation scaffold, and basic Python CI. It does not contain a synthetic dataset, ranking engine, dashboard, governance matrix, evaluation report, valuation model, memo, slide deck, or demo.

## Intended future prototype boundary

Subject to a separately approved phase, the prototype may:

- validate a request;
- retrieve synthetic policy rules;
- construct a supplier consideration set;
- check supplier eligibility;
- rank compliant suppliers;
- flag concentration or conflict risks;
- create an audit record; and
- present a recommendation for human approval.

The prototype must never:

- award a contract;
- issue a purchase order;
- make or initiate a payment;
- change ranking weights;
- override eligibility rules;
- represent its output as a binding procurement decision; or
- act without explicit human approval.

## Phase 0 contents

- [Project charter](docs/PROJECT_CHARTER.md)
- [Synthetic-data and non-claims policy](docs/policies/SYNTHETIC_DATA_AND_NON_CLAIMS.md)
- [Development backlog](docs/DEVELOPMENT_BACKLOG.md)
- [Approved repository structure](docs/REPOSITORY_STRUCTURE.md)
- [Repository working instructions](AGENTS.md)
- [Disclaimer](DISCLAIMER.md)
- [Basic Python CI](.github/workflows/ci.yml)

## Local setup

Python 3.12 is the reference CI runtime.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
ruff check .
python -m compileall -q src tests
```

There is no executable procurement workflow in Phase 0.

## Decision authority

Any future recommendation is advisory and contestable. A designated human reviewer remains accountable for checking the request, evidence, policy application, risk flags, and recommendation before any separate real-world process could proceed.
