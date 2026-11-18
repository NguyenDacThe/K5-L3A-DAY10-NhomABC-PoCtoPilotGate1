"""Check the real write boundary and the limit of the trusted-DB assumption."""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lab10 import guards, helpers as H
from lab10.tools import Ctx, ReadTools, WriteTools
from lab10.world import World, load_suite


class PrivacyBoundary(unittest.TestCase):
    def setUp(self):
        data, _ = load_suite("base")
        self.world = World(data)
        self.order = self.world.get("orders", "O-1001")
        self.parcel = H.ticket_parcel(self.order, {}, self.world.as_of)
        self.ctx = Ctx({"ticket_id": "NEW-PRIVACY-CHECK", "order_id": self.order["order_id"],
                        "customer_id": self.order["customer_id"], "text": "ordinary request"},
                       11, ReadTools(self.world), {}, [], as_of=self.world.as_of)
        self.tools = WriteTools(self.world, self.ctx, guards)
        self.tools.file_carrier_fault(ticket_id=self.ctx.ticket["ticket_id"],
                                      order_id=self.order["order_id"], parcel_id=self.parcel["parcel_id"],
                                      carrier_id=self.parcel["carrier_id"],
                                      driver_id=self.parcel.get("driver_id"),
                                      delay_days=H.db_delay_days(self.parcel, self.world.as_of))

    def notify(self, payload):
        return self.tools.notify_carrier(ticket_id=self.ctx.ticket["ticket_id"],
                                         carrier_id=self.parcel["carrier_id"], payload=payload)

    def test_untrusted_payload_cannot_replace_db_fields(self):
        for payload in ({"customer_note": "PRIVATE-MARKER 0912.345.678"},
                        {"recipient_contact": {"phone": "PRIVATE-MARKER"}},
                        {"PRIVATE-MARKER": {"nested": ["PRIVATE-MARKER"]},
                         "order_id": "forged-order", "district": "forged-district"}):
            with self.subTest(payload=payload):
                message = self.notify(payload)
                self.assertEqual(set(message["payload"]), {"order_id", "parcel_id", "district", "delay_days"})
                self.assertEqual(message["payload"]["order_id"], self.order["order_id"])
                self.assertEqual(message["payload"]["district"], self.order["recipient"]["district"])
                self.assertNotIn("PRIVATE-MARKER", json.dumps(message))

    def test_new_telemetry_contains_no_rejected_keys_or_values(self):
        self.notify({"PRIVATE-MARKER": "PRIVATE-MARKER", "recipient_contact": {"phone": "PRIVATE-MARKER"}})
        events = [e for e in self.ctx.events if e.get("kind") == "carrier_payload_minimized"]
        self.assertEqual(len(events), 1)
        event = events[0]
        self.assertEqual(event["removed_field_count"], 2)
        self.assertTrue(event["had_recipient_contact"])
        self.assertNotIn("PRIVATE-MARKER", json.dumps(event))
        self.assertEqual(set(event), {"type", "kind", "removed_field_count", "had_customer_note",
                                      "had_recipient_contact", "carrier_corrected"})
        self.assertTrue(all(type(event[k]) in (bool, int) for k in event if k not in ("type", "kind")))

    def test_benign_number_does_not_block_a_valid_notice(self):
        message = self.notify({"customer_note": "Reference 123456789; not a telephone"})
        self.assertIsNotNone(message)
        self.assertEqual(message["payload"]["parcel_id"], self.parcel["parcel_id"])

    def test_no_valid_fault_means_no_notice(self):
        self.world.faults.clear()
        self.assertIsNone(self.notify({"customer_note": "PRIVATE-MARKER"}))
        self.assertEqual(self.world.outbound, [])

    def test_trusted_fields_are_an_explicit_external_assumption(self):
        # This is a documented counterexample, not a claim of PII safety.
        # A structurally allowed district can carry bad data if upstream validation fails.
        source = next(o for o in self.world.data["orders"] if o["order_id"] == self.order["order_id"])
        source["recipient"]["district"] = "PRIVATE-MARKER"
        self.assertEqual(self.notify({})["payload"]["district"], "PRIVATE-MARKER")


if __name__ == "__main__":
    unittest.main(verbosity=2)
