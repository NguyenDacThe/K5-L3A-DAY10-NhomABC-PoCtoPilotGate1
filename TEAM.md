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
- Đã chỉ rõ nguồn trace, trường cần lấy, bộ nền 22 ticket × 5 seed, nguồn nhãn độc lập theo ngày hiệu lực và phân công Thông lập nhãn, Thể đối chiếu. Việc đối chiếu của Thể đang chờ thực hiện.
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
