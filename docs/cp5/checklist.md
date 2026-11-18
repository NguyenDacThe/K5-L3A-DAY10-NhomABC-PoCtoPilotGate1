# Checklist CP5 · 18/11/2026 (GMT+7)

**Chỉ thẻ S7.** Đây là kiểm hồ sơ và trạng thái thực tế, không thay điểm chấm. Grade cuối `R-S7-grade-20261118-173554-d5f014` vẫn FAIL do integrity; v2 giữ **Cải tiến thêm**.

| Mục theo hướng dẫn | Kết quả / bằng chứng |
|---|---|
| Đúng repo, lớp, nhóm | Đạt: K5-L3A-DAY10-NhomABC-PoCtoPilotGate1; L3A; NhomABC |
| Bốn thành viên, MSSV, vai và mục cá nhân | Đủ trong TEAM; khớp submission.members; đã bỏ mẫu, phần trùng và các trạng thái lỗi thời |
| Phần dùng AI và exit ticket | Đủ nội dung cho bốn người; ghi rõ phần CP5 do Codex làm và các ghi chú cần cá nhân rà soát, không giả nhận mỗi người đã xác nhận |
| Ký trước đánh giá, không sửa tiêu chí | Đạt: signed15:15:34; commit60fbf2c lúc15:29:04; lần eval đầu15:29:20; hash36863666… còn nguyên |
| Cổng vòng1 giữ nguyên | Đạt: checkpoint0580db3e; so hash trước/sau demo không đổi |
| Phiếu A/B/C và C12 | Đủ mục theo kiểm thành phần; C3 chỉ phần S7; v1 giữ nguyên, v2 và ba câu bắt buộc khớp submission.json |
| Kiểm thử bản cuối | 13 test công khai,8 kiểm cổng,9 kiểm monitor,5 kiểm ranh giới chạy thành công; 1 phép kiểm ranh giới chủ đích tái hiện giới hạn, không coi là an toàn |
| Grade đúng một thẻ | Đã chạy duy nhất `--incident S7`; không lấy thẻ khác, không sửa grader/manifest |
| Kết quả chức năng | S7after40/40, nền110/110; criteria/visible/regression/monitor đạt, coverage1.0 |
| Integrity đầy đủ | **Chưa đạt:** manifest đòi28file S1–S6/S8 chưa được giao; mọi file hiện có khớp hash. Cần hướng dẫn chính thức từ Coach |
| Chạy thử demo kỹ thuật | Xong: S7-01/S7-20/S7-05 ở base/prepared/after và hai ticket hiểm B7.3, có output; không đổi cấu hình |
| Demo/phản biện trước lớp | **Chưa xác nhận:** đã có kịch bản5phút, câu hỏi phản biện và lệnh; không ghi thành đã trình bày trước Coach/bàn khác |
| Gom bản cuối và manifest | Chạy collect sau cập nhật tài liệu; kết quả chính thức xem evidence/submission-check.txt |
| Kiểm secret trong phần nộp | Không có file .env/API-key/mật khẩu được đưa vào gói; đối chiếu danh sách file trước commit |
| Lưu và đẩy bản cuối | Đang chuẩn bị commit/push CP5; sẽ ghi kết quả xác nhận sau thao tác thực tế |
| Repo Private, quyền Read của team chấm | **Chưa xác minh qua công cụ hiện có:** trưởng nhóm kiểm Settings và đúng tài khoản Coach cung cấp; không tự nhận đã mời |
| Gửi link cho Coach/team chấm | Có [nội dung sẵn để gửi](submission-message.md); chưa gửi qua công cụ nhắn tin/email |
| LMS từng người | **Chưa xác nhận:** Thể, Thông, Bảo, Bách phải dùng tài khoản cá nhân nộp cùng link repo; không tự ghi đã nộp |

## Thời hạn và việc cần làm bằng tài khoản cá nhân

- Nếu là lab buổi sáng18/11: trước23h59 ngày18/11/2026 (GMT+7).
- Nếu là lab chiều/tối18/11: trước11h59 ngày19/11/2026 (GMT+7).
- Chưa biết ca học/gia hạn cụ thể, không tự chọn hạn khác. Mỗi người kiểm hạn LMS và rà mục cá nhân trước khi nộp.
- Link chung: https://github.com/NguyenDacThe/K5-L3A-DAY10-NhomABC-PoCtoPilotGate1

Chưa tick hoàn tất những việc ngoài máy vì chưa có bằng chứng; không bỏ các mục này khỏi checklist chỉ để tất cả thành Đạt.
