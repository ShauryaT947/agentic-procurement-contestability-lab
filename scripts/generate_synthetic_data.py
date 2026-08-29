#!/usr/bin/env python3
"""Generate deterministic fictional procurement fixtures.

FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY.
NOT A REAL PROCUREMENT RECORD OR DECISION.
NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT.

This standard-library-only script performs no network, API, or real-data access.
It creates no rankings, recommendations, awards, scoring weights, or results.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

SEED = 20260827
NOTICE = "FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY. NOT A REAL PROCUREMENT RECORD OR DECISION. NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT."
CATEGORIES = [
    "Electrical spares",
    "HVAC components",
    "Water-pump parts",
    "Road-maintenance materials",
    "Safety equipment",
]
ZONES = [f"Synthetic Zone {letter}" for letter in "ABCDEFGHIJ"]
URGENCIES = ["Routine", "Planned", "Time-sensitive"]
WARRANTIES = [3, 6, 12, 18, 24]
CATEGORY_CONFIG = {
    "Electrical spares": {"quantity_min": 5, "quantity_max": 60, "reference_unit": 260},
    "HVAC components": {"quantity_min": 2, "quantity_max": 30, "reference_unit": 1250},
    "Water-pump parts": {"quantity_min": 2, "quantity_max": 25, "reference_unit": 1900},
    "Road-maintenance materials": {
        "quantity_min": 100,
        "quantity_max": 2000,
        "reference_unit": 14,
    },
    "Safety equipment": {"quantity_min": 20, "quantity_max": 400, "reference_unit": 65},
}
DELIVERY_RANGES = {
    "Routine": (45, 60),
    "Planned": (21, 40),
    "Time-sensitive": (7, 20),
}
OUTPUT_FILENAMES = [
    "suppliers.csv",
    "procurement_requests.csv",
    "offers.csv",
    "policy_rules.json",
]


class DeterministicRng:
    """Small cross-language-stable 32-bit linear congruential generator."""

    def __init__(self, seed: int) -> None:
        self.state = seed & 0xFFFFFFFF

    def next_float(self) -> float:
        self.state = (1664525 * self.state + 1013904223) & 0xFFFFFFFF
        return self.state / 4294967296

    def randint(self, minimum: int, maximum: int) -> int:
        return minimum + int(self.next_float() * (maximum - minimum + 1))

    def choice(self, values: list[Any]) -> Any:
        return values[self.randint(0, len(values) - 1)]

    def chance(self, probability: float) -> bool:
        return self.next_float() < probability

    def shuffle(self, values: list[Any]) -> None:
        for index in range(len(values) - 1, 0, -1):
            swap_index = self.randint(0, index)
            values[index], values[swap_index] = values[swap_index], values[index]


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def money_from_cents(cents: int) -> str:
    return f"{cents // 100}.{cents % 100:02d}"


def generate_suppliers(rng: DeterministicRng) -> list[dict[str, str]]:
    suppliers: list[dict[str, str]] = []
    for number in range(1, 101):
        primary = CATEGORIES[(number - 1) % len(CATEGORIES)]
        other_categories = [category for category in CATEGORIES if category != primary]
        rng.shuffle(other_categories)
        additional_count = rng.randint(0, 2)
        selected = {primary, *other_categories[:additional_count]}
        coverage = [category for category in CATEGORIES if category in selected]
        suppliers.append(
            {
                "supplier_id": f"SUP-{number:03d}",
                "fictional_name": f"Fictional Maintenance Supplier {number:03d}",
                "category_coverage": "|".join(coverage),
                "sme_flag": bool_text(rng.chance(0.55)),
                "incumbent_flag": bool_text(rng.chance(0.30)),
                "catalogue_integration_flag": bool_text(rng.chance(0.65)),
                "location": rng.choice(ZONES),
                "quality_score": str(rng.randint(60, 98)),
                "on_time_delivery_score": str(rng.randint(55, 99)),
                "risk_score": str(rng.randint(5, 65)),
                "conflict_risk_flag": bool_text(rng.chance(0.08)),
                "is_synthetic": "true",
                "synthetic_notice": NOTICE,
            }
        )
    return suppliers


def generate_requests(rng: DeterministicRng) -> list[dict[str, str]]:
    requests: list[dict[str, str]] = []
    for number in range(1, 201):
        category = CATEGORIES[(number - 1) % len(CATEGORIES)]
        config = CATEGORY_CONFIG[category]
        quantity = rng.randint(config["quantity_min"], config["quantity_max"])
        budget_percent = rng.randint(110, 160)
        budget_cents = quantity * config["reference_unit"] * budget_percent
        urgency = rng.choice(URGENCIES)
        delivery_min, delivery_max = DELIVERY_RANGES[urgency]
        requests.append(
            {
                "request_id": f"REQ-{number:04d}",
                "category": category,
                "quantity": str(quantity),
                "budget": money_from_cents(budget_cents),
                "urgency": urgency,
                "minimum_quality_requirement": str(rng.randint(65, 90)),
                "delivery_requirement_days": str(rng.randint(delivery_min, delivery_max)),
                "is_synthetic": "true",
                "synthetic_notice": NOTICE,
            }
        )
    return requests


def generate_offers(
    rng: DeterministicRng,
    suppliers: list[dict[str, str]],
    requests: list[dict[str, str]],
) -> list[dict[str, str]]:
    offers: list[dict[str, str]] = []
    offer_number = 1
    for request in requests:
        category = request["category"]
        quantity = int(request["quantity"])
        delivery_requirement = int(request["delivery_requirement_days"])
        candidates = [
            supplier
            for supplier in suppliers
            if category in supplier["category_coverage"].split("|")
        ]
        rng.shuffle(candidates)
        for position, supplier in enumerate(candidates[:5]):
            reference_cents = CATEGORY_CONFIG[category]["reference_unit"] * 100
            variance_percent = rng.randint(80, 120)
            unit_price_cents = max(1, (reference_cents * variance_percent + 50) // 100)
            if position < 3:
                available_quantity = quantity + rng.randint(0, max(1, quantity // 2))
                delivery_days = rng.randint(1, delivery_requirement)
                technical_compliance = True
            else:
                minimum_available = max(1, (quantity + 1) // 2)
                maximum_available = max(minimum_available, (quantity * 13 + 9) // 10)
                available_quantity = rng.randint(minimum_available, maximum_available)
                delivery_days = rng.randint(1, delivery_requirement + 20)
                technical_compliance = rng.chance(0.75)
            offers.append(
                {
                    "offer_id": f"OFR-{offer_number:05d}",
                    "request_id": request["request_id"],
                    "supplier_id": supplier["supplier_id"],
                    "unit_price": money_from_cents(unit_price_cents),
                    "available_quantity": str(available_quantity),
                    "delivery_days": str(delivery_days),
                    "warranty_months": str(rng.choice(WARRANTIES)),
                    "technical_compliance": bool_text(technical_compliance),
                    "is_synthetic": "true",
                    "synthetic_notice": NOTICE,
                }
            )
            offer_number += 1
    return offers


def policy_fixture() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "fixture_id": "SYN-POLICY-20260827",
        "is_synthetic": True,
        "synthetic_notice": NOTICE,
        "scope": {
            "authority": "Fictional Infrastructure Authority",
            "scenario": "Routine low-risk maintenance supplies",
            "currency": "synthetic AED-equivalent units",
            "categories": CATEGORIES,
        },
        "eligibility_evidence_requirements": [
            {
                "evidence_id": "SYN-EVID-001",
                "label": "Synthetic supplier declaration",
                "required": True,
            },
            {
                "evidence_id": "SYN-EVID-002",
                "label": "Synthetic category capability record",
                "required": True,
            },
            {
                "evidence_id": "SYN-EVID-003",
                "label": "Synthetic technical compliance response",
                "required": True,
            },
            {
                "evidence_id": "SYN-EVID-004",
                "label": "Synthetic conflict disclosure",
                "required": True,
            },
        ],
        "approval_thresholds": [
            {
                "threshold_id": "SYN-APPROVAL-LOW",
                "minimum_budget_inclusive": 0,
                "maximum_budget_exclusive": 25000,
                "required_human_role": "Fictional Request Reviewer",
                "human_approval_required": True,
            },
            {
                "threshold_id": "SYN-APPROVAL-MEDIUM",
                "minimum_budget_inclusive": 25000,
                "maximum_budget_exclusive": 100000,
                "required_human_role": "Fictional Procurement Reviewer",
                "human_approval_required": True,
            },
            {
                "threshold_id": "SYN-APPROVAL-HIGH",
                "minimum_budget_inclusive": 100000,
                "maximum_budget_exclusive": None,
                "required_human_role": "Fictional Senior Reviewer",
                "human_approval_required": True,
            },
        ],
        "conflict_escalation": {
            "trigger_field": "conflict_risk_flag",
            "trigger_value": True,
            "action": "stop_and_request_synthetic_conflict_review",
            "required_human_role": "Fictional Conflict Reviewer",
            "automated_override_permitted": False,
        },
        "missing_evidence_handling": {
            "fail_closed": True,
            "action": "stop_and_request_human_review",
            "record_missing_evidence": True,
            "automated_waiver_permitted": False,
        },
        "human_approval": {
            "required": True,
            "action_before_approval": "no_procurement_action",
            "approval_reference_required": True,
            "agent_self_approval_permitted": False,
        },
        "prohibited_automation": [
            "award_contract",
            "issue_purchase_order",
            "make_payment",
            "change_scoring_weights",
            "override_eligibility_rules",
            "act_without_human_approval",
        ],
        "limitations": [
            "These fixtures are invented and are not UAE law or policy.",
            "No code applies these policy fixtures in Phase 1.",
            "The fixtures are not legal, procurement, financial, or compliance advice.",
            "The fixtures do not establish eligibility, ranking, recommendation, award, or outcome.",
        ],
    }


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def generate(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = DeterministicRng(SEED)
    suppliers = generate_suppliers(rng)
    requests = generate_requests(rng)
    offers = generate_offers(rng, suppliers, requests)

    write_csv(output_dir / "suppliers.csv", list(suppliers[0]), suppliers)
    write_csv(output_dir / "procurement_requests.csv", list(requests[0]), requests)
    write_csv(output_dir / "offers.csv", list(offers[0]), offers)
    with (output_dir / "policy_rules.json").open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(policy_fixture(), handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def parse_args() -> argparse.Namespace:
    default_output = Path(__file__).resolve().parents[1] / "data" / "synthetic"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=default_output,
        help="Directory for generated synthetic fixtures.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generate(args.output_dir)
    print(f"Generated {len(OUTPUT_FILENAMES)} synthetic fixture files in {args.output_dir}")


if __name__ == "__main__":
    main()
