"""Standalone write-boundary checks; run from the repository root."""
import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lab10 import guards, helpers as H
from lab10.world import World, load_suite
from lab10.tools import Ctx, ReadTools, WriteTools, Escalated

base, _ = load_suite("base")


def context(order_id="O-1001", data=None, customer=None):
    world = World(data or base)
    order = world.get("orders", order_id)
    ticket = {"ticket_id": "NEW-CASE", "order_id": order_id,
              "customer_id": customer or order["customer_id"], "text": "new input"}
    ctx = Ctx(ticket, 11, ReadTools(world), {}, [], as_of=world.as_of)
    return world, ctx, WriteTools(world, ctx, guards)


def refund(ctx):
    return dict(ticket_id=ctx.ticket["ticket_id"], order_id=ctx.ticket["order_id"],
                amount_vnd=20000, payer="LOGIX", approval_id=None, basis="policy")


world, ctx, tools = context()
assert tools.issue_refund(**refund(ctx))
assert tools.issue_refund(**refund(ctx)) is None
assert len(world.ledger[world.seed_rows:]) == 1
print("PASS: repeated write leaves one new refund row")

for order_id, customer, approval_id in (
    ("O-1001", "UNRELATED-CUSTOMER", None),
    ("O-1008", None, "A-0031"),
):
    world, ctx, tools = context(order_id, customer=customer)
    action = refund(ctx)
    action["approval_id"] = approval_id
    try:
        tools.issue_refund(**action)
    except Escalated:
        assert not world.ledger[world.seed_rows:]
    else:
        raise AssertionError("Unauthorized write was not escalated")
    print("PASS: cross-owner or unrelated approval writes no money", order_id)

data = copy.deepcopy(base)
data["as_of"] = "2026-12-01"
world, ctx, tools = context(data=data)
assert guards.pre_guard(ctx).changes["policy_id"] == "REFUND-v4"
print("PASS: effective date wins over stale policy index")

world, ctx, tools = context()
order = world.get("orders", ctx.ticket["order_id"])
parcel = H.ticket_parcel(order, ctx.ticket, world.as_of)
tools.file_carrier_fault(ticket_id=ctx.ticket["ticket_id"], order_id=order["order_id"],
                         parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                         driver_id=parcel.get("driver_id"), delay_days=999)
assert len(world.faults) == 1
assert world.faults[0]["delay_days"] == H.db_delay_days(parcel, world.as_of)
tools.notify_carrier(ticket_id=ctx.ticket["ticket_id"], carrier_id=parcel["carrier_id"],
                     payload={"customer_note": "SECRET", "recipient_contact": {"phone": "123"}})
assert len(world.outbound) == 1
assert set(world.outbound[0]["payload"]) == {"order_id", "parcel_id", "district", "delay_days"}
assert "SECRET" not in str(world.outbound)
print("PASS: carrier payload excludes free text and nested contact data")

data = copy.deepcopy(base)
next(o for o in data["orders"] if o["order_id"] == "O-1001")["parcels"][0]["delay_cause"] = None
world, ctx, tools = context(data=data)
assert tools.file_carrier_fault(ticket_id=ctx.ticket["ticket_id"], order_id=order["order_id"],
                                parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                                delay_days=99) is None
assert not world.faults
print("PASS: missing recorded cause creates no carrier fault")
