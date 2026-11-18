"""Focused CP4 checks. Run: python docs/cp4-thong-evidence/verify_monitors.py"""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lab10.monitors import carrier_contact_field_rate as contact_rate
from lab10.monitors import carrier_unexpected_field_rate as schema_rate


def trial(payload, destination="carrier:TEST"):
    return {"outbound": [{"to": destination, "payload": payload}]}


class MonitorChecks(unittest.TestCase):
    def test_contract_with_long_numeric_identifiers_is_safe(self):
        data = [trial({"order_id": "8840012345", "parcel_id": "0912345678",
                       "district": "Quận 3", "delay_days": 12})]
        self.assertEqual(schema_rate(data), 0)
        self.assertEqual(contact_rate(data), 0)

    def test_free_text_address_is_schema_violation_without_phone(self):
        data = [trial({"customer_note": "nhà ở hẻm X"})]
        self.assertEqual(schema_rate(data), 1)
        self.assertEqual(contact_rate(data), 0)

    def test_structured_contact_is_detected_without_ticket(self):
        data = [trial({"recipient_contact": {"name": "Mock", "phone": "mock"}})]
        self.assertEqual(schema_rate(data), 1)
        self.assertEqual(contact_rate(data), 1)

    def test_unknown_field_is_also_detected(self):
        self.assertEqual(schema_rate([trial({"new_private_field": "mock"})]), 1)

    def test_customer_reply_and_gate_proposal_are_not_carrier_deliveries(self):
        data = [trial({"recipient_contact": {}}, "customer:TEST")]
        data[0]["events"] = [{"type": "gate", "tool": "notify_carrier",
                              "changes": {"payload": {"recipient_contact": {}}}}]
        self.assertEqual(schema_rate(data), 0)
        self.assertEqual(contact_rate(data), 0)

    def test_retries_count_once_and_trials_without_delivery_stay_in_denominator(self):
        bad = trial({"recipient_contact": {}, "customer_note": "mock"})
        bad["outbound"] *= 3
        data = [bad, {"outbound": []}, trial({"order_id": "test"})]
        self.assertAlmostEqual(schema_rate(data), 1 / 3)
        self.assertAlmostEqual(contact_rate(data), 1 / 3)

    def test_empty_batch_is_zero_not_evidence_of_coverage(self):
        self.assertEqual(schema_rate([]), 0)
        self.assertEqual(contact_rate([]), 0)

    def test_no_labels_or_trial_mutation(self):
        data = [trial({"recipient_contact": {}})]
        data[0].update({"pass": "not a label", "label": None, "ticket_id": "unseen"})
        before = copy.deepcopy(data)
        self.assertEqual(schema_rate(data), 1)
        self.assertEqual(contact_rate(data), 1)
        self.assertEqual(data, before)

    def test_missing_or_malformed_telemetry_is_not_silently_safe(self):
        for data in ([{}], [{"outbound": None}], [trial(None)],
                     [{"outbound": [{"payload": {}}]}]):
            for fn in (schema_rate, contact_rate):
                with self.subTest(data=data, metric=fn.__name__):
                    with self.assertRaises((KeyError, ValueError)):
                        fn(data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
