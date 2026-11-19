# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** Simple (K5-L3B-DAY10-Simple-PoCtoPilotGate1) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giảm tổng chi phí xử lý mỗi yêu cầu hoàn tiền giao trễ xuống dưới mức làm tay (10.000đ/ticket) và giữ số tiền hoàn sai = 0, để Gate 1 có đủ căn cứ quyết định chạy pilot ở 2 depot hay không.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mỗi tuần, chị Oanh có thể đối chiếu các khoản hoàn tiền và ghi nhận lỗi hãng với sổ cái, hãng vận chuyển và shop; mỗi khoản có đủ thông tin truy nguyên để xác định đúng số tiền, bên chịu trách nhiệm và giao dịch liên quan.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Chị Hạnh nhận được các ca trợ lý chuyển lên trong thời hạn vận hành, có đủ căn cứ và phần giải thích để duyệt nhất quán các ca vượt hạn mức hoặc chưa rõ; khối lượng ca chuyển không vượt khả năng xử lý của ca trực.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước "chọn độ trễ": agent quyết số ngày trễ dùng để tính tiền hoàn | Gửi thông báo từ LogiX cho hãng vận chuyển (`notify_carrier`). |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chạy mà số ngày trễ agent dùng để tính tiền **khác** số ngày trễ theo tracking DB (%) | Số và tỷ lệ thông báo gửi cho hãng có chứa thông tin cá nhân của người nhận (tên, số điện thoại hoặc địa chỉ), tính theo thông báo/24 giờ và phần trăm. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `model_override` (có `db`, `ticket`) và `tracking.db_delay_days` trong `runs/<mã>/traces/`; bộ nền 22 ticket × 5 seed. Nhãn đúng/sai suy ra từ chính DB (không cần người gán) | Log thông báo gửi ra ngoài (mã giao dịch và payload) đối chiếu với các trường người nhận trong hồ sơ đơn hàng. Đây là tín hiệu quy tắc, không cần nhãn đúng/sai; chỉ ghi bộ đếm, mã tham chiếu và trạng thái cảnh báo, không ghi giá trị PII vào log giám sát. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Đếm số lần có `model_override` chia cho số lần có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng | Tỷ lệ = số thông báo có ít nhất một trường PII khớp ÷ tổng thông báo gửi cho hãng × 100%. Nếu thiếu payload hoặc không đối chiếu được hồ sơ người nhận, đánh dấu “không xác minh được” và phát cảnh báo, không coi là an toàn. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Cửa sổ trượt 24 giờ; báo động ngay khi phát hiện từ 1 thông báo trở lên có PII hoặc có thông báo không xác minh được. PIC báo người trực và tạm dừng gửi thông báo cho hãng để kiểm tra. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy trường hợp **chính tracking DB sai**, hoặc lỗi trễ hệ thống ở đơn nhiều kiện | Có thể bỏ sót PII được diễn đạt khác, thông tin nhạy cảm ngoài các trường đối chiếu hoặc dữ liệu gửi qua kênh khác; đối chiếu tự động cũng có thể báo nhầm. Cần điều tra sự cố, không xem telemetry là kết luận pháp lý. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) ✓ · (c) · (d)**

Giải thích một câu: Chênh lệch 1 lần chạy (49/50 so với 50/50) nằm trong khoảng tin cậy 95% [0,9400; 1,0] của X, nên chưa đủ căn cứ nói Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu `pass_rate` trên bộ nền hoặc trên gói sự cố tụt dưới **0,97** thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn dưới thì Thu hẹp. | Nếu `pass_rate` tụt dưới 0,97 thì Thu hẹp ngay phần (kho / loại ticket) đang kéo tỉ lệ xuống, ghi rõ phần bị cắt. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu `pass^k` tụt dưới **0,91** (tức dưới 21/22 ticket đúng cả 5/5 seed) thì chúng tôi sẽ không chọn Tiếp tục. | Nếu `pass^k` tụt dưới 0,91 thì Cải tiến thêm một vòng vào đúng ticket hỏng, có hạn chót. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai vượt quá **0đ** thì chúng tôi sẽ Cải tiến thêm một vòng (có hạn); quá hạn vẫn > 0 thì Dừng tự động hoá khoản hoàn. | — |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục; sau một vòng sửa vẫn vượt thì tắt tool ghi lỗi hãng và Thu hẹp. | — |
| `pii_leaks_max` | Nếu số lần lộ dữ liệu cá nhân vượt quá **0** thì chúng tôi sẽ tắt ngay tính năng gửi thông tin người nhận cho hãng và không chọn Tiếp tục. | — |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt **0,25** thì chúng tôi sẽ soát lại điều kiện cổng (đang chuyển người quá tay) trước khi chốt. | — |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Không bao giờ hoàn vượt quyền lợi tính từ tracking DB, và không ghi lỗi hãng khi kiện không có `delay_cause` thuộc `fault_causes`.
- Ngưỡng chuyển cho người duyệt: Khi khoản hoàn vượt hạn mức tự động (200.000đ theo REFUND-v3) hoặc khi số ngày trễ khách khai lệch với tracking DB thì chuyển cho người duyệt.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: khách được hoàn đúng, hãng không bị phạt oan, shop không bị trừ sai, người duyệt không quá tải, kế toán đối soát được. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép tỉ lệ tự động cao → hãng (VNX…) gánh lỗi oan và LogiX gánh tiền hoàn sai; ép chuyển người nhiều → chị Hạnh quá tải, chi phí tăng. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng: ngày 1 thành công = hoàn đúng + rẻ hơn làm tay (≤ 9.000đ/ticket) + không lỗi oan. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Không còn nguyên: khi REFUND-v4 hiệu lực 2026-12-01 (hạ `auto_limit_vnd` xuống 100.000đ, bỏ FORCE_MAJEURE) thì ngưỡng `cost_per_ticket_vnd_max` và ranh giới phải viết lại. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **9.000** · `roi_min` **0,3** · `queue_stuck_max` **0**
- Ngày xem lại tiêu chí: `2026-11-23 (một tuần sau pilot)` · Ai dự: `Cả bàn + NV-HANH, NV-TUNG, NV-OANH` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-19T14:49:17` (signed_at trong `config/acceptance_criteria.lock`) |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `2e78acd` (commit "Sign acceptance criteria") |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
