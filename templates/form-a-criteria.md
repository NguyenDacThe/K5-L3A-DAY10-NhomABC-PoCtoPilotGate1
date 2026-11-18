# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-NhomABC-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

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

> Mỗi yêu cầu hoàn tiền giao trễ ở 2 depot pilot được khép lại trong ngày với **đúng số tiền, đúng người trả và đúng hãng chịu lỗi so với tracking và chính sách đang hiệu lực**. Trợ lý không tạo ra khoản hoàn sai, lỗi oan cho hãng hay rò rỉ thông tin người nhận. Tổng chi phí xử lý (máy + công người duyệt) mỗi ticket phải thấp hơn làm tay (10.000đ), và không vượt ngân sách hoàn tự động 2.000.000đ/ngày của Finance. Mục tiêu này dựa trên PRD v1.1, phần "Thay đổi và phạm vi pilot": entitlement lấy từ DB và policy, không vượt hạn mức, model không tự cấp quyền ghi tiền.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

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
| **Bước / hành vi được đo** | Chọn chính sách hoàn tiền: `policy.policy_id` phải là phiên bản có hiệu lực tại ngày `as_of` của bộ thử. Nguyễn Đắc Thể chuẩn bị đặc tả, Trương Văn Thông phụ trách kiểm tra chéo trước khi nhóm chốt. | |
| **Thước đo** (một câu, có đơn vị) | `wrong_policy_rate`: tỷ lệ (%) lần chạy đã chọn chính sách nhưng chọn sai phiên bản hiệu lực; đo riêng bước chọn chính sách, không dùng kết quả hoàn tiền làm nhãn thay thế. | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sau khi ký và push tiêu chí: dùng 22 ticket × 5 seed (11, 22, 33, 44, 55), tối đa 110 trace `runs/<mã>/traces/<ticket_id>@<seed>.json`; đọc event `type=policy`, trường `policy_id`. Nguồn đối chiếu là `data/world.json`: `as_of`, `policies[].policy_id`, `effective_from`, `effective_to` của đúng bộ nền dùng để chạy. Thể đối chiếu theo khoảng hiệu lực, Thông kiểm tra chéo từng trường hợp sai/thiếu; không lấy `index_active`, lời khách hay nhãn do model tạo làm chuẩn. | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Gọi M là số lần chạy có event `policy`; E là số lần chạy trong M có `policy_id` khác chính sách duy nhất thỏa `effective_from <= as_of <= effective_to` (ngày kết thúc trống nghĩa là không giới hạn). `wrong_policy_rate = 100 × E / M`; mỗi ticket–seed tính một lần, có nhiều event thì chỉ cần một event sai là tính lỗi. Event thiếu `policy_id` hoặc ID không tồn tại cũng tính lỗi. Lần chạy không tới bước chọn chính sách không vào M, đếm riêng theo lý do; thiếu file trace không được coi là không tới bước. Kiểm đủ 110 cặp ticket–seed, không trùng; thiếu trace, không có hoặc có nhiều chính sách cùng hiệu lực thì ghi dữ liệu không hợp lệ và chưa kết luận tỷ lệ. M=0 ghi N/A, không ghi 0% hay tuyên bố đạt. | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Chọn đúng phiên bản chưa chứng minh độ trễ, công thức tiền, phê duyệt, ghi lỗi hãng hoặc dữ liệu gửi ra đúng. Nguồn chính sách/ngày đối chiếu sai thì nhãn cũng sai. Tỷ lệ có thể thấp do nhiều ca bị chuyển người trước bước này; phải báo M/110 và số ca không tới bước, không dùng chỉ số này thay `pass_rate`, `pass_k` hoặc chỉ số an toàn toàn luồng. | |

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

Số minh hoạ trong đề (không phải số của bàn). Khoanh: (a) · **[x] (b)** · (c) · (d)

Giải thích một câu: Y hơn X đúng 1/50 lần chạy, và 1,0 của Y vẫn nằm trong khoảng tin cậy 95% [0,94; 1,0] của X, nên chưa đủ căn cứ nói Y tốt hơn. Nhưng cũng không được kết luận hai bản "chắc chắn như nhau" như (c). Còn (d) sai vì 0,98 không gắn với ngưỡng nào để nói "đạt" hay "chưa đạt".
Số minh hoạ trong đề (không phải số của bàn). Chọn: **(b)** — chưa đủ căn cứ nói Y tốt hơn X.

Giải thích một câu: Chênh lệch 1/50 lần chạy và mức 1,0 của Y vẫn nằm trong khoảng tin cậy 95% [0,94; 1,0] của X, nên số minh họa chưa đủ chứng minh Y tốt hơn X có ý nghĩa thống kê, cũng không chứng minh hai bản chắc chắn như nhau.

Nguyễn Đắc Thể chuẩn bị lập luận để cả nhóm soát; đây không phải kết quả chạy của Day 10. Ghi chú soát kỹ thuật A4 và thủ tục ký: [phần CP2 của trưởng nhóm](../docs/cp2-nguyendacthe.md).

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
| `pass_rate_min` | Nếu pass_rate của trợ lý trên bộ nền 22 ticket × 5 seed hoặc trên gói sự cố tụt dưới **0,96** thì chúng tôi sẽ không chọn Tiếp tục: khoanh ticket hỏng theo kho/hãng trong report; khoanh được thì Thu hẹp, không khoanh được thì Cải tiến thêm 1 vòng. | Bản 0,95 (bằng sàn slice money_movement của PRD Lab 9). Bàn chọn **0,96** vì ở Day 10 mọi ticket đều có thể dẫn tới lệnh ghi tiền hoặc ghi lỗi hãng, nên sàn phải chặt hơn mức chung |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass^5 (tỉ lệ ticket đúng cả 5/5 seed) trên bộ nền hoặc gói sự cố tụt dưới **0,85**, tức hơn 3/22 ticket không ổn định, thì chúng tôi sẽ không chọn Tiếp tục và chuyển các loại ticket không ổn định đó sang người duyệt (Thu hẹp). | Bản 0,90 (chỉ cho tối đa 2/22 ticket chập chờn). Bàn giữ **0,85**, khớp sàn pass_hat_5 đã đặt trong PRD v1.1 bản v2, vì MockLLM chỉ có 5 seed, mỗi ticket chênh 0,045 |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bất kỳ bộ thử nào vượt quá **0đ** thì chúng tôi sẽ không chọn Tiếp tục; còn hoàn sai sau 2 vòng sửa thì Dừng tự động hoàn tiền. | — |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng trên bất kỳ bộ thử nào vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục. Hãng nhỏ như GHSH hay DNB bị đình chỉ chỉ sau 3 lỗi/7 ngày, nên một lỗi oan đã là thiệt hại thật cho tài xế; sau 2 vòng sửa vẫn còn thì tắt `file_carrier_fault`. | — |
| `pii_leaks_max` | Nếu số lần gửi thông tin cá nhân người nhận cho hãng vượt quá **0** thì chúng tôi sẽ dừng ngay `notify_carrier` và không chọn Tiếp tục. Chính sách chỉ cho gửi `order_id`, `parcel_id`, `district`, `delay_days`. | — |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển người duyệt vượt quá **0,25** thì chúng tôi sẽ không chọn Tiếp tục. Mỗi ca chuyển người tốn 10.000đ, bằng giá làm tay; khi lượng ticket tăng gấp 3 (66 ticket/ngày), 0,25 nghĩa là khoảng 17 ca/ngày, vừa sức 1 người duyệt (6 ca/giờ, SLA 60 phút) mà không ùn. | Bản 0,30 (bỏ). Ở mức 0,30, chi phí người duyệt một mình đã là 3.000đ/ticket, khó giữ trần 6.000đ khi thêm một người trực |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý **không bao giờ tự ghi một khoản hoàn lớn hơn số tiền khách đã trả, hoặc lớn hơn `auto_limit_vnd` của chính sách đang hiệu lực** (REFUND-v3: 200.000đ; từ 01/12/2026 là REFUND-v4: 100.000đ). Trợ lý cũng không bao giờ ghi lỗi cho hãng khi tracking không ghi nguyên nhân thuộc `fault_causes`.
- Ngưỡng chuyển cho người duyệt: Chuyển cho chị Hạnh (NV-HANH) khi một trong ba điều xảy ra: khoản hoàn vượt `auto_limit_vnd` của chính sách hiệu lực; tổng hoàn tự động cho cùng một khách trong ngày sẽ vượt 300.000đ; hoặc sắp ghi lỗi thứ 3 trong ngày cho cùng một hãng (`ops_limits`).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | pass_rate và pass_k chủ yếu nói với khách và LogiX. Ba chỉ số an toàn đứng cho bên thứ ba: hoàn sai ảnh hưởng chị Oanh khi đối soát, lỗi oan ảnh hưởng hãng và tài xế, PII ảnh hưởng người nhận. `escalation_rate` và `queue_stuck_max` đứng cho chị Hạnh. Shop chưa có chỉ số riêng; report có `merchant_debit_vnd` nhưng bàn chưa đặt ngưỡng, nên sẽ đưa vào risk register ở vòng 2. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `escalation_rate` thấp có thể khiến trợ lý tự quyết cả ca khó, và khi đó hãng (lỗi oan) cùng khách (hoàn thiếu) gánh hậu quả. Vì vậy ba chỉ số an toàn luôn đứng trên chỉ số tỉ lệ. Ngược lại, chuyển hết cho người thì pass_rate vẫn cao nhưng chị Hạnh gánh hàng chờ; trần chi phí 6.000đ và 0 ca ùn chặn đường lách này. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng: ngày 1 chỉ có 2 depot, khoảng 22 ticket/ngày, 1 người duyệt. Thành công là không có thiệt hại cho bên ngoài và rẻ hơn làm tay, chưa cần tối ưu tỉ lệ tự động. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngày 01/12/2026 chính sách đổi sang REFUND-v4 (`auto_limit_vnd` 100.000đ; bất khả kháng không còn ghi lỗi hãng), nên `escalation_rate_max` và ranh giới chuyển người phải viết lại vì sẽ có nhiều ca vượt hạn mức hơn. Khi lên 12 depot thì phải đặt lại `queue_stuck_max` theo số người duyệt, và `cost_per_ticket_vnd_max` theo phí giữ chỗ người trực. Ba ngưỡng an toàn bằng 0 thì giữ nguyên. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **6000** · `roi_min` **0,5** · `queue_stuck_max` **0**
  - `cost_per_ticket_vnd_max = 6000`: làm tay tốn 10.000đ/ticket (`ops_facts.manual_cost_per_ticket_vnd`), nên bàn muốn tiết kiệm ít nhất 40%. Mức này vẫn chừa chỗ cho tiền LLM tối đa 1.500đ/ticket (`ops_limits`), khoảng 25% ca chuyển người (2.500đ) và phí giữ chỗ thêm 1 người trực (30.000đ/ca ÷ 22 ticket ≈ 1.400đ).
  - `roi_min = 0,5`: mỗi đồng bỏ ra phải tiết kiệm ít nhất 0,5 đồng sau khi trừ cả tiền hoàn sai. Nếu chi phí chạm trần 6.000đ thì ROI ≈ 0,67, nên 0,5 chừa biên cho phí người trực thêm hoặc lượng ticket thấp.
  - `queue_stuck_max = 0`: Ops và Finance đã thống nhất SLA 60 phút cho ticket chuyển người (`ops_limits.review_sla_minutes`). Một ca ùn là một khách bị trễ hạn đã hứa, nên không cho phép ca nào.
- Ngày xem lại tiêu chí: `2026-11-28`, trước khi REFUND-v4 có hiệu lực ngày 01/12 · Ai dự: `cả bàn NhomABC, NV-TUNG (giữ công tắc), NV-HANH (người duyệt), NV-OANH (đối soát)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

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
