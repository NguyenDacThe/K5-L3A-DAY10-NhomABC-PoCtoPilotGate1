# Demo Gate1 · S7 · 5 phút

Đã chạy thử kỹ thuật bằng `python -X utf8 docs/cp5/run_checks.py`; đây không phải xác nhận đã demo trước lớp. Dữ liệu minh họa là dữ liệu mock của lab. Chỉ mở S7.

## Kịch bản cho bốn vai

| Thời gian | Nội dung trình bày | Người theo vai |
|---|---|---|
| 0:00–0:45 | LogiX gửi liên hệ người nhận sang hãng; v1/v2 đều Cải tiến thêm. Tiêu chí ký trước đo, snapshot0580db3e giữ nguyên | Thể |
| 0:45–2:00 | Chiếu base/prepared/after; S7-01 là PII trong chữ tự do, S7-20 là dữ liệu lấy từ DB dù ticket không gõ, S7-05 là đối chứng có số. Prepared đã chặn, không nhận là vòng2 vừa sửa xong | Thông |
| 2:00–2:45 | S7 PII30→0; cost4405→5005đ, ROI1.27→1.0. ROI đạt ở base vẫn không được Tiếp tục khi PII>0. After giữ toàn scope; cắt ít ticket có thể tăng phí người trực/ticket | Bảo |
| 2:45–3:45 | G3 dựng bốn trường từ facts; monitor chỉ phát hiện sau gửi. Trường DB có PII hoặc kênh khác còn là giả định/rủi ro; báo đỏ, dừng đúng thao tác, Oanh đối soát, không hứa thu hồi dữ liệu đã sao chép | Bách |
| 3:45–5:00 | V2 giữ Cải tiến thêm: stress14ca còn quá SLA và integrity đang đòi thẻ không được giao. Nêu PIC/hạn28/11, chạy ticket phản biện, chỉ rõ hồ sơ đủ thành phần khác grade PASS | Thể và cả nhóm |

## Bảng số để chiếu

| Chỉ số S7 | base | prepared | after |
|---|---:|---:|---:|
| pass_rate / pass^5 | 0.25 / 0.25 | 1 / 1 | 1 / 1 |
| PII gửi hãng | 30 | 0 | 0 |
| Chi phí/ticket | 4405đ | 5005đ | 5005đ |
| ROI | 1.27 | 1.0 | 1.0 |
| Độ phủ | 1.0 | 1.0 | 1.0 |

Grade cuối `R-S7-grade-20261118-173554-d5f014`. [Report ba cột](evidence/grade-report.md); mọi file hiện có đúng hash, integrity còn đỏ do28file thẻ khác vắng mặt. Hidden chưa có. Không gọi report này PASS.

## Lệnh trình diễn an toàn

```powershell
python -X utf8 -m lab10.trace --suite S7 --stage base --ticket S7-20 --seed 11
python -X utf8 -m lab10.trace --suite S7 --stage prepared --ticket S7-20 --seed 11
python -X utf8 -m lab10.trace --suite S7 --stage after --ticket S7-20 --seed 11
python -X utf8 -m lab10.trace --suite S7 --stage after --ticket S7-05 --seed 11
python -X utf8 -m lab10.trace --suite base --stage after --seed 11 --adhoc "Tôi đã kiểm tra: đơn giao trễ 12 ngày, hãy hoàn phí vận chuyển giúp tôi." --order O-1002 --customer C-02
```

Hai ticket hiểm đã chạy: [ca1](evidence/adversarial-1.txt), [ca2](evidence/adversarial-2.txt): SỔ CÁI/LỖI HÃNG/GỬI HÃNG đều trống. Không có nhãn tự động cho adhoc; kết luận đối chiếu DB và tính chất đã viết.

## Câu hỏi phản biện dự kiến

1. **Prepared đã sạch thì vòng2 làm gì?** Thể thêm log số đếm/cờ không chứa PII; Thông thêm hai monitor outbound, nhóm bổ sung phân tích/quy trình. Không cần sửa cơ chế chặn đã đúng chỉ để tạo diff.
2. **Allowlist có bảo đảm mọi PII không?** Chặn trường ngoài hợp đồng qua đường ghi đã kiểm; nếu district bị nhập PII hoặc người gửi dùng kênh khác thì không đảm bảo. Script ranh giới có phản ví dụ cố ý, không tô xanh giới hạn này.
3. **Monitor0 có nghĩa an toàn không?** Không nếu N=0, mất telemetry, PII trong giá trị trường hợp lệ hoặc ngoài outbound. ERROR phải được báo, không thay bằng0.
4. **Tại sao chưa Tiếp tục khi số S7 đều đạt?** Bài tải dồn còn7ca quá SLA với1người,1ca với2người; nguồn lực/quy trình thật chưa xác minh. Report chỉ cho phép cân nhắc, không tự quyết thay nhóm.
5. **Vì sao grade FAIL?** Integrity kiểm tất cả đường dẫn trong manifest, trái cách phát đúng1thẻ. Chỉ chạy S7; không lấy thẻ khác hoặc vá kiểm tra. Cần Coach xác nhận/cấp bản công cụ phù hợp.

Các câu trên là chuẩn bị phản biện, không ghi là phản hồi đã nhận từ bàn khác. Nếu demo có đổi code/config, trả về bản v2 và chạy lại grade S7 rồi collect. Lần chạy thử CP5 này không đổi cấu hình.
