# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

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

> …

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
| **Bước / hành vi được đo** | | Hành động ghi: ghi lỗi cho hãng vận chuyển và gửi tiền hoàn cho khách (hai nơi thiệt hại ra ngoài LogiX: hãng bị phạt/đình chỉ oan, khách/shop bị hoàn sai) |
| **Thước đo** (một câu, có đơn vị) | | Số lỗi ghi cho hãng KHÔNG có nguyên nhân giao trễ trong tracking (lỗi oan, đơn vị: lỗi/hãng/ngày) và tỉ lệ lỗi hãng bị hãng khiếu nại hoặc kế toán đảo lại (%/7 ngày). Thước đo phụ: số lỗi thứ 3 trở đi của cùng một hãng trong ngày mà chưa có người duyệt (phải bằng 0) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | Không có nhãn đúng/sai. Dùng tín hiệu thay nhãn: (1) bảng ghi lỗi hãng của trợ lý, (2) sự kiện tracking của đúng đơn đó (có sự kiện trễ hay không), (3) kênh khiếu nại của hãng, (4) dòng đảo/huỷ khi chị Oanh đối soát hằng tuần. Toàn bộ lỗi hãng trong pilot, không lấy mẫu; hai nhà vận chuyển nhỏ (ví dụ nhóm tài xế tự do, 80.000đ/lỗi, đình chỉ sau 3 lỗi/7 ngày) được tách riêng |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | Lỗi oan = số bản ghi lỗi hãng mà tracking không có sự kiện trễ chứng minh, theo từng hãng, từng ngày, đối chiếu tự động cuối ngày. Tỉ lệ khiếu nại = (lỗi bị hãng khiếu nại + lỗi bị đảo) / tổng lỗi đã ghi trong cửa sổ 7 ngày. Lỗi chưa có tracking (thiếu dữ liệu) KHÔNG loại khỏi tử số: tính là lỗi oan nghi ngờ và đếm riêng để chị Oanh soát tay |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Quét cuối mỗi ca (480 phút) và cuối ngày. Báo động đỏ ngay khi lỗi oan ≥ 1 trong ngày hoặc có hãng chạm lỗi thứ 3 mà chưa qua người duyệt (báo cho giám sát vận hành giữ công tắc tắt). Báo động vàng khi tỉ lệ khiếu nại/đảo > 5% trong 7 ngày, hoặc một hãng sắp tới ngưỡng đình chỉ (2 lỗi/ngày). Ngưỡng là đề xuất của Vận hành và pháp lý, cả bàn chốt |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | Không thấy lỗi oan mà chính tracking cũng sai (hãng cập nhật trễ), không thấy hãng chịu thiệt mà không khiếu nại (hãng nhỏ, tài xế tự do), và độ trễ 7 ngày của kênh đối soát nên thiệt hại đã xảy ra trước khi thấy. Cũng không đo khách bị hoàn thiếu mà im lặng, hay dữ liệu cá nhân gửi cho bên thứ ba (cần chỉ số riêng) |

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
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | (Bách soát, nhóm chốt) `pass_rate` và `pass_k` chỉ phản ánh đúng/sai trên bộ nền, không nói gì về hãng vận chuyển hay người duyệt. Hãng chỉ được bảo vệ bởi `wrongful_carrier_faults_max`; người duyệt (chị Hạnh) chỉ được bảo vệ nếu có ngưỡng `escalation_rate_max` và `queue_stuck_max`; chị Oanh cần các khoản hoàn và lỗi hãng khớp sổ. Đề nghị giữ `escalation_rate_max` ở mức "nên có" thành có, vì thiếu nó thì người duyệt không có tiếng nói trong tiêu chí |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | (Bách soát, nhóm chốt) Ép tỉ lệ tự động cao thì chị Hạnh gánh dồn ngược: ca chuyển ít đi nhưng ca khó dồn vào cuối ngày, vượt 6 ca/giờ mỗi người duyệt và quá hạn 60 phút. Ép `pass_rate` cao bằng cách ghi lỗi cho hãng dễ dãi thì hãng nhỏ (80.000đ/lỗi, bị đình chỉ sau 3 lỗi trong 7 ngày) và tài xế tự do thiệt, họ không có mặt trong cuộc họp và không có nhãn để kêu. Ép chi phí thấp thì khách bị từ chối oan phải gọi lại, tốn công tay hơn 10.000đ/ca |
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
