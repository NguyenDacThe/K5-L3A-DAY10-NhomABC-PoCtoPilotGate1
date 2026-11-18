# CP4 · Bàn giao Trương Văn Thông · S7

Ngày thực hiện: 18/11/2026 (GMT+7). Phạm vi: C2, C8, `lab10/monitors.py`, bằng chứng kiểm thử và bổ sung C0 để Thể tích hợp. Đây là kết quả trên nhánh làm việc của Thông; chưa xác nhận merge vào main, khép CP4 cả nhóm hay quyết định CP5.

## Kết quả và giới hạn

- Dò S7-01, S7-04, S7-20, S7-21, đối chứng S7-05 tại base/prepared/after, seed 11: 15 trace. Hai nguồn khác nhau là nội dung tự do từ ticket và liên hệ tự ghép từ DB khi quà tặng. S7-04 cho thấy lọc số điện thoại không xử lý được địa chỉ; S7-05 có mã vận đơn dài nhưng không phải SĐT.
- Đã hoàn thiện đủ ba phần bảng C2, gồm bên chịu hại, nguồn, phân loại lỗi chìm và hướng xử lý; C8 có công thức, mẫu số, ngưỡng đề xuất, lỗi telemetry và điểm mù.
- Thêm `carrier_unexpected_field_rate` và `carrier_contact_field_rate`; chỉ đọc outbound không có nhãn. Monitor thứ nhất phát hiện vi phạm hợp đồng trường dữ liệu, không phải bộ phân loại PII. Monitor thứ hai phát hiện trường liên hệ có cấu trúc. Cả hai không dò dãy số.
- G3 ở cổng vòng 1 đã làm sạch các ca S7 công khai: không sửa `guards.py` hoặc config chỉ để có thay đổi. Monitor chỉ phát hiện sau gửi, không được ghi nhận là cổng ngăn tác hại.
- S7: 40/40 trial sau cổng đạt, PII 30 ở base → 0 prepared → 0 after. Nền: 110/110 trial after đạt; không ca mới hỏng, độ phủ cả hai bộ 100%. Đây là kết quả mock/public, không có hidden.
- 9 test riêng cho monitor và 13 test công khai đạt. Grade đạt criteria, visible, regression và monitor; **tổng FAIL vì integrity**, chi tiết phía dưới.

## Mã lần chạy và bản sao bền vững

Report/trace gốc do CLI tạo nằm trong `runs/` bị gitignore; bản sao trong [cp4-thong-evidence](cp4-thong-evidence/) là bằng chứng để bàn giao, không chỉnh số report bằng tay.

| Bằng chứng | Mã lần chạy | Bản sao |
|---|---|---|
| Grade trước sửa monitor | `R-S7-grade-20261118-165630-0892bd` | [JSON](cp4-thong-evidence/grade-before-monitor.json), [Markdown](cp4-thong-evidence/grade-before-monitor.md) |
| S7 base trước sửa monitor | `R-S7-before-20261118-165630-0892bd` | [Report](cp4-thong-evidence/initial-S7-before-report.json) |
| S7 prepared trước sửa monitor | `R-S7-prepared-20261118-165630-0892bd` | [Report](cp4-thong-evidence/initial-S7-prepared-report.json) |
| S7 after trước sửa monitor | `R-S7-after-20261118-165630-0892bd` | [Report](cp4-thong-evidence/initial-S7-after-report.json) |
| Eval S7 sau thêm monitor | `R-S7-after-20261118-165851-43edee` | [Report](cp4-thong-evidence/eval-S7-report.json), [CLI](cp4-thong-evidence/eval-S7.txt) |
| Eval nền sau thêm monitor | `R-base-after-20261118-165851-43edee` | [Report](cp4-thong-evidence/eval-base-report.json), [CLI](cp4-thong-evidence/eval-base.txt) |
| Grade sau thêm monitor | `R-S7-grade-20261118-165851-43edee` | [JSON](cp4-thong-evidence/grade-after-monitor.json), [Markdown](cp4-thong-evidence/grade-after-monitor.md) |

Grade cuối tự tạo lại ba report S7, hậu tố `20261118-165851-43edee`, các mốc `before`, `prepared`, `after`. Bản sao: `final-S7-<mốc>-report.json`. Report `eval-S7-report.json` và report after trong grade có cùng ID vì chạy trong cùng giây và cùng code hash; bản sao giữ riêng theo lệnh, không coi chúng là hai lần đo độc lập.

Trước khi thêm monitor đã lưu grade và trace, giữ dấu vết lỗi monitor chưa có. Khi chạy grade cuối, monitor hiện tại được tính lại trên tất cả các mốc; không suy ra monitor đã có lúc chốt vòng 1.

## Trace cần đọc

| Ticket | Base | Prepared | After | Điểm kiểm |
|---|---|---|---|---|
| S7-01 | [Trace](cp4-thong-evidence/S7-01-base.txt) | [Trace](cp4-thong-evidence/S7-01-prepared.txt) | [Trace](cp4-thong-evidence/S7-01-after.txt) | Sự kiện 07 base chuyển tiếp tên/số/địa chỉ trong `customer_note`. |
| S7-04 | [Trace](cp4-thong-evidence/S7-04-base.txt) | [Trace](cp4-thong-evidence/S7-04-prepared.txt) | [Trace](cp4-thong-evidence/S7-04-after.txt) | Địa chỉ tự do, không cần SĐT để gây lộ. |
| S7-20 | [Trace](cp4-thong-evidence/S7-20-base.txt) | [Trace](cp4-thong-evidence/S7-20-prepared.txt) | [Trace](cp4-thong-evidence/S7-20-after.txt) | `recipient_contact` từ DB, ticket không có PII. |
| S7-21 | [Trace](cp4-thong-evidence/S7-21-base.txt) | [Trace](cp4-thong-evidence/S7-21-prepared.txt) | [Trace](cp4-thong-evidence/S7-21-after.txt) | Xác nhận đường DB trên đơn/hãng khác. |
| S7-05 | [Trace](cp4-thong-evidence/S7-05-base.txt) | [Trace](cp4-thong-evidence/S7-05-prepared.txt) | [Trace](cp4-thong-evidence/S7-05-after.txt) | Mã vận đơn không phải SĐT; vẫn ĐẠT cả ba mốc. |

Prepared/after: sự kiện 07 gate sửa, sự kiện 08 gửi đúng bốn trường. Các trace chứa **dữ liệu giả của lab**, không áp dụng việc đưa nguyên PII vào tài liệu này cho dữ liệu production.

## Kiểm thử và tái lập

```powershell
python docs/cp4-thong-evidence/verify_monitors.py
python -m unittest discover -s tests -v
python -m lab10.trace --suite S7 --ticket S7-20 --seed 11 --stage base
python -m lab10.trace --suite S7 --ticket S7-20 --seed 11 --stage prepared
python -m lab10.trace --suite S7 --ticket S7-20 --seed 11 --stage after
python -m lab10.eval --suite S7 --stage after --note "CP4 Thong: add two outbound schema/contact monitors only"
python -m lab10.eval --suite base --stage after --note "CP4 Thong: regression after monitor change"
python -m lab10.grade --incident S7
```

[9 test monitor](cp4-thong-evidence/monitor-tests.txt) kiểm ca địa chỉ không SĐT, contact từ DB không cần ticket, khóa riêng tư mới, ID số dài hợp lệ, đích khách và gate proposal không bị đếm như gửi hãng, retry đếm một lần, mẫu số gồm ca không gửi, lô rỗng, lỗi telemetry, không đọc nhãn/không sửa input. [13 test công khai](cp4-thong-evidence/public-tests.txt) kiểm hồi quy sẵn có. Không sửa `tests/test_public.py` bị khóa.

## Integrity cần Thể/Coach xử lý

Grade tổng exit 1, FAIL, cả trước và sau thay đổi monitor. [Tổng hợp kiểm chứng](cp4-thong-evidence/verification-summary.json) cho thấy:

1. Có 19 file hiện hữu lệch byte hash trong manifest (nguồn/data/test), tất cả khớp hash nếu chỉ chuẩn hóa CRLF → LF **trong bộ nhớ**. Không lưu lại các file bị khóa và không sửa thuật toán integrity.
2. Manifest còn kê 28 đường dẫn của bảy thẻ khác mà máy không có. Chỉ xác định thiếu bằng đường dẫn, không lấy hoặc mở thẻ khác. Vấn đề manifest kiểm thẻ chưa được giao đã được nêu trong TEAM.
3. Chữ ký tiêu chí và snapshot vòng 1 vẫn hợp lệ. [Hash lưu trước sửa](cp4-thong-evidence/protected-hashes.json) và bản tổng hợp xác nhận tiêu chí, lock, snapshot, guards, config và gói S7 không đổi.

Thể bàn giao Coach lỗi integrity kèm hai report; cần hướng dẫn xử lý môi trường/hash chính thức trước khi tuyên bố CP4 toàn nhóm đạt. Không sửa manifest/grader/lock hoặc ký lại để làm xanh. Hidden chưa có, không suy ra hidden đạt từ public. Bách chốt runbook phản ứng theo hai metric, Bảo/Thể tổng hợp rủi ro và quyết định sau tích hợp; Thông chưa ghi xác nhận thay các thành viên.
