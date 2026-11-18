# Rà soát file và phân công CP4–CP5

## File bắt buộc và bản chính

Đối chiếu CHECKPOINTS, SUBMISSION và `submission/README.md`: nộp một `TEAM.md` và một gói `submission/` chung, không bắt buộc mỗi người có một Phiếu C hoặc một C12 riêng. Kết quả kiểm đường dẫn, nội dung các mục, liên kết tài liệu và hash nằm trong [file-audit.json](file-audit.json); kết quả lệnh 7 trong [submission-check.txt](evidence/submission-check.txt).

| Thành phần | Nơi kiểm tra |
|---|---|
| Bốn thành viên, MSSV, vai, đóng góp, bằng chứng, dùng AI và exit ticket | [TEAM](../../TEAM.md) |
| Phiếu A A1–A5, Phiếu B B0–B8, Phiếu C C0–C12 | `templates/form-*.md`; bản gom tương ứng trong `submission/docs/` |
| Tiêu chí đã ký, lock, cổng/config hai vòng và switches | `config/`, `lab10/`; bản gom trong `submission/config/`, `submission/code/` |
| Team, bốn thành viên, S7, v1/v2 và ba dòng bắt buộc | [submission.json](../../submission/submission.json) |
| Report S7 base/prepared/after, grade JSON/Markdown, nhật ký và manifest | `submission/runs/`, [manifest](../../submission/manifest.json) |

## Phần đã bổ sung sau rà soát

- Thống nhất TEAM và tài liệu CP5: đây là công việc chung của nhóm theo từng vai. Giữ khai báo AI hỗ trợ theo yêu cầu bài.
- Bổ sung [bàn giao Bách](../cp4-bach.md), nêu đủ C3.3/C4/C11 và phần phối hợp C5/C7/C10, **C12**, metadata/gom bài. Trong C12 chung có bảng đối chiếu năng lực, pháp lý, PIC/hạn và hồ sơ nộp của vai Bách.
- Bổ sung [bàn giao Bảo](../cp4-bao.md), nêu C1/C7/C10 và trách nhiệm tổng hợp C12. Thể tích hợp/đẩy bài; Thông kiểm thử/monitor; Bách phối hợp C12 và phụ trách metadata/gom bài.
- Sửa đoạn C0 cuối CP5 bị mất dấu tiếng Việt. Chuyển liên kết bằng chứng ngoài gói trong Phiếu B/C sang URL repo để vẫn mở đúng từ các bản được lệnh 7 chép vào `submission/docs/`.
- Gom lại bằng lệnh chính thức; không sửa tay bản chép Phiếu C hoặc hash manifest bài nộp.

Các file `docs/cp4-integration/source-<commit>-form-c.md` là bản lịch sử trước tích hợp: giữ nguyên ô trống và số liệu lúc bàn giao. C12 cuối được điền một lần trong Phiếu C chung; không sửa bản lịch sử để tạo cảm giác đã hoàn thành sớm hơn.

## Việc còn cần xác nhận

Không thiếu thành phần bắt buộc trong gói nộp khi lệnh 7 báo ĐỦ THÀNH PHẦN. Grade vẫn FAIL vì manifest đòi 28 file thẻ không được giao; không bổ sung chúng, chỉ dùng S7. Quyền truy cập team chấm, demo thực tế, rà soát mục cá nhân và LMS theo [checklist](checklist.md), không đánh dấu hoàn thành chỉ từ sự tồn tại của file.
