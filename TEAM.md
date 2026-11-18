# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomABC
- Lớp: `L3A`
- Repo của bàn: https://github.com/NguyenDacThe/K5-L3A-DAY10-NhomABC-PoCtoPilotGate1.git
- Thẻ sự cố đã bốc (S1–S8):

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

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TruongVanThong-2A202603560

### Phần việc phụ trách

Kỹ sư cổng · kiểm thử và theo dõi. Trong CP2, cầm bút Phiếu A mục A2, câu 1.3: thiết kế offline metric cho một bước của agent, phối hợp Thể rà soát. Phạm vi cập nhật lần này chỉ là CP2; các nhiệm vụ CP3–CP5 trong bảng phân công chưa được ghi nhận là đã làm.

### Đóng góp cụ thể

- Đã điền cột Offline của A2 câu 1.3 trong `templates/form-a-criteria.md`, chọn bước chọn phiên bản chính sách và đặt tên thước đo `policy_version_error_rate` (đơn vị %).
- Đã chỉ rõ nguồn trace, trường cần lấy, bộ nền 22 ticket × 5 seed, nguồn nhãn độc lập theo ngày hiệu lực và phân công Thông lập nhãn, Thể đối chiếu. Thể đã rà soát tĩnh cấu trúc event và ngày hiệu lực; đối chiếu kết quả trace thực tế chờ sau ký.
- Đã viết công thức E/N, quy tắc mẫu số, cách xử lý trial không tới bước, dữ liệu không đánh giá được và trường hợp N = 0; yêu cầu báo số ca và độ phủ để tránh hiểu nhầm dữ liệu bị thiếu là kết quả tốt.
- Đã nêu điểm mù: đúng phiên bản chưa bảo đảm đúng tiền/quyền/dữ liệu gửi ngoài; ngày hiệu lực trong DB có thể sai và bộ nền một ngày chưa kiểm được ngày chuyển chính sách.
- Đã đối chiếu tĩnh dữ liệu mock: `as_of = 2026-11-16` thuộc hiệu lực `REFUND-v3`; mốc bắt đầu `REFUND-v4` là 2026-12-01. Đây là ví dụ xác định nhãn, chưa phải số đo agent.
- A2 câu 1.4 do Bách phụ trách; ngưỡng và quyết định chung do nhóm thống nhất. Chưa ký tiêu chí, chưa sửa code cổng/monitor và chưa chạy `lab10.eval`, `lab10.trace` hoặc `lab10.grade` trong lần làm CP2 này.

### Phần dùng AI

Dùng Codex đọc README, CHECKPOINTS, TEAM, đề bài, tài liệu Lab 9 và cấu trúc code/dữ liệu Day 10; hỗ trợ soạn thước đo câu 1.3, soát công thức, điểm mù và cập nhật mục cá nhân. Nội dung cần được Thông rà soát và trao đổi với Thể trước khi nhóm chốt tiêu chí; không coi nội dung AI soạn là phê duyệt của cả nhóm.

### Bằng chứng

- Sản phẩm CP2: [Phiếu A · A2, cột Offline câu 1.3](templates/form-a-criteria.md#a2), đủ bước đo, thước đo, dữ liệu, công thức và điểm mù.
- Căn cứ dữ liệu: `data/world.json`, mục `as_of` và `policies`; cấu trúc sự kiện `policy` trong `lab10/agent.py`; quy ước file trace trong `lab10/eval.py`. Chỉ đọc các file này.
- Kiểm tra môi trường theo CP1: `python -m unittest discover -s tests -v`, Python 3.11.9, ngày 18/11/2026 (GMT+7): **13 tests, OK**. Đây là kiểm tra công khai, không phải báo cáo đánh giá hay bằng chứng đạt Gate 1.
- Chưa tạo commit hoặc mã lần chạy đánh giá cho phần CP2 này. A5 và việc ký, commit, push tiêu chí do trưởng nhóm thực hiện sau khi cả nhóm thống nhất.

### Exit ticket

- Điều học được ở CP2: thước đo cho một bước cần có nhãn độc lập và mẫu số rõ ràng; loại ca thiếu dữ liệu mà không báo độ phủ có thể khiến tỉ lệ trông tốt hơn thực tế.
- Điều còn chưa chắc: ngày hiệu lực trong dữ liệu mock có phản ánh đúng quy trình cập nhật chính sách ngoài thực tế hay không; cần nhóm xác minh nguồn và người chịu trách nhiệm trước pilot.
- Đây là ghi chú học tập CP2; exit ticket cuối buổi sẽ được cập nhật khi hoàn thành CP5.

## NguyenDacThe-2A202603529

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng: hỗ trợ A2 câu 1.3 cùng Trương Văn Thông; chuẩn bị lập luận A3 và soát kỹ thuật A4; điều phối ký sau khi nhóm thống nhất.

### Đóng góp cụ thể

Đã chuẩn bị đặc tả (sau hợp nhất dùng tên `policy_version_error_rate`) cho riêng bước chọn chính sách, quy định nguồn đối chiếu, mẫu số, ca thiếu dữ liệu và điểm mù trong Phiếu A. Đã viết lập luận A3 và bản bàn giao kiểm tra trước ký tại `docs/cp2-nguyendacthe.md`. Dùng Codex hỗ trợ đọc code tĩnh và soạn nội dung, chưa tính số đánh giá Day 10.

### Bằng chứng

[Phiếu A, mục A2–A3](templates/form-a-criteria.md#a2) và [bản soát CP2 của trưởng nhóm](docs/cp2-nguyendacthe.md). Chưa có mã lần chạy, commit CP2 hoặc chữ ký tiêu chí; chưa ghi nhận nhóm đã duyệt các ngưỡng.

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
- Chưa làm: B8 (chờ mã lần chạy base và prepared), Phiếu C (chờ thẻ sự cố). Các lăng kính còn lại của B6 do cả bàn điền.

### Bằng chứng

- Commit `1817d93` "CP2: draft acceptance criteria and Phieu A (1.1, 1.5, 1.6)", merge vào `main` qua PR #3 (`d203dfd`).
- Commit CP3 (B3, B7.4, mục `business`, A5): `________` (điền sau khi commit).
- Mã lần chạy dùng cho B8 và C12: `________` (điền sau khi có).
- Dòng trong phiếu: Phiếu A mục A1 câu 1.1, A3, A4, A5; Phiếu B mục B3, B6 (dòng Kinh doanh), B7.4.

### Dùng AI

Dùng Claude để đọc các file markdown của đề, đọc `data/world.json` và PRD Lab 9, rồi viết nháp Phiếu A (1.1, 1.5, 1.6, A5), Phiếu B (B3, B7.4) và đề xuất ngưỡng, con số cổng `business`. Claude cũng giúp phát hiện lỗi lệch xuống dòng CRLF/LF của file tiêu chí. Mọi ngưỡng và con số do cả bàn soát và chịu trách nhiệm giải thích lúc demo.

### Exit ticket

- Một điều học được: phải viết ngưỡng và hành động "nếu trượt thì làm gì" trước khi xem kết quả; ngưỡng an toàn (hoàn sai, lỗi oan cho hãng, lộ PII) phải đứng trên các chỉ số tỉ lệ.
- Một điều còn chưa chắc: trần chi phí 6.000đ và `escalation_rate_max` 0,25 có quá chặt khi lượng ticket tăng hoặc khi REFUND-v4 hạ hạn mức tự hoàn xuống 100.000đ hay không.

## Rà soát CP2 trước ký

Phần việc bốn thành viên đã hợp nhất trong Phiếu A. Xem [bản rà soát CP2](docs/cp2-review.md) để biết bổ sung theo từng người. Chưa ghi nhận chữ ký hoặc đồng thuận cuối của cả nhóm; không tự điền exit ticket cho thành viên khác.
