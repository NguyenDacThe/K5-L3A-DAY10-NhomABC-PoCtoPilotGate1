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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## NguyenDacThe-2A202603529

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng: hỗ trợ A2 câu 1.3 cùng Trương Văn Thông; chuẩn bị lập luận A3 và soát kỹ thuật A4; điều phối ký sau khi nhóm thống nhất.

### Đóng góp cụ thể

Đã chuẩn bị đặc tả `wrong_policy_rate` cho riêng bước chọn chính sách, quy định nguồn đối chiếu, mẫu số, ca thiếu dữ liệu và điểm mù trong Phiếu A. Đã viết lập luận A3 và bản bàn giao kiểm tra trước ký tại `docs/cp2-nguyendacthe.md`. Dùng Codex hỗ trợ đọc code tĩnh và soạn nội dung, chưa tính số đánh giá Day 10.

### Bằng chứng

[Phiếu A, mục A2–A3](templates/form-a-criteria.md#a2) và [bản soát CP2 của trưởng nhóm](docs/cp2-nguyendacthe.md). Chưa có mã lần chạy, commit CP2 hoặc chữ ký tiêu chí; chưa ghi nhận nhóm đã duyệt các ngưỡng.

### Exit ticket

Chưa điền; cá nhân tự ghi sau khi hoàn thành phần việc và thảo luận với nhóm.
