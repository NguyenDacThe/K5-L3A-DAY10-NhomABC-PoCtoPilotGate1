# CP2 · Phần việc Nguyễn Đắc Thể · 2A202603529

## Sản phẩm trên nhánh NguyenDacThe

- Đặc tả chỉ số offline cho bước chọn chính sách trong Phiếu A, mục A2 câu 1.3; đây là phần hỗ trợ Trương Văn Thông theo TEAM.
- Lập luận câu 1.5 trong A3 để nhóm review.
- Bản soát kỹ thuật A4 và trình tự ký ở dưới. Chưa có kết luận nhóm đã thống nhất ngưỡng; A4, config và A5 còn chờ các phần việc khác.

## Cơ sở kỹ thuật cho A2

`lab10/agent.py` phát event `policy` chứa `policy_id` và `pinned` tại bước chọn chính sách. `lab10/eval.py` ghi trace từng cặp ticket–seed vào `runs/<mã>/traces/`. Đây là vị trí lấy dữ liệu sau khi ký, không cần sửa code phát sẵn.

`lab10/helpers.py` định nghĩa `effective_policy` theo khoảng ngày hiệu lực, gồm cả hai đầu; `effective_to` trống là không giới hạn. Dùng quy tắc này để đối chiếu, đồng thời yêu cầu chỉ có một phiên bản hiệu lực để tránh oracle mơ hồ. Ngày đối chiếu lấy từ `world.as_of` của bộ thử, không lấy ngày hiện tại trên máy. A2 chỉ thiết kế phép đo, chưa chạy trợ lý hoặc tính kết quả.

PRD Lab 9 nêu rủi ro FM-06 dùng chính sách hết hiệu lực; eval card lưu ý kết quả tiền không tự chỉ ra nguyên nhân. Vì vậy chỉ số A2 quan sát trực tiếp phiên bản được chọn. Đây là chỉ số chẩn đoán bổ sung, không thêm khóa vào JSON tiêu chí và không tự đặt ngưỡng mới thay phần của Bảo.

## A4 · Soát kỹ thuật để trao đổi với nhóm

| Nội dung cần soát | Ý kiến kỹ thuật của Thể | Trạng thái hiện tại |
|---|---|---|
| Ý nghĩa với các bên | `pass_rate` cần đi cùng trần hoàn sai, lỗi hãng oan và lộ PII; tỷ lệ tổng thể cao vẫn có thể che tác hại cho shop, hãng hoặc khách. Chi phí/ROI và hàng chờ phải xét cùng khả năng vận hành. | Chờ Bảo/Bách điền tiêu chí cụ thể để đối chiếu. |
| Ai có thể thiệt khi tối ưu | Ép ít chuyển người có thể dẫn tới tự ghi sai; chuyển mọi ca cho người có thể làm ùn hàng chờ và tăng chi phí. Tỷ lệ chọn đúng chính sách chỉ có nghĩa khi báo cả số ca tới bước. | Cần ghi rõ hành động khi trượt, không chỉ ghi con số. |
| Thành công ngày 1 | Chỉ xét phạm vi pilot và năng lực trực mà nhóm thực sự bố trí; không lấy số Lab 9 làm kết quả Day 10. Các ranh giới tiền/quyền và dữ liệu phải được soát ngay cả khi tỷ lệ đúng cao. | Chưa có ngưỡng hoặc phạm vi được nhóm chốt. |
| Ngày 1.000 | Khi tăng depot, đổi chính sách hoặc lượng ticket, phải đánh giá lại độ phủ dữ liệu, chi phí và năng lực người duyệt. Ghi ngày xem lại trên phiếu; tiêu chí đã ký của buổi lab vẫn giữ nguyên. | Chờ nhóm chốt ngày và người dự, không sửa JSON sau ký. |

Phân biệt để review: `pass_rate` = số lần chạy pass / tổng lần chạy; `pass_k` trong Day 10 là pass^5 = số ticket pass đủ 5/5 seed / tổng ticket; pass@5 chỉ yêu cầu ít nhất một trong năm lần pass và không thay được pass^5.

## Điều kiện bàn giao trước ký

Hiện A1, cột telemetry A2, A4 và JSON tiêu chí còn nguyên mẫu; A5 chưa có giờ ký, commit hoặc bằng chứng push. Vì vậy chưa đánh dấu CP2 toàn nhóm hoàn tất.

Trưởng nhóm kiểm lần cuối sau khi nhận phần việc của các bạn:

- Bảo hoàn tất A1 câu 1.1, A4 và config; Bách hoàn tất câu 1.2 và telemetry; Thông kiểm tra chéo đặc tả offline. Nhóm soát A3 và mỗi ngưỡng cùng lý do.
- A4 đủ năm tiêu chí bắt buộc, chỉ số nên có, nhóm `business_ops`, phiên bản thứ hai cho chỉ số tranh luận nhiều nhất, bốn câu soát, hai ranh giới đầu ra và ngày xem lại.
- Mỗi câu có chỉ số/đơn vị, bộ thử, ngưỡng và hành động khi trượt; thống nhất tỷ lệ dùng thang 0–1 trong JSON, tiền dùng VND, các số đếm dùng đơn vị rõ ràng.
- `team` đúng `K5-L3A-DAY10-NhomABC-PoCtoPilotGate1`, `signed_by` có người ký, không còn ngưỡng `null`; đủ `stop_condition` và cả bốn dòng `decision_rule`. Chỉ cho phép Tiếp tục khi đạt đầy đủ tiêu chí bắt buộc và kinh doanh/vận hành đã ký.
- So chi phí với `ops_facts.manual_cost_per_ticket_vnd`, phân biệt chi phí toàn ticket với ngân sách LLM trong `ops_limits`. Không tự sao ngưỡng Lab 9 hay file example.
- Review và merge các phần CP2 về `main` trước khi ký. Khi ký, bảo đảm working tree của tiêu chí là bản cuối đã được nhóm thống nhất; không mang bản tiêu chí cũ từ nhánh khác đè lên bản đã ký.

## Thủ tục ký khi nhóm đã sẵn sàng

Các lệnh dưới đây là hướng dẫn, chưa được thực hiện trong phần việc này. Chỉ ký một lần trên `main`, sau khi nhóm thống nhất và cho phép commit/push. Trong PowerShell, chạy từng dòng, chỉ tiếp tục khi dòng trước thành công:

```powershell
git branch --show-current
git status --short
python -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock
git commit -m "Sign acceptance criteria"
git push -u origin main
git log --oneline -1
python -m lab10.criteria verify
```

Ghi `signed_at` trong lock và mã commit ký vào A5; chỉ đánh dấu đã push khi push thực sự thành công. Sau đó Bảo cập nhật A5 ở một commit tài liệu riêng; không lưu lại hay chỉnh định dạng file JSON đã ký. Khi commit ký đã lên GitHub, nhóm mới chuyển sang baseline CP3.

## Sử dụng AI và phần còn lại

Đã dùng Codex đọc code tĩnh, hỗ trợ viết đặc tả chỉ số và bản soát kỹ thuật. Chưa chạy `eval`/`trace`/`grade`, chưa ký, chưa commit/push. Từng thành viên vẫn tự ghi exit ticket sau khi làm bài.
