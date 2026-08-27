# Synthetic-data and non-claims policy

## Purpose

This policy governs all data, examples, narratives, interfaces, analyses, and outputs in the Agentic Procurement Contestability Lab. It applies now and to any later authorised phase.

## Mandatory classification

All organisations, authorities, suppliers, people, policies, requests, transactions, approvals, audit records, rankings, flags, metrics, and results created for the lab must be fictional and synthetic.

Every dataset and user-facing output must prominently state:

> FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY. NOT A REAL PROCUREMENT RECORD OR DECISION. NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT.

## Permitted material

- invented entity and person names that are not intended to identify real parties;
- generated identifiers with an explicit synthetic namespace;
- artificial maintenance-supply catalogues, requests, policy rules, and transaction histories;
- documented scenario assumptions;
- general public background used only with a citation and clear separation from synthetic scenario content; and
- aggregate test metrics explicitly labelled as simulated or synthetic.

## Prohibited material

- personal data or identifiers belonging to real people;
- confidential, proprietary, restricted, leaked, or security-sensitive information;
- real supplier bids, procurement requests, purchase orders, payments, contracts, conflicts, or performance records;
- copied records from live public-sector or supplier systems;
- scraped supplier profiles used as scenario data;
- real logos, seals, letterheads, signatures, or visual devices that imply official status;
- invented quotations attributed to real people or entities; and
- synthetic names or identifiers deliberately made confusingly similar to real parties.

## Generation and provenance controls

When synthetic-data work is separately authorised:

1. define a schema and generation purpose before creating records;
2. use deterministic seeds where practical;
3. document distributions, constraints, assumptions, and transformations;
4. include machine-readable fields such as `is_synthetic: true` and a scenario/version identifier;
5. run checks for accidental real names, identifiers, and implausible leakage;
6. keep source and generated data separated;
7. prohibit network retrieval of live procurement or supplier data; and
8. record changes so results can be reproduced and challenged.

Phase 0 does not authorise creation of the dataset.

## Claims policy

Do not state or imply that the lab:

- was commissioned, sponsored, approved, certified, adopted, or endorsed by a UAE government body or any real organisation;
- describes an actual UAE authority, procurement, supplier, person, or transaction;
- complies with all applicable UAE law or procurement policy;
- produced observed savings, fairness, efficiency, compliance, competition, or value;
- predicts or guarantees a real-world outcome; or
- is suitable for production or autonomous use.

Synthetic evaluations may be described only as results within a documented simulation. Use language such as “in the synthetic scenario” and report assumptions and limitations alongside results.

## Review and incident handling

Contributors must check new content for policy compliance before review. If real, personal, confidential, or misleading material is found:

1. stop further use and distribution;
2. notify the repository owner;
3. remove the material from active branches and artifacts using an approved remediation process;
4. assess whether history, caches, or external copies require separate cleanup; and
5. document the incident without reproducing sensitive content.

Exceptions are not granted by the agent. Any proposed policy change requires explicit repository-owner approval and documented rationale.
