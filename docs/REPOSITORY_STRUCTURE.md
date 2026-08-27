# Approved repository structure

The following structure is approved for Phase 0. Directories reserved for later phases contain only `.gitkeep` placeholders and do not imply authorisation to implement their contents.

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── config/
│   └── .gitkeep
├── data/
│   └── synthetic/
│       └── .gitkeep
├── docs/
│   ├── policies/
│   │   └── SYNTHETIC_DATA_AND_NON_CLAIMS.md
│   ├── DEVELOPMENT_BACKLOG.md
│   ├── PROJECT_CHARTER.md
│   └── REPOSITORY_STRUCTURE.md
├── src/
│   └── .gitkeep
├── tests/
│   └── .gitkeep
├── AGENTS.md
├── DISCLAIMER.md
├── README.md
└── requirements.txt
```

The existing `.gitignore` remains at the repository root.

## Directory responsibilities

- `.github/workflows/`: CI definitions only.
- `config/`: future non-secret, versioned configuration. No rules or weights exist in Phase 0.
- `data/synthetic/`: future policy-compliant synthetic fixtures. No dataset exists in Phase 0.
- `docs/`: charter, policies, backlog, design decisions, and future evidence.
- `src/`: future Python implementation of the bounded prototype. No functional code exists in Phase 0.
- `tests/`: future automated controls and behaviour tests. No product tests exist before product code.

## Structural controls

- Do not store real, personal, confidential, procurement, supplier, ordering, or payment data anywhere in the repository.
- Do not commit secrets or production endpoints.
- Do not add executable procurement or payment integrations.
- Keep generated artifacts out of source directories.
- Add new top-level directories only with an approved purpose and documentation update.
- Keep future configuration, rules, code, tests, and synthetic data separate so each can be reviewed and versioned.
