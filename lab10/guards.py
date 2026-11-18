"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # G1: validity dates, not a cached active flag, decide the policy version.
    policies = [p for p in ctx.tools.lookup_policies()
                if p["effective_from"] <= ctx.as_of
                and (not p.get("effective_to") or ctx.as_of <= p["effective_to"])]
    if len(policies) != 1:
        return Verdict.escalate("không xác định duy nhất chính sách hiệu lực")
    return Verdict.allow(policy_id=policies[0]["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()

    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not policy or order["customer_id"] != ctx.ticket.get("customer_id"):
        return Verdict.escalate("thiếu đơn/chính sách hoặc người gửi không sở hữu đơn")
    if action.get("ticket_id") != ctx.ticket.get("ticket_id"):
        return Verdict.escalate("lệnh ghi không thuộc ticket đang xử lý")
    if tool != "notify_carrier" and action.get("order_id") != order["order_id"]:
        return Verdict.escalate("lệnh ghi không thuộc đơn đang xử lý")
    if not order.get("parcels"):
        return Verdict.escalate("thiếu kiện hàng để đối chiếu")
    pid = ctx.ticket.get("parcel_id")
    if pid and not any(p["parcel_id"] == pid for p in order["parcels"]):
        return Verdict.escalate("kiện trong yêu cầu không thuộc đơn")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)

    # G2: derive the remaining refund from DB facts and the ledger.
    if tool == "issue_refund":
        if action.get("basis") != "policy":
            return Verdict.escalate("không ghi tiền từ chế độ bỏ qua kiểm tra chính sách")
        entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        remaining = max(0, entitled - paid)
        if remaining == 0:
            return Verdict.deny("không còn quyền lợi hoàn theo DB và sổ cái")
        approval_id = action.get("approval_id")
        if approval_id or remaining > policy["auto_limit_vnd"]:
            approvals = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
            approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
            valid = any(a.get("status") == "valid"
                        and a.get("ticket_id") == ctx.ticket["ticket_id"]
                        and a.get("order_id") == order["order_id"]
                        and a.get("customer_id") == order["customer_id"]
                        and a.get("expires_at", "") >= ctx.as_of
                        and a.get("max_vnd", 0) >= remaining
                        and (not approver or a.get("approver_id") == approver)
                        for a in approvals)
            if not valid:
                return Verdict.escalate("thiếu phê duyệt hợp lệ đúng đối tượng và đủ hạn mức")
        if action.get("amount_vnd") != remaining or action.get("payer") != "LOGIX":
            return Verdict.modify("đối chiếu quyền lợi DB và số đã hoàn", amount_vnd=remaining, payer="LOGIX")

    # G3: fault attribution and outgoing data must follow the actual parcel.
    if tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking không chứng minh hãng chịu lỗi theo chính sách")
        facts = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                 "driver_id": parcel.get("driver_id"), "delay_days": delay}
        if any(action.get(k) != v for k, v in facts.items()):
            return Verdict.modify("ghi lỗi đúng kiện/hãng/tài xế và độ trễ DB", **facts)
    if tool == "notify_carrier":
        faults = ctx.tools.fault_rows(ticket_id=ctx.ticket["ticket_id"], order_id=order["order_id"],
                                     parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"])
        if not faults or not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("chưa có bản ghi lỗi hãng hợp lệ để thông báo")
        facts = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                 "district": order.get("recipient", {}).get("district"), "delay_days": delay}
        allowed = set(policy.get("carrier_notice_fields", []))
        payload = {k: v for k, v in facts.items() if k in allowed}
        if action.get("payload") != payload or action.get("carrier_id") != parcel["carrier_id"]:
            return Verdict.modify("chỉ gửi dữ kiện chính sách cho phép, bỏ nội dung tự do/PII",
                                  carrier_id=parcel["carrier_id"], payload=payload)
    return Verdict.allow()
