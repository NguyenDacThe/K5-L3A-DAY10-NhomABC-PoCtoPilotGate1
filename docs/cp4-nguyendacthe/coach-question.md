# Nội dung chuẩn bị để trưởng nhóm hỏi Coach

Nhóm NhomABC được giao S7 và làm theo hướng dẫn chỉ lấy `incidents/S7/` gồm bốn file. Cả bốn file khớp SHA-256 trong manifest; không có thay đổi code kiểm tra hoặc dữ liệu thẻ.

Chạy `python -X utf8 -m lab10.grade --incident S7`, report `R-S7-grade-20261118-165225-2bd310` báo integrity không đạt vì thiếu28file của S1–S6/S8. `lab10/grade.py::integrity` duyệt toàn manifest nên các gói không được giao cũng bị báo "file khoá bị đổi". Trong số28đường dẫn bị báo không có file S7.

Nhờ Coach xác nhận cách kiểm integrity dành cho mô hình phát đúng một gói thẻ, hoặc cung cấp bản công cụ/manifest chính thức tương thích. Nhóm chưa tự tải thẻ của bàn khác, sửa manifest, bỏ qua kiểm tra hoặc đổi dữ liệu để làm xanh.

Lưu ý riêng: monitor mới chưa được thành viên phụ trách bàn giao; lỗi monitor là phần việc CP4 của nhóm, không gộp vào vấn đề công cụ integrity.

Đây là bản nháp để trưởng nhóm chuyển cho Coach, chưa được gửi qua bất kỳ dịch vụ nhắn tin/email nào.
