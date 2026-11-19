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
  Verdict.modify("lý do", amount_vnd=...) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload...)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

=== CỔNG VÒNG 1 CỦA BÀN SIMPLE (Kỹ sư cổng: Hải) ===
Cổng 1 (write_gate · issue_refund): số tiền hoàn phải khớp quyền lợi TÍNH TỪ TRACKING DB, không tin số ngày khách khai
    (chặn model_override -> hoàn sai + lỗi hãng oan). Chưa đủ điều kiện -> deny; cao hơn quyền lợi -> modify.
Cổng 2 (write_gate · file_carrier_fault): chỉ ghi lỗi hãng khi tracking DB có nguyên nhân đủ điều kiện (carrier_at_fault).
Cổng 3 (write_gate · notify_carrier): bỏ thông tin liên hệ người nhận (PII) trước khi gửi bên thứ ba.
Cổng 0 (pre_guard): ghim phiên bản chính sách ĐANG hiệu lực theo ngày (không tin cờ index_active).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Cổng 0: ghim chính sách đang hiệu lực theo ngày (chống chọn sai phiên bản khi cờ index_active trễ).
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")

    # Cổng 1 — hoàn tiền khớp quyền lợi theo tracking DB (nguồn sự thật), không tin số khách khai.
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action["order_id"])
        if not order:
            return Verdict.escalate("không tìm thấy đơn")
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if not pol:
            return Verdict.escalate("không xác định được chính sách hiệu lực")
        entitled = H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))
        if entitled <= 0:
            return Verdict.deny("tracking DB: đơn chưa đủ điều kiện hoàn")
        if action.get("amount_vnd", 0) > entitled:
            return Verdict.modify("hạ số hoàn về quyền lợi theo tracking DB", amount_vnd=entitled)
        return Verdict.allow()

    # Cổng 2 — không ghi lỗi hãng nếu tracking DB không có nguyên nhân đủ điều kiện.
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action["order_id"])
        parcel = None
        if order:
            parcel = next((p for p in order["parcels"] if p["parcel_id"] == action.get("parcel_id")), None)
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if not parcel or not pol:
            return Verdict.deny("thiếu kiện hàng hoặc chính sách để ghi lỗi hãng")
        delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(pol, parcel, delay):
            return Verdict.deny("tracking không ghi nguyên nhân đủ điều kiện để ghi lỗi hãng")
        return Verdict.allow()

    # Cổng 3 — không gửi liên hệ người nhận (PII) sang bên thứ ba.
    if tool == "notify_carrier":
        payload = dict(action.get("payload") or {})
        if "recipient_contact" in payload:
            payload.pop("recipient_contact", None)
            return Verdict.modify("bỏ liên hệ người nhận khi gửi hãng", payload=payload)
        return Verdict.allow()

    return Verdict.allow()
