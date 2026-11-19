# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Tetris
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Tetris-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |  Khổng Ngọc Anh         |    2A202603974  |   Kỹ sư cổng  |             |
|   2 |     Lý Hà Trân Trân      |   2A202603968   |   Kỹ sư cổng  |             |
|   3 |      Võ Thị Kim Ý     |   2A202603965   |  Sản phẩm và kinh doanh   |             |
|   4 |   Vương Thu Thảo         |   2A202603966   |   Vận hành và pháp lý  |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## LyHaTranTran-2A202603968

### Phần việc phụ trách

Vai **Kỹ sư cổng**.
- **Phiếu A:** câu 1.3 (mục A2, cột "Offline").
- **Phiếu B:** câu 2.2 (B2), câu 2.5 (B6, bản nháp cho cả bàn), câu 2.6 (B7.1), chốt cổng vòng 1 và nháp quyết định v1 (B8), dòng 2–3 của nhật ký B0, dòng 1 và 4 của checklist B5.
- **Phiếu C (thẻ S5):** câu 3.0 (C0 dòng 1, C1) và câu 3.1 (C2, C3.5, C4).
- **File:** `lab10/guards.py` (bản chốt `lab10/guards_round1.py`).

### Đóng góp cụ thể

- **1.3:** thiết kế offline metric "tỉ lệ ghi oan cho hãng" cho bước `file_carrier_fault`. Nhãn lấy từ `label.faults`, nối với trace theo `ticket_id`. Có quy tắc cho mẫu số bằng 0, cho ca ghi trùng và cho ca chưa có nhãn.
- **2.2:** dò `T-002@55`. Tách thành hai lỗi chìm (hoàn sai 20.000đ; ghi oan cho VNX kèm gửi thừa `customer_note`). Nguồn lỗi: đầu vào và thứ bậc hệ thống.
- **2.5:** viết nháp pre-mortem 8 lý do, đủ bốn lăng kính, mỗi lý do có bằng chứng kiểm được. Chọn 3 lý do làm cổng phòng ngừa.
- **2.6:** code ba cổng trong `lab10/guards.py`:
  - **Cổng 1 (hoàn tiền):** tính lại quyền lợi từ tracking DB và chính sách theo ngày hiệu lực, kiểm phê duyệt; `pre_guard` ghim phiên bản chính sách.
  - **Cổng 2 (ghi lỗi hãng):** chỉ ghi khi có nguyên nhân đã ghi nhận, ghi đúng kiện bị trễ, tối đa 2 lỗi mỗi hãng mỗi ngày.
  - **Cổng 3 (gửi hãng):** chỉ giữ các trường trong `carrier_notice_fields`.

  Kiểm lại: không làm hỏng ca nào trên bộ nền; tự dựng ca thử cho cổng 2 và cổng 3, vì bộ nền không có ca nào chạm hai cổng này.
- **B8:** chạy `lab10.checkpoint`, chạy eval mốc base và prepared, chạy `lab10.gate`. Nháp quyết định v1 "Tiếp tục" trong phạm vi HN + HCM, và ghi chú chỗ runbook lệch với config (`pilot_scope`).
- **3.0–3.1 (S5):** chạy grade ở mốc prepared, tách phần cổng đỡ được (chủ yếu nhờ config `business`) khỏi phần còn lọt (hoàn trùng cùng đơn). Dò 5 ticket, tìm ra 3 lỗi đến từ 3 nguồn: cờ `refund_status` cập nhật theo batch đêm; CSKH hoàn tay và trợ lý cùng ghi sổ; kho sỉ vượt hạn mức nên luôn phải chuyển người. Viết HAZOP 4 dòng, trong đó có nhánh chưa thấy trên trace là một phê duyệt bị dùng hai lần. Phát hiện lỗi `integrity: false` do CRLF trên Windows.

### Bằng chứng

- **Commit:**
  - `d9f1d6f`: 1.3
  - `abf0304`: 2.2
  - `c948adf`: 2.5
  - `b762dc4`: 2.6
  - `6b8f904`: chốt vòng 1 + v1
  - `5941fed`: 3.0 + 3.1
- **Mã lần chạy:**
  - `R-base-after-20261119-164251-844614`: cổng vòng 1, pass_rate 1,0, 0/0/0.
  - `R-base-before-20261119-170700-94d269`: base.
  - `R-base-prepared-20261119-170701-94d269`: prepared, đạt cả 5 ngưỡng bắt buộc và 3 ngưỡng kinh doanh, vận hành.
  - `R-S5-grade-20261119-171427-94d269`: grade S5, kèm `R-S5-before-…-94d269` và `R-S5-prepared-…-94d269`.
- **Hash chốt vòng 1:** `ae87608c`.
- **Dòng trong phiếu:**
  - Phiếu A mục A2, cột Offline.
  - Phiếu B mục B2, B6, B7.1, B8, B0 dòng 2–3, B5 dòng 1 và 4.
  - Phiếu C mục C0 dòng 1, C1, C2, C3.5, C4.

### Exit ticket

- **Học được:** một cổng "đạt 100% bộ nền" vẫn có thể bỏ lọt cả một loại lỗi. Cổng 1 so số tiền với quyền lợi của **một** lần hoàn, nên hoàn trùng cùng đơn ở thẻ S5 lọt qua, vì bộ nền không bao giờ có hai ticket cùng đơn trong một ngày. Phải hỏi "trường này là nguồn sự thật hay bản sao" (`refund_status` so với sổ cái) trước khi tin nó.
- **Còn chưa chắc:** cổng trần lỗi hãng (`escalate` ở bước ghi lỗi) chạy **sau** khi tiền đã hoàn. Chưa rõ nên chặn sớm hơn ở `issue_refund`, hay giữ như hiện tại để không làm khách chờ.
