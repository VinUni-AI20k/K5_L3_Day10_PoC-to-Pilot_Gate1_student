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


def fail_open_rate(trials):
    """Tỉ lệ trial mà LLM policy_check nghẽn và agent rơi vào fail_open (tự quyết khi không kiểm được policy).

    Sự cố S4 (LLM trả 429 giờ cao điểm) làm chỉ số này sáng đèn; theo dõi nó để biết trợ lý có đang
    duyệt khi chưa kiểm được chính sách hay không.
    """
    hits = sum(any(e.get("type") == "llm_fallback" and e.get("mode") == "fail_open" for e in t["events"])
               for t in trials)
    return hits / max(1, len(trials))


def queue_stuck_rate(trials):
    """Tỉ lệ trial bị ùn ở hàng chờ người duyệt (chờ quá SLA hoặc hết ca chưa tới lượt)."""
    return sum(bool(t.get("queue_stuck")) for t in trials) / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "fail_open_rate": fail_open_rate,        # metric mới: bắt LLM nghẽn -> fail_open (kỹ thuật, S4)
    "queue_stuck_rate": queue_stuck_rate,    # metric mới: bắt hàng chờ ùn (vận hành, S4)
}
STARTER_MONITORS = ("escalation_rate",)