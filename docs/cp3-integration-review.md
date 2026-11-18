# CP3 sau merge bốn nhánh · 18/11/2026

## Nguồn hợp nhất

| Thành viên | Nhánh nguồn | Commit nguồn | Nội dung |
|---|---|---|---|
| Nguyễn Đắc Thể | NguyenDacThe | 4382f2d | G1–G3, B0–B1/B7.1, report baseline/after |
| Trương Văn Thông | Thông | 2ea029f | B2, B7.2/B7.3, ghi chú kiểm thử |
| Phan Gia Bảo | 2A202603562_PhanGiaBao | 964aae9 | B3, phần kinh doanh B6/B7.4, business config |
| Nguyễn Tuấn Bách | bach | a810352 | B4–B5, operations/legal, runbook B7.5–B7.6 |

Nhánh `bach` được lấy vào remote-tracking `origin/bach-cp3` để tránh xung đột tên với `origin/bach/cp2-phieu-a` cũ. Không xoá nhánh nguồn. Các phần được ghép theo ranh giới B0–B8; giữ đóng góp và output lỗi lịch sử, thêm kết quả sau tích hợp, không chọn bỏ toàn bộ một phía khi xung đột.

## Phần thiếu đã bổ sung

- Sửa trạng thái tài liệu cũ nói chưa ký/chưa có cổng để phân biệt thời điểm trước và sau tích hợp.
- Chạy lại hai ticket hiểm của Thông; cả hai không ghi tiền, không quy lỗi hoặc gửi thông báo cho hãng. Lưu output trong `cp3-evidence/adhoc-1-integrated.txt` và `adhoc-2-integrated.txt`.
- Khép vòng HAZOP của Bách: chỉ phân tích một tool ở bảng kỹ thuật, chuyển rủi ro dữ liệu ra ngoài bảng; sửa trường độ trễ, xác định đúng phiên bản policy, bổ sung chặn ghi lỗi cùng kiện và từ lỗi hãng thứ ba trong ngày ở G3.
- Cụ thể hoá PIC, trực thay, kênh cảnh báo mô phỏng, người nhận khiếu nại và phương án dừng. Chốt cap tự động 1.600.000đ theo phần Bảo, giữ ngân sách máy 1.500đ và ROI 0,5. Phân biệt review_rate có kiểm mẫu với escalation_rate.
- Bổ sung checklist 9 nhóm có PIC và bằng chứng, giữ trạng thái Chưa cho các điều kiện pilot thật chưa chứng minh. Không bịa kênh bên ngoài, người đã được bố trí, cuộc họp hoặc phê duyệt.
- Kiểm tra chi phí phương án 2 người và hàng chờ tải dồn. Bổ sung B0 đủ các lần chạy, B8 có quyết định/ba bằng chứng/ngày xem lại/PIC.

## Kết quả và quyết định

| Hạng mục | Kết quả |
|---|---|
| Chữ ký | Hash 36863666… nguyên vẹn; lịch sử ký đúng tên, commit 60fbf2c trước baseline |
| Baseline | R-base-before-20261118-152920-bde05c: 109/110 đúng, 20.000đ hoàn sai, 1 lỗi oan |
| Tích hợp after | R-base-after-20261118-160500-13075f: 110/110 đúng, không tác hại an toàn, không hồi quy |
| Chốt vòng 1 | Lock **0580db3e**; hai snapshot được tạo bằng checkpoint, không sửa sau khi chốt |
| Prepared | **R-base-prepared-20261118-160738-0892bd**: pass_rate=1, pass^5=1, hoàn sai/lỗi oan/PII=0, escalation=0.2273, chi phí=4456đ, ROI=1.24, coverage=1, 0 ca ùn và không ops.violations trên bộ nền |
| Phương án 2 người | R-base-after-20261118-160609-0a1abe: 5820đ/ticket, ROI=0.72 trên lịch đến nền; config thử và report được lưu, config chính đã trả về 1 người trước checkpoint |
| Stress hàng chờ riêng | 14 ca duyệt tới cùng lúc: 1 người có 7 ca quá SLA, chờ tối đa 130 phút; 2 người còn 1 ca quá SLA, chờ tối đa 65 phút |
| Kiểm thử | 13 test công khai; 8 kiểm tra biên G1–G3, bao gồm ghi lặp và cap hãng; hai ticket adhoc đạt |
| Quyết định v1 | **Cải tiến thêm**: không lấy bộ nền xanh làm bằng chứng đủ tải cao điểm; còn queue_stuck > 0 trong kiểm tra bất lợi, có giả thuyết vận hành và hạn 2026-11-28 |

Stress queue dùng `ops.attach_queue` trên dữ liệu mô phỏng riêng, không phải báo cáo eval có mã run, không đổi dữ liệu gốc hoặc gắn nhãn production. Config chính 1 người được giữ như giả thuyết đã đo để làm mốc prepared; v1 chưa cho phép mở pilot thật. Tăng người có chi phí nên cần đo cả phân tải và luồng tay trước khi quyết định lại.

CP3 hoàn chỉnh về nội dung/hồ sơ và kiểm tra local; các dòng Chưa trong checklist là lý do để quyết định Cải tiến thêm, không được tô Xong để làm đẹp báo cáo. Đạt CP3 không đòi quyết định phải là Tiếp tục. Việc push commit chốt vòng 1 vẫn là bước cần làm trước khi chuyển tiếp theo đúng hướng dẫn.

## Giữ đúng hash trên Windows và máy khác

Bảo phát hiện `acceptance_criteria.json` ký bằng CRLF, trong Git là LF; đã thêm `.gitattributes` yêu cầu checkout riêng file tiêu chí bằng CRLF, giữ nguyên hash/lock, không ký lại. Source đang tham gia hash report được quy định rõ xuống dòng; hai snapshot dùng `-text` để giữ chính xác byte đã chốt. Các file code/data bị khóa trước đó lệch manifest chỉ do CRLF đã được trả về đúng byte LF có hash gốc; không thay logic, dữ kiện, nhãn hoặc manifest.

Trước khi commit đã so chữ ký, checkpoint, hash report với source hiện tại, kiểm hồi quy, snapshot và ancestry bốn nhánh. Không mở thẻ sự cố hay chạy grade khi chưa bốc thẻ. Không chạy check_submission để ép hồ sơ CP4/CP5 hoàn tất sớm.

## Bước tiếp theo

Review kết luận v1 và commit tích hợp trên main, push khi trưởng nhóm yêu cầu. Khi Coach phát thẻ và bốc đúng số, mới làm CP4: ghi thẻ, chạy grade trước mọi sửa vòng 2, giữ nguyên tiêu chí và bản chốt vòng 1.
