# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Simple`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Simple-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S4`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Ngô Ngọc Hải | 2A202603939 | Kỹ sư cổng | ✓ |
|   2 | Trần Minh Đức | 2A202603977 | Vận hành và pháp lý |  |
|   3 | Lê Thị Ly | 2A202603989 | Sản phẩm và kinh doanh |  |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NgoNgocHai-2A202603939

### Phần việc phụ trách

Kỹ sư cổng: `lab10/guards.py`, `lab10/monitors.py`; chạy các lệnh `lab10.eval`, `lab10.trace`, `lab10.gate`, `lab10.checkpoint`. Câu 1.3, 2.1, 2.2, 2.6–2.8, 3.1 (trace), 3.6. Trưởng nhóm, phụ trách repo.

### Đóng góp cụ thể

Kỹ sư cổng + trưởng nhóm: dựng repo (fork/Public/collaborators), sửa danh tính Git về MSSV; câu 1.3 (offline metric `model_override`); chạy base + soát `T-002@55`; viết 3 cổng trong `guards.py` (hoàn theo tracking DB, chặn lỗi hãng oan, bỏ PII) — base: hoàn sai 20.000đ→0, lỗi hãng oan 1→0; chốt cổng vòng 1 (`12398971`) + quyết định v1; thẻ S4: trace `S4-07/S4-08`, thêm monitor `fail_open_rate`/`queue_stuck_rate`, chỉnh config S4 (trần hoàn 300.000đ, 2 người trực, 12 ca/giờ); `grade --incident S4` → **PASS-VISIBLE** (`R-S4-grade-20261119-165027-eee280`); viết `PHAN-VAI-NHOM.md`.

### Bằng chứng

Mã commit: `1846da4` (chốt vòng 1 + v1), `b9d5ff5` (thẻ S4). Mã run: base `R-base-before-20261119-153723-b45eeb`, after `R-base-after-20261119-165011-eee280`, prepared `R-base-prepared-20261119-161030-535bf6`; S4 base `R-S4-before-20261119-165028-eee280`, prepared `R-S4-prepared-20261119-165028-eee280`, after `R-S4-after-20261119-165028-eee280`, grade `R-S4-grade-20261119-165027-eee280` (PASS-VISIBLE). Phiếu: A (1.3); B (B0/B1/B2/B7.1–B7.3); C (C0/C1/C2/C7/C8).

### Exit ticket

Điều học được: cổng phải dựa trên **nguồn sự thật (tracking DB)**, không tin số khách khai — vá đúng chỗ rẻ hơn nhiều so với tin model. Điều chưa chắc: khi LLM nghẽn nên chặn hẳn (escalate) `fail_open` hay chỉ cần đối chiếu DB như hiện tại; tôi chọn đối chiếu DB để giữ tính hữu dụng, nhưng chưa đo trên bài kiểm tra ẩn.

## TranMinhDuc-2A202603977

### Phần việc phụ trách

Vận hành và pháp lý: `config/operating_gates.json` (mục `operations`, `legal`), runbook, `submission/`, `TEAM.md`. Câu 1.2, 1.4, 2.4 (HAZOP + checklist 9 nhóm), 2.10, 3.3, phần riêng theo thẻ, runbook 4–5.

### Đóng góp cụ thể

Hoàn thiện HAZOP vòng 1 B4 (ba nhánh kỹ thuật và hai nhánh ngoài kỹ thuật), bổ sung tiêu chí kiểm và PIC cho checklist B5, cùng pre-mortem B6 đủ bốn lăng kính (đã chốt). Rà soát runbook vận hành/pháp lý B7.5–B7.6; bổ sung C1, giả định môi trường và specification tại C5, checklist C11 và runbook 4–5. Đối chiếu S4: 30/41 ticket đến trong một giờ; sau khi sửa cấu hình (trần 300.000đ, 2 người trực, 12 ca/giờ) mốc after còn 0 ca ùn, chờ 15 phút, hoàn tự động 292.000đ ≤ 300.000đ, hoàn sai/lỗi hãng oan/PII đều 0 (mốc prepared trước đó: 5 ca ùn, chờ 82 phút, hoàn tự động 422.000đ > 300.000đ).

### Bằng chứng

Grade S4: `R-S4-grade-20261119-165027-eee280`; các mốc `R-S4-before-20261119-165028-eee280`, `R-S4-prepared-20261119-165028-eee280`, `R-S4-after-20261119-165028-eee280`. Kết quả kiểm integrity đạt (`integrity.ok = true`); cả 6 mục kiểm (integrity/criteria/visible/regression/monitor) đều ✅; verdict **PASS-VISIBLE**; `ceilings.violations = []`; `continue_allowed = true`. Xem Phiếu B B4–B7.6 và Phiếu C C1, C5, C11.

### Exit ticket

**Một điều học được:** Thêm người trực không tự động giải quyết đỉnh tải; cần đo tốc độ ticket đến theo giờ, giới hạn tự động và chi phí/ROI cùng lúc.

**Một điều còn chưa chắc:** Người dự phòng thực tế có thể vào ca trong bao lâu, và ngân sách/ngưỡng Finance nào được áp dụng nhất quán ở từng depot trong pilot thật.

## LeThiLy-2A202603989

### Phần việc phụ trách

Sản phẩm và kinh doanh: `config/acceptance_criteria.json`, mục `business` trong `config/operating_gates.json`; nội dung Product & Business trong `templates/form-a-criteria.md`, `form-b-evaluation-gates.md`, `form-c-incident.md`. Câu 1.1, 1.6, 2.3, 2.9, 3.2; chủ trì tổng hợp quyết định Gate 1 v1 (B8) và v2 (C12). Phối hợp câu chung 1.5, 2.5 và phân tích sự cố. Cập nhật đóng góp cá nhân trong TEAM.md.

### Đóng góp cụ thể

Tham gia xây dựng mục tiêu hệ thống và tiêu chí Product & Business tại Phiếu A câu 1.1 và 1.6; xây dựng Data Map và ví dụ policy drift tại Phiếu B mục B3; chốt bốn Business Gates tại B7.4. Hoàn thiện specification cho S4 tại Phiếu C câu 3.2 và quyết định v2 (C12) = **Tiếp tục** kèm 3 dòng, dựa trên report S4 (after: 0 ca ùn, chờ 15 phút, hoàn tự động 292.000đ ≤ 300.000đ).

Sử dụng Codex hỗ trợ audit repository, phân tích yêu cầu và review tài liệu.

### Bằng chứng

`8c82874`: bản nháp tiêu chí Product & Business; `a3b5c51`: nội dung Data Map B3; `ca978d1`: Business Gates B7.4; `35540f9`: merge PR #1. Ký tiêu chí: `hash 523ab187`, commit `2e78acd`. Xem Phiếu A câu 1.1, 1.6; Phiếu B mục B3, B7.4; Phiếu C C5, C12 (v2 = Tiếp tục).

### Exit ticket

**Một điều học được:** Tiêu chí chấp nhận cần được ký trước khi đánh giá. Quyết định Gate 1 phải dựa trên bằng chứng thực nghiệm, đồng thời cân nhắc chất lượng, an toàn, chi phí và khả năng vận hành.

**Một điều còn chưa chắc:** Ngưỡng/ngân sách Finance (trần hoàn/ngày) nào áp dụng nhất quán ở từng depot trong pilot thật, và cách giữ ROI/độ phủ ổn định khi lưu lượng ticket tăng.
