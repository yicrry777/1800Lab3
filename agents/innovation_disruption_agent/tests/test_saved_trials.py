"""Check the saved manual ChatGPT/Codex trials and context-contrast invariant."""

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[3]
AGENT = ROOT / "agents" / "innovation_disruption_agent"


def read_json(relative):
    return json.loads((AGENT / relative).read_text())


class SavedTrialTests(unittest.TestCase):
    def test_cases_hold_technology_and_application_constant(self):
        cases = [read_json(f"cases/{name}.json") for name in ("primary", "contrast_1", "contrast_2")]
        self.assertEqual(len({case["emerging_technology"] for case in cases}), 1)
        self.assertEqual(len({case["intended_application"] for case in cases}), 1)
        self.assertEqual(len({case["organization"] for case in cases}), 3)

    def test_saved_responses_follow_frozen_contract(self):
        for name in ("primary_response", "contrast_1_response", "contrast_2_response", "primary_pre_revision_weak"):
            with self.subTest(name=name):
                path = AGENT / "responses" / f"{name}.json"
                result = subprocess.run(
                    [sys.executable, str(ROOT / "tools" / "validate_response.py"), str(path)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_revision_preserves_general_finding_but_changes_business_exposure(self):
        primary = read_json("responses/primary_response.json")
        internal = read_json("responses/contrast_1_response.json")
        borderline = read_json("responses/contrast_2_response.json")
        self.assertEqual(primary["general_et_finding"], internal["general_et_finding"])
        self.assertEqual(primary["application_finding"], internal["application_finding"])
        self.assertEqual(primary["general_et_finding"], borderline["general_et_finding"])
        self.assertIn("Judgment: High", primary["organization_specific_finding"])
        self.assertIn("Judgment: Low", internal["organization_specific_finding"])
        self.assertIn("Judgment: Moderate", borderline["organization_specific_finding"])
        self.assertIn("High is a plausible alternative", borderline["organization_specific_finding"])

    def test_weak_trial_is_retained_as_failed_analysis(self):
        weak = read_json("responses/primary_pre_revision_weak.json")
        revised = read_json("responses/primary_response.json")
        self.assertIn("Potentially Existential", weak["organization_specific_finding"])
        self.assertIn("unsupported", revised["organization_specific_finding"])


if __name__ == "__main__":
    unittest.main()
