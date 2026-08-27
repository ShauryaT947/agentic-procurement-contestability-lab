# Synthetic scenario design

> FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY.  
> NOT A REAL PROCUREMENT RECORD OR DECISION.  
> NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT.

## Synthetic assumptions versus facts

The only facts documented here are facts about how this repository's generator operates. Every authority, supplier, request, offer, policy fixture, price, score, threshold, and relationship it produces is a synthetic assumption. Nothing represents measured procurement practice, a UAE legal requirement, a real market distribution, or a real organisation's behaviour.

## Scope

The scenario imagines a fictional infrastructure authority reviewing routine, low-risk maintenance-supply requests. Phase 1 creates inert test fixtures only. It does not apply eligibility rules, calculate rankings, recommend suppliers, allocate awards, measure competition, or produce decisions.

## Determinism

- Fixed seed: `20260827`.
- Generator: `scripts/generate_synthetic_data.py`.
- Pseudorandom method: a documented 32-bit linear congruential generator with multiplier `1664525`, increment `1013904223`, and modulus `2^32`.
- Serialization: UTF-8, LF line endings, stable row order, fixed headers, two-decimal monetary strings, and deterministic JSON key order.
- Reproducibility test: regenerates into a temporary directory and compares every output byte-for-byte with committed fixtures.

This generator is appropriate for repeatable testing, not cryptography, privacy protection, statistical inference, or production simulation.

## Categories

Exactly five fictional maintenance-supply categories are used:

1. Electrical spares
2. HVAC components
3. Water-pump parts
4. Road-maintenance materials
5. Safety equipment

Each category is the guaranteed primary category for 20 suppliers and appears in 40 requests. Suppliers may receive zero to two additional categories. Category assignment is a synthetic balancing device, not a statement about real supplier markets.

## Supplier generation

Exactly 100 suppliers are generated with IDs `SUP-001` through `SUP-100`. Names follow the deliberately generic pattern `Fictional Maintenance Supplier NNN`. Locations are ten invented labels, `Synthetic Zone A` through `Synthetic Zone J`.

Attribute assumptions:

| Attribute | Synthetic distribution |
| --- | --- |
| Additional category coverage | Discrete uniform choice of 0, 1, or 2 additional categories |
| SME flag | Approximately 55% probability |
| Incumbent flag | Approximately 30% probability |
| Catalogue-integration flag | Approximately 65% probability |
| Quality score | Discrete uniform integer 60–98 |
| On-time-delivery score | Discrete uniform integer 55–99 |
| Risk score | Discrete uniform integer 5–65 |
| Conflict-risk flag | Approximately 8% probability |

These values are not verified capabilities, eligibility findings, performance evidence, allegations, weights, or real-world prevalence estimates.

## Request generation

Exactly 200 requests are produced, 40 per category. Categories cycle in the documented order.

| Category | Quantity range | Synthetic reference unit value |
| --- | ---: | ---: |
| Electrical spares | 5–60 | 260 |
| HVAC components | 2–30 | 1,250 |
| Water-pump parts | 2–25 | 1,900 |
| Road-maintenance materials | 100–2,000 | 14 |
| Safety equipment | 20–400 | 65 |

Budgets equal quantity multiplied by the synthetic reference value and a discrete multiplier from 110% through 160%. This formula provides internally plausible test values only; it is not a cost estimate or market fact.

Urgency is selected from Routine, Planned, and Time-sensitive. Corresponding delivery-requirement ranges are 45–60, 21–40, and 7–20 days. Minimum quality requirements are integers from 65 through 90. Every record remains within the fictional routine, low-risk scenario regardless of urgency label.

## Offer generation

Exactly five offers are created for every request, for 1,000 offers total.

- Candidate suppliers must list the request category in `category_coverage`.
- A request cannot receive two offers from the same supplier.
- Unit prices vary from 80% through 120% of the category's synthetic reference value.
- Warranties are selected from 3, 6, 12, 18, and 24 months.
- The first three generated offers for each request are constructed to cover requested quantity, meet the delivery requirement, and set technical compliance to `true`.
- The remaining two offers retain category coverage but may vary in quantity, delivery, and technical-compliance values.

“Plausible” means only that the fixture satisfies those simple internal constraints. It does not mean eligible, preferred, competitive, recommended, or awardable.

## Policy fixtures

`policy_rules.json` contains fictional evidence labels, budget bands, conflict escalation, fail-closed missing-evidence handling, mandatory human approval, and prohibited automation. The thresholds and roles are invented. Phase 1 includes no code that interprets or enforces the fixture.

## Safety and non-claims design

- No network or API library is imported.
- No external or real data is retrieved.
- No person names, addresses, company brands, logos, government identifiers, or production identifiers are generated.
- Synthetic markers and the required notice appear in every record/file.
- Tests constrain supplier names and locations to declared fictional patterns.
- Tests reject prohibited decision-output fields such as ranks, winners, recommendations, awards, or weights.
- Results cannot be used to infer real savings, quality, risk, market structure, competition, or policy compliance.

## Limitations

The distributions are intentionally simple and are not calibrated to real procurement. Correlations are minimal, category units are abstract, conflict flags are not allegations, and scores are not independently meaningful. The fixtures are suitable only for deterministic software tests and demonstrations within the stated non-claims boundary.
