# Danh sách việc trước khi nộp lên Innovation and Development

Nguồn yêu cầu: Instructions for Authors của tạp chí (trang tandfonline.com, đọc ngày 9/10/2026).

## Yêu cầu của tạp chí và tình trạng

| Yêu cầu | Tình trạng |
|---|---|
| Tối đa 8.000 từ, gồm bảng, tài liệu tham khảo, chú thích hình | **Đạt**: 7.882 từ (đếm trong docx, gồm chỗ giữ chỗ); bản cũ dài 17.800 từ nên đã rút gọn, chi tiết chuyển sang Supporting Information |
| Phản biện kín hai chiều (double blind) | Bản `06_submission_manuscript` không có tên tác giả; trang tựa đề tách riêng ở `06a_title_page`. Cần kiểm lại thuộc tính file docx (File, Info) xoá tên tác giả trước khi tải lên |
| Tóm tắt không cấu trúc, 200 từ | 196 từ |
| 5 đến 6 từ khoá | 6 từ khoá |
| Định dạng tự do, một kiểu trích dẫn nhất quán (T&F áp kiểu Chicago tác giả-năm sau khi chấp nhận) | Đang dùng tác giả-năm; nhất quán |
| Hình 300 dpi màu | `fig1_threshold_ladder.png` là 300 dpi |
| Bảng sửa được | Bảng là bảng Word |
| Chính tả Anh hoặc Mỹ, nhất quán | Anh |
| Số liệu ghi theo đơn vị SI | Dùng MW, kW |
| Vai trò CRediT, tài trợ, tuyên bố xung đột lợi ích | Điền ở cổng nộp và trang tựa đề |
| **Tuyên bố sử dụng AI tạo sinh** | **Bắt buộc.** Đã điền theo lời bạn (AI chỉ polish văn phong, tác giả duyệt và chịu trách nhiệm). Cần tác giả xác nhận câu này mô tả đủ mọi cách đã dùng AI, và ghi tên công cụ nếu tạp chí hỏi |

## Chỗ giữ chỗ còn lại trong bản nộp (tìm "AUTHORS TO COMPLETE" và "CITATION")

1. **Lý do loại Indonesia** (mục 3.1). Người đọc sẽ hỏi.
2. **Kết quả người mã hoá thứ hai** (mục 3.2): phần trăm đồng thuận, kappa Cohen theo từng chiều, các bất đồng đã giải quyết. Dùng `03a_second_coder_blind_sheet.csv` (29 dòng).
3. **Nguồn cho 12 kW của một máy chủ 8 GPU** (mục 3.2): thêm datasheet của hãng.
4. Lời cảm ơn, tuyên bố xung đột lợi ích, tài trợ (cuối bản thảo, và trang tựa đề).
5. Tên đồng tác giả, nếu có (trang tựa đề). Trang tựa đề hiện điền sẵn Quang-Vinh Dang theo thông tin nghiên cứu của bạn; đổi nếu bài này dùng thông tin khác.

## Những điều bản nộp nói thẳng là chưa làm (mục 3.2, 5.1, 7)

* Chưa đọc: bản gốc tiếng Thái và công báo của thông báo BOI; các thông tư thi hành của Việt Nam; hướng dẫn điều kiện của SIPP 2026.
* Giả định A1 đã được thử bằng mô hình hoà vốn (Table S5, `08a_viability_model.py`) nhưng chỉ dựa trên giá từ blog nhà cung cấp và danh sách đại lý. Kết quả: khả thi chỉ khi bán được gần 3 USD/GPU-giờ trở lên. Muốn mạnh hơn: dữ liệu giá mà nhà cung cấp nhỏ khu vực thực sự nhận được.
* Chưa xác nhận MDEC có chấp nhận bán lại năng lực tính toán là hoạt động MD hay không (mục 4.3). Nếu không, bằng chứng E2 đổi sang "tương thích".
* Chưa mã các chương trình chung (SME, khởi nghiệp, nghiên cứu) và các chương trình trước thời AI.
* Tỷ giá ghi gần đúng; nên ghi nguồn và ngày trước khi nộp.

## Việc nên làm trước khi bấm nộp

1. Người thứ hai mã 29 dòng, điền kết quả vào mục 3.2.
2. Điền các chỗ giữ chỗ ở trên; đọc lại câu "one author coded" ở mục 3.2 và mục 7 cho khớp thực tế.
3. Đọc bản gốc tiếng Thái của Sor. 9/2568 và hỏi BOI về 8.2.2 hay 8.2.4.1 cho nhà cung cấp GPU nhỏ (một email là đủ).
4. Nếu có thời gian: lấy dữ liệu giá thật của nhà cung cấp GPU nhỏ trong khu vực (báo giá, hợp đồng), vì A1 hiện chỉ đúng có điều kiện.
5. Bản dài `02_revised_manuscript.md` chưa cập nhật theo kết quả A1; dùng `06_submission_manuscript` làm bản chính.
