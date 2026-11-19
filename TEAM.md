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
|   2 | Võ Thị Phương Nhung | 2A202603918 | Kỹ sư cổng, code | Không |
|   3 | Nguyễn Tiến Đạt | 2A202603922 | Kỹ sư cổng, đánh giá và bằng chứng | Không |
|   4 | Nguyễn Anh Quân | 2A202603950 | Vận hành và pháp lý | Không |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenAnhQuan-2A202603950

### Phần việc phụ trách

Vai Vận hành và pháp lý: Phụ trách câu 1.2, 1.4 (Phiếu A mục A1, A2); câu 2.4, 2.5, 2.10 (Phiếu B mục B4 HAZOP vòng 1, B5 Checklist go-live 9 nhóm việc, B6 Pre-mortem, B7.5 Runbook phần 1–3, B7.6 Giờ cao điểm); câu 3.1, 3.3, 3.4, 3.5, 3.7 (Phiếu C mục C3 phần riêng theo thẻ, C4 HAZOP của thẻ, C5 giả định môi trường, C6 & C9 Fault tree trước và sau khi sửa, C10 Risk register, C11 cập nhật Checklist & Runbook phần 4–5); cấu hình `operations` và `legal` trong `config/operating_gates.json`; hoàn thiện `submission/submission.json` và chạy gom bài nộp `lab10.check_submission --collect`.

### Đóng góp cụ thể

- Xác định mục tiêu vận hành & đối soát từ góc nhìn chị Oanh (`NV-OANH`) và chị Hạnh (`NV-HANH`), thiết kế telemetry production không nhãn theo dõi rò rỉ PII và lỗi ghi oan cho bên thứ ba.
- Phân tích HAZOP mở rộng (kỹ thuật & ngoài kỹ thuật), lập Checklist go-live 9 nhóm việc gắn PIC cụ thể, thiết lập cổng `operations` (`pic: "NV-TUNG"`, `approver_id: "NV-HANH"`, SLA 60 phút, điều kiện dừng) và `legal` (`pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`) trong `config/operating_gates.json`.
- Xây dựng Runbook vận hành phần 1–5, phương án Giờ cao điểm, phân tích phần riêng theo thẻ (C3), Fault tree đa tầng (C6, C9), Risk register (C10) và đóng gói `submission/submission.json`.

### Bằng chứng

- Mã commit: `4c4671b` (Giai đoạn 1), `03a0da2` (Giai đoạn 2), cùng commit đóng gói Giai đoạn 3 trên nhánh `dat_vanhanh&phaply` / `main`.
- Mã lần chạy: `R-base-before-20261119-150226-bde05c`, `R-base-after-20261119-150553-08c90d`, `R-base-prepared-20261119-150714-08c90d` (và các lần chạy đánh giá gói sự cố).
- Các mục phiếu: Phiếu A (`A1`, `A2`), Phiếu B (`B4`, `B5`, `B6`, `B7.5`, `B7.6`), Phiếu C (`C3`, `C4`, `C5`, `C6`, `C9`, `C10`, `C11`, `C12`).

### Exit ticket

- **Một điều học được:** Một hệ thống AI Agent có quyền ghi sổ (`issue_refund`, `file_carrier_fault`, `notify_carrier`) không thể chỉ dựa vào prompt hay độ chính xác của model; để đưa lên pilot an toàn bắt buộc phải kết hợp cổng chặn tất định bằng code (`guards.py`) với cổng giới hạn bằng con số, phân quyền con người (`approver_id`, `reviewers_on_shift`, `decision_note`, `review_sampling_pct`) và quy trình dừng khẩn cấp trong Runbook.
- **Một điều còn chưa chắc:** Khi triển khai thực tế ở nhiều depot với lưu lượng biến động lớn theo mùa sale/bão lũ, làm thế nào để tối ưu động (dynamic scaling) giữa tỉ lệ kiểm mẫu (`review_sampling_pct`), số người trực ca và phạm vi tự động hóa sao cho vừa giữ được lòng tin của nhân viên duyệt vừa không làm đội chi phí giữ chỗ khi tải thấp.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
