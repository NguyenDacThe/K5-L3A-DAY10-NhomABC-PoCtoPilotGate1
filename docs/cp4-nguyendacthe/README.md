# CP4 · Phần Nguyễn Đắc Thể · S7

Bản bàn giao tại thời điểm commit `d634d3e`; trạng thái chờ bên dưới mô tả thời điểm đó. Bản chung sau tích hợp và CP5 xem [Phiếu C](../../templates/form-c-incident.md), [phân công/hồ sơ cuối](../cp5/file-review.md).

Nhánh thực hiện: `NguyenDacThe`, dựa trên commit `f1d4e31`. Phạm vi theo TEAM: C0–C1, C5–C7, C9, cổng hệ thống và phối hợp tích hợp. Chưa commit/push phần việc này; chưa merge các nhánh CP4 khác, chọn v2 hoặc gom bài CP5.

## Nội dung đã làm

- Điền C0–C1 bằng grade trước sửa đã có, giữ rõ mốc base/prepared và tình trạng FAIL; không tạo lại mốc prepared hay viết đè bằng kết quả sau sửa.
- C5: specification outbound cuối, nguồn dữ liệu và giả định môi trường; phân biệt bảo vệ tên trường với nghĩa dữ liệu nằm bên trong trường.
- C6: fault tree có nhánh PII từ ticket, liên hệ từ DB đơn quà và các giả định ngoài phần mềm; ghi rõ lớp G3/legal đã có trước CP4.
- C7: giữ cơ chế chặn đã đúng; chỉ thêm telemetry tối thiểu tại `write_gate` nhánh `notify_carrier` trước khi trả `Verdict.modify`.
- C9: cây sau bổ sung, gắn lớp chặn đã có và tín hiệu quan sát mới; giữ các nhánh chưa được giải quyết, không tuyên bố mọi PII đã bị ngăn.
- Lưu report, trace chọn lọc và nhật ký trong `evidence/`; các bản sao chuẩn hóa xuống dòng LF, giữ nguyên nội dung JSON, không sửa điểm/nhãn/timestamp. Thư mục `runs/` gốc không được đưa vào Git.

## Kết quả có bằng chứng

| Mốc | Mã / file | Kết quả |
|---|---|---|
| Grade ban đầu trước sửa | R-S7-grade-20261118-163825-0892bd; evidence/initial-grade.json | FAIL do integrity/monitor; criteria, visible, regression đạt |
| S7 base ban đầu | R-S7-before-20261118-163826-0892bd | pass_rate=0.25, pass^5=0.25, PII=30 |
| S7 prepared ban đầu | R-S7-prepared-20261118-163826-0892bd | 40/40 đúng, PII=0; checkpoint 0580db3e |
| S7 sau thêm log | R-S7-after-20261118-165018-2bd310; evidence/S7-after-eval-report.json | 40/40 đúng, PII/hoàn sai/lỗi oan=0, coverage=1, chi phí5005đ, ROI1.0, không ca ùn |
| Bộ nền sau thêm log | R-base-after-20261118-165018-2bd310; evidence/base-after-eval-report.json | 110/110 đúng, không hồi quy, chi phí4456đ, ROI1.24 |
| Grade sau thêm log | R-S7-grade-20261118-165225-2bd310; evidence/current-grade.json | Vẫn FAIL: thiếu28file thẻ khác, chưa có monitor mới; không có ca S7 hỏng hoặc ops.violations |

Các run ID đầy đủ của ba mốc do grade sinh nằm trong [run-ids.json](run-ids.json). Dòng review_rate=0.125 của S7 gồm kiểm mẫu; escalation_rate thực của S7 là0.0.

## Đầu vào bàn giao cho Thông

Event mới trong `trial['events']`:

```python
{
    "type": "guard",
    "kind": "carrier_payload_minimized",
    "removed_field_count": 2,       # số khóa đề xuất bị loại, không phải số lần rò PII
    "had_customer_note": True,
    "had_recipient_contact": True,
    "carrier_corrected": False,
}
```

Đây là ví dụ hình dạng event, không phải một dòng trace được chép nguyên trạng. Không log giá trị bị loại, toàn bộ ticket, recipient, hay tên khóa không tin cậy do đầu vào tùy ý đặt. Event được phát khi G3 phải chỉnh payload/hãng; không ghi nhận event cho ticket không tới nhánh thông báo.

Số đếm thực trong hai lần eval sau thay đổi:

| Tập | Tổng trial | Event minimization | Có recipient_contact bị loại | Có customer_note bị loại |
|---|---:|---:|---:|---:|
| Bộ nền | 110 | 55 | 0 | 55 |
| S7 | 40 | 35 | 10 | 35 |

Thông có thể thiết kế monitor đếm trial có cờ recipient_contact, kèm mẫu số/độ phủ. Giá trị 10/40=0.25 và0/110=0 là dữ liệu quan sát, **không phải monitor đã được đăng ký** hoặc threshold nhóm đã chốt. Có cờ là hệ thống từng đề xuất trường không được phép và đã chặn; không được đặt tên khiến người đọc hiểu là25% thông báo đã rò. C8 và `MONITORS` vẫn do Thông phụ trách; sau khi merge phải chạy grade lại để xác minh monitor sáng đèn và không báo lỗi.

## Kiểm thử và giới hạn

Đã chạy:

```powershell
python -X utf8 -m unittest discover -s tests
python -X utf8 docs/cp3-evidence/verify_guards.py
python -X utf8 docs/cp4-nguyendacthe/verify_privacy_boundary.py
```

- 13 test công khai đạt; 8 kiểm tra biên CP3 vẫn đạt sau thêm event.
- Script CP4 có4 phép kiểm bảo vệ: payload không tin cậy không thay được facts; log mới không chứa khóa/giá trị bị loại; số tham chiếu không chặn thông báo đúng; không có lỗi hãng hợp lệ thì không gửi.
- Phép kiểm thứ5 **tái hiện giới hạn**: thay district trong world copy bằng PRIVATE-MARKER thì marker vẫn được chuyển trong trường district. Test đạt vì tái hiện đúng phản ví dụ về giả định, **không có nghĩa trường hợp này an toàn**. Không thay dữ liệu repo hay nhãn public để làm test; chưa bổ sung bộ kiểm địa danh/nguồn nhập liệu vào hệ thống.

Do đó chỉ kết luận G3 ngăn xuất các trường ngoài allowlist qua ranh giới đã kiểm dưới giả định facts/allowlist đúng; cần quản trị nguồn DB và mọi đường xuất. Không tự sửa cổng thành regex số điện thoại để che hạn chế hoặc làm hỏng ticket đối chứng chứa số.

## Vướng mắc và việc còn lại

- **Integrity:** bốn file S7 khớp hash gốc, code/data hiện có và snapshot còn nguyên; grader vẫn đòi các file S1–S6/S8 vắng mặt. [Thông tin để hỏi Coach](coach-question.md). Chưa gửi tin nhắn cho Coach hoặc sửa grader/manifest.
- **Thông:** C2/C8 và monitor mới; kiểm lại sau tích hợp event. C2/C8 trong Phiếu C chưa được viết thay.
- **Bách:** C3.3, C4, C11, xác nhận giả định/kiểm soát dữ liệu nguồn và quy trình liên hệ bên thứ ba.
- **Bảo:** C10, phần kinh doanh C1/C7, rủi ro trường DB được phép chứa dữ liệu không đúng nghĩa và chi phí vận hành thật.
- **Thể sau bàn giao:** merge các nhánh CP4, kiểm cả guard/monitor/config, chạy S7/base/grade và cập nhật C0/C7/C9 bằng report bản tích hợp. Chưa thực hiện bước này khi phần các bạn chưa được bàn giao.

Chưa chốt C12 hoặc xác nhận CP4 toàn nhóm đạt. Tiêu chí, cả hai snapshot và round1.lock giữ nguyên; không mở thẻ khác.
