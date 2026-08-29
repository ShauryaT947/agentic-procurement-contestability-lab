"""Validation tests for Phase 1 fictional and synthetic fixtures.

FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY.
NOT A REAL PROCUREMENT RECORD OR DECISION.
NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT.
"""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import tempfile
import unittest
from collections import Counter, defaultdict
from pathlib import Path

NOTICE = "FICTIONAL AND SYNTHETIC — FOR RESEARCH AND DEMONSTRATION ONLY. NOT A REAL PROCUREMENT RECORD OR DECISION. NO UAE GOVERNMENT COMMISSIONING OR ENDORSEMENT."
CATEGORIES = {
    "Electrical spares",
    "HVAC components",
    "Water-pump parts",
    "Road-maintenance materials",
    "Safety equipment",
}
BOOLEAN_TEXT = {"true", "false"}
OUTPUT_FILENAMES = {
    "suppliers.csv",
    "procurement_requests.csv",
    "offers.csv",
    "policy_rules.json",
}


class SyntheticDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(__file__).resolve().parents[1]
        cls.data_dir = cls.root / "data" / "synthetic"
        cls.suppliers = cls.read_csv("suppliers.csv")
        cls.requests = cls.read_csv("procurement_requests.csv")
        cls.offers = cls.read_csv("offers.csv")
        cls.policy = json.loads((cls.data_dir / "policy_rules.json").read_text(encoding="utf-8"))

    @classmethod
    def read_csv(cls, name: str) -> list[dict[str, str]]:
        with (cls.data_dir / name).open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def test_exact_record_counts(self) -> None:
        self.assertEqual(len(self.suppliers), 100)
        self.assertEqual(len(self.requests), 200)
        self.assertEqual(len(self.offers), 1000)
        self.assertEqual(Counter(row["category"] for row in self.requests), {category: 40 for category in CATEGORIES})

    def test_ids_are_unique_and_well_formed(self) -> None:
        checks = [
            (self.suppliers, "supplier_id", r"SUP-\d{3}"),
            (self.requests, "request_id", r"REQ-\d{4}"),
            (self.offers, "offer_id", r"OFR-\d{5}"),
        ]
        for rows, field, pattern in checks:
            values = [row[field] for row in rows]
            self.assertEqual(len(values), len(set(values)), field)
            self.assertTrue(all(re.fullmatch(pattern, value) for value in values), field)

    def test_relationships_and_offer_plausibility(self) -> None:
        suppliers = {row["supplier_id"]: row for row in self.suppliers}
        requests = {row["request_id"]: row for row in self.requests}
        offers_by_request: dict[str, list[dict[str, str]]] = defaultdict(list)

        for offer in self.offers:
            self.assertIn(offer["supplier_id"], suppliers)
            self.assertIn(offer["request_id"], requests)
            supplier = suppliers[offer["supplier_id"]]
            request = requests[offer["request_id"]]
            self.assertIn(request["category"], supplier["category_coverage"].split("|"))
            offers_by_request[offer["request_id"]].append(offer)

        self.assertEqual(set(offers_by_request), set(requests))
        for request_id, request in requests.items():
            offers = offers_by_request[request_id]
            self.assertGreaterEqual(len(offers), 3)
            self.assertEqual(len(offers), 5)
            self.assertEqual(len({offer["supplier_id"] for offer in offers}), len(offers))
            plausible = [
                offer
                for offer in offers
                if int(offer["available_quantity"]) >= int(request["quantity"])
                and int(offer["delivery_days"]) <= int(request["delivery_requirement_days"])
                and offer["technical_compliance"] == "true"
            ]
            self.assertGreaterEqual(len(plausible), 3, request_id)

    def test_positive_prices_quantities_budgets_and_periods(self) -> None:
        for request in self.requests:
            self.assertGreater(int(request["quantity"]), 0)
            self.assertGreater(float(request["budget"]), 0)
            self.assertGreater(int(request["delivery_requirement_days"]), 0)
        for offer in self.offers:
            self.assertGreater(float(offer["unit_price"]), 0)
            self.assertGreater(int(offer["available_quantity"]), 0)
            self.assertGreater(int(offer["delivery_days"]), 0)
            self.assertIn(int(offer["warranty_months"]), {3, 6, 12, 18, 24})

    def test_scores_percentages_and_flags_are_in_range(self) -> None:
        for supplier in self.suppliers:
            self.assertGreaterEqual(int(supplier["quality_score"]), 0)
            self.assertLessEqual(int(supplier["quality_score"]), 100)
            self.assertGreaterEqual(int(supplier["on_time_delivery_score"]), 0)
            self.assertLessEqual(int(supplier["on_time_delivery_score"]), 100)
            self.assertGreaterEqual(int(supplier["risk_score"]), 0)
            self.assertLessEqual(int(supplier["risk_score"]), 100)
            for field in [
                "sme_flag",
                "incumbent_flag",
                "catalogue_integration_flag",
                "conflict_risk_flag",
            ]:
                self.assertIn(supplier[field], BOOLEAN_TEXT)
        for offer in self.offers:
            self.assertIn(offer["technical_compliance"], BOOLEAN_TEXT)

    def test_every_record_is_explicitly_synthetic(self) -> None:
        for rows in [self.suppliers, self.requests, self.offers]:
            for row in rows:
                self.assertEqual(row["is_synthetic"], "true")
                self.assertEqual(row["synthetic_notice"], NOTICE)
        self.assertIs(self.policy["is_synthetic"], True)
        self.assertEqual(self.policy["synthetic_notice"], NOTICE)

    def test_declared_categories_only(self) -> None:
        self.assertEqual({row["category"] for row in self.requests}, CATEGORIES)
        for supplier in self.suppliers:
            coverage = supplier["category_coverage"].split("|")
            self.assertGreaterEqual(len(coverage), 1)
            self.assertLessEqual(len(coverage), 3)
            self.assertEqual(len(coverage), len(set(coverage)))
            self.assertTrue(set(coverage).issubset(CATEGORIES))

    def test_no_real_people_companies_logos_or_government_identifiers(self) -> None:
        allowed_zones = {f"Synthetic Zone {letter}" for letter in "ABCDEFGHIJ"}
        for number, supplier in enumerate(self.suppliers, start=1):
            self.assertEqual(
                supplier["fictional_name"],
                f"Fictional Maintenance Supplier {number:03d}",
            )
            self.assertIn(supplier["location"], allowed_zones)

        data_fields = []
        excluded = {"synthetic_notice"}
        for rows in [self.suppliers, self.requests, self.offers]:
            for row in rows:
                data_fields.extend(str(value).lower() for key, value in row.items() if key not in excluded)
        business_text = "\n".join(data_fields)
        forbidden_identifiers = {
            "adnoc",
            "dewa",
            "etihad",
            "emirates",
            "taqa",
            "ministry",
            "municipality",
            "government id",
            "trade license",
            "passport",
            "email",
            "phone",
            "logo",
        }
        for identifier in forbidden_identifiers:
            self.assertNotIn(identifier, business_text)

    def test_no_rankings_recommendations_awards_weights_or_results(self) -> None:
        headers = set(self.suppliers[0]) | set(self.requests[0]) | set(self.offers[0])
        prohibited_fragments = {"rank", "recommend", "award", "winner", "weight", "competition_result"}
        for header in headers:
            self.assertFalse(any(fragment in header.lower() for fragment in prohibited_fragments), header)

    def test_policy_fixture_is_inert_and_human_gated(self) -> None:
        self.assertEqual(self.policy["fixture_id"], "SYN-POLICY-20260827")
        self.assertEqual(len(self.policy["eligibility_evidence_requirements"]), 4)
        self.assertTrue(all(item["required"] for item in self.policy["eligibility_evidence_requirements"]))
        self.assertTrue(all(item["human_approval_required"] for item in self.policy["approval_thresholds"]))
        self.assertTrue(self.policy["missing_evidence_handling"]["fail_closed"])
        self.assertFalse(self.policy["missing_evidence_handling"]["automated_waiver_permitted"])
        self.assertTrue(self.policy["human_approval"]["required"])
        self.assertFalse(self.policy["human_approval"]["agent_self_approval_permitted"])
        self.assertIn("act_without_human_approval", self.policy["prohibited_automation"])

    def test_generation_is_byte_for_byte_reproducible(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            subprocess.run(
                [
                    sys.executable,
                    str(self.root / "scripts" / "generate_synthetic_data.py"),
                    "--output-dir",
                    str(output_dir),
                ],
                cwd=self.root,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual({path.name for path in output_dir.iterdir()}, OUTPUT_FILENAMES)
            for filename in OUTPUT_FILENAMES:
                self.assertEqual(
                    (output_dir / filename).read_bytes(),
                    (self.data_dir / filename).read_bytes(),
                    filename,
                )


if __name__ == "__main__":
    unittest.main()
