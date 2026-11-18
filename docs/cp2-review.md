# Rà soát CP2 trước ký · NhomABC

Ngày rà soát: 2026-11-18 (GMT+7). Cơ sở: working tree `main` sau các PR #1–#4, HEAD `6330a43`. Rà soát dựa trên phần đã merge trong repo, không chứng nhận từng người đã đọc/đồng ý bản cuối.

## Theo từng thành viên

| Thành viên | Phần việc đã có | Vấn đề phát hiện | Đã bổ sung/sửa trong lần rà soát |
|---|---|---|---|
| Nguyễn Đắc Thể | Hỗ trợ A2, lập luận A3, bản soát kỹ thuật A4 | Nội dung của Thể trùng với Thông ở A2, với Bảo ở A3; ghi chú bàn giao còn nói các phần khác trống | Hợp nhất A2 theo tên `policy_version_error_rate`, chỉ giữ một đáp án A3; cập nhật trạng thái bàn giao, đồng bộ quy tắc v1/v2 và người ký dự kiến là trưởng nhóm |
| Trương Văn Thông | Offline metric câu 1.3 đủ bước, dữ liệu, nhãn, công thức, mẫu số, ca thiếu và điểm mù | Hai tên chỉ số, hai quy tắc xử lý event cùng tồn tại sau merge | Giữ đặc tả N/E của Thông; dữ liệu không đánh giá được phải điều tra, chưa được kết luận đạt; ghi đủ độ phủ và cặp ticket–seed. Thể kiểm tĩnh event trong agent/eval và ngày hiệu lực |
| Phan Gia Bảo | A1 câu 1.1, A3, A4, ngưỡng và quy tắc JSON | A4 có dòng trùng/trống; số ticket và công suất tổng bị diễn giải như dự báo; điều kiện Tiếp tục đòi gói sự cố cả ở v1; quy tắc 1/2 vòng sửa không thống nhất; điều kiện dừng thiếu hoàn sai | Gộp bốn câu soát, làm rõ ngưỡng 106/110 và 19/22, bổ sung cách tính chi phí/ROI/queue; phân biệt v1/v2, tối đa 2 vòng tổng cộng, thêm hoàn sai vào stop condition. Giữ nguyên toàn bộ ngưỡng số |
| Nguyễn Tuấn Bách | Mục tiêu Oanh/Hạnh, telemetry bảo vệ hãng, ý kiến A4 | Bảng telemetry rời khỏi bảng chính; cộng khiếu nại với lỗi đảo gây đếm đôi; mẫu số 0 chưa rõ; gọi tín hiệu nghi ngờ là lỗi oan; quét cuối ca nhưng yêu cầu báo ngay | Gộp telemetry vào cột riêng, dùng hợp ID và mẫu số theo cohort 7 ngày, N/A khi không có lỗi; theo dõi phản hồi tới muộn, thiếu tracking là nghi ngờ; kiểm theo sự kiện và đối soát cuối ca, sửa dữ kiện GHSH/DNB |

## Ngưỡng giữ nguyên từ bản nhóm đã điền

| Khóa | Giá trị |
|---|---:|
| `required.pass_rate_min` | 0.96 |
| `required.pass_k_min` | 0.85 |
| `required.wrongful_refund_vnd_max` | 0 |
| `required.wrongful_carrier_faults_max` | 0 |
| `required.pii_leaks_max` | 0 |
| `nice_to_have.escalation_rate_max` | 0.25 |
| `business_ops.cost_per_ticket_vnd_max` | 6000 |
| `business_ops.roi_min` | 0.5 |
| `business_ops.queue_stuck_max` | 0 |

Việc giữ số không xác nhận nhóm đã duyệt. Cần giải thích mức 0.96/0.85 theo khả năng chịu lỗi, phạm vi và chi phí, không chỉ vì từng dùng ở Lab 9. 0.25 được nhóm yêu cầu ở dòng Tiếp tục dù vẫn nằm trong `nice_to_have`; cách xếp khóa không tự quyết định chính sách của nhóm.

## Điểm cần biết trước ký

- A1–A4 đã có nội dung và hai ranh giới đầu ra. A5 cố ý ghi chưa ký; không bịa giờ, hash, commit hoặc trạng thái push.
- `signed_by` dự kiến là Nguyễn Đắc Thể, MSSV 2A202603529, theo vai trưởng nhóm trong TEAM. Chưa tạo chữ ký.
- Quy tắc kinh doanh dùng chi phí máy + duyệt/kiểm lại + giữ chỗ; ROI đã trừ tiền hoàn sai. Một người duyệt có 48 ca/ca trực về công suất tổng, không bảo đảm SLA nếu dồn giờ cao điểm.
- Tạm dừng ghi khi có tín hiệu đỏ là ứng phó; chuyển hết về người hoặc coverage bằng 0 không làm pilot đạt.
- Mọi kết luận Thu hẹp phải có report đo lại đầy đủ và phần giữ coverage > 0; không xoá dòng lỗi khỏi dữ liệu. Một ngưỡng không đạt là không Tiếp tục.
- `lab10.gate` không tự cưỡng chế toàn bộ câu chữ `decision_rule`; trưởng nhóm phải đọc đủ các ngưỡng kinh doanh, escalation, violations và hồi quy.
- Không tự viết lời tự đánh giá/exit ticket hoặc xác nhận đồng thuận thay Bảo/Bách. Mục cá nhân cuối buổi thuộc CP5; việc chưa có mục cá nhân không đồng nghĩa thiếu câu trả lời CP2.

## Trình tự còn lại

1. Cả nhóm đọc bản Phiếu A và JSON sau rà soát, xác nhận ngưỡng, hành động, người ký dự kiến và ngày xem lại 2026-11-28.
2. Khi trưởng nhóm yêu cầu ký: ký một lần trên bản `main` cuối cùng; commit đúng `Sign acceptance criteria` và push thành công trước đánh giá đầu tiên. Hướng dẫn PowerShell ở A5.
3. Điền A5 bằng thời gian và mã commit thực tế; giữ nguyên JSON sau ký.

Chưa chạy trợ lý, chưa tạo kết quả baseline hoặc mở thẻ sự cố trong lần rà soát này. Các đề xuất đã ghi là bản để nhóm xác nhận trước ký.
