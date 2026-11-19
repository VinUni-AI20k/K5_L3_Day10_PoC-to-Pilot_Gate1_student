# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HiLab
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-HiLab-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trần Duy Thành | 2A202603919 | Trưởng nhóm, Sản phẩm và kinh doanh | Có |
|   2 | Võ Thị Phương Nhung | 2A202603918 | Kỹ sư cổng, đánh giá và bằng chứng | Không |
|   3 | Nguyễn Tiến Đạt | 2A202603922 | Vận hành và pháp lý  | Không |
|   4 | Nguyễn Anh Quân | 2A202603950 | Kỹ sư cổng, code | Không |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TranDuyThanh-2A202603919

### Phần việc phụ trách

Vai Trưởng nhóm, Sản phẩm và kinh doanh: Thiết lập repo và quản lý nhánh Git; chủ trì Phiếu A (câu 1.1, 1.6 ở mục A1, A4, A5), điền và ký `config/acceptance_criteria.json`; làm bản đồ dữ liệu và phân tích drift (câu 2.3 ở Phiếu B mục B3), đặt cổng kinh doanh `business` trong `config/operating_gates.json` (câu 2.9 ở mục B7.4), chốt quyết định Gate 1 v1 (mục B8) và v2 (Phiếu C mục C5 câu 3.2, C7, C12).

### Đóng góp cụ thể

- Thiết lập mục tiêu cấp hệ thống, xây dựng bộ câu tiêu chí *"Nếu … thì chúng tôi sẽ …"*, điền ngưỡng vào `config/acceptance_criteria.json` và ký niêm phong trước lần chạy đánh giá đầu tiên (commit `9eee4b7`).
- Xây dựng bản đồ dữ liệu nguồn sự thật vs. bản sao và phân tích kịch bản policy drift từ `REFUND-v3` sang `REFUND-v4` ngày `2026-12-01` (mục B3).
- Thiết lập các ngưỡng cổng kinh doanh (`daily_refund_cap_vnd = 1800000`, `cost_budget_per_ticket_vnd = 1200`, `pilot_scope` tại 2 kho `HN` và `HCM`, `roi_min = 0.10`) và chủ trì quyết định Gate 1 v1 & v2.

### Bằng chứng

- Mã commit: `9eee4b7` (`Sign acceptance criteria`), `589bbe2` (`Complete form A and team roster`), `816c8ee` (`B3, B7.4`).
- Mã lần chạy: `R-base-before-20261119-150226-bde05c`, `R-base-prepared-20261119-150714-08c90d`.
- Các mục phiếu: Phiếu A (`A1`, `A4`, `A5`), Phiếu B (`B3`, `B7.4`, `B8`), Phiếu C (`C5`, `C7`, `C12`).

### Exit ticket

- **Một điều học được:** Việc ký niêm phong tiêu chí chấp nhận và quy tắc quyết định (`decision_rule`) trước khi nhìn số liệu giúp nhóm giữ kỷ luật khách quan tại Gate 1, không hạ chuẩn theo kết quả chạy thử và biết cách dùng phạm vi pilot (`pilot_scope`) cùng trần ngân sách để kiểm soát rủi ro kinh doanh.
- **Một điều còn chưa chắc:** Khi mở rộng từ 2 kho đơn lẻ (`HN`, `HCM`) sang các kho có đặc thù đơn hàng khác biệt (như kho sỉ `HCM-B2B`), cần thu thập bao nhiêu ngày dữ liệu thực tế để tách riêng bộ ngưỡng `cost_per_ticket_vnd_max` và `auto_limit_vnd` cho từng phân khúc.

## VoThiPhuongNhung-2A202603918

### Phần việc phụ trách

Vai Kỹ sư cổng, đánh giá và bằng chứng (Vai 3): Thiết kế chỉ số offline ở Phiếu A (câu 1.3 mục A2, câu 1.5 mục A3); chạy các lệnh `eval`, `gate`, `trace`, `checkpoint` sau khi tiêu chí đã ký; điền nhật ký và phân tích lần chạy đầu tiên cùng bảng soát lỗi `T-002@55` (Phiếu B mục B0, B1, B2); viết hai bước chống rò rỉ dữ liệu và thiết kế 2 ticket hiểm Behavioral Test (`--adhoc`) cho buổi demo (mục B7.2, B7.3); chạy `grade` và dò trace ca lỗi ở Vòng 2 (Phiếu C mục C0, C1, C2).

### Đóng góp cụ thể

- Thiết kế offline metric đo tỉ lệ ghi lỗi hãng oan ở bước `file_carrier_fault` (mục A2) và phân tích khoảng tin cậy 95% (mục A3).
- Chạy đánh giá mốc `base`, `after`, chốt checkpoint `42bfd853` (`prepared`), dò trace `T-002@55` chỉ ra lỗi chìm `model_override` khiến hệ thống hoàn sai `20.000đ` và phạt oan hãng `VNX` (mục B0–B2).
- Thiết kế và chạy kiểm chứng 2 ticket hiểm `--adhoc` trên đơn quà tặng `O-1024` và `O-1026` để chứng minh hệ thống cắt bỏ hoàn toàn `customer_note` và `recipient_contact` khi gửi thông báo cho hãng (mục B7.2–B7.3).

### Bằng chứng

- Mã commit: `f7c3ade` (`Upcode`), `9e2bdd0`, `302e35b` (PR #1).
- Mã lần chạy: `R-base-before-20261119-150226-bde05c`, `R-base-after-20261119-150553-08c90d`, `R-base-prepared-20261119-150714-08c90d`.
- Các mục phiếu: Phiếu A (`A2 - câu 1.3`, `A3 - câu 1.5`), Phiếu B (`B0`, `B1`, `B2`, `B7.2`, `B7.3`), Phiếu C (`C0`, `C1`, `C2`).

### Exit ticket

- **Một điều học được:** Chỉ nhìn `pass_rate` tổng thể (`0.9909`) rất dễ bỏ lọt các lỗi chìm nghiêm trọng như `T-002@55`; phải kết hợp dò trace từng bước, tách chỉ số theo phân khúc kho/hãng (`by_segment`) và kiểm thử hành vi (`behavioral test`) bằng các ticket hiểm ngoài bộ nền.
- **Một điều còn chưa chắc:** Cách thiết kế bộ ticket behavioral test tự động quy mô lớn để bao phủ hết các biến thể ngôn ngữ tự nhiên của khách hàng khi hệ thống chuyển từ MockLLM sang mô hình LLM thật.

## NguyenTienDat-2A202603922

### Phần việc phụ trách

Vai Vận hành và pháp lý (Vai 4): Phụ trách câu 1.2, 1.4 (Phiếu A mục A1, A2); câu 2.4, 2.5, 2.10 (Phiếu B mục B4 HAZOP vòng 1, B5 Checklist go-live 9 nhóm việc, B6 Pre-mortem, B7.5 Runbook phần 1–3, B7.6 Giờ cao điểm); câu 3.1, 3.3, 3.4, 3.5, 3.7 (Phiếu C mục C3 phần riêng theo thẻ, C4 HAZOP của thẻ, C5 giả định môi trường, C6 & C9 Fault tree trước và sau khi sửa, C10 Risk register, C11 cập nhật Checklist & Runbook phần 4–5); cấu hình `operations` và `legal` trong `config/operating_gates.json`; hoàn thiện `submission/submission.json` và chạy gom bài nộp `lab10.check_submission --collect`.

### Đóng góp cụ thể

- Xác định mục tiêu vận hành & đối soát từ góc nhìn chị Oanh (`NV-OANH`) và chị Hạnh (`NV-HANH`), thiết kế telemetry production không nhãn theo dõi rò rỉ PII và lỗi ghi oan cho bên thứ ba.
- Phân tích HAZOP mở rộng (kỹ thuật & ngoài kỹ thuật), lập Checklist go-live 9 nhóm việc gắn PIC cụ thể, thiết lập cổng `operations` (`pic: "NV-TUNG"`, `approver_id: "NV-HANH"`, SLA 60 phút, điều kiện dừng) và `legal` (`pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`) trong `config/operating_gates.json`.
- Xây dựng Runbook vận hành phần 1–5, phương án Giờ cao điểm, phân tích phần riêng theo thẻ (C3), Fault tree đa tầng (C6, C9), Risk register (C10) và đóng gói `submission/submission.json`.

### Bằng chứng

- Mã commit: `4c4671b` (Giai đoạn 1 - PR #2), `03a0da2` (Giai đoạn 2), `bf88988` (Giai đoạn 3 - PR #5) trên nhánh `dat_vanhanh&phaply` / `main`.
- Mã lần chạy: `R-base-before-20261119-150226-bde05c`, `R-base-after-20261119-150553-08c90d`, `R-base-prepared-20261119-150714-08c90d`.
- Các mục phiếu: Phiếu A (`A1`, `A2`), Phiếu B (`B4`, `B5`, `B6`, `B7.5`, `B7.6`), Phiếu C (`C3`, `C4`, `C5`, `C6`, `C9`, `C10`, `C11`, `C12`).

### Exit ticket

- **Một điều học được:** Một hệ thống AI Agent có quyền ghi sổ (`issue_refund`, `file_carrier_fault`, `notify_carrier`) không thể chỉ dựa vào prompt hay độ chính xác của model; để đưa lên pilot an toàn bắt buộc phải kết hợp cổng chặn tất định bằng code (`guards.py`) với cổng giới hạn bằng con số, phân quyền con người (`approver_id`, `reviewers_on_shift`, `decision_note`, `review_sampling_pct`) và quy trình dừng khẩn cấp trong Runbook.
- **Một điều còn chưa chắc:** Khi triển khai thực tế ở nhiều depot với lưu lượng biến động lớn theo mùa sale/bão lũ, làm thế nào để tối ưu động (dynamic scaling) giữa tỉ lệ kiểm mẫu (`review_sampling_pct`), số người trực ca và phạm vi tự động hóa sao cho vừa giữ được lòng tin của nhân viên duyệt vừa không làm đội chi phí giữ chỗ khi tải thấp.

## NguyenAnhQuan-2A202603950

### Phần việc phụ trách

Vai Kỹ sư cổng, code (Vai 2): Trực tiếp thiết kế và lập trình các cổng phòng ngừa cấp hệ thống trong `lab10/guards.py` (`pre_guard` và `write_gate`), kiểm thử hồi quy với `unittest` và `lab10.eval`, điền bảng mô tả cổng ở Phiếu B mục B7.1; nâng cấp cổng xử lý nguyên nhân kỹ thuật ở Vòng 2 và viết chỉ số theo dõi mới trong `lab10/monitors.py` (Phiếu C mục C7, C8).

### Đóng góp cụ thể

- Lập trình `pre_guard` ghim đúng phiên bản chính sách đang hiệu lực (`H.effective_policy`) tại ngày `ctx.as_of`.
- Lập trình 3 nhánh bảo vệ trong `write_gate` (`lab10/guards.py`): (1) Đối chiếu trực tiếp với `tracking DB` để từ chối hoàn tiền sai hoặc điều chỉnh số tiền hoàn về đúng quyền lợi `entitled`; (2) Kiểm tra `H.carrier_at_fault` để chặn ghi lỗi oan cho hãng vận chuyển; (3) Lọc bỏ trường dữ liệu cá nhân `recipient_contact` trước khi gửi thông báo cho hãng.
- Chạy kiểm chứng đạt `110/110` trials trên bộ nền (`pass_rate = 1.0`, `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`) tại lần chạy `R-base-after-20261119-151846-92bcb1` và vượt qua toàn bộ 13 unit tests.

### Bằng chứng

- Mã commit: `469ca0f` (`feat(guards): implement 3 round-1 safety guards in guards.py and fill B7.1`), `5cbeb6f` (PR #3).
- Mã lần chạy: `R-base-after-20261119-151846-92bcb1`.
- Các mục phiếu & file: `lab10/guards.py`, `lab10/monitors.py`, Phiếu B (`B7.1`), Phiếu C (`C7`, `C8`).

### Exit ticket

- **Một điều học được:** Đặt cổng kiểm tra tất định (`pre_guard`, `write_gate`) dựa trên nguồn sự thật (`tracking DB`, `effective_policy`, `ledger_rows`) ở bên ngoài model là cách hiệu quả nhất để biến các lỗi chìm của LLM thành hành vi an toàn có thể kiểm chứng được mà không làm hỏng các ca hợp lệ (`regression`).
- **Một điều còn chưa chắc:** Khi các quy tắc nghiệp vụ phức tạp hơn (nhiều kiện hàng, nhiều chặng trung chuyển, lỗi hỗn hợp giữa shop và hãng), làm sao cân bằng giữa việc tự động sửa tham số (`Verdict.modify`) và việc chuyển cho con người (`Verdict.escalate`) để không làm quá tải hàng chờ CSKH.
