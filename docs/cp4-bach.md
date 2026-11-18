# CP4–CP5 · Bàn giao Nguyễn Tuấn Bách · S7

Vai: Vận hành và pháp lý. Hồ sơ này liên kết nội dung đã tích hợp vào bản chung; không thay Phiếu C, không phải xác nhận quy trình đã được triển khai ngoài lab.

## Phần việc và nơi kiểm tra

| Mốc / mục | Nội dung bàn giao | Bản chính |
|---|---|---|
| CP4 · C3.3 | Lòng tin của người đặt/người nhận quà ở hai mốc tin quá mức và không tin; bên chịu hậu quả khi dữ liệu rời hệ thống | [C3, phần S7](../templates/form-c-incident.md#c3) |
| CP4 · C4 | HAZOP riêng cho `notify_carrier`, sai phạm vi dữ liệu và cách phản ứng | [C4](../templates/form-c-incident.md#c4) |
| CP4 · C5/C7/C10 | Phối hợp giả định nguồn DB, quy trình và rủi ro dữ liệu trong trường được phép, tải dồn và trách nhiệm bên thứ ba | [C5](../templates/form-c-incident.md#c5), [C7](../templates/form-c-incident.md#c7), [C10](../templates/form-c-incident.md#c10) |
| CP4 · C11 | Checklist chín nhóm có PIC; runbook 4–5 có tín hiệu, ngưỡng, dừng/khôi phục, người xử lý và ba kịch bản tuần đầu | [C11](../templates/form-c-incident.md#c11) |
| CP5 · C12 | Phối hợp Bảo tổng hợp v2 về năng lực, pháp lý, PIC, hạn, điều kiện đánh giá lại và ba dòng bắt buộc | [C12, đối chiếu vận hành/pháp lý](../templates/form-c-incident.md#c12) |
| CP5 · Metadata và gom bài | Đúng team, bốn thành viên/MSSV, S7, v1/v2 và ba câu khớp C12; gom bằng lệnh 7, kiểm manifest và thành phần | [submission.json](../submission/submission.json), [manifest](../submission/manifest.json), [log kiểm bài](cp5/evidence/submission-check.txt) |

C12 thuộc CP5 theo CHECKPOINTS, là quyết định chung của nhóm. Bách phối hợp phần vận hành/pháp lý và hồ sơ nộp; Bảo cầm bút tổng hợp quyết định, Thông kiểm số liệu, Thể tích hợp. Không cần một bản C12 khác trên từng nhánh hoặc bốn bộ submission riêng.

## Kết luận vận hành/pháp lý cho C12

- S7 after 40/40, nền 110/110, hàng chờ 0 trên các bộ đã đo. Kiểm tải dồn B7.6 vẫn có 7 ca quá SLA với 1 người hoặc 1 ca với 2 người khi 14 ca tới cùng lúc. Chưa có bằng chứng phương án phân tải mới đạt SLA và chi phí.
- Hai monitor quan sát outbound không có nhãn; chỉ phát hiện sau gửi. Chúng không chứng minh trường DB được phép không chứa PII hoặc không còn kênh xuất khác.
- Giữ **Cải tiến thêm** ở v2; Bách phối hợp Hạnh/Tùng kiểm nguồn lực, Pháp chế kiểm căn cứ chia sẻ, trước ngày **2026-11-28**. Giữ giới hạn tối đa 2 vòng sửa tổng cộng theo bản ký; hết hạn/giới hạn vẫn chưa đạt thì Dừng.
- Grade cuối `R-S7-grade-20261118-173554-d5f014` vẫn FAIL do 28 đường dẫn thẻ không được giao vắng mặt. Chỉ dùng S7; kiểm đủ thành phần không biến FAIL thành PASS.

## Bằng chứng và nguồn

Commit CP4 `8dd380e` đã tích hợp; nguồn bổ sung trên nhánh bach: `1819afd`, `1143577`. Phiếu C nguồn được giữ nguyên tại [bản bàn giao CP4](cp4-integration/source-8dd380e-form-c.md); các ô chưa điền trong bản lịch sử không phải tình trạng Phiếu C cuối. Bản cuối là `templates/form-c-incident.md` và bản gom của nó trong `submission/docs/`.

Report: [JSON](cp5/evidence/grade-report.json), [ba mốc](cp5/evidence/grade-report.md); tải dồn: [peak-queue-check.json](cp3-evidence/peak-queue-check.json). Khai báo AI và exit ticket nằm trong [TEAM](../TEAM.md#nguyentuanbach-2a202603596).

Các mốc phản ứng 15 phút/24 giờ trong runbook là đề xuất vận hành. Quyền truy cập, demo thực tế, xác nhận từng người và nộp LMS được theo dõi tại [checklist CP5](cp5/checklist.md), không suy từ việc có file.
