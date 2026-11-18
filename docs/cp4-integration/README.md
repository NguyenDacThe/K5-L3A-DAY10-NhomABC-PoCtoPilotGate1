# CP4 và C12 sau tích hợp · NhomABC · S7

## Nguồn đã merge vào main local

| Nhánh | Commit nguồn | Phần chính |
|---|---|---|
| NguyenDacThe | d634d3e | C0–C1/C5–C7/C9, G3 telemetry và bằng chứng |
| Thông | 91ea2ca | C2/C8, hai monitor outbound, 9 kiểm tra monitor và trace |
| 2A202603562_PhanGiaBao | 989d5cb | Phân tích kinh doanh C1/C7, risk register C10 |
| bach (theo dõi bằng origin/bach-cp4) | 8dd380e | C3.3, C4, checklist/runbook C11 |

Bốn bản Phiếu C nguồn được giữ tại `source-<commit>-form-c.md`. Phiếu C chính được ghép theo từng mục, không dùng lựa chọn bỏ toàn bộ một phía khi xung đột. TEAM giữ phần cá nhân của người viết; không tự tạo exit ticket cho thành viên khác. Các commit merge đều local, chưa push trong lượt này.

## Lệnh đã chạy trên bản tích hợp

```powershell
python -X utf8 -m lab10.eval --suite S7 --stage after --note "CP4 merge 4 branches"
python -X utf8 -m lab10.eval --suite base --stage after --note "CP4 integrated regression"
python -X utf8 -m lab10.grade --incident S7
python -X utf8 -m lab10.gate --run docs/cp4-integration/evidence/S7-after-report.json --baseline docs/cp4-nguyendacthe/evidence/initial-before-report.json
python -X utf8 -m lab10.gate --run docs/cp4-integration/evidence/base-eval-report.json --baseline docs/cp3-evidence/baseline-report.json
```

Hai câu note ở trên mô tả mục đích tái lập; note thực tế của lần đã chạy được giữ nguyên trong report. Lệnh grade không tự điền Phiếu C: C12 được tổng hợp từ các report và tiêu chí, không tạo số giả để lấp bảng.

| Mốc S7 | Run ID | pass_rate / pass^5 | PII |
|---|---|---:|---:|
| base | R-S7-before-20261118-171745-d5f014 | 0.25 / 0.25 | 30 |
| prepared | R-S7-prepared-20261118-171745-d5f014 | 1.0 / 1.0 | 0 |
| after | R-S7-after-20261118-171745-d5f014 | 1.0 / 1.0 | 0 |

Grade cuối: **R-S7-grade-20261118-171745-d5f014**, verdict **FAIL**, exit1. Không ghi thành PASS-VISIBLE hay Đạt toàn bộ.

| Kiểm | Kết quả thực tế |
|---|---|
| criteria | Đạt; tiêu chí/lock không đổi, hash36863666… |
| checkpoint | Hợp lệ, hash0580db3e; không chốt lại vòng1 |
| visible | Đạt, 40/40 trial S7 after, không vi phạm trần, coverage1.0 |
| regression | Đạt, nền110/110, không ca mới hỏng |
| monitor | Đạt; schema ở base nền0.509091/S70.875, contact0/S70.25; prepared/after đều0 |
| hidden | Không có trên máy, không tuyên bố đã kiểm |
| integrity | Không đạt do28đường dẫn S1–S6/S8 chưa được giao; không có file hiện hữu nào sai hash |

S7 after: chi phí5005đ/ticket, ROI1.0, escalation0, review_rate0.125, hàng chờ0ca, coverage1.0. Nền after:4456đ, ROI1.24, escalation0.2273, hàng chờ0ca. Hai gate so tiêu chí đều đạt. Các con số này không tự chứng minh năng lực tải dồn, nghĩa dữ liệu nguồn hoặc kênh vận hành ngoài mock.

## Bổ sung sau merge

- C0 có mã chạy tích hợp; C1 giữ dữ liệu ban đầu và thêm kinh doanh của Bảo. Sửa nhận định “lộ ở cả4kho” thành3/4 (CT0), phân biệt review_rate với escalation_rate.
- C7/C9 ghi monitor đã được tích hợp, không tiếp tục mô tả là chưa có; vẫn giữ lịch sử trước merge. Không đổi G3/config chỉ để có thêm lần sửa khi cơ chế hiện tại đã bảo vệ bộ công khai.
- C8 có kết quả monitor của bản main và giải thích lỗi CRLF trước đây trên máy khác không còn xuất hiện ở máy tích hợp.
- C10 bổ sung rủi ro dữ liệu nằm trong trường whitelist và tải dồn; không suy xác suất từ việc tồn tại bộ hidden.
- C11 đủ9nhóm có PIC/bằng chứng, hai runbook có ngưỡng/việc/người, phân biệt đề xuất vận hành với điều kiện đã được triển khai thật. Không coi việc chuyển toàn bộ ca sang cùng một hàng chờ là giải quyết quá tải.
- C12 điền đủ bảng, ba bằng chứng và ba câu bắt buộc; ba câu được chép nguyên vào submission/submission.json cùng team, bốn thành viên, S7 và quyết định v1/v2.

## Kết luận C12

**Giữ Cải tiến thêm ở v2**, không mở pilot thật. Các ngưỡng số trên nền/S7 đều đạt và report cho phép cân nhắc Tiếp tục, nhưng không bắt buộc chọn Tiếp tục. Bài kiểm bất lợi B7.6 còn7ca quá SLA với1người và1ca với2người, chưa có phương án phân tải được đo lại; xác nhận integrity cũng chưa có. Quyết định nêu rõ nguyên nhân, PIC, giới hạn tối đa2vòng tổng cộng theo tiêu chí và ngày xem lại **2026-11-28**.

Không đổi v1, chữ ký, snapshot hoặc dữ liệu thẻ. Các phần đã đạt không bị phủ nhận vì lỗi đóng gói/công cụ; lỗi integrity cũng không bị bỏ qua vì số public đẹp.

## Phần không tự xử lý được trong phạm vi repo cho phép

Hướng dẫn nhận thẻ chỉ cho lấy đúng S7, trong khi `lab10/grade.py::integrity` duyệt tất cả file trong manifest. Người dùng xác nhận Coach chưa có hướng dẫn mới. Chỉ có thể nộp mô tả và yêu cầu bản công cụ/manifest chính thức tương thích, hoặc xác nhận từ Coach về quy trình; chưa gửi tin nhắn thay người dùng.

Không tải/xem thẻ khác, tạo file giả, sửa manifest, vá grader, monkeypatch hoặc chạy chế độ bỏ integrity để biến FAIL thành PASS. [Bản nháp hỏi Coach](../cp4-nguyendacthe/coach-question.md) và report cuối cung cấp bằng chứng cụ thể. Sự thiếu28file là vướng mắc công cụ/phân phối, không được ghi là nhóm đã hoàn tất tiêu chí integrity.

## Kiểm thử

13 test công khai,9 kiểm tra monitor và5 kiểm tra ranh giới đều chạy thành công trên bản tích hợp; trong5 kiểm tra ranh giới có1 kiểm tra cố ý tái hiện phản ví dụ về district, không phải bằng chứng phản ví dụ đó an toàn. Nguồn/command có sẵn để review:

```powershell
python -X utf8 -m unittest discover -s tests
python -X utf8 docs/cp4-thong-evidence/verify_monitors.py
python -X utf8 docs/cp4-nguyendacthe/verify_privacy_boundary.py
```

Report và nhật ký máy tích hợp được lưu trong evidence. Báo cáo/tài liệu các nhánh nguồn vẫn giữ để truy vết; không tạo lại nhật ký của máy thành viên khác nếu chưa được cung cấp. Kiểm đủ thành phần bài nộp sau collect chỉ xác nhận cấu trúc hồ sơ, không thay grade hay xác nhận đóng hết các điều kiện pilot thật.

Đã chạy `python -X utf8 -m lab10.check_submission --collect`: kết quả **ĐỦ THÀNH PHẦN**. Bản gom có ba phiếu, code/config hai vòng, tiêu chí/lock, report ba mốc, nhật ký và manifest19file. `.gitattributes` giữ nguyên byte trong submission để các hash vẫn hợp lệ sau checkout, kể cả tiêu chí CRLF. Kết quả kiểm thành phần được lưu ở `evidence/submission-check.txt`; nội dung grade FAIL do integrity được giữ trong gói, không bị thay bằng kết luận kiểm đủ hồ sơ.
