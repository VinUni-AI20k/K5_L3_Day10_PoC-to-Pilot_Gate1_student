# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** Teris · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

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
- Hệ thống trợ lý hoàn tiền LogiX-VN phải xử lý ticket giao trễ nhanh và ít tốn hơn làm tay, đồng thời chỉ tạo các lệnh hoàn tiền, ghi sổ và ghi lỗi hãng vận chuyển chính xác, không phát sinh rò rỉ dữ liệu hoặc thiệt hại cho khách, shop và hãng vận chuyển.

> …

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Đảm bảo các khoản hoàn tiền, lỗi quy trách nhiệm cho hãng vận chuyển và dữ liệu ghi nhận trong sổ cái được chính xác, đầy đủ, có căn cứ truy vết; giúp chị đối soát số liệu với hãng vận chuyển và shop hàng tuần nhanh chóng, hạn chế sai lệch và thất thoát tài chính.

- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Đảm bảo các yêu cầu hoàn tiền được trợ lý xử lý đúng quy trình, các trường hợp phức tạp hoặc không chắc chắn được chuyển đến người duyệt kịp thời; giúp chị kiểm soát khối lượng công việc, tránh ùn tắc yêu cầu chờ duyệt và đảm bảo khách hàng được phản hồi đúng thời hạn.

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
| **Bước / hành vi được đo** | Bước **ghi lỗi hãng** (`file_carrier_fault`). Mỗi bản ghi ở bước này là một "gậy" phạt hãng vận chuyển (bên thứ ba) và đi thẳng vào sổ đối soát của chị Oanh. Bước này có hai điểm yếu đã thấy trong code: nguyên nhân trễ bị trống thì agent mặc định ghi `CARRIER`, và agent luôn ghi cho hãng của **kiện đầu tiên** (`parcels[0]`), không phải kiện bị trễ. | Theo dõi hành vi ghi lỗi hãng (file_carrier_fault), phát hiện trường hợp hãng vận chuyển hoặc shop khiếu nại, yêu cầu điều chỉnh do bị quy trách nhiệm sai. |
| **Thước đo** (một câu, có đơn vị) | **Tỉ lệ ghi oan cho hãng (%)**: trong các bản ghi lỗi hãng agent đã tạo, bao nhiêu phần trăm có cặp `[carrier_id, parcel_id]` không đúng với nhãn. Kèm một số phụ là **số lần bỏ sót** (nhãn có lỗi hãng nhưng agent không ghi), báo riêng, không gộp vào tỉ lệ. | 	Tỷ lệ ghi lỗi hãng bị khiếu nại (%) và tổng giá trị ghi lỗi đang tranh chấp (VNĐ). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | **Bản ghi agent tạo:** trường `faults` trong `runs/<mã lần chạy>/traces/<ticket_id>@<seed>.json` (cùng nội dung với sự kiện `tool` có `tool = file_carrier_fault`). **Nhãn:** `label.faults` trong `data/tickets.jsonl`, nối với trace theo `ticket_id` (file trace không chứa nhãn). **Cỡ mẫu:** bộ nền có 22 ticket × 5 seed (11, 22, 33, 44, 55) = 110 lần chạy; 11/22 ticket có nhãn lỗi hãng, nên nếu agent ghi đúng hết thì có 55 bản ghi. **Người gán nhãn:** người soạn bộ nền đã gán sẵn, căn cứ `delay_cause` của từng kiện trong `data/world.json`. Ticket mới mà bàn tự thêm thì chị Oanh (kế toán đối soát hãng) gán nhãn, căn cứ biên bản xác nhận lỗi của hãng. Kỹ sư cổng không tự gán nhãn. | Bản ghi lỗi hãng trong hệ thống; lịch sử khiếu nại từ hãng và shop; biên bản xác minh, kết quả đối soát. Chị Oanh phối hợp với hãng và shop xác minh. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | **Tỉ lệ ghi oan = số bản ghi sai ÷ tổng số bản ghi lỗi hãng agent đã tạo × 100%**, cộng dồn trên cả 110 lần chạy. Một bản ghi là **sai** khi cặp `[carrier_id, parcel_id]` của nó không có trong `label.faults` của ticket đó. Nếu cùng một ticket bị ghi hai lần cùng một cặp, bản thứ hai cũng tính là sai, vì hãng bị phạt hai lần. **Mẫu số = 0** (agent không ghi bản nào): ghi "không xác định", không ghi 0%. **Lần chạy không tới bước ghi lỗi** (escalated, denied, replied): không vào mẫu số; nếu nhãn của lần chạy đó có lỗi hãng thì cộng vào số bỏ sót. **Ticket không có nhãn** (ví dụ ticket `--adhoc`): loại khỏi cả tử số và mẫu số, đếm riêng là "chưa gán nhãn". Báo kèm danh sách `ticket_id@seed` của mọi bản ghi sai để người khác đối chiếu lại được. | Tỷ lệ khiếu nại = Số bản ghi bị khiếu nại ÷ Tổng bản ghi lỗi hãng do trợ lý tạo × 100%. Mỗi bản ghi chỉ tính một lần. Bản ghi chưa xác minh được đánh dấu chờ xử lý, không mặc định là đúng hoặc sai.|
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo dõi liên tục, tổng hợp hàng ngày. Cảnh báo vàng khi có từ 1 khiếu nại/ngày; cảnh báo đỏ khi có từ 2 khiếu nại/7 ngày hoặc phát hiện một trường hợp ghi sai có bằng chứng. Khi cảnh báo đỏ, tạm dừng tự động ghi lỗi hãng và chuyển sang người duyệt. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | (1) Nhãn lấy từ `delay_cause` trong DB, nên nếu chính DB ghi sai nguyên nhân thì thước đo vẫn chấm là đúng. (2) Không thấy nội dung gửi hãng (`notify_carrier`), ví dụ có lộ số điện thoại người nhận hay không. Việc đó cần thước đo PII riêng. (3) Bộ nền chỉ có 1/25 đơn nhiều kiện (O-1013), nên lỗi "ghi cho hãng của kiện đầu" ít có dịp lộ ra: tỉ lệ thấp ở bộ nền chưa chứng minh bước này an toàn với đơn nhiều kiện. (4) Không thấy bản ghi bị cổng pháp lý chặn trước khi ghi: thước đo đo đầu ra cuối, không đo ý định của agent. | Không phải mọi bản ghi sai đều bị khiếu nại; khiếu nại không đồng nghĩa trợ lý sai; không phát hiện được rò rỉ dữ liệu cá nhân nếu không có chỉ số giám sát riêng. |

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

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

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
| `pass_rate_min` | | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | | |
| `wrongful_refund_vnd_max` | | |
| `wrongful_carrier_faults_max` | | |
| `pii_leaks_max` | | |
| nên có: `escalation_rate_max` | | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

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
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
