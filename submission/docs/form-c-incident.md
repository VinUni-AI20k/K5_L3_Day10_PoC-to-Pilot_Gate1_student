# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** Simple · **Thẻ đã bốc:** S4 *(Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/S4/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | R-S4-prepared-20261119-165028-eee280 | S4 · prepared | nhận thẻ, chưa sửa thêm (đúng cổng vòng 1) | 1,0 (CI95 [1,0;1,0]) | 1,0 | 0đ · 0 · 0 | 0,3902 | Cổng vòng 1 vá safety (hoàn sai/oan/PII = 0) nhưng còn vượt trần: 5 ca ùn (82') + hoàn tự động 422.000đ > 300.000đ |
| 2 | R-S4-after-20261119-165028-eee280 | S4 · after | sửa vòng 2: trần hoàn 300.000đ + 2 người trực · 12 ca/giờ | 1,0 (CI95 [1,0;1,0]) | 1,0 | 0đ · 0 · 0 | 0,5366 | Hết ùn (0 ca), chờ ≤ 15', hoàn tự động 292.000đ ≤ 300.000đ, cost 7.296đ, ROI 0,37, độ phủ 1,0 |
| 3 | R-base-after-20261119-165011-eee280 | base · after | (kiểm không regression: 2 người trực + trần 300.000đ) | 1,0 (CI95 [1,0;1,0]) | 1,0 | 0đ · 0 · 0 | 0,2727 | Bộ nền vẫn pass 1,0; cost 5.820đ ≤ 9.000, ROI 0,72 ≥ 0,3, 0 ùn |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident S4
```

- Mã lần chạy grade: `R-S4-grade-20261119-165027-eee280` · base: `R-S4-before-20261119-165028-eee280` · prepared: `R-S4-prepared-20261119-165028-eee280`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): trên gói S4 visible, base→prepared: pass_rate 0,8683→1,0; pass_k 0,6829→1,0; hoàn sai 160.000đ→0; lỗi hãng oan 27→0; PII 0. Cổng vòng 1 chặn hoàn sai + lỗi hãng oan + PII.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: prepared vẫn vượt — hàng chờ 5 ca ùn (chờ lâu nhất 82' > 60'), tổng hoàn tự động 422.000đ > ngân sách 300.000đ (ngày 11.11).

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Con người & vận hành (chính) + Kỹ thuật (LLM 429 → fail_open) + Kinh doanh (ngân sách 300k ngày sale).
- Có nằm trong các lý do bàn đã viết không? Có một phần — B6 có ý "chi phí/ticket vượt mục tiêu khi nhiều ca chuyển người" (kinh doanh). Thiếu hai lý do: "LLM nghẽn → fail_open duyệt khi chưa kiểm được policy" và "một người trực không đủ khi việc gấp ba" — thêm ở bảng dưới.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| LLM 429 giờ cao điểm → agent fail_open tự duyệt khi chưa kiểm được policy (S4-08@11) | Kỹ thuật | trace S4-08: `llm_error`, `llm_fallback(fail_open)`, `proposal.basis=fail_open`; monitor `fail_open_rate` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite S4 --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `khách, hãng vận chuyển, và LogiX (Finance)` · đo bằng gì `số ca ùn, thời gian chờ, tổng hoàn tự động/ngày, hoàn sai` · bao nhiêu ở mốc base `4 ca ùn (78'), hoàn tự động 466.000đ > 300.000đ, hoàn sai 160.000đ, 27 lỗi hãng oan`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | Trace S4-08@11: dòng 06 `llm_fallback fail_open` → dòng 07 `proposal basis=fail_open`, hoàn 24.000đ khi chưa kiểm được policy (đơn do shop xuất kho trễ) | Khách/LogiX: chi tiền khi chưa kiểm chính sách; hãng có thể bị ghi oan | cao | chìm |
| 2 | Report S4: 5 ca bị ùn, chờ lâu nhất 82 phút > SLA 60' (1 người trực · 6 ca/giờ, 39% ticket chuyển người) | Khách chờ lâu; chị Hạnh quá tải | cao | ngữ cảnh |
| 3 | Report S4: tổng hoàn tự động một ngày 422.000đ > ngân sách Finance 300.000đ ngày 11.11 | LogiX/Finance vượt ngân sách; rủi ro kiểm soát chi | cao | ngữ cảnh |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Có — fail_open tự lấy kết quả khi policy_check nghẽn | Không | Không |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | Có — policy_check không trả lời được | Có — thiếu người trực cho đỉnh việc | Không |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | Không | Không | Không |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Có — nhiều 429 liên tiếp đẩy sang fail_open | Có — việc dồn hết một giờ cao điểm | Không |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Duyệt khi chưa kiểm được policy → rủi ro hoàn sai/ghi oan | Khách chờ quá SLA 60 phút | Vượt ngân sách Finance chốt cho ngày sale |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Giới hạn thiệt hại: cổng vòng 1 tính lại quyền lợi theo tracking DB + monitor fail_open | Vận hành: thêm người trực + cam kết công suất | Giới hạn: hạ trần hoàn tự động 300k (config) |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | fail_open → cổng đối chiếu DB; không đủ điều kiện → chuyển người duyệt | Ticket ùn → người duyệt trong SLA | Khoản vượt trần → chuyển người duyệt |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `fail_open_rate` | `queue_stuck_rate` | theo dõi tổng hoàn tự động (report) + `queue_stuck_rate` |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `policy_check`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `policy_check` (lời gọi LLM) | INCAPABLE | Ticket `S4-08@11`: LLM 429 giờ cao điểm → `policy_check` không trả lời → agent `fail_open` tự quyết (trace: `llm_error`, `llm_fallback(fail_open)`, `proposal.basis=fail_open`); hoàn 24.000đ khi chưa kiểm được policy. | Khách/LogiX: chi tiền khi chưa kiểm chính sách; hãng có thể bị ghi oan. | Report ghi `fail_open_rate` trên S4 = 0,1854; cổng vòng 1 tính lại quyền lợi theo tracking DB. | `write_gate · issue_refund` tính lại quyền lợi theo tracking DB + metric `fail_open_rate` (chặn + giám sát). |
| Năng lực người duyệt (vận hành) | INCAPABLE | 30/41 ticket đến trong một giờ, vượt năng lực 1 người × 6 ca/giờ → prepared còn 5 ca ùn, chờ lâu nhất 82'. | Khách chờ quá SLA 60'; chị Hạnh quá tải. | Vòng 1 chỉ có 1 người · 6 ca/giờ, chưa có cách giảm tải. | Cổng vận hành: `reviewers_on_shift=2`, `review_capacity_per_hour=12` (giảm tải). |
| `parcel_id` / `carrier_id` (đơn nhiều kiện) | INVALID / WRONG (chưa thấy trên trace) | Giả định, chưa thấy trong trace S4: đơn nhiều kiện/kho với dữ liệu kiện-hãng cũ → ghi lỗi cho sai kiện hoặc sai hãng. | Hãng/tài xế không liên quan bị quy lỗi; kế toán khó đối soát. | Trace S4 chưa có ca này; chưa có kiểm tra nhất quán kiện-hãng. | Chỉ ghi khi `order_id`/`parcel_id`/`carrier_id` khớp bản ghi kiện hiện hành; thiếu/mơ hồ thì chuyển người (chặn/giới hạn). |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: **đề xuất (đã đối chiếu trên report S4, grade `R-S4-grade-20261119-165027-eee280`).**

1. **LLM lỗi / fail-open:** Khi kiểm tra policy thất bại và `proposal.basis == "fail_open"`, không được tự động ghi hoàn hoặc ghi lỗi hãng dựa trên đề xuất fail-open; chuyển người trước thao tác ghi. **Invariant:** số lệnh ghi tự động dựa trên đề xuất fail-open bằng 0. **Kiểm chứng:** đối chiếu event `llm_fallback`, `proposal.basis`, verdict và sổ cái/lỗi hãng theo từng trial; nguồn kiểm là trace/report S4 và `lab10/guards.py`. **Trạng thái: đã kiểm trên report S4** — `fail_open_rate` trên S4 = 0,1854 (bộ nền 0); cổng vòng 1 tính lại quyền lợi theo tracking DB nên không có lệnh ghi tự động nào dựa trên fail_open.
2. **Trần hoàn tự động ngày sale:** Khi khoản hoàn tự động kế tiếp làm tổng ngày vượt ngân sách Finance có hiệu lực, không ghi khoản đó tự động và chuyển người duyệt. **Invariant:** tổng các dòng hoàn tự động không có `approval_id` trong mỗi ngày mô phỏng không vượt `ops_limits.daily_auto_refund_budget_vnd` (mock S4: 300.000đ). **Kiểm chứng:** đối chiếu từng dòng ledger theo ngày/seed và `ops.refund.auto_refund_day_max_vnd` với ngân sách trong report S4. **Trạng thái: đã kiểm trên report S4** — sau sửa vòng 2, tổng hoàn tự động 292.000đ ≤ 300.000đ; không còn dòng vượt ngân sách.
3. **An toàn khi tải tăng:** Khi tải tăng hoặc LLM nghẽn, không được có hoàn sai hoặc ghi oan hãng; không dùng tỷ lệ tự động hóa cao để thay thế kiểm tra an toàn. **Metric:** `wrongful_refund_vnd = 0` và `wrongful_carrier_faults = 0` theo tiêu chí đã ký, đọc cùng tỷ lệ chuyển người và độ phủ. **Kiểm chứng:** so report S4 base/prepared/after và trace lỗi theo seed, có phân đoạn nếu report hỗ trợ. **Trạng thái: đã kiểm trên report S4** — `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`, `pii_leaks = 0` trên S4 sau sửa.
4. **Hàng chờ duyệt:** Khi nhu cầu duyệt tăng, ca cần người phải được nhận xử lý trong SLA mock 60 phút; nếu nguy cơ vượt SLA hoặc ca bị ùn thì kích hoạt cảnh báo và quy trình can thiệp do Ops phê duyệt. **Invariant/metric:** `queue_stuck = 0` theo tiêu chí đã ký, đồng thời `queue_wait_max_min ≤ 60`; theo dõi số ca và độ phủ. **Kiểm chứng:** đọc khối queue và các dòng vượt trần của report S4 theo từng mốc; kiểm runbook và cấu hình nhân sự với Đức. **Trạng thái: đã kiểm trên report S4** — `queue_stuck = 0` sau sửa (prepared còn 5 ca ùn/82'), `queue_wait_max_min = 15 ≤ 60`.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): `write_gate`/event và ledger cho fail-open; `business.daily_refund_cap_vnd` và `ops.refund` cho trần; report `wrongful_refund_vnd`, `wrongful_carrier_faults`, `ops.queue`, `coverage` và trace tương ứng. Đây là cách kiểm đề xuất, không khẳng định đã đạt.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Trong ca cao điểm sẽ có đủ người duyệt đã được đào tạo và người dự phòng có thể được gọi kịp; Ops/Finance công bố đúng ngân sách/ngưỡng trước ca; lượng ticket theo giờ được dự báo đủ sát để quyết định giảm tải. Các giả định này có thể sai khi 30 ticket đến trong một giờ hoặc người dự phòng không sẵn sàng.

Vì sao có thể sai: S4 có 30/41 ticket đến trong một giờ trong khi một người chỉ duyệt khoảng 6 ca/giờ; đây là giới hạn nhân lực và thời điểm đến ngoài phần mềm. Báo cáo cũng cho thấy cap nhóm 500.000đ không khớp ngân sách Finance 300.000đ của thẻ.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S4-prepared-20261119-165028-eee280`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: Đêm 11.11 — hàng chờ duyệt ngập + hoàn tự động vượt ngân sách + fail_open duyệt khi chưa kiểm policy (cho ai: khách, hãng vận chuyển, LogiX/Finance; đo bằng: số ca ùn, thời gian chờ, tổng hoàn tự động/ngày, hoàn sai)
 └─ HOẶC
 ├─ [1] LLM 429 giờ cao điểm → agent fail_open tự duyệt khi chưa kiểm được policy  tầng: kỹ thuật / hành động
 │ └─ vì: policy_check không trả lời → proposal.basis=fail_open, hoàn khi chưa kiểm policy  bằng chứng: ticket S4-08@seed 11 (llm_error, llm_fallback fail_open)
 ├─ [2] Một người trực × 6 ca/giờ không đủ so với 30 ticket đến trong một giờ  tầng: con người / vận hành
 │ └─ vì: hàng chờ dồn trong giờ cao điểm  bằng chứng: report prepared — 5 ca ùn, chờ lâu nhất 82'
 └─ [3] Trần hoàn cap 500.000đ > ngân sách Finance 300.000đ ngày sale  tầng: kinh doanh
 └─ vì: tổng hoàn tự động vượt ngân sách  bằng chứng: report prepared — hoàn tự động 422.000đ > 300.000đ
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Không được tự động ghi hoàn/ghi lỗi hãng dựa trên đề xuất fail-open; phải chuyển người trước thao tác ghi. | LLM luôn trả lời kịp trong giờ cao điểm. |
| [2] | Ca cần người phải được xử lý trong SLA 60 phút; phải có phương án nhân sự cho đỉnh tải. | Trong ca cao điểm luôn đủ người duyệt đã đào tạo và gọi được người dự phòng kịp. |
| [3] | Tổng hoàn tự động trong ngày không vượt ngân sách Finance. | Ngân sách/trần đặt khớp ngân sách Finance ngày sale (cap 500.000đ ≠ 300.000đ). |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite S4 --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident S4
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | LLM 429 → fail_open duyệt khi chưa kiểm policy | (cổng vòng 1) `guards.py write_gate · issue_refund` tính lại quyền lợi theo tracking DB; monitor `fail_open_rate` | chặn + giới hạn thiệt hại | GIẢM mạnh; NGĂN hẳn hoàn vượt quyền lợi theo DB | R-S4-after-20261119-165028-eee280 |
| [2] | 1 người trực không đủ khi việc gấp ba | `config/operating_gates.json`: `operations.reviewers_on_shift=2`, `review_capacity_per_hour=12` | vận hành | GIẢM khả năng ùn: 5 ca ùn → 0, chờ 82'→15' | R-S4-after-20261119-165028-eee280 |
| [3] | Hoàn tự động vượt ngân sách 300k ngày sale | `config/operating_gates.json`: `business.daily_refund_cap_vnd=300000` (tools.py chặn phần vượt, chuyển người) | giới hạn thiệt hại | NGĂN hẳn phần vượt ngân sách: hoàn tự động 422k→292k | R-S4-after-20261119-165028-eee280 |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `fail_open_rate` (và `queue_stuck_rate`) |
| **Bước / hành vi được đo** | Bước kiểm chính sách: LLM policy_check nghẽn → agent rơi vào fail_open (và hàng chờ người duyệt bị ùn) |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ trial có sự kiện fail_open (%) và tỉ lệ trial bị ùn hàng chờ (%) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `trial["events"]` (type=llm_fallback, mode=fail_open) và `trial["queue_stuck"]` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | số trial có event fail_open ÷ tổng trial; số trial queue_stuck ÷ tổng trial; trial thiếu events/queue_stuck coi là không có (đếm riêng) |
| **Khung thời gian / ngưỡng báo động** | theo ngày/ca; VÀNG khi fail_open_rate > 0,05 hoặc queue_stuck_rate > 0; ĐỎ khi > 0,15 hoặc > 0,05 |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy fail_open ở kênh khác ngoài policy_check; queue_stuck_rate phụ thuộc mô phỏng hàng chờ, không phản ánh chất lượng quyết định |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | fail_open_rate: 0 · 0,1854; queue_stuck_rate: 0 (base) · 0,0976 (before) / 0 (after) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S4-after-20261119-165028-eee280`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Đêm 11.11 — hàng chờ duyệt ngập + hoàn tự động vượt ngân sách + fail_open duyệt khi chưa kiểm policy
 └─ HOẶC
 ├─ [1] fail_open duyệt khi chưa kiểm policy  VÀ [write_gate issue_refund tính lại quyền lợi theo tracking DB hỏng]
 ├─ [2] đỉnh tải vượt năng lực người trực  VÀ [config reviewers_on_shift=2, review_capacity_per_hour=12 hỏng]
 └─ [3] hoàn tự động vượt ngân sách  VÀ [business.daily_refund_cap_vnd=300000 hỏng] (còn hở: tracking DB/ngân sách sai)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `write_gate · issue_refund` (tính lại quyền lợi theo tracking DB) + metric `fail_open_rate` | chặn + giới hạn thiệt hại | NGĂN hẳn hoàn vượt quyền lợi theo DB; chỉ GIẢM/không ngăn nếu chính tracking DB sai. | Tracking DB sai hoặc thiếu. |
| [2] | `operations.reviewers_on_shift=2`, `review_capacity_per_hour=12` | vận hành | GIẢM: 5 ca ùn → 0, chờ 82' → 15'; không ngăn hẳn nếu đỉnh tải thật vượt 12 ca/giờ. | Đỉnh tải thật vượt 12 ca/giờ. |
| [3] | `business.daily_refund_cap_vnd=300000` | giới hạn thiệt hại | NGĂN phần vượt: 422.000đ → 292.000đ; còn hở nếu ngân sách Finance công bố sai. | Ngân sách/trần công bố sai. |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Đỉnh tải ngày sale lớn hơn mock (30 ticket/giờ) vượt 12 ca/giờ sau sửa | Trung bình | Cao | NV-TUNG | `queue_stuck_rate` / `queue_wait_max_min` (monitors.py/report) | Gọi người dự phòng, thu hẹp phạm vi (giữ coverage > 0), tắt thao tác ghi nếu chờ > 60'. | Ảnh hưởng Bước đánh giá 2. | MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 Chất lượng / tính toàn vẹn | Chưa | Grade `R-S4-grade-20261119-165027-eee280`: các chỉ số an toàn S4 sau là 0, pass_rate/pass_k = 1,0000, verdict PASS-VISIBLE, tự kiểm tra integrity/criteria/visible/regression/monitor đều ✅, ceilings.violations = []. Còn phải đo lại trên pilot thật (đỉnh tải, năng lực duyệt). | Ngô Ngọc Hải |
| 3 Bảo mật | Chưa | B4 đã xác định `customer_note` là dữ liệu tự do; S4 after `pii_leaks=0`; chưa có kiểm chứng payload trên pilot thật. | Trần Minh Đức |
| 5 Hiệu năng, hạ tầng | Chưa | S4 after đã hết ùn: `queue.wait_max_min=15 ≤ 60`, `queue.stuck=0` (trước đó 1 người × 6 ca/giờ không đủ; nay 2 người × 12 ca/giờ); còn phải đo lại đỉnh tải thật ngoài mock. | Trần Minh Đức |
| 7 Vận hành | Chưa | S4 after hết ùn (0 ca), report `ops.violations` rỗng; ngưỡng gọi hỗ trợ đã nêu ở B7.6 nhưng chưa được vận hành/đo trong pilot. | Trần Minh Đức |
| 8 Con người, pháp lý | Chưa | S4 after ghi 0 lỗi hãng oan và 0 PII; cần xác minh quy trình khiếu nại và quyền dừng trước go-live. | Trần Minh Đức |
| 9 Quyết định | Chưa | S4 after: chờ 15 phút, 0 ca ùn, tổng hoàn tự động 292.000đ ≤ ngân sách 300.000đ; đã chốt quyết định v2 (Tiếp tục) ở C12. | Lê Thị Ly |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Có `queue_wait_max`, `queue_stuck` và tổng hoàn/ngân sách trong report. Ngưỡng vàng 30 phút/đỏ 60 phút và ngưỡng Finance phải phát cảnh báo trước khi chạm trần; ở mốc prepared grade S4 ghi 82 phút, 5 ca ùn và 422.000đ > 300.000đ, sau sửa vòng 2 (after) hết ùn (chờ 15 phút, 0 ca ùn) và hoàn tự động 292.000đ ≤ 300.000đ. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Giữ SLA đỏ 60 phút, gọi hỗ trợ từ >6 ca chờ hoặc >30 phút. Đổi cảnh báo hoàn từ 80% của cap 500.000đ (=400.000đ) sang 80% ngân sách Finance 300.000đ (=240.000đ), dừng hoàn tự động tại 300.000đ. Đây là đề xuất; Ly cần cập nhật business cap và chạy lại. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | NV-HANH duyệt, NV-TUNG là PIC gọi người dự phòng và giữ công tắc. Gọi thêm người khi >6 ca chờ hoặc >30 phút; không coi việc thêm một người là đủ nếu chưa đo lại hàng chờ/ROI. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Khi chờ >60 phút/có ca ùn: tạm dừng lệnh ghi tự động, chuyển tay và thu hẹp phạm vi còn >0. Cảnh báo tài chính ở 240.000đ, hard stop 300.000đ. Mô phỏng what-if chưa ghi journal cho HCM-only + cap 300.000đ cho coverage 26,83%, chờ 6 phút, 0 ùn, ROI 0,61; đây chỉ là phương án để Ly/Hải chạy lại bằng `eval`, chưa phải kết quả chính thức. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | NV-OANH đối soát với hãng/shop; NV-HANH thông tin cho CSKH/người duyệt về các quyết định bị rà soát. NV-TUNG điều phối qua `slack:#logix-refund-pilot` trong ca; chỉ thông báo khoản đã xác minh, không suy đoán hoặc tiết lộ PII. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | S4 report hiện `pii_leaks=0`, nên chưa có bằng chứng PII rời hệ thống; không tuyên bố có sự cố lộ. Nếu payload/log thực tế xác nhận lộ, NV-TUNG bảo toàn log và báo đầu mối pháp lý/Privacy cùng NV-OANH ngay, không xóa dấu vết. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Số đo report phát hiện chờ 82 phút/5 ca ùn ở mốc prepared và hoàn vượt ngân sách; phản hồi của giám sát giúp nhận diện đỉnh tải. `grade` xác nhận monitor ✅ sau khi đăng ký `fail_open_rate`/`queue_stuck_rate`; cần thêm alert trực tiếp theo hàng chờ, tốc độ ticket đến và tổng hoàn theo ngày. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu tốc độ đến vượt 6 ticket/giờ/người hoặc hàng chờ >6 ca thì NV-TUNG gọi người dự phòng; nếu chờ >60 phút/có ca ùn thì dừng lệnh ghi tự động, chuyển thủ công và thu hẹp phạm vi.
2. Nếu nhà cung cấp LLM lỗi liên tục quá 5 phút thì fail-closed: dừng các lệnh ghi tự động, không dùng fallback để tự duyệt, chuyển ticket sang người; NV-TUNG chỉ bật lại sau khi Hải xác minh lỗi đã hết và người duyệt ký.
3. Nếu người duyệt không tin một quyết định thì tạm dừng thao tác liên quan, kiểm tra 100% các ca cùng kiểu trong ca đó, ghi lý do và chỉ bật lại khi NV-HANH cùng NV-TUNG xác nhận bằng chứng.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `2e78acd` (giống v1) |
| Hash chốt cổng vòng 1 | `12398971` (giống v1) |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S4-before-20261119-165028-eee280` · prepared: `R-S4-prepared-20261119-165028-eee280` · after: `R-S4-after-20261119-165028-eee280` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | KHÔNG — after: 0 ca ùn, chờ 15' ≤ 60', hoàn tự động 292.000đ ≤ 300.000đ, cost 7.296đ ≤ 9.000, ROI 0,37 ≥ 0,3. |
| Kho hoặc hãng có số xấu nhất: kho DN (chi phí 7.568đ). Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Kho DN có chi phí/ticket 7.568đ (xấu nhất); không đổi quyết định nhưng cần theo dõi. |
| Quyết định (khoanh một) | **Tiếp tục** (mọi chỉ số bắt buộc đạt, không vượt trần) |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S4-after-20261119-165028-eee280` · wrongful_refund 0, wrongful_carrier_faults 0, pii_leaks 0, queue_stuck 0, pass_rate 1,0 ≥ 0,97, pass_k 1,0 ≥ 0,91 — ĐẠT. |
| Bằng chứng 2 | `R-S4-prepared-20261119-165028-eee280`: cổng vòng 1 đưa hoàn sai 160.000đ → 0 và lỗi hãng oan 27 → 0 (pass_rate 0,8683 → 1,0). |
| Bằng chứng 3 | `R-S4-after-20261119-165028-eee280`: sửa vòng 2 hết ùn (5 → 0 ca, 82' → 15') và đưa hoàn tự động 422.000đ → 292.000đ ≤ 300.000đ; độ phủ 1,0. |
| Khớp dòng nào trong `decision_rule` đã ký? | "Tiếp tục": mọi chỉ số bắt buộc đạt, không vượt trần, độ phủ 1,0 > 0. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | (không áp dụng) |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (không áp dụng) |
| Nếu Dừng: bài học ghi lại | (không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | 2026-11-23 |
| PIC ký | Ngô Ngọc Hải (trưởng nhóm) |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: GIỮ (Tiếp tục) nhưng mạnh hơn nhờ bằng chứng S4 + sửa vòng 2: an toàn (hoàn sai/oan/PII) = 0 trên cả bộ nền và S4, hết ùn (5 → 0 ca), hoàn tự động 292.000đ ≤ 300.000đ.
- Report tự kiểm tra: mã lần chạy `R-S4-grade-20261119-165027-eee280` · ô nào còn đỏ (nguyên nhân × tầng): không còn ô đỏ; verdict PASS-VISIBLE, ceilings.violations = [], continue_allowed = true.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: đỡ được 160.000đ hoàn sai + 27 lỗi hãng oan → 0; bỏ sót ùn và vượt ngân sách (còn 5 ca ùn/82' và 422.000đ > 300.000đ).
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: report ghi "được phép cân nhắc Tiếp tục" (continue_allowed = true) → quyết định khớp.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: năng lực duyệt thật và lượng ticket đến ngoài mô phỏng.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. **environment_assumption:** "Pilot giả định Ops có đủ người duyệt đã đào tạo và gọi được người dự phòng kịp giờ cao điểm, và Finance công bố đúng ngân sách 300.000đ/ngày sale trước ca; đây có thể sai vì S4 có 30/41 ticket đến trong một giờ."
2. **reduce_or_prevent:** "Cổng vòng 1 NGĂN hẳn hoàn sai, lỗi hãng oan và PII (về 0 trên bộ nền và S4); sửa vòng 2 (trần hoàn 300.000đ + 2 người trực · 12 ca/giờ) NGĂN hẳn phần vượt ngân sách (422.000đ→292.000đ) và hết ùn (5→0 ca, 82'→15'); các cổng chỉ GIẢM (không ngăn hẳn) rủi ro quá tải thật ngoài mô phỏng."
3. **measure_in_pilot:** "Cần đo lại trong pilot thật: ticket đến theo giờ, thời gian chờ và số ca ùn, tỉ lệ chuyển người, tổng hoàn tự động so với cap Finance, lỗi hãng/PII, chi phí mỗi ticket và ROI theo kho trước Bước đánh giá 2."
