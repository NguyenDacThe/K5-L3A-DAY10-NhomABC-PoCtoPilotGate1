# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-NhomABC-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

**Trạng thái:** đã ký theo yêu cầu trưởng nhóm Nguyễn Đắc Thể; thời gian trong lock `2026-11-18T15:15:34`, SHA-256 bắt đầu `36863666`. Commit xác nhận đúng tên `Sign acceptance criteria`: `60fbf2c`, đã push trước baseline CP3. Giữ nguyên JSON tiêu chí từ thời điểm ký.

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

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mỗi khoản trợ lý hoàn cho khách và mỗi lỗi ghi cho hãng phải truy ngược được tới một ticket, một đơn và một nguyên nhân trong tracking, để cuối tuần tổng hoàn trong sổ cái khớp với số tiền khách nhận và số lỗi/tiền phạt đối soát với hãng, không còn dòng "mồ côi" nào chị phải tự đi tìm hoặc xin hãng huỷ.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Hàng chờ chuyển sang chị vừa sức (nằm trong 6 ca/giờ mỗi người duyệt, mỗi ca nhận xử lý trong 60 phút) và mỗi ca đến kèm đủ thông tin (đơn, độ trễ, chính sách áp dụng, lý do chuyển) để chị duyệt trong khoảng 10 phút mà không phải mở lại ticket; đồng thời các quyết định tự động có ghi chú giải thích, để chị và nhân viên có thể kiểm mẫu thay vì kiểm lại bằng tay từng ca.

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
| **Bước / hành vi được đo** | Chọn phiên bản chính sách tại event `policy`, trước khi tính quyền lợi. Thông thiết kế, Thể rà soát tĩnh. | Ghi lỗi cho hãng vận chuyển: phát hiện dấu hiệu hãng/tài xế bị phạt hoặc đình chỉ oan, không dùng nhãn chuẩn offline. |
| **Thước đo** (một câu, có đơn vị) | `policy_version_error_rate`: tỷ lệ (%) trial chọn sai phiên bản chính sách hiệu lực tại `as_of` của bộ thử. | Số bản ghi lỗi hãng thiếu bằng chứng tracking, đơn vị lỗi/hãng/ngày; tỷ lệ bản ghi lỗi bị khiếu nại hoặc đảo/huỷ trong 7 ngày, đơn vị %. Theo dõi thêm số lỗi thứ 3 trở đi trong ngày chưa có người duyệt. Đây là tín hiệu nghi ngờ tác hại, chưa phải nhãn lỗi oan đã xác minh. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sau khi ký và push: 22 ticket × 5 seed (11, 22, 33, 44, 55), tối đa 110 trace `runs/<mã>/traces/<ticket_id>@<seed>.json`; đọc `events[type=policy].policy_id`. Nhãn độc lập từ `data/world.json`: `as_of`, `policies[].policy_id/effective_from/effective_to`. Thông lập bảng nhãn, Thể kiểm tra khoảng ngày; không lấy `index_active` hay model làm chuẩn. | Toàn bộ bản ghi lỗi hãng trong pilot, tracking đúng đơn/parcel, nguyên nhân trễ, chính sách, phê duyệt gắn với hành động, khiếu nại và dòng đảo/huỷ từ Oanh. Ghép bằng ID bản ghi lỗi, phân tổ từng hãng; GHSH chịu 150.000đ/lỗi và DNB chịu 80.000đ/lỗi, cùng ngưỡng đình chỉ 3 lỗi/7 ngày. Oanh xác minh ca nghi ngờ, Hạnh soát phê duyệt; không tạo nhãn bằng model. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Nhãn là chính sách duy nhất có `effective_from <= as_of <= effective_to`, kết thúc null là vô hạn. N là số trial có đúng một event `policy`, ID đầy đủ và nhãn duy nhất; E là số trial trong N có ID khác nhãn (ID không tồn tại cũng là sai). Tỷ lệ = 100 × E/N. Ca kết thúc hợp lệ trước bước này đếm riêng; thiếu/hỏng trace, thiếu ID, nhiều event hoặc nhãn không duy nhất là không đánh giá được, phải điều tra, chưa kết luận đạt. Báo N, E, số không tới bước, số không đánh giá được; kiểm đủ 110 cặp ticket–seed, không trùng. N=0 ghi N/A. | Ca nghi ngờ = số ID lỗi không tìm được parcel tương ứng, không có bằng chứng trễ đủ mức chính sách, hoặc nguyên nhân không được ghi nhận/không thuộc `fault_causes`. Thiếu tracking tính ca nghi ngờ và đếm riêng. D là tập ID lỗi đã ghi trong 7 ngày gần nhất; tỷ lệ = 100 × số ID thuộc D có khiếu nại hoặc bị đảo/huỷ / số ID trong D; một lỗi có cả hai chỉ tính một lần. D rỗng ghi N/A và báo 0 bản ghi. Theo dõi riêng khiếu nại tới muộn về lỗi ngoài D. Đếm riêng lỗi thứ 3 trở đi trong ngày của hãng không có phê duyệt hợp lệ. |
| **Khung thời gian / ngưỡng báo động** | Không áp dụng cho offline. | Kiểm khi có bản ghi lỗi mới; đối soát lại cuối ca 480 phút và cuối ngày. Đỏ khi có ít nhất 1 ca nghi ngờ hoặc lỗi thứ 3 trở đi chưa được duyệt: báo NV-TUNG và NV-HANH, tạm dừng ghi lỗi hãng để xác minh. Vàng nếu tỷ lệ khiếu nại/đảo > 5% trong 7 ngày hoặc hãng đạt 2 lỗi/ngày: gọi người duyệt trước lỗi tiếp theo; kiểm cả số lỗi 7 ngày so với ngưỡng đình chỉ từng hãng. Mức 5% là cảnh báo vận hành đề xuất, không thay trần 0 lỗi oan trong tiêu chí. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Đúng phiên bản chưa chứng minh đúng tiền, quyền hoặc dữ liệu gửi ngoài. DB hiệu lực có thể sai so với văn bản gốc; ca chưa tới bước không được đo. Báo thêm N/110; bộ nền một ngày chưa chứng minh đúng ngày chuyển phiên bản. | Tracking sai có thể che lỗi; hãng nhỏ có thể không khiếu nại hoặc phản hồi sau 7 ngày. Không chứng minh khiếu nại nào cũng đúng. Chưa đo hoàn thiếu, ghi nợ shop sai hoặc lộ PII; cần đối chiếu sổ cái, phản hồi và chỉ số riêng sau này. |

**Ghi chú rà soát của Thể:** ngày mock `2026-11-16` thuộc `REFUND-v3`; từ `2026-12-01` là `REFUND-v4`. Đây là đối chiếu tĩnh, chưa phải kết quả agent. Hợp nhất hai tên chỉ số thành tên Thông dùng: `policy_version_error_rate`. Telemetry giữ ý tưởng bảo vệ hãng của Bách, bổ sung quy tắc ghép ID, dữ liệu thiếu và báo động khi có sự kiện.

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

Số minh hoạ trong đề (không phải số của bàn). Chọn **(b)**.

Giải thích một câu: Y hơn X đúng 1/50 lần chạy và 1,0 vẫn nằm trong khoảng tin cậy 95% [0,94; 1,0] của X, nên theo số minh hoạ chưa đủ căn cứ nói Y tốt hơn X có ý nghĩa thống kê, cũng không chứng minh hai bản chắc chắn như nhau.

Bảo tổng hợp, Thể rà soát lập luận. Không dùng phép nhìn khoảng tin cậy này thay một kiểm định so sánh đầy đủ trên dữ liệu thực.

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
| `pass_rate_min` | Nếu pass_rate trên bộ nền 22 ticket × 5 seed hoặc gói sự cố được giao tụt dưới **0,96** thì không Tiếp tục: xác định phần hỏng theo kho/hãng/loại ticket; chỉ Thu hẹp khi đo lại phạm vi giữ chứng minh đạt đủ, nếu chưa chứng minh được thì Cải tiến thêm trong tối đa 2 vòng tổng cộng trước 2026-11-28 hoặc Dừng. | Phương án 0,95 tham khảo từ Lab 9; phương án đang điền là **0,96**, yêu cầu ít nhất 106/110 trial đúng trên bộ nền, tương ứng tối đa 4 lần hỏng. Hai bên cần cân nhắc độ tin cậy và chi phí; đây là lựa chọn của nhóm, không phải ngưỡng tự suy ra từ Lab 9. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass^5 trên bộ nền hoặc gói sự cố được giao tụt dưới **0,85** thì không Tiếp tục; chỉ Thu hẹp khi phần giữ đo lại đạt đủ, nếu không thì Cải tiến thêm trong hạn. Trên bộ nền cần ít nhất 19/22 ticket đúng cả 5 seed; gói khác dùng số ticket thực tế. | Phương án **0,85** cho tối đa 3/22 ticket không ổn định; 0,90 cho tối đa 2/22. Nhóm cần giải thích vì sao chấp nhận mức này trước ký, không lấy số seed hoặc sàn Lab 9 làm lý do duy nhất. |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bất kỳ bộ thử nào vượt quá **0đ** thì chúng tôi sẽ không chọn Tiếp tục; còn hoàn sai sau 2 vòng sửa thì Dừng tự động hoàn tiền. | — |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng trên bất kỳ bộ thử nào vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục. Hãng nhỏ như GHSH hay DNB bị đình chỉ chỉ sau 3 lỗi/7 ngày, nên một lỗi oan đã là thiệt hại thật cho tài xế; sau 2 vòng sửa vẫn còn thì tắt `file_carrier_fault`. | — |
| `pii_leaks_max` | Nếu số lần gửi thông tin cá nhân người nhận cho hãng trên bộ nền hoặc gói thử được giao vượt quá **0** thì chúng tôi sẽ dừng ngay `notify_carrier` và không chọn Tiếp tục. Chính sách chỉ cho gửi `order_id`, `parcel_id`, `district`, `delay_days`. | — |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển người duyệt vượt quá **0,25** thì chúng tôi sẽ không chọn Tiếp tục. Mỗi ca chuyển người tốn 10.000đ, bằng giá làm tay; khi lượng ticket tăng gấp 3 (66 ticket/ngày), 0,25 nghĩa là khoảng 17 ca/ngày so với công suất danh nghĩa 48 ca/ca trực 8 giờ. Đây chỉ là công suất tổng: dồn ticket giờ cao điểm hoặc kiểm lại quyết định vẫn có thể gây ùn; phải kiểm hàng chờ thực tế trong report. | Bản 0,30 (bỏ). Ở mức 0,30, chi phí người duyệt một mình đã là 3.000đ/ticket, khó giữ trần 6.000đ khi thêm một người trực |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không ghi khoản hoàn vượt quyền lợi theo chính sách và dữ kiện DB, không tự động vượt `auto_limit_vnd` khi chưa có phê duyệt hợp lệ gắn đúng ticket/đơn, còn hiệu lực và đủ hạn mức (REFUND-v3: 200.000đ; từ 01/12/2026 là REFUND-v4: 100.000đ). Trợ lý cũng không bao giờ ghi lỗi cho hãng khi tracking không ghi nguyên nhân thuộc `fault_causes`.
- Ngưỡng chuyển cho người duyệt: Chuyển cho chị Hạnh (NV-HANH) khi một trong ba điều xảy ra: khoản hoàn vượt `auto_limit_vnd` của chính sách hiệu lực; tổng hoàn tự động cho cùng một khách trong ngày sẽ vượt 300.000đ; hoặc sắp ghi lỗi thứ 3 trong ngày cho cùng một hãng (`ops_limits`).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số có ý nghĩa với mọi bên liên quan? | `pass_rate` và `pass_k` đo toàn luồng gồm tiền, người trả, hãng và PII, nhưng vẫn giữ riêng các trần an toàn để tỷ lệ tổng không che tác hại. Oanh cần sổ cái khớp; hãng cần không bị ghi oan; người nhận cần bảo vệ PII; Hạnh cần hàng chờ vừa sức. Shop còn rủi ro ghi nợ sai: đọc `merchant_debit_vnd` và check `payer`, không coi đúng số tiền là đủ. |
| Chạy theo chỉ số có thể làm ai thiệt? | Ép chuyển người ít có thể khiến agent tự quyết ca khó; chuyển hết làm Hạnh quá tải và tăng chi phí. GHSH/DNB có thể bị đình chỉ sau 3 lỗi/7 ngày; DNB chịu 80.000đ/lỗi. Giữ trần an toàn 0, kiểm chi phí, ROI và hàng chờ đồng thời. `escalation_rate_max` giữ khóa trong `nice_to_have`, nhưng nhóm chủ động yêu cầu đạt trong dòng Tiếp tục; exit code gate riêng lẻ chưa đủ xác nhận mọi điều kiện. |
| Thành công ngày 1? | Pilot dự kiến 2 depot; bộ nền 22 ticket giả lập mỗi seed không phải dự báo sản lượng thật. Một người duyệt có công suất danh nghĩa 6 ca/giờ; cần kiểm giờ cao điểm, kiểm lại và SLA nhận xử lý 60 phút. Phạm vi và nhân sự phải được cụ thể hóa ở CP3, chưa khẳng định đã bố trí đầy đủ. |
| Ngày 1.000, ngưỡng nào cần xem lại? | Khi mở 12 depot hoặc đổi cơ cấu ticket/chính sách, xem lại tỷ lệ chuyển người, chi phí, ROI và năng lực trực theo dữ liệu mới, không tự nới SLA/trần an toàn. REFUND-v4 từ 01/12/2026 hạ auto limit xuống 100.000đ và đổi nguyên nhân chịu lỗi. Giữ nguyên tiêu chí đã ký trong bài lab; tiêu chí giai đoạn sau lập ở hồ sơ riêng. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **6000** · `roi_min` **0,5** · `queue_stuck_max` **0**
  - `cost_per_ticket_vnd_max = 6000`: làm tay tốn 10.000đ/ticket (`ops_facts.manual_cost_per_ticket_vnd`), nên bàn muốn tiết kiệm ít nhất 40%. Mức này vẫn chừa chỗ cho tiền LLM tối đa 1.500đ/ticket (`ops_limits`), khoảng 25% ca chuyển người (2.500đ) và phí giữ chỗ 1 người trực (30.000đ/ca ÷ 22 ticket ≈ 1.400đ).
  - `roi_min = 0,5`: mỗi đồng bỏ ra phải tiết kiệm ít nhất 0,5 đồng sau khi trừ cả tiền hoàn sai. Nếu chi phí chạm trần 6.000đ thì ROI ≈ 0,67, nên 0,5 chừa biên cho phí người trực thêm hoặc lượng ticket thấp.
  - `queue_stuck_max = 0`: Ops và Finance đã thống nhất SLA 60 phút cho ticket chuyển người (`ops_limits.review_sla_minutes`). Một ca ùn là một khách bị trễ hạn đã hứa, nên không cho phép ca nào.
- Cách tính và hành động kinh doanh/vận hành: chi phí/ngày gồm máy + công duyệt/kiểm lại + phí giữ chỗ; chi phí/ticket chia số ticket trong scope. ROI = (chi phí làm tay tương đương − tổng chi phí − hoàn sai/ngày) / tổng chi phí, theo `lab10/ops.py`. Nếu chi phí > 6.000đ, ROI < 0,5 hoặc có ca ùn thì không Tiếp tục; chỉ Thu hẹp khi đo lại phần giữ có độ phủ > 0 đạt đủ, nếu chưa chứng minh được thì Cải tiến thêm trong tối đa 2 vòng tổng cộng trước 2026-11-28 hoặc Dừng theo config. `queue_stuck` là số ca ùn tệ nhất giữa các seed, không phải trung bình (chờ quá SLA 60 phút hoặc hết ca chưa tới lượt).
- Tỷ lệ trong JSON dùng thang 0–1; A2 dùng %. Tiền hoàn sai/lỗi oan/PII cộng các trial trong từng report, không lấy trung bình để che vi phạm; chi phí/ROI dùng cách quy ngày trong report. V1 kiểm bộ nền; v2 kiểm thêm đúng gói sự cố đã bốc.
- Ngày xem lại tiêu chí: `2026-11-28`, trước khi REFUND-v4 có hiệu lực ngày 01/12 · Ai dự: `cả bàn NhomABC, NV-TUNG (giữ công tắc), NV-HANH (người duyệt), NV-OANH (đối soát)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

Chỉ chạy trên `main` khi cả nhóm xác nhận bản cuối và trưởng nhóm yêu cầu ký, commit/push; chạy từng dòng PowerShell, dừng khi có lỗi:

```powershell
python -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock
git commit -m "Sign acceptance criteria"
git push -u origin main
python -m lab10.criteria verify
```


| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-18T15:15:34`; Nguyễn Đắc Thể (2A202603529). Verify: `ok: true`, hash `36863666b80ee368aa62fec1a3a1f73290a88066d5e86d2b97177648493b04ee`. |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `60fbf2c` — commit xác nhận đúng tên; JSON/lock được lưu từ `dddb073` và giữ nguyên. |
| Đã push lên `origin main` thành công? | Có. `git push origin main` thành công từ `f5ef383` tới `60fbf2c` trước lần baseline `R-base-before-20261118-152920-bde05c`. |

Kiểm tra trước CP3 đã đạt: `criteria.status()['ok'] == True` và `criteria.check_sign_git_history()[0] == True`. Commit xác nhận `60fbf2c` không sửa file tiêu chí, không ký lại và không đổi lock.

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
