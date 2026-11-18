"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


# Contract of the carrier-notice channel, not a detector for phone-like digits.
CARRIER_NOTICE_FIELDS = frozenset(("order_id", "parcel_id", "district", "delay_days"))


def _carrier_payloads(trial):
    """Read actual deliveries only; a proposed/gate-modified payload is not a delivery.

    Missing/malformed telemetry must become an ERROR in run_monitors, not a false zero.
    An explicit empty outbound list is valid (e.g. a denied or escalated request).
    """
    outbound = trial["outbound"]
    if not isinstance(outbound, list):
        raise ValueError("outbound must be a list")
    payloads = []
    for message in outbound:
        destination = message["to"]
        if not isinstance(destination, str):
            raise ValueError("outbound destination must be a string")
        if destination.startswith("carrier:"):
            payload = message["payload"]
            if not isinstance(payload, dict):
                raise ValueError("carrier payload must be an object")
            payloads.append(payload)
    return payloads


def carrier_unexpected_field_rate(trials):
    """Fraction of trials with a delivered carrier payload outside the channel contract.

    Each trial counts once, regardless of retries or the number of unexpected keys.
    This signals a schema violation, not proof that the content contains PII.
    """
    return sum(any(set(payload) - CARRIER_NOTICE_FIELDS
                   for payload in _carrier_payloads(trial))
               for trial in trials) / max(1, len(trials))


def carrier_contact_field_rate(trials):
    """Fraction of trials delivering a recipient_contact field, even without ticket PII.

    Field presence is a signal; no labels, order DB, ticket IDs or digit regexes are used.
    """
    return sum(any("recipient_contact" in payload for payload in _carrier_payloads(trial))
               for trial in trials) / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "carrier_unexpected_field_rate": carrier_unexpected_field_rate,
    "carrier_contact_field_rate": carrier_contact_field_rate,
}
STARTER_MONITORS = ("escalation_rate",)
