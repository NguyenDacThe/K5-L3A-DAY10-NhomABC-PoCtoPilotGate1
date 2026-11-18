# TEAM · NhomABC

## Thông tin và thành viên

- Tên nhóm: `NhomABC` · Lớp: `L3A`.
- Repo: https://github.com/NguyenDacThe/K5-L3A-DAY10-NhomABC-PoCtoPilotGate1
- Thẻ được giao: **S7**. Chỉ dùng `incidents/S7/`; không lấy hoặc làm thẻ khác.
- Tài liệu chung Lab 9: [PRD v1.1](docs/lab9/PRD_v1.1.md), [eval card](docs/lab9/eval_card.md); [nguồn và giới hạn](docs/lab9/README.md).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
|---:|---|---|---|:---:|
| 1 | Nguyễn Đắc Thể | 2A202603529 | Kỹ sư cổng, điều phối và tích hợp | Có |
| 2 | Trương Văn Thông | 2A202603560 | Kiểm thử, trace và monitor | |
| 3 | Phan Gia Bảo | 2A202603562 | Sản phẩm và kinh doanh | |
| 4 | Nguyễn Tuấn Bách | 2A202603596 | Vận hành và pháp lý | |

## Hồ sơ chung cuối buổi

| Mốc | Bằng chứng |
|---|---|
| Ký tiêu chí trước đánh giá | `60fbf2c`; signed_at `2026-11-18T15:15:34`; hash `36863666…`; không sửa sau ký |
| Chốt vòng 1 | Checkpoint `0580db3e`; hai snapshot và `round1.lock` còn nguyên |
| Quyết định v1 và v2 | **Cải tiến thêm**; xem [B8](templates/form-b-evaluation-gates.md#b8) và [C12](templates/form-c-incident.md#c12) |
| Grade sau chạy thử demo CP5 | `R-S7-grade-20261118-173554-d5f014`; S7 after 40/40, nền 110/110, không hồi quy; không có PII trên mẫu after |
| Trạng thái grade | Criteria/visible/regression/monitor đạt; tổng **FAIL** vì 28 đường dẫn thẻ không được giao vắng mặt. Mọi file hiện có khớp hash; không sửa grader/manifest để làm xanh |
| CP5 | Đã chuẩn bị demo, chạy thử kỹ thuật, soát checklist và gom hồ sơ; xem [checklist cuối](docs/cp5/checklist.md) |

Đóng góp bên dưới được rút từ commit, phiếu và report, không phải xác nhận từng người tự chạy mọi lệnh. Theo yêu cầu trưởng nhóm, **Codex thực hiện phần hoàn thiện CP5 cho cả bốn vai**. Exit ticket của Thông/Bảo được rút gọn từ nội dung đã có; phần của Thể/Bách được soạn hoặc chuẩn hóa từ bằng chứng để cá nhân rà soát. Không tự xác nhận đã demo trước lớp, được Coach phê duyệt, hoặc đã nộp LMS.

## NguyenDacThe-2A202603529

### Phần việc và đóng góp

- CP2: phối hợp metric chọn chính sách, soát tiêu chí và tổ chức ký; hỗ trợ A2–A5, giữ tiêu chí nguyên vẹn.
- CP3: chạy baseline/gate, viết G1–G3 ngoài model, điền B0–B1/B7.1, tích hợp cấu hình và chốt prepared; quyết định v1 dựa cả bằng chứng tải dồn.
- CP4: C0–C1/C5–C7/C9; thêm telemetry G3 chỉ ghi số đếm/cờ, tích hợp monitor, hồ sơ và C12, giữ các giới hạn dữ liệu nguồn và integrity.
- CP5 (Codex thực hiện thay): tổng hợp bản cuối, kiểm tính nhất quán C12/submission, chạy thử demo và chuẩn bị đẩy bài.

### Bằng chứng

Commit `4382f2d` (CP3), `d634d3e` (CP4), `1bbad85` (tích hợp/C12); [hồ sơ CP4](docs/cp4-nguyendacthe/README.md), [report CP5](docs/cp5/evidence/grade-report.md).

### Dùng AI

Codex hỗ trợ đọc repo/trace, soạn phiếu, viết và kiểm cổng/telemetry, tích hợp, kiểm thử và hoàn thiện CP5. Không xử lý riêng theo ID ticket/seed; không sửa tiêu chí hoặc snapshot để hợp thức hóa số đo.

### Exit ticket · bản soạn để cá nhân rà soát

- Điều học được từ phần việc: cần tách base, prepared và after để chứng minh cổng có trước sự cố đã đỡ được gì; report đẹp không thay quyết định khớp các điều kiện vận hành.
- Điều còn chưa chắc: dữ liệu nhạy cảm có thể nằm ngay trong trường DB được phép; cần kiểm nguồn dữ liệu và mọi đường xuất trước pilot thật.

## TruongVanThong-2A202603560

### Phần việc và đóng góp

- CP2: A2 câu 1.3, `policy_version_error_rate`, nguồn nhãn theo ngày hiệu lực, mẫu số và ca không đánh giá được.
- CP3: B2 trace T-002@55, B7.2 chống rò dữ liệu đánh giá, B7.3 hai ticket hiểm và kiểm hồi quy. Kết quả lỗi trước sửa đã được giữ và chạy lại đạt sau tích hợp.
- CP4: C2 phân biệt PII từ ticket với liên hệ từ DB; C8 và hai monitor `carrier_unexpected_field_rate`/`carrier_contact_field_rate`, chỉ đọc outbound không có nhãn; 9 kiểm tra monitor.
- CP5 (Codex thực hiện thay): kiểm thử bản cuối, chạy thử ca ba mốc và hai ticket hiểm, lưu output để demo/phản biện.

### Bằng chứng

Commit `2ea029f` (CP3), `91ea2ca` (CP4); [bàn giao monitor](docs/cp4-thong.md), [kịch bản demo](docs/cp5/demo.md), [kiểm thử cuối](docs/cp5/evidence/monitor-tests.txt).

### Dùng AI

Theo khai báo trong nhánh cá nhân, dùng Codex hỗ trợ đọc dữ liệu/code, trace, thước đo, ticket kiểm thử, monitor và ghi bằng chứng; Codex tiếp tục hoàn thiện CP5 theo yêu cầu trưởng nhóm. Monitor phát hiện sau gửi, không tự nhận là biện pháp ngăn hay thu hồi dữ liệu.

### Exit ticket · rút gọn từ ghi chú cá nhân

- Điều học được: dữ liệu có thể tự đi từ DB ra ngoài dù ticket không có PII; vi phạm schema và bằng chứng lộ PII là hai tín hiệu khác nhau.
- Điều còn chưa chắc: PII trong giá trị trường được phép hoặc kênh ngoài outbound có thể không hiện ở hai monitor; cần kiểm dữ liệu thật và chất lượng telemetry.

## PhanGiaBao-2A202603562

### Phần việc và đóng góp

- CP2: A1 câu 1.1, A3/A4, bản nháp ngưỡng và hành động; các ngưỡng số giữ trong bản ký. Phát hiện vấn đề CRLF/LF của file tiêu chí, không tự sửa lock.
- CP3: B3 bản đồ dữ liệu/drift, B6 phần kinh doanh, B7.4; cap tự động 1.600.000đ, ngân sách máy 1.500đ, phạm vi all và ROI tối thiểu 0,5, có lý do từ dữ liệu.
- CP4: phần kinh doanh C1/C7 và C10; chỉ ra ROI/chi phí đạt vẫn có thể che 30 lần lộ PII, cùng rủi ro phí người trực khi lượng ticket thấp và nhóm kho chưa xác định.
- CP5 (Codex thực hiện thay): đối chiếu số cuối với tiêu chí, giữ v2 Cải tiến thêm và chuẩn bị lập luận demo về ROI, độ phủ và hàng chờ.

### Bằng chứng

Commit `1817d93` (CP2), `964aae9` (CP3), `989d5cb` (CP4); [C1/C7/C10/C12](templates/form-c-incident.md#c1), [tóm tắt quyết định](docs/cp5/demo.md).

### Dùng AI

Theo khai báo cá nhân, Claude hỗ trợ nháp tiêu chí, phân tích dữ liệu, phần kinh doanh và phát hiện lệch CRLF/LF. Codex hỗ trợ rà soát/tích hợp bản chung và thực hiện CP5. Ngưỡng và quyết định phải được nhóm hiểu, giải thích và chịu trách nhiệm; không coi AI là phê duyệt kinh doanh.

### Exit ticket · rút gọn từ ghi chú cá nhân

- Điều học được: viết ngưỡng cùng hành động trước khi xem kết quả; trần hoàn sai, lỗi hãng oan và PII phải được đọc riêng trước ROI/pass_rate.
- Điều còn chưa chắc: chi phí 6.000đ/ticket và escalation tối đa 0,25 có còn phù hợp khi tăng tải hoặc REFUND-v4 hạ hạn mức tự hoàn xuống 100.000đ hay không.

## NguyenTuanBach-2A202603596

### Phần việc và đóng góp

- CP2: mục tiêu của Oanh/Hạnh và telemetry A2 câu 1.4; tác động lên người duyệt và bên thứ ba.
- CP3: HAZOP/checklist B4–B5, khối operations/legal và runbook B7.5–B7.6; phân tích giới hạn năng lực giờ cao điểm.
- CP4: C3.3 lòng tin người đặt/người nhận, C4 HAZOP kênh notify_carrier và C11 checklist/runbook; phần cập nhật vận hành C7 và tên monitor ở commit mới được đối chiếu khi hoàn thiện hồ sơ.
- CP5 (Codex thực hiện thay): bổ sung mục cá nhân còn thiếu, soát chín nhóm checklist, runbook, thông tin bốn thành viên và bản gom bài nộp.

### Bằng chứng

Commit `2f11502` (CP2), `a810352` (CP3), `8dd380e` (CP4 đã merge); nguồn bổ sung mục cá nhân `1819afd` và cập nhật vận hành `1143577` trên nhánh bach. Nội dung cuối xem [C3.3/C4/C11](templates/form-c-incident.md#c3) và [checklist CP5](docs/cp5/checklist.md); không ghi hai commit bổ sung là đã được merge nếu lịch sử chưa có.

### Dùng AI

Theo khai báo trong cập nhật nhánh bach, Claude Code hỗ trợ đọc repo/thẻ S7, trace chẩn đoán, nháp phần vận hành/pháp lý và thử tích hợp. Codex chuẩn hóa mục cá nhân, soát bản chung và thực hiện CP5. Các mốc phản ứng 15 phút/24 giờ là đề xuất vận hành, không tự nhận là nghĩa vụ pháp lý đã xác minh.

### Exit ticket · bản nháp từ nhánh cá nhân đã chuẩn hóa

- Điều học được: chỉ số kinh doanh có thể đạt trong khi bên thứ ba vẫn chịu lộ thông tin; allowlist phải đi cùng trách nhiệm vận hành và kiểm soát nguồn dữ liệu.
- Điều còn chưa chắc: cổng đúng trên mock chưa chứng minh đủ PII thật, kênh ngoài hệ thống hoặc nghĩa vụ thông báo; cần Pháp chế xác nhận và diễn tập trước pilot.
