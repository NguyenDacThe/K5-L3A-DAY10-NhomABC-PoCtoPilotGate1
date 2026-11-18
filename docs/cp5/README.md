# CP5 · Bản cuối của NhomABC · S7

CP5 là phần việc chung của nhóm: Thể tích hợp và đẩy bài; Thông kiểm thử, trace và monitor; Bảo tổng hợp quyết định v2/C12; Bách phối hợp C12 về vận hành/pháp lý, phụ trách metadata và gom bài. Phần trình bày thật, xác nhận cá nhân, quyền truy cập team chấm và LMS được theo dõi riêng theo bằng chứng.

## Tài liệu dùng trực tiếp

- [Checklist cuối](checklist.md): phân biệt đã làm trên máy với các việc cần tài khoản/con người xác nhận.
- [Demo 5 phút](demo.md): nội dung cho bốn vai, bảng ba mốc, câu hỏi dự kiến và lệnh minh họa.
- [Nội dung gửi Coach/team chấm](submission-message.md): sẵn để gửi đúng kênh Coach chỉ định; chưa gửi thay người dùng.
- [TEAM đã chuẩn hóa](../../TEAM.md): đủ bốn mục cá nhân, đóng góp/bằng chứng/AI/exit ticket; bỏ mẫu và trạng thái cũ.
- [C12 cuối](../../templates/form-c-incident.md#c12) và [thông tin bài nộp](../../submission/submission.json): cùng giữ v1/v2 **Cải tiến thêm**.
- [Report sau chạy thử demo](evidence/grade-report.md), [metadata kiểm cuối](summary.json), log trong evidence.
- [Bàn giao Bách](../cp4-bach.md), [bàn giao Bảo](../cp4-bao.md): liên kết phần CP4 sang C12/CP5, không tách thành quyết định riêng cho từng người.
- [Rà soát file và phân công](file-review.md), [kết quả kiểm file](file-audit.json).

## Đã thực hiện

1. Đọc CHECKPOINTS, README, SUBMISSION, RULES, RUBRIC và submission/README.
2. Chạy lại 13 test công khai, 8 kiểm cổng, 9 kiểm monitor, 5 kiểm ranh giới. Phép kiểm district là phản ví dụ có chủ đích, không chứng minh trường hợp đó an toàn.
3. Chạy thử S7-01 (PII từ chữ tự do), S7-20 (liên hệ tự lấy từ DB) và S7-05 (đối chứng có số) ở base/prepared/after; chạy lại hai ticket hiểm B7.3. Các output lưu riêng, không ghi là đã có buổi phản biện cùng bàn khác.
4. Chỉ chạy `python -X utf8 -m lab10.grade --incident S7`, không tải/xem/làm thẻ khác. Snapshot và mọi file bảo vệ được so hash trước/sau chạy thử, không đổi.
5. Cập nhật C0/C12 bằng mã sau demo; soát checklist C11, giữ các mục Chưa có căn cứ. Gom lại bài từ templates bằng lệnh chính thức, không sửa tay bản chép submission/docs.
6. Kiểm tên repo/team, bốn thành viên/MSSV, chữ ký trước lần đo, code hash báo cáo, byte của gói nộp và manifest trước khi lưu/đẩy.

Script tái lập phần kiểm kỹ thuật:

```powershell
python -X utf8 docs/cp5/run_checks.py
```

Script không đổi code/config, nhưng tạo grade mới. Nếu chạy lại, cập nhật C0/C12 sang mã mới khi cần, rồi chạy `python -X utf8 -m lab10.check_submission --collect` trước khi nộp. Không dùng exit0 của script điều phối để thay verdict thật của grade.

## Kết quả và giới hạn

S7 after40/40, nền110/110, PII/hoàn sai/lỗi hãng oan bằng0, coverage1.0, không hồi quy; criteria/visible/regression/monitor đạt. S7 chi phí5005đ/ticket, ROI1.0; nền4456đ, ROI1.24. Hai monitor ở after đều0.

Grade tổng vẫn **FAIL**, exit1, vì manifest kiểm28đường dẫn S1–S6/S8 chưa được giao. Mọi file hiện có (gồm bốn file S7) đúng hash. Chưa có hướng dẫn Coach để giải quyết mâu thuẫn phát một thẻ/kiểm tám gói; không sửa grader, manifest, tạo file giả hoặc lấy thẻ khác. Giữ nguyên lỗi trong gói để team chấm xem xét.

V2 giữ Cải tiến thêm: số trên bộ đã chạy đạt nhưng giả lập tải dồn14ca vẫn quá SLA với1–2người, nguồn dữ liệu/kênh thật chưa được xác minh; chưa mở pilot thật. Kiểm đủ thành phần không thay điều kiện integrity hoặc chấm điểm.

## Dọn TEAM.md

Bỏ phân công dài lặp lại, hướng dẫn mẫu, dấu chờ điền, thông báo chưa ký/chưa có cổng/chưa merge đã lỗi thời và các đoạn tích hợp trùng. Giữ thông tin nhóm, bốn thành viên và nguồn Lab9; mỗi người có phần việc/đóng góp, bằng chứng commit/phiếu, khai báo AI và exit ticket. Bổ sung phần Bách dựa trên commit nhánh bach (`1819afd`, `1143577`), không tự nhận hai commit nguồn đó đã nằm trong ancestry main.

Không xóa bằng chứng lịch sử khỏi git hoặc các báo cáo nguồn. Các exit ticket được giữ/rút gọn/soạn từ bằng chứng có ghi rõ trong TEAM; thành viên phải đọc và chịu trách nhiệm giải thích khi demo. Không bịa việc gửi tin, demo trước lớp, cấp quyền hay nộp LMS.
