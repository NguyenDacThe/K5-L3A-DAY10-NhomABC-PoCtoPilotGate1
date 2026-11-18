# CP4–CP5 · Bàn giao Phan Gia Bảo · S7

Vai: Sản phẩm và kinh doanh. Bản chính là Phiếu C chung; tài liệu này liên kết phần CP4 với quyết định v2/C12 và bài nộp CP5.

| Mốc / mục | Nội dung bàn giao | Bản chính |
|---|---|---|
| CP4 · C1 | So sánh base/prepared/after, ROI/chi phí và tác hại bên thứ ba theo kho/hãng | [C1](../templates/form-c-incident.md#c1) |
| CP4 · C7 | Lý do giữ cấu hình business/phạm vi; không thu hẹp về 0 hoặc sửa ngưỡng đã ký để làm đẹp report | [C7](../templates/form-c-incident.md#c7), [cấu hình](../config/operating_gates.json) |
| CP4 · C10 | Risk register với PIC, tín hiệu, hành động, rủi ro chi phí người trực và nguồn dữ liệu | [C10](../templates/form-c-incident.md#c10) |
| CP5 · C12 | Tổng hợp quyết định v2, ba bằng chứng, giữ/đổi so với v1, hạn và ba dòng bắt buộc; phối hợp Bách về vận hành/pháp lý | [C12](../templates/form-c-incident.md#c12) |
| CP5 · Demo | Giải thích ROI đạt vẫn có thể che PII, chi phí cả luồng tay, độ phủ và lý do chưa mở pilot | [kịch bản demo](cp5/demo.md) |

## Số liệu và quyết định

Grade `R-S7-grade-20261118-173554-d5f014`: S7 base có 30 lần lộ PII dù ROI 1,27; prepared/after PII 0, 40/40 trial, chi phí 5.005đ/ticket, ROI 1,0, độ phủ 1,0. Nền after 110/110, chi phí 4.456đ/ticket, ROI 1,24. Các ngưỡng số trên hai bộ đã chạy đều đạt; không coi đó là phê duyệt pilot thật.

V2 giữ **Cải tiến thêm**: kiểm tải dồn vẫn quá SLA với 1–2 người, chưa đo phương án mới cùng tổng chi phí; integrity cần Coach làm rõ. Trước **2026-11-28**, Bảo kiểm chi phí/phạm vi cùng Bách kiểm năng lực và pháp lý, Thông kiểm thử, Thể tích hợp. Giữ tối đa 2 vòng sửa tổng cộng theo tiêu chí; hết hạn/giới hạn vẫn chưa đạt thì Dừng. Ba câu bắt buộc trong C12 và `submission/submission.json` phải giống nhau.

## Bằng chứng

Commit CP4 `989d5cb`; [Phiếu C nguồn](cp4-integration/source-989d5cb-form-c.md), [report cuối](cp5/evidence/grade-report.md), [tải dồn](cp3-evidence/peak-queue-check.json), [metadata bài nộp](../submission/submission.json), [mục cá nhân](../TEAM.md#phangiabao-2a202603562). Phiếu C nguồn giữ lịch sử trước tích hợp; không điền ngược các ô C12 còn trống trong bản lịch sử.
