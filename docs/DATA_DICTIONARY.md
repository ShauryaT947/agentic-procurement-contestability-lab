# Data dictionary

> FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY.  
> NOT A REAL PROCUREMENT RECORD OR DECISION.  
> NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT.

## Dataset purpose and limits

These fixtures support testing of a future bounded procurement-recommendation prototype in a fictional routine, low-risk maintenance-supply scenario. They are generated, not observed. They contain no real authorities, companies, people, procurements, policies, prices, performance, conflicts, or decisions. Values must not be interpreted as benchmarks, market evidence, legal requirements, forecasts, or outcomes.

All CSV files use UTF-8, a header row, comma delimiters, `.` as the decimal separator, lower-case `true`/`false` booleans, and one record per subsequent row. Category lists use `|` as the within-field separator. Monetary values are synthetic AED-equivalent units, not market observations.

## Relationships

```text
suppliers.supplier_id 1 ── * offers.supplier_id
procurement_requests.request_id 1 ── * offers.request_id
```

Every offer references one existing supplier and one existing request. The supplier's `category_coverage` includes the request's `category`. Each request has exactly five offers in this fixture and at least three plausible offers that cover the requested quantity, meet the delivery requirement, and are technically compliant. This is not an eligibility decision or ranking.

## data/synthetic/suppliers.csv

**Synthetic purpose:** provide fictional supplier attributes for relationship, range, risk-flag, and later authorised test scenarios.  
**Cardinality:** exactly 100 rows.

| Field | Type | Required | Allowed values/range | Definition and limitation |
| --- | --- | --- | --- | --- |
| `supplier_id` | string | Yes | Unique `SUP-001`–`SUP-100` | Synthetic stable key; not a government or company identifier. |
| `fictional_name` | string | Yes | `Fictional Maintenance Supplier NNN` | Deliberately generic invented label; never a real company name. |
| `category_coverage` | pipe-delimited string | Yes | One to three of the five defined categories | Synthetic catalogue coverage; not accreditation or eligibility. |
| `sme_flag` | boolean string | Yes | `true`, `false` | Invented scenario attribute; not a legal SME classification. |
| `incumbent_flag` | boolean string | Yes | `true`, `false` | Invented prior-supply status; no real contract history. |
| `catalogue_integration_flag` | boolean string | Yes | `true`, `false` | Invented technical-capability flag; no integration exists. |
| `location` | string | Yes | `Synthetic Zone A`–`Synthetic Zone J` | Fictional zone, not a real address or jurisdiction. |
| `quality_score` | integer | Yes | 60–98 inclusive | Synthetic descriptive test score; not a ranking weight or verified performance. |
| `on_time_delivery_score` | integer | Yes | 55–99 inclusive | Synthetic percentage-like test score; not observed delivery performance. |
| `risk_score` | integer | Yes | 5–65 inclusive | Synthetic risk indicator; lower/higher values have no policy effect in Phase 1. |
| `conflict_risk_flag` | boolean string | Yes | `true`, `false` | Invented flag for later escalation testing; not an allegation. |
| `is_synthetic` | boolean string | Yes | Always `true` | Machine-readable synthetic marker. |
| `synthetic_notice` | string | Yes | Exact project notice | Human-readable non-claims marker. |

## data/synthetic/procurement_requests.csv

**Synthetic purpose:** provide fictional routine, low-risk demand records for later authorised validation tests.  
**Cardinality:** exactly 200 rows, 40 per category.

| Field | Type | Required | Allowed values/range | Definition and limitation |
| --- | --- | --- | --- | --- |
| `request_id` | string | Yes | Unique `REQ-0001`–`REQ-0200` | Synthetic stable key; not a purchase or tender identifier. |
| `category` | string | Yes | One of the five defined categories | Requested maintenance-supply category. |
| `quantity` | integer | Yes | Category-specific positive range, documented below | Invented unit count; units are abstract within each category. |
| `budget` | decimal string | Yes | Positive, two decimal places | Synthetic AED-equivalent budget; not a market price or approval decision. |
| `urgency` | string | Yes | `Routine`, `Planned`, `Time-sensitive` | Scenario scheduling label; every request remains fictional and low risk. |
| `minimum_quality_requirement` | integer | Yes | 65–90 inclusive | Synthetic minimum score; no eligibility code applies it in Phase 1. |
| `delivery_requirement_days` | integer | Yes | 7–60 inclusive | Synthetic maximum desired delivery time. |
| `is_synthetic` | boolean string | Yes | Always `true` | Machine-readable synthetic marker. |
| `synthetic_notice` | string | Yes | Exact project notice | Human-readable non-claims marker. |

Category-specific quantity ranges are: Electrical spares 5–60; HVAC components 2–30; Water-pump parts 2–25; Road-maintenance materials 100–2,000; Safety equipment 20–400.

## data/synthetic/offers.csv

**Synthetic purpose:** exercise relational and constraint validation only. Offers are not bids, recommendations, rankings, awards, or competition results.  
**Cardinality:** exactly 1,000 rows; five per request.

| Field | Type | Required | Allowed values/range | Definition and limitation |
| --- | --- | --- | --- | --- |
| `offer_id` | string | Yes | Unique `OFR-00001`–`OFR-01000` | Synthetic stable key; not a bid identifier. |
| `request_id` | string | Yes | Existing request ID | Foreign key to `procurement_requests.csv`. |
| `supplier_id` | string | Yes | Existing supplier ID | Foreign key to `suppliers.csv`; unique within a request. |
| `unit_price` | decimal string | Yes | Positive, two decimal places | Generated synthetic AED-equivalent unit price; not observed or recommended. |
| `available_quantity` | integer | Yes | Positive | Invented offered quantity. At least three offers per request cover the request quantity. |
| `delivery_days` | integer | Yes | 1–80 inclusive | Invented delivery time. At least three offers meet the request requirement. |
| `warranty_months` | integer | Yes | 3, 6, 12, 18, or 24 | Invented warranty period. |
| `technical_compliance` | boolean string | Yes | `true`, `false` | Synthetic fixture field, not an eligibility determination. |
| `is_synthetic` | boolean string | Yes | Always `true` | Machine-readable synthetic marker. |
| `synthetic_notice` | string | Yes | Exact project notice | Human-readable non-claims marker. |

## data/synthetic/policy_rules.json

**Synthetic purpose:** provide inert, fictional policy fixtures for later authorised retrieval and validation work. No Phase 1 code applies these rules.

| Field/path | Type | Allowed values/range | Definition and limitation |
| --- | --- | --- | --- |
| `schema_version` | string | `1.0` | Fixture schema version. |
| `fixture_id` | string | `SYN-POLICY-20260827` | Synthetic identifier; not an official policy reference. |
| `is_synthetic` | boolean | Always `true` | Machine-readable synthetic marker. |
| `synthetic_notice` | string | Exact project notice | Human-readable non-claims marker. |
| `scope` | object | Fixed fixture metadata | States the fictional, routine, low-risk maintenance scenario. |
| `eligibility_evidence_requirements` | array of objects | Four `SYN-EVID-*` fixtures | Evidence labels and required flags; not real compliance requirements. |
| `approval_thresholds` | array of objects | Three contiguous positive budget bands | Fictional reviewer routing; each band still requires human approval. |
| `conflict_escalation` | object | `conflict_risk_flag=true` trigger | Requires synthetic specialist review and blocks automated progression. |
| `missing_evidence_handling` | object | Fail-closed fixture | Records missing evidence and requests human review; no rule engine exists. |
| `human_approval` | object | `required=true` | Prohibits autonomous progression and records a human approval reference. |
| `prohibited_automation` | array of strings | Six prohibited actions | Documents actions no future agent may perform. |
| `limitations` | array of strings | Non-claims statements | Confirms that fixtures are not law, policy, advice, or production controls. |

## Five allowed categories

1. Electrical spares
2. HVAC components
3. Water-pump parts
4. Road-maintenance materials
5. Safety equipment
