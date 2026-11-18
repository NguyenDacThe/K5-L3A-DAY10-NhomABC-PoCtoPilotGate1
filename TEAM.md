# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomABC
- Lớp: `L3A`
- Repo của bàn: https://github.com/NguyenDacThe/K5-L3A-DAY10-NhomABC-PoCtoPilotGate1.git
- Thẻ sự cố đã bốc (S1–S8): S7

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Đắc Thể | 2A202603529 | Kỹ sư cổng · điều phối | Có |
|   2 | Trương Văn Thông | 2A202603560 | Kỹ sư cổng · kiểm thử và theo dõi |     |
|   3 | Phan Gia Bảo | 2A202603562 | Sản phẩm và kinh doanh |     |
|   4 | Nguyễn Tuấn Bách | 2A202603596 | Vận hành và pháp lý |     |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Tài liệu chung từ Lab 9

- Chọn bộ tài liệu của Nguyễn Đắc Thể trong repo `K5-L3A-DAY09-NguyenDacThe-2A202603529-EvaluationandFailureAnalysis`.
- Tài liệu chính: [PRD v1.1](docs/lab9/PRD_v1.1.md).
- Tài liệu đi kèm theo yêu cầu Day 10: [eval card](docs/lab9/eval_card.md).
- Nguồn, phạm vi sử dụng và giới hạn: [ghi chú tham chiếu](docs/lab9/README.md).

## Phân công từ CP1

| Thành viên | CP2 · Phiếu A | CP3 · Phiếu B | CP4–CP5 · Sự cố và nộp bài |
|---|---|---|---|
| Nguyễn Đắc Thể | Cùng Thông thiết kế chỉ số offline A2; điều phối soát tiêu chí, ký và push sau khi cả nhóm thống nhất | Chạy baseline, đọc gate; code cổng trong `lab10/guards.py` (B1, B7.1); chốt vòng 1 sau khi nhóm soát | Sửa cổng theo nguyên nhân, chạy báo cáo ba mốc, điều phối demo và đẩy bài |
| Trương Văn Thông | Cầm bút A2 câu 1.3: chọn một bước, dữ liệu, công thức và điểm mù | Dò trace T-002@55 và B2; kiểm thử B7.2–B7.3 cùng Bách; kiểm tra hồi quy | Dò trace sự cố, thêm chỉ số trong `lab10/monitors.py`, ghi bằng chứng kiểm thử và C8 |
| Phan Gia Bảo | Cầm bút A1 câu 1.1, A4 và config tiêu chí; tổng hợp A3 cả nhóm, ghi A5 sau ký | Bản đồ dữ liệu/drift B3; cổng `business` và B7.4; tổng hợp quyết định v1 B8 | Phân tích chi phí/ROI/phạm vi, tổng hợp C12 và quyết định v2 theo bằng chứng |
| Nguyễn Tuấn Bách | A1 câu 1.2, A2 câu 1.4; soát tác động lên người duyệt và bên thứ ba | HAZOP B4, checklist B5; config `operations`/`legal`; runbook B7.5–B7.6 | Runbook C11, risk register, gom bài và `submission/submission.json`, kiểm đủ thành phần |

- Cả nhóm cùng làm pre-mortem B6, soát A3–A4 và thống nhất mọi ngưỡng, quyết định v1/v2; người cầm bút không tự quyết thay nhóm.
- CP2 chỉ viết tiêu chí; sau khi ký, commit và push thành công mới chạy đánh giá. CP1 chưa sửa cổng hay đặt ngưỡng.
- Từng thành viên tự ghi đóng góp, bằng chứng, phần dùng AI và exit ticket vào mục cá nhân trước khi nộp; bảng trên là việc được giao.

## Phân công CP4 · Thẻ S7

**Sự cố:** lộ thông tin người nhận quà qua thông báo gửi hãng vận chuyển. Phân công dưới đây là việc cần làm, không phải xác nhận từng thành viên đã hoàn thành hoặc cả nhóm đã họp chốt. Chỉ làm thẻ S7; CP5 và quyết định v2 sẽ thực hiện sau khi đủ bằng chứng CP4.

| Thành viên · nhánh | Công việc chính | Mục Phiếu C / file phụ trách | Sản phẩm bàn giao |
|---|---|---|---|
| **Nguyễn Đắc Thể** · `NguyenDacThe` | Điều phối và giữ bằng chứng trước sửa; tổng hợp cổng vòng 1 đã đỡ được gì. Viết specification, giả định môi trường và fault tree trước/sau. Chỉ sửa cổng nếu phân tích chỉ ra phần còn thiếu; tích hợp các nhánh, chạy kiểm tra cuối. | **C0–C1, C5–C7, C9**; `lab10/guards.py`; tích hợp config sau khi Bảo/Bách bàn giao | Mã report base/prepared/after thực tế; spec kênh gửi hãng và giả định; hai fault tree có nhánh code, dữ liệu, người/quy trình; bảng sửa nêu giảm hay ngăn và nguyên nhân. Report cuối không hồi quy; báo Coach vấn đề integrity kiểm thẻ chưa được giao. |
| **Trương Văn Thông** · `Thông` | Dò ít nhất hai ca lỗi theo cơ chế khác nhau ở mốc base, so với prepared/after. Kiểm các ca S7-01, S7-04, S7-20, S7-21 theo gợi ý thẻ; chọn ca thể hiện hai cơ chế khác nhau, dùng S7-05 làm đối chứng có số nhưng không phải SĐT. Thiết kế, thêm và kiểm chứng ít nhất một monitor mới. | **C2, C8**; `lab10/monitors.py`; phối hợp Thể ghi lần chạy vào C0 | Bảng lỗi đủ biểu hiện, bên chịu hại, mức độ, loại lỗi, nguồn và hướng xử lý; trace có vị trí sự kiện. Monitor nhận `trials` không có nhãn, trả về số và được đăng ký trong `MONITORS`; đủ thước đo–dữ liệu–cách tính, ngưỡng/điểm mù. Kiểm hồi quy và ghi đúng kết quả, không coi mọi dãy số là PII. |
| **Phan Gia Bảo** · `2A202603562_PhanGiaBao` | Đọc chi phí, ROI, độ phủ, hàng chờ, phân khúc theo kho/hãng của S7; phân biệt tác hại bên thứ ba với chỉ số tổng thể. Đề xuất thay đổi kinh doanh nếu bằng chứng yêu cầu, tổng hợp rủi ro còn lại. | Phần kinh doanh **C1, C7**; cầm bút **C10**; `config/operating_gates.json` mục `business` | Bảng so base/prepared/after kèm mã report; lý do từng thay đổi tiền/phạm vi, giữ độ phủ >0; ít nhất một dòng risk register có PIC, tín hiệu, hành động. Bàn giao số liệu cho C12 ở CP5, chưa tự chốt v2 trong CP4. |
| **Nguyễn Tuấn Bách** · `bach` | Phân tích lòng tin của người đặt và người nhận quà, dữ liệu rời hệ thống khi họ không biết. Làm HAZOP riêng cho S7, cập nhật trách nhiệm, khiếu nại, điều kiện dừng và phục hồi. Soát giả định môi trường và rủi ro cùng Thể/Bảo. | **C3.3, C4, C11**; phần vận hành/pháp lý **C5, C7, C10**; config mục `operations` và `legal` | C3.3 đủ hai mốc tin quá mức/không tin cho cả hai đối tượng; HAZOP ít nhất ba dòng, không ghi đè B4. Checklist đủ chín nhóm, mỗi dòng có PIC; runbook phần 4–5 có tín hiệu, ngưỡng, người quyết định, hành động và điều kiện bật lại, khớp config và monitor. Căn cứ pháp lý chưa xác minh ghi rõ cần Pháp chế kiểm. |

### Thứ tự làm và bàn giao CP4

1. **Đồng bộ bản chung:** sau khi trưởng nhóm đã đưa bản CP3 và thẻ S7 lên `main`, mỗi người cập nhật `main` vào nhánh của mình. Kiểm tra chữ ký và snapshot còn nguyên. Không chép thẻ của bàn khác.
2. **Giữ mốc trước sửa:** Thể lưu report grade S7 ban đầu vào C0–C1. Grade đã được chạy trước sửa vòng 2; cả nhóm dùng cùng mã bằng chứng, không coi báo cáo sau sửa là prepared ban đầu. Vấn đề integrity do manifest kiểm cả thẻ khác phải nhờ Coach hướng dẫn, không sửa grader/manifest để làm xanh.
3. **Phân tích trước:** Thông bàn giao C2, Bách bàn giao C3.3–C4; Thể tổng hợp C5–C6 với dữ kiện của Bảo. Cả nhóm đối chiếu specification và giả định, chọn đúng nguyên nhân rồi mới triển khai thay đổi vòng 2.
4. **Sửa và đo:** Thể phụ trách cổng, Thông phụ trách monitor; Bảo/Bách chỉ chỉnh khối JSON được giao. Ghi mỗi thay đổi và mã lần chạy vào C0/C7. Cổng vòng 1 đã bảo vệ được bộ S7 công khai thì không sửa chỉ để có thay đổi; vẫn phải có monitor mới theo yêu cầu thẻ và kiểm tra các giả định/điểm mù.
5. **Tích hợp:** từng người bàn giao commit hoặc PR trên nhánh riêng. Thể merge theo từng mục Phiếu C và khối config, giữ đủ nội dung; chạy lại S7, bộ nền và grade trên bản tích hợp. Không tự ghi kết quả từ code nhánh riêng thành kết quả của `main`.
6. **Khép CP4:** Thể hoàn thiện C9, Bảo C10, Bách C11; soát C0–C11 và bằng chứng. Mục tiêu tự kiểm: integrity, visible, regression, monitor đạt và độ phủ >0; nếu còn lỗi thì ghi đúng nguyên nhân, không tuyên bố CP4 đã đạt. Sau đó cả nhóm mới tổng hợp quyết định v2/C12 và bài nộp CP5.

### Quy ước tránh xung đột và giữ bằng chứng

- `templates/form-c-incident.md` là file chung: mỗi người chỉ chỉnh mục được giao; các mục phối hợp gửi nội dung cho người cầm bút chính, không thay cả file bằng bản từ nhánh mình.
- `config/operating_gates.json`: Bảo giữ `business`, Bách giữ `operations`/`legal`, Thể tích hợp và kiểm cả ba khối. Không tự đặt lại ngưỡng trong tiêu chí đã ký.
- Giữ nguyên `config/acceptance_criteria.json`, `.lock`, `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock` và nội dung gói `incidents/S7/` đã khớp hash gốc. Không xử lý riêng theo mã ticket, seed hay câu chữ.
- Report/trace trong `runs/` bị gitignore: người chạy cung cấp mã và bản bằng chứng để các bạn đọc được; không chỉ gửi tên thư mục trên máy cá nhân. Chỉ điền phần riêng **C3.3 của S7**, không làm phần thẻ khác.
- Mỗi người ghi phần dùng AI và đóng góp thật trong mục cá nhân; không tự viết xác nhận hoàn thành hoặc exit ticket thay thành viên khác.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TruongVanThong-2A202603560

### Phần việc phụ trách

Kỹ sư cổng · kiểm thử và theo dõi. Trong CP2, cầm bút Phiếu A mục A2, câu 1.3: thiết kế offline metric cho một bước của agent, phối hợp Thể rà soát. Trong CP3, phụ trách trace T-002@55/B2, hai bước tránh rò rỉ dữ liệu B7.2, hai ticket kiểm tính chất B7.3 và kiểm tra hồi quy. CP4 phụ trách C2, C8, monitor và bằng chứng S7, phối hợp bàn giao mã run vào C0. CP5 chưa thực hiện.

### Đóng góp cụ thể

- Đã điền cột Offline của A2 câu 1.3 trong `templates/form-a-criteria.md`, chọn bước chọn phiên bản chính sách và đặt tên thước đo `policy_version_error_rate` (đơn vị %).
- Đã chỉ rõ nguồn trace, trường cần lấy, bộ nền 22 ticket × 5 seed, nguồn nhãn độc lập theo ngày hiệu lực và phân công Thông lập nhãn, Thể đối chiếu. Việc đối chiếu của Thể đang chờ thực hiện.
- Đã viết công thức E/N, quy tắc mẫu số, cách xử lý trial không tới bước, dữ liệu không đánh giá được và trường hợp N = 0; yêu cầu báo số ca và độ phủ để tránh hiểu nhầm dữ liệu bị thiếu là kết quả tốt.
- Đã nêu điểm mù: đúng phiên bản chưa bảo đảm đúng tiền/quyền/dữ liệu gửi ngoài; ngày hiệu lực trong DB có thể sai và bộ nền một ngày chưa kiểm được ngày chuyển chính sách.
- Đã đối chiếu tĩnh dữ liệu mock: `as_of = 2026-11-16` thuộc hiệu lực `REFUND-v3`; mốc bắt đầu `REFUND-v4` là 2026-12-01. Đây là ví dụ xác định nhãn, chưa phải số đo agent.
- A2 câu 1.4 do Bách phụ trách; ngưỡng và quyết định chung do nhóm thống nhất. Chưa ký tiêu chí, chưa sửa code cổng/monitor và chưa chạy `lab10.eval`, `lab10.trace` hoặc `lab10.grade` trong lần làm CP2 này.

**CP3 · Kiểm thử và phân tích lỗi (18/11/2026):**

- Đã chạy `python -m lab10.trace --suite base --ticket T-002 --seed 55` và điền đủ ba phần B2: hai hậu quả (hoàn sai 20.000đ, ghi lỗi oan VNX), nguồn lỗi, bên chịu hại và hướng xử lý. Trace 03 ghi `model_override` từ DB 2 ngày sang lời khai 5 ngày; kết quả `HỎNG` ở status, refund_amount và carrier_fault.
- Đã hoàn thiện B7.2: phân biệt bộ phát triển/hồi quy công khai với kiểm tra độc lập, không xử lý riêng theo ticket hoặc seed, chỉ dùng đúng thẻ sự cố khi tới CP4, không tìm bộ ẩn hoặc sửa nhãn/ngưỡng để hợp thức hoá kết quả.
- Đã thiết kế và chạy hai ticket adhoc ở mốc `after`, seed 11, trên O-1002/C-02 và O-1004/C-04; ghi nội dung, lệnh tái lập, kết quả kỳ vọng và kết quả thực tế ở B7.3. Cả hai **không giữ được tính chất**: hoàn sai lần lượt 30.000đ và 33.000đ, kèm lỗi hãng sai. Bách chưa xác nhận phần rà soát chung.
- Đã chạy bộ kiểm tra công khai: **13 tests, OK**, gồm kiểm tra không làm hỏng ca vốn đúng. Lỗi nền T-002@55 và hai ticket hiểm vẫn còn vì cổng hiện tại chưa được sửa; không ghi là đã sửa xong hoặc đạt Gate 1.
- Đã bàn giao đề xuất cho Thể: kiểm quyền lợi từ tracking/chính sách trước `issue_refund` và kiểm điều kiện ghi lỗi độc lập trước `file_carrier_fault`. Chờ cổng B7.1 để chạy lại hai ticket và xác nhận hồi quy trên bản sửa; chưa tự làm phần code cổng, ký/chốt vòng 1 hay quyết định v1 của nhóm.
- Tiêu chí vẫn chưa ký: chỉ chạy trace chẩn đoán và unittest, không chạy eval/grade hoặc tạo báo cáo đạt ngưỡng. Chưa thêm monitor CP4; các tên metric ở B2 chỉ là đề xuất.

**CP4 · Thẻ S7 · Phần của Thông (18/11/2026):**

- Trên bản chung đã có chữ ký và snapshot hợp lệ, đã lưu grade trước thêm monitor; dò 15 trace: S7-01/04/20/21 và đối chứng S7-05, mỗi ticket ở base/prepared/after, seed 11. Đã điền đủ ba phần C2 cho hai nguồn lộ khác nhau: chép PII từ ticket và tự thêm liên hệ người nhận từ DB; ghi rõ địa chỉ không cần SĐT và mã vận đơn không phải PII.
- Thêm, đăng ký `carrier_unexpected_field_rate` và `carrier_contact_field_rate` trong `lab10/monitors.py`, chỉ dùng outbound không có nhãn. Điền C8 đủ dữ liệu, công thức/mẫu số, lỗi telemetry, ngưỡng đề xuất và điểm mù; không đọc mã ticket/seed hay coi mọi dãy số là điện thoại.
- Đã kiểm thử: 9 test monitor và 13 test công khai đạt. Grade đạt criteria/visible/regression/monitor, nền after 110/110 và S7 after 40/40, độ phủ 100%; PII S7 từ base 30 xuống prepared/after 0. Không có hidden để xác nhận.
- Cổng G3 vòng 1 đã bảo vệ S7 công khai, nên giữ nguyên guards/config/tiêu chí/snapshot/gói S7. Thay đổi của Thông chỉ thêm phát hiện; không nhận monitor là biện pháp ngăn hoặc nhận công sửa cổng của Thể.
- Grade tổng vẫn **FAIL integrity** cả trước và sau: 19 file cũ lệch hash do CRLF/LF, 28 đường dẫn thuộc thẻ khác không có. Đã chẩn đoán chỉ đọc, không sửa manifest/grader hoặc lấy thẻ khác. Bàn giao chi tiết để Thể/Coach xử lý; chưa xác nhận CP4 toàn nhóm đạt hay quyết định v2.

### Phần dùng AI · CP4

Dùng Codex đọc phân công/thẻ S7, chạy trace/eval/grade và kiểm thử, hỗ trợ viết monitor, C2/C8, lưu bằng chứng và bàn giao. Các kết quả là output thực chạy trên nhánh cá nhân; chưa ghi nhận Bách đã chốt ngưỡng runbook hoặc Thể đã merge. Ngưỡng giám sát pilot mới là đề xuất, không sửa tiêu chí đã ký.

### Bằng chứng

- Sản phẩm CP2: [Phiếu A · A2, cột Offline câu 1.3](templates/form-a-criteria.md#a2), đủ bước đo, thước đo, dữ liệu, công thức và điểm mù.
- Căn cứ dữ liệu: `data/world.json`, mục `as_of` và `policies`; cấu trúc sự kiện `policy` trong `lab10/agent.py`; quy ước file trace trong `lab10/eval.py`. Chỉ đọc các file này.
- Kiểm tra môi trường theo CP1: `python -m unittest discover -s tests -v`, Python 3.11.9, ngày 18/11/2026 (GMT+7): **13 tests, OK**. Đây là kiểm tra công khai, không phải báo cáo đánh giá hay bằng chứng đạt Gate 1.
- Chưa tạo commit hoặc mã lần chạy đánh giá cho phần CP2 này. A5 và việc ký, commit, push tiêu chí do trưởng nhóm thực hiện sau khi cả nhóm thống nhất.
- Sản phẩm CP3: [Phiếu B · B2](templates/form-b-evaluation-gates.md#b2) và [B7.2–B7.3](templates/form-b-evaluation-gates.md#b7), có lệnh trace tái lập và kết quả thực chạy. CLI trace chỉ in kết quả, không tạo thư mục `runs/<mã>`; không có mã eval để ghi vào B0.
- Kiểm tra CP3: `python -m unittest discover -s tests -v` ngày 18/11/2026, Python 3.11.9: **13 tests, OK**. `test_team_guards_do_not_break_base` đạt trên bản hiện tại; cần chạy lại sau khi cổng thay đổi. Chưa tạo commit cho lần cập nhật CP3 này.
- CP4: [bàn giao và lệnh tái lập](docs/cp4-thong.md), [C2](templates/form-c-incident.md#c2), [C8](templates/form-c-incident.md#c8), [bản sao report/trace](docs/cp4-thong-evidence/verification-summary.json). Grade trước `R-S7-grade-20261118-165630-0892bd`; grade sau `R-S7-grade-20261118-165851-43edee`; eval nền sau `R-base-after-20261118-165851-43edee`. Chưa tạo commit/push cho phần CP4 trong lần làm này.

### Exit ticket

- Điều học được ở CP2: thước đo cho một bước cần có nhãn độc lập và mẫu số rõ ràng; loại ca thiếu dữ liệu mà không báo độ phủ có thể khiến tỉ lệ trông tốt hơn thực tế.
- Điều còn chưa chắc: ngày hiệu lực trong dữ liệu mock có phản ánh đúng quy trình cập nhật chính sách ngoài thực tế hay không; cần nhóm xác minh nguồn và người chịu trách nhiệm trước pilot.
- Đây là ghi chú học tập CP2; exit ticket cuối buổi sẽ được cập nhật khi hoàn thành CP5.
- Điều học được ở CP3: test hồi quy xanh chỉ chứng minh chưa phá ca vốn đúng; hai ticket mới vẫn có thể làm lộ tính chất an toàn bị vi phạm. Cần đọc cả tracking, sổ cái và lỗi hãng thay vì chỉ đọc lời trả lời khách.
- Điều chưa chắc ở CP3: sau khi Thể thêm cổng, tính chất có giữ được trên hai ticket mới và các ca vốn đúng hay không; cần chạy lại trên đúng bản cổng đã sửa trước khi chốt.
- Điều học được ở CP4: dữ liệu có thể tự đi từ DB ra ngoài dù ticket không có PII; tín hiệu vi phạm schema và bằng chứng lộ PII là hai điều khác nhau. Monitor sau gửi phát hiện được sự cố nhưng không thu hồi thông tin.
- Điều chưa chắc ở CP4: PII có thể lọt qua giá trị của trường được phép hoặc kênh ngoài outbound; cần kiểm dữ liệu thật và chất lượng telemetry. Grade còn lỗi integrity môi trường, cần Thể/Coach xử lý trước khi khép CP4.

## NguyenDacThe-2A202603529

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng: hỗ trợ A2 câu 1.3 cùng Trương Văn Thông; chuẩn bị lập luận A3 và soát kỹ thuật A4; điều phối ký sau khi nhóm thống nhất.

### Đóng góp cụ thể

Đã chuẩn bị đặc tả (sau hợp nhất dùng tên `policy_version_error_rate`) cho riêng bước chọn chính sách, quy định nguồn đối chiếu, mẫu số, ca thiếu dữ liệu và điểm mù trong Phiếu A. Đã viết lập luận A3 và bản bàn giao kiểm tra trước ký tại `docs/cp2-nguyendacthe.md`. Dùng Codex hỗ trợ đọc code tĩnh và soạn nội dung, chưa tính số đánh giá Day 10.

**CP4 · Phần việc nhánh Thể (S7):** đã tổng hợp C0–C1 từ grade trước sửa, viết C5–C7/C9 và lưu bằng chứng. Bổ sung log tối thiểu vào G3 để Thông có dữ liệu monitor, không sửa cơ chế chặn vốn đã bảo vệ prepared. S7 after R-S7-after-20261118-165018-2bd310 đạt40/40; bộ nền R-base-after-20261118-165018-2bd310 đạt110/110, không hồi quy. Kiểm bổ sung ghi rõ phản ví dụ khi dữ liệu nhạy cảm nằm ngay trong district được whitelist, không nhận là đã ngăn mọi PII. Chưa sửa monitors/config thay các bạn, chưa chốt C12 hoặc gửi báo cáo cho Coach; đã soạn nội dung bàn giao. Dùng Codex hỗ trợ phân tích code/trace, viết telemetry, kiểm thử và ghi phiếu. [Hồ sơ phần Thể](docs/cp4-nguyendacthe/README.md).

### Bằng chứng

[Phiếu A, mục A2–A3](templates/form-a-criteria.md#a2) và [bản soát CP2 của trưởng nhóm](docs/cp2-nguyendacthe.md). Đã ký, commit xác nhận `60fbf2c` được push trước đánh giá. Trong CP3: baseline `R-base-before-20261118-152920-bde05c`, after `R-base-after-20261118-153059-1c7843`; đã viết G1–G3 trong `lab10/guards.py`, điền B0–B1/B7.1 và đề xuất phối hợp B6. [Report và bàn giao](docs/cp3-nguyendacthe.md). Dùng Codex hỗ trợ code/kiểm thử, không xử lý riêng theo mã ticket. Chưa chốt prepared hay quyết định v1; chưa commit/push phần code CP3.

### Exit ticket

Chưa điền; cá nhân tự ghi sau khi hoàn thành phần việc và thảo luận với nhóm.

## PhanGiaBao-2A202603562

### Phần việc phụ trách

Vai: **Sản phẩm và kinh doanh**.

- CP2 · Phiếu A: câu 1.1 (A1), tổng hợp câu 1.5 (A3), câu 1.6 (A4), file `config/acceptance_criteria.json` (bản nháp trước ký), A5 sau khi ký.
- CP3 · Phiếu B: câu 2.3 (B3, bản đồ dữ liệu và drift), câu 2.9 (B7.4 và mục `business` trong `config/operating_gates.json`), lăng kính kinh doanh trong pre-mortem B6, tổng hợp quyết định v1 (B8).
- CP4–CP5 · Phiếu C: phân tích chi phí, ROI, phạm vi pilot; tổng hợp quyết định v2 (C12).

### Đóng góp cụ thể

- **Bản tiêu chí** (`config/acceptance_criteria.json`): đề xuất toàn bộ ngưỡng số mà bản đã ký giữ nguyên: `pass_rate_min` 0,96 · `pass_k_min` 0,85 · ba chỉ số an toàn bằng 0 · `escalation_rate_max` 0,25 · `cost_per_ticket_vnd_max` 6.000đ · `roi_min` 0,5 · `queue_stuck_max` 0. Viết bản đầu `stop_condition` và bốn dòng `decision_rule`; bản ký là bản đã được Thể rà soát lại (phân biệt v1/v2, tối đa 2 vòng sửa), xem `docs/cp2-review.md`.
- **Phiếu A:** câu 1.1; câu 1.5 chọn (b) kèm giải thích; câu 1.6 gồm câu "Nếu … thì chúng tôi sẽ …" cho 6 chỉ số, hai câu ranh giới đầu ra, bảng soát bốn câu hỏi, lý do nhóm `business_ops`, ngày xem lại 28/11/2026 (trước khi REFUND-v4 có hiệu lực ngày 01/12).
- **Phiếu A mục A5:** cập nhật giờ ký, commit `60fbf2c` "Sign acceptance criteria", trạng thái push. Phát hiện file tiêu chí được ký trên bản xuống dòng CRLF (hash `36863666…`) trong khi repo lưu LF (hash `afdd890f…`), nên máy lấy về bản LF thấy "ĐÃ BỊ SỬA sau khi ký". Đã báo trưởng nhóm, không tự sửa JSON hay file khoá.
- **Phiếu B mục B3:** bản đồ dữ liệu 9 dòng (nguồn sự thật hay bản sao cho từng trường then chốt) và ví dụ drift REFUND-v3 → v4 ngày 01/12/2026 (concept drift; ảnh hưởng `wrongful_carrier_faults_max`, `escalation_rate_max`; v4 đang `index_active = false`).
- **Phiếu B mục B7.4 và `config/operating_gates.json` mục `business`:** `daily_refund_cap_vnd` 1.600.000 · `cost_budget_per_ticket_vnd` 1.500 · `pilot_scope` all · `roi_min` 0,5, mỗi số một câu lý do từ `ops_limits`, `ops_facts`.
- **Phiếu B mục B6 (lăng kính Kinh doanh):** ba lý do thất bại: chi phí mỗi ticket vượt làm tay; tổng hoàn tự động vượt ngân sách Finance; ticket giá trị lớn luôn phải chuyển người. Hai lý do đầu gắn với cổng config đã đặt (`cost_budget_per_ticket_vnd`, `roi_min`, `daily_refund_cap_vnd`) và đề xuất một cổng code trần 300.000đ/khách/ngày; lý do thứ ba vào risk register.
- **CP4 · Thẻ S7 · Phiếu C:** phần kinh doanh của **C1** (bảng so base/prepared trên gói S7: 30 lần lộ PII → 0 trong khi ROI 1,27 → 1,0 và chi phí 4.405đ → 5.005đ, đều đạt trần; theo kho và hãng cho thấy lộ PII rải ở 3 kho, 3 hãng nên Thu hẹp theo kho không xử lý được S7), phần kinh doanh của **C7** (giữ nguyên mục `business`, kèm lý do; ước tính dưới khoảng 7 ticket/ngày thì vượt trần chi phí 6.000đ; danh sách số phải kiểm lại ở mốc after), cầm bút **C10** (3 dòng risk register: chỉ số tổng che tác hại bên thứ ba · lượng ticket thấp làm vượt trần chi phí · ticket không tra được đơn đắt hơn làm tay).
- Chưa làm: cột after của C7 phần kinh doanh (chờ Thể sửa vòng 2), C12 và quyết định v2 (CP5). Các lăng kính còn lại của B6 do cả bàn điền.

### Bằng chứng

- Commit `1817d93` "CP2: draft acceptance criteria and Phieu A (1.1, 1.5, 1.6)", merge vào `main` qua PR #3 (`d203dfd`).
- Commit CP3 (B3, B6 dòng Kinh doanh, B7.4, mục `business`, A5): `964aae9`, merge vào `main` qua `050d10e`.
- Mã lần chạy dùng cho B8 (theo Phiếu B mục B8): base `R-base-before-20261118-152920-bde05c` · prepared `R-base-prepared-20261118-160738-0892bd`. Mã lần chạy cho C12: `________` (điền ở CP5).
- Dòng trong phiếu: Phiếu A mục A1 câu 1.1, A3, A4, A5; Phiếu B mục B3, B6 (dòng Kinh doanh), B7.4; Phiếu C mục C1 (phần kinh doanh), C7 (phần kinh doanh), C10.
- Số liệu CP4 lấy từ grade S7 trước sửa vòng 2 trên `main` @ `f1d4e31`, hash code đội `0892bd295a9e`, cổng vòng 1 `0580db3e`.

### Dùng AI

Dùng Claude để đọc các file markdown của đề, đọc `data/world.json` và PRD Lab 9, rồi viết nháp Phiếu A (1.1, 1.5, 1.6, A5), Phiếu B (B3, B7.4) và đề xuất ngưỡng, con số cổng `business`. Claude cũng giúp phát hiện lỗi lệch xuống dòng CRLF/LF của file tiêu chí. Mọi ngưỡng và con số do cả bàn soát và chịu trách nhiệm giải thích lúc demo.

### Exit ticket

- Một điều học được: phải viết ngưỡng và hành động "nếu trượt thì làm gì" trước khi xem kết quả; ngưỡng an toàn (hoàn sai, lỗi oan cho hãng, lộ PII) phải đứng trên các chỉ số tỉ lệ.
- Một điều còn chưa chắc: trần chi phí 6.000đ và `escalation_rate_max` 0,25 có quá chặt khi lượng ticket tăng hoặc khi REFUND-v4 hạ hạn mức tự hoàn xuống 100.000đ hay không.

## NguyenTuanBach-2A202603596

### Phần việc phụ trách

Vận hành và pháp lý. CP2: Phiếu A câu 1.2 (A1) và câu 1.4 (A2), soát tác động lên người duyệt và bên thứ ba. CP3: HAZOP B4, checklist B5, config `operations`/`legal`, runbook B7.5–B7.6. CP4 (thẻ S7): C3.3, C4, phần vận hành/pháp lý của C5 và C10, C11 (checklist và runbook 4–5). Việc cuối CP4 (risk register tổng, `submission.json`, kiểm đủ thành phần) và CP5 chưa làm.

### Đóng góp cụ thể

- **CP2:** viết mục tiêu nhìn từ hai người (chị Oanh kế toán đối soát, chị Hạnh trưởng ca CSKH) ở A1 câu 1.2. Điền cột telemetry A2 câu 1.4 cho bước ghi lỗi hãng: thước đo lỗi thiếu bằng chứng và tỷ lệ bị khiếu nại/đảo, cách ghép ID, ngưỡng vàng/đỏ, điểm mù.
- **CP3:** HAZOP B4 cho `file_carrier_fault` (4 dòng kỹ thuật, 4 dòng ngoài kỹ thuật); checklist B5 đủ 9 nhóm việc, ghi trung thực nhóm 5, 7, 8 là "Chưa"; config `operations` (PIC, người duyệt, công suất, SLA, điều kiện dừng, kênh cảnh báo) và `legal` (trường PII bị chặn, bắt buộc có nguyên nhân khi ghi lỗi hãng); runbook 1–3 và kiểm giờ cao điểm B7.6 (14 ca cùng lúc: 1 người chờ tối đa 130 phút, 2 người chờ 65 phút, vẫn còn ca quá SLA).
- **CP4 · S7** (nhánh `bach`, commit `8dd380e`), trong `templates/form-c-incident.md`:
  - **C3.3:** bốn mốc lòng tin cho người đặt và người nhận quà. Dữ liệu rời hệ thống mà họ không biết: `customer_note` (chữ tự do, S7-01, S7-04) và `recipient_contact` lấy từ DB dù khách không gõ (S7-20, S7-21).
  - **C4:** bốn dòng HAZOP cho `notify_carrier`, gồm một nhánh chưa thấy trên trace (PII đi ra qua kênh ngoài hệ thống, người duyệt chép ticket gửi hãng).
  - **C5 (phần vận hành/pháp lý):** giả định môi trường và specification; ghi căn cứ pháp lý là chưa xác minh, cần Pháp chế kiểm.
  - **C10:** một dòng risk register về PII rò qua kênh ngoài allowlist, PIC NV-TUNG.
  - **C11:** cập nhật checklist nhóm 3, 7, 8; Runbook 4 (7 câu) và Runbook 5 (ba kịch bản: tải gấp 3 lần, LLM lỗi quá 15 phút, người duyệt không tin một quyết định). Hệ số 3 lần và ngưỡng 15 phút là đề xuất, chưa đo thực.
- Config `operations`/`legal` không đổi ở CP4: `legal` đã chặn đủ `recipient_contact`, `customer_note`, `name`, `phone`, `street`. Trace chẩn đoán `--stage prepared`/`after` trên S7-01 và S7-20 seed 11: payload chỉ còn `order_id`, `parcel_id`, `district`, `delay_days`.
- Chưa làm: C7 phần vận hành/pháp lý (cần mã lần chạy sau sửa), risk register tổng, `submission/submission.json`, CP5.

### Bằng chứng

- CP2: [Phiếu A, A1 câu 1.2 và A2 câu 1.4](templates/form-a-criteria.md#a2), commit `2f11502`.
- CP3: [Phiếu B, B4, B5, B7.5–B7.6](templates/form-b-evaluation-gates.md#b4), `config/operating_gates.json` mục `operations`/`legal`; commit `9c7cf5d`, `a810352`, `fb345b8`; đã merge qua `f050f71`.
- CP4: [Phiếu C, C3.3, C4, C5, C10, C11](templates/form-c-incident.md#c3), commit `8dd380e` trên nhánh `bach`.
- Mã lần chạy dùng trong C11 (lấy từ bằng chứng của Thể và Thông, Bách không tự tạo mã mới): grade ban đầu `R-S7-grade-20261118-163825-0892bd`; S7 after `R-S7-after-20261118-165018-2bd310`; S7 after sau thêm monitor `R-S7-after-20261118-165851-43edee`. Grade trên bản tích hợp thử trên máy: `R-S7-grade-20261118-171221-d5f014`, đạt criteria, visible, regression, monitor; FAIL integrity vì thiếu 28 file thẻ khác, chờ Coach.

### Dùng AI

Dùng Claude Code để đọc `TEAM.md`, các phiếu A/B/C, thẻ S7 và gói `incidents/S7/`, chạy `lab10.trace` chẩn đoán trên S7-01, S7-04, S7-05, S7-20, S7-21 (base, prepared, after), và soạn nháp C3.3, C4, C5, C10, C11 cùng việc rà các nhánh để thử tích hợp. Chưa chạy `lab10.eval`; grade tích hợp chỉ chạy trên máy cá nhân. Nội dung, các con số đề xuất (15 phút, 3 lần, mẫu thông báo cố định) và căn cứ pháp lý do Bách xem lại và chịu trách nhiệm; căn cứ pháp lý chưa được Pháp chế xác nhận.

### Exit ticket

*(Bản nháp từ việc đã làm; Bách đọc lại và sửa theo ý mình trước khi nộp.)*

- Điều học được ở CP4: một chỉ số tổng (ROI 1,27, chi phí 4.405đ) có thể đạt hết trong khi người nhận quà bị lộ tên và số điện thoại; chỉ số pháp lý `pii_leaks` phải được đọc riêng và đứng trên chỉ số kinh doanh. Bảo vệ tên trường (allowlist) ngăn được dữ liệu cấu trúc, nhưng không thấy đường dữ liệu đi ra ngoài hệ thống như người duyệt tự chép sang hãng.
- Điều còn chưa chắc: cổng chặn tốt trên bộ mock công khai không chứng minh bắt hết PII thật; chưa biết quy trình tiếp nhận phản ánh của người nhận quà và nghĩa vụ báo cáo pháp lý trên thực tế, cần Pháp chế xác nhận trước khi pilot.

## Tích hợp CP3

Đã merge nội dung các nhánh Thể, Thông, Bảo và Bách vào main local; đối chiếu phần từng người trong Phiếu B B0–B8. Bản chốt 0580db3e, prepared R-base-prepared-20261118-160738-0892bd. Các số nền đạt, stress queue còn vượt SLA nên v1 Cải tiến thêm. Không tự điền exit ticket hoặc ghi nhận cuộc họp chưa diễn ra. Xem [kiểm tra CP3 sau merge](docs/cp3-integration-review.md).

## Tích hợp CP4 và C12

Đã merge bốn nhánh CP4 vào main local, ghi đủ Phiếu C C0–C12 theo phần bàn giao và report `R-S7-grade-20261118-171745-d5f014`. S7 40/40, nền110/110; criteria/visible/regression/monitor đạt; grade tổng FAIL vì thiếu28file thẻ khác theo manifest. V2 giữ Cải tiến thêm, không xác nhận pilot thật. Xem [bản kiểm tra tích hợp](docs/cp4-integration/README.md). Chưa nhận hướng dẫn Coach xử lý integrity, chưa gửi tin nhắn hoặc nộp LMS.
