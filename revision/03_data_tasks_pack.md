# Gói công việc dữ liệu (những việc cần người thật)

Các việc dưới đây là điều kiện để gỡ các ô **PENDING** trong `02_revised_manuscript.md`. Không số liệu nào trong gói này được tạo ra thay tác giả.

## A. Mã hoá độc lập lần hai (R1-6, Editor 3)

**Người làm:** một người không tham gia mã hoá lần đầu và chưa xem Bảng S1 của Supporting Information.

**Cách làm**

1. Đưa cho người này: `03a_second_coder_blind_sheet.csv` (chỉ có tên công cụ và nguồn cần đọc), Phụ lục A của bản thảo (codebook), và các văn bản gốc ở Bảng 2. **Không đưa Bảng S1.**
2. Người này mã hoá cả 20 công cụ trên 5 chiều. Lý do mã hoá cả 20 thay vì ≥8 như SI đề nghị: với số đơn vị nhỏ, kappa trên một mẫu con sẽ rất bất ổn; 20 dòng không tốn nhiều công hơn.
3. Ghi vào cột "Page/article cited" nơi tìm thấy từng con số và đánh dấu mọi quyết định không chắc.
4. Người mã hoá lần đầu và người thứ hai so sánh. Tính, **theo từng chiều**: % đồng thuận, Cohen's kappa, và Krippendorff's alpha (để đối chiếu vì số đơn vị nhỏ). Với chiều "ngưỡng chính thức" (số), coi là đồng thuận khi giá trị gốc giống nhau và quy đổi sai khác ≤5%.
5. Ghi cả đồng thuận **trước** và **sau** thảo luận. Ghi lại mọi bất đồng đã giải quyết và lý do (nhật ký quyết định).
6. Thay đoạn "Reliability" ở mục 3.3 bằng kết quả thật. Nếu kappa thấp ở một chiều, sửa codebook cho chiều đó rồi mã hoá lại, và báo cáo cả hai vòng.

## B. Xác minh nguồn của 14 dòng chưa xác minh (R1-8)

Với mỗi dòng: đối chiếu con số/điều khoản với **văn bản gốc**, ghi ngày kiểm tra, người kiểm tra, trang/điều. Dòng 10, 11, 12, 13, 19, 20 đã được SI ghi là đã verify; vẫn nên ghi ngày.

| Dòng S1 | Công cụ | Cần xác minh | Nguồn | Kết quả / ngày / người |
|---|---|---|---|---|
| 1 | TH Activity 8.1.1 | Ngưỡng ≈1,5 triệu baht chi lương địa phương; miễn thuế không giới hạn | BOI Ann. 8/2565; Guide 2025 | |
| 2 | TH R&D cơ bản | Cùng ngưỡng với dòng 1 | như trên | |
| 3 | TH competitiveness enhancement | 200 triệu baht; thời hạn 13 năm; tỷ lệ doanh thu tối thiểu; **cơ chế dành riêng cho khối Digital hay xuyên ngành?** (ảnh hưởng đến H3) | BOI Ann. 10/2565 | |
| 4 | TH 8.2.4 GPU data hosting | Vốn tối thiểu ≈5.000 triệu baht; chế độ chứng nhận | BOI Guide hiện hành | |
| 5 | TH TISO / BPO | Mức ưu đãi thấp nhất, không miễn thuế | BOI Guide 2025 | |
| 6 | TH smart-logistics (quy tắc nhân sự) | ≥20% nhân sự kỹ thuật/AI/dữ liệu | BOI Guide 2025 | |
| 7 | VN research-centre track | 60% / 70% nhân sự R&D; 65–70% chi R&D trên ngân sách | Decree 260/2026 | |
| 8 | VN startup track Art. 11 | Điều 11; tiêu chí doanh thu tăng trưởng hoặc công nghệ sẵn sàng thương mại hoá | Decree 260/2026 | |
| 9 | VN National Venture Capital Fund | Phân biệt với NATIF (cho vay ưu đãi) | Decree 260/2026 | |
| 14 | MY Malaysia Digital | RM50.000 vốn đã nộp; xác nhận kiểm toán độc lập hằng năm | MDEC Guidelines 2024 | |
| 15 | MY DESAC entry | RM2,5 triệu vốn đã nộp | MIDA DESAC 2022 | |
| 16 | MY DESAC full tier | RM1 tỷ chi tiêu vốn luỹ kế | MIDA DESAC 2022 | |
| 17 | MY DESAC quy tắc nhân sự | ≥50% nhân sự toàn thời gian là người Malaysia; **mức lương cụ thể** (hiện chưa xác định) | MIDA DESAC 2022 | |
| 18 | PH đăng ký tiêu chuẩn | SIPP: cách xử lý AI so với hạ tầng data centre; **phiên bản và ngày của SIPP** | RA 12066; IRR; SIPP | |

Các mục xác minh ngoài bảng (SI §4):

* Thống kê BOI 2025 theo hoạt động nhỏ: số dự án, vốn, tỷ lệ sở hữu Thái/nước ngoài (96 dự án/933,0 triệu baht; 24 dự án/457.999,8 triệu baht; 1 dự án/126.793,0 triệu baht; 46/54, 15/85, 0/100).
* Malaysia: phát biểu ngân sách 2025, **tên người, ngày, nguyên văn** (hiện SI ghi chưa xác nhận đúng người và ngày).
* Vietnam: số liệu White Book 2024 (<10% doanh nghiệp, >90% doanh thu) và Niên giám 2024 (9.348 doanh nghiệp; 57,9%; 35,7%).
* Vietnam: tên Luật AI 2025 (số 134/2025/QH15), ngày có hiệu lực.
* Tỷ giá: ghi ngày và tỷ giá dùng cho mỗi đồng tiền (THB, MYR, PHP).
* Trích dẫn kỹ thuật ở mục 5.1: định nghĩa hyperscale 40 MW; 12 kW cho máy chủ 8 GPU; điều khoản colocation 5–20 kW.

## C. Giao thức tìm kiếm cho khẳng định "không có công cụ dưới quy mô facility" (C-5, R3-5)

Điền cho **mỗi nước**:

| Mục | Ghi |
|---|---|
| Danh sách công cụ đã đọc toàn văn (tên, số hiệu, ngày) | |
| Từ khoá tìm trong bản tiếng Anh và bản tiếng bản địa | colocation, co-location, cloud service, compute, GPU, shared infrastructure, modular, edge, resale, leased capacity, data center / data centre / trung tâm dữ liệu / ศูนย์ข้อมูล / pusat data / data center (Filipino dùng tiếng Anh) |
| Ngày tìm | |
| Người tìm | |
| Công cụ gần nhất với compute dưới quy mô facility (nếu có) và vì sao không áp dụng | |
| Kết luận: có / không có | |

## D. Mã hoá công cụ chung (SME, startup, nghiên cứu) (R3-5)

Mục tiêu: kiểm tra xem một nhà cung cấp colocation hoặc bán lại compute nhỏ có thể dùng công cụ nào không mang nhãn AI. Dùng đúng 5 chiều của Phụ lục A. Mẫu:

| Nước | Công cụ chung | Cơ quan | Tầng (cross-cutting) | Cơ chế | Ngưỡng | Ưu đãi cho doanh nghiệp mới/nhỏ | Gánh nặng tuân thủ | Một nhà cung cấp compute nhỏ có đủ điều kiện không? Vì sao | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| Thailand | (ví dụ: chương trình hỗ trợ SME / startup chung của BOI hoặc cơ quan khác) | | | | | | | | |
| Vietnam | (ví dụ: chương trình hỗ trợ doanh nghiệp nhỏ và vừa, đổi mới sáng tạo) | | | | | | | | |
| Malaysia | | | | | | | | | |
| Philippines | (ví dụ: ưu đãi MSME) | | | | | | | | |

Các ví dụ trong ngoặc chỉ để gợi ý loại công cụ cần tìm. Tên và số hiệu thực phải do người mã hoá tìm trong nguồn, không dùng các ví dụ này làm dữ liệu.

## F. Kiểm tra văn bản có thẩm quyền và còn hiệu lực (R2-6)

Với **mỗi** nguồn ở Bảng 2, điền:

| Nguồn | Phiên bản có hiệu lực vào ngày mã hoá | Có sửa đổi, hợp nhất, bãi bỏ trong danh mục công bố của cơ quan ban hành không? (liệt kê) | Có văn bản hướng dẫn, thông tư thi hành làm đổi cách hiểu điều khoản đã mã hoá không? | Điều khoản đã mã hoá có bị ảnh hưởng không? | Ngày kiểm tra / người kiểm tra |
|---|---|---|---|---|---|
| BOI Ann. 8/2565, 9/2565, 10/2565 và Guide 2025 | | | | | |
| Decree 260/2026/ND-CP | | | | | |
| Decision 21/2026/QD-TTg (thay Decision 1131/QD-TTg năm 2025) | | | | | |
| MDEC Guidelines 2024 | | | | | |
| MIDA DESAC Guidelines 2022 | | | | | |
| RA 12066 | | | | | |
| FIRB Advisory 001-2025 và IRR | | | | | |

Quy tắc: kiểm tra trên trang công bố chính thức của cơ quan ban hành (không dùng tin báo chí hay tóm tắt của hãng luật). Đồng thời ghi **quy tắc chọn công cụ vào mẫu** cho từng nước: danh sách chương trình của cơ quan nào đã đọc, và tiêu chí nhận một công cụ vào mẫu (đang có hiệu lực trong giai đoạn nghiên cứu; nêu AI, cloud, trung tâm dữ liệu hoặc hoạt động số là hoạt động đủ điều kiện hoặc ưu tiên, hoặc đặt điều kiện cho chương trình đăng ký hoạt động đó).

## E. Việc cần quyết định của tác giả (không thể điền thay)

1. Lý do loại Indonesia (mục 3.1).
2. Tên người mã hoá thứ hai và thời gian.
3. Xác nhận rằng bài vẫn chưa nộp ở tạp chí khác và rằng tác giả đã đồng ý nộp cho tạp chí mới.
4. Xác nhận cách các nguồn (Ke 2024, Zheng 2024, Bahar et al. 2026, Bianchi et al. 2024) đo hoặc phân loại trap, để điền các ô VERIFY ở §2.1 và §3.1 (R2-2, R2-5).
