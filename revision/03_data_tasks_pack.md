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


## G. Kết quả tra cứu bản mới của Malaysia (9/10/2026): các nguồn chính thức đã đọc

Các file này tôi đã tải và đọc toàn văn; các dòng SI dưới đây cần cập nhật theo chúng.

| Nguồn | Link | Ghi chú |
|---|---|---|
| MIDA, Guidelines and Procedures for the Application of DESAC (bản đăng 12/2024, đơn nhận đến 31/12/2027) | https://www.mida.gov.my/wp-content/uploads/2024/12/DESAC-Guideline_MIDA.pdf | Thay bản 2022 |
| Guideline for Sustainable Development of Data Centre (12/2024) | https://www.mida.gov.my/wp-content/uploads/2024/12/Guideline-for-Sustainable-Development-of-Data-Centre.pdf | Danh mục cơ sở nhỏ nhất: 0,85 MW |
| MIDA, New Incentive Framework (NIF) và FAQ (2026) | https://www.mida.gov.my/media-release/new-incentive-framework-nif/ | Sản xuất từ 1/3/2026; dịch vụ từ Q2/2026 (ngày chưa công bố); FAQ câu 20: DESAC vẫn mở đến hết hạn |
| MDEC, Guidelines on MD Tax Incentive, New Investment (sửa 22/7/2025) | https://www.mdec.my/announcement/md-tax-incentive-revised-guidelines | Thay bản 2024; vốn đã nộp RM50.000; tự khai hằng năm có kiểm toán độc lập do công ty trả |

Cập nhật cho SI:

* **Dòng 14 (MD tax incentive):** RM50.000 vốn đã nộp và bản tự khai hằng năm có kiểm toán độc lập, công ty trả chi phí, **đã được xác nhận** với hướng dẫn MDEC bản 7/2025. Cần ghi thêm: phải có MD Status, hoạt động mới (chưa xuất hóa đơn trước khi nộp đơn), "cloud" là một công nghệ thúc đẩy được ưu tiên, nhân viên tri thức lương cơ bản tối thiểu RM5.000/tháng.
* **Dòng 15 và 16 (DESAC):** RM2,5 triệu vốn đã nộp là điều kiện tối thiểu chung cho **cả hai bậc** (Tier 1 và Tier 2); hai bậc khác nhau ở điều kiện kết quả, không khác ở vốn. RM1 tỷ chi tiêu vốn luỹ kế là điều kiện của **năm thứ sáu đến mười**. Doanh nghiệp hiện hữu: thêm điều kiện RM300 triệu trong năm năm.
* **Dòng 17 (nhân sự):** nay đã biết con số: lao động Malaysia toàn thời gian lương cơ bản tối thiểu RM5.000/tháng, chiếm ít nhất 50% tổng nhân lực; "việc làm giá trị cao" từ RM10.000/tháng.
* **Thêm dòng mới:** hạng mục cơ sở nhỏ nhất trong Guideline for Sustainable Development of Data Centre (0,85 MW đến dưới 4,25 MW, điện áp thấp 11 kV); ưu đãi DESAC chỉ áp dụng cho chi tiêu vốn đủ điều kiện **không gồm đất**; phải nộp đơn trước khi bắt đầu dự án và được Ủy ban Đầu tư Quốc gia duyệt.
* **Thailand (nguồn thứ cấp, chưa phải văn bản BOI):** Activity 8.2.4 tối thiểu THB 5 tỷ **không gồm đất và vốn lưu động**, hệ thống điện tối thiểu 2 MW, tối thiểu hai trung tâm dữ liệu đạt ISO/IEC 27001 tại Thái Lan; Activity 8.2.1 bậc cao cần PUE ≤1,3 và tải IT ≥2 MW; Activity 8.2.2 (dịch vụ đám mây) tồn tại. Hàng 4 và ô "Thailand cloud: không có riêng" trong SI cần sửa sau khi đọc thông báo BOI gốc. Tìm: https://www.tilleke.com/insights/thailand-announces-new-investment-incentives-for-data-hosting/ (bản tóm tắt của hãng luật, không phải nguồn gốc).

Việc còn lại cho Malaysia: hỏi hoặc tìm thực tiễn của MDEC về việc "cung cấp năng lực tính toán như một dịch vụ" có được chấp nhận là hoạt động Malaysia Digital hay không (câu hỏi quyết định cho kết quả của bài), và đo chi phí kiểm toán so với RM50.000.


## H. Kết quả đọc văn bản gốc của Thailand (BOI) và Vietnam (Nghị định 260/2026), 9/10/2026

**BOI là gì:** Board of Investment of Thailand, cơ quan xúc tiến đầu tư của Chính phủ Thái Lan, cấp ưu đãi thuế cho các dự án đầu tư đủ điều kiện theo danh mục hoạt động được khuyến khích.

| Nguồn | Link | Ghi chú |
|---|---|---|
| BOI, Investment Promotion Guide 2026 (193 trang; danh mục toàn bộ hoạt động và điều kiện) | https://www.boi.go.th/upload/content/BOI_A_Guide_EN.pdf | Thay Guide 2025 trong bài; phần 8 là ngành số |
| BOI, Announcement No. Sor. 9/2568 (14/11/2025), điều kiện trung tâm dữ liệu 8.2.1 (bản dịch không chính thức) | https://www.boi.go.th/upload/content/sor9_2568EN.pdf | Sửa 9/2565 và Sor. 5/2568; cần đối chiếu bản gốc tiếng Thái và Công báo |
| BOI, tài liệu giới thiệu ngành số (4/8/2026) | https://www.boi.go.th/upload/content/20260804%20BOI%20EN.pdf | Tóm tắt |
| BOI, thông cáo báo chí số 67/2569 (6/5/2026) | https://www.boi.go.th/upload/content/PR67_2569EN.pdf | Phê duyệt 958 tỷ baht, ba dự án trung tâm dữ liệu |

Các điều chỉnh cho SI (Thailand):

* **Hàng 1 (8.1.1):** ngưỡng 1,5 triệu baht/năm tính trên lương nhân sự IT Thái được tuyển thêm: **đúng**. Nhưng ưu đãi **không "không giới hạn"**: nhóm A2, miễn thuế TNDN 8 năm, trần bằng 100% chi phí đủ điều kiện (lương, nhân sự thời vụ, đào tạo, chi phí chứng chỉ ISO 29110/CMMI). Cần sửa.
* **Hàng 3 (Competitiveness Enhancement):** là biện pháp **xuyên ngành** (Announcement 10/2565), áp dụng mọi nhóm hoạt động; điều kiện là chi cho R&D, cấp phép công nghệ nội địa, phát triển nhân lực, phát triển nhà cung ứng địa phương từ 1% doanh thu 3 năm đầu (hoặc 200 triệu baht, lấy mức thấp hơn) trở lên cho thêm 1 năm miễn thuế, đến 5% (hoặc 1.000 triệu baht) cho thêm 5 năm; tối đa 13 năm. Không phải "200 triệu baht cố định".
* **Hàng 4 (8.2.4):** tách hai: 8.2.4.1 (dịch vụ cho thuê thiết bị tính toán có năng lực xử lý cao như GPU, nhóm A2) và 8.2.4.2 (dịch vụ lưu trữ khác, nhóm A3); cả hai: ≥5.000 triệu baht **không gồm đất và vốn lưu động**, đặt tại ít nhất hai trung tâm dữ liệu đạt ISO/IEC 27001 tại Thái Lan, kế hoạch lợi ích cho Thái Lan.
* **Thêm hàng mới:** 8.2.1.1 và 8.2.1.2 (trung tâm dữ liệu): cả hai cần hệ thống điện cho tải IT ≥2 MW; 4 tuyến viễn thông; ISO/IEC 27001; ≥50% vị trí điều hành/chuyên gia là người Thái trong 3 năm; PUE ≤1,3 chỉ cho bậc cao. **8.2.2 (dịch vụ đám mây, nhóm A2): không có vốn tối thiểu**; đặt tại ≥2 trung tâm dữ liệu ISO 27001, kết nối ≥10 Gbps có dự phòng, ISO/IEC 27001 (bảo mật đám mây) và ISO/IEC 20000-1.
* **Hàng 5 (TISO, hoạt động 10.1.1):** nhóm B (không miễn thuế TNDN); chi bán hàng và quản lý hằng năm ≥10 triệu baht; phạm vi gồm cả BPO quốc tế qua mạng viễn thông: **đúng** như bản thảo.
* **Ô "Thailand cloud: không có riêng":** **sai**; có hoạt động 8.2.2.

Các điều chỉnh cho SI (Vietnam, từ toàn văn Nghị định 260/2026/NĐ-CP, ban hành 30/6/2026, hiệu lực 1/7/2026, thay Nghị định 10/2024):

* **Hàng 7:** trung tâm R&D công nghệ cao: ≥60% lao động làm R&D (≥85% đại học trở lên, ≥10% thạc sĩ trở lên), chi R&D ≥65% chi hoạt động hằng năm; công nghệ chiến lược: 70%, 85%, 20% (trong đó ≥5% tiến sĩ), 70% (Điều 8). **Đúng**, nay đã có số chi tiết.
* **Hàng 8:** điều kiện doanh nghiệp khởi nghiệp công nghệ cao (Điều 11): R&D thuộc danh mục; tăng trưởng doanh thu bình quân ≥20%/năm trong 2 năm liên tiếp (doanh nghiệp ≥3 năm tuổi) **hoặc** công nghệ/sản phẩm sẵn sàng chuyển giao hoặc thương mại hoá có kết quả thử nghiệm và phương án khả thi; khả năng mở rộng thị trường. Ủy ban nhân dân cấp tỉnh xác nhận trong 40 ngày; hiệu lực 5 năm; báo cáo hằng năm; kiểm tra sau 12 tháng rồi mỗi 2 năm.
* **Hàng 9:** Quỹ đầu tư mạo hiểm quốc gia: **được ưu tiên xem xét** đồng đầu tư, đầu tư, bảo lãnh, hỗ trợ kỹ thuật; **NATIF hỗ trợ lãi suất vay (70% lãi suất hợp đồng, tối đa 8%/năm, tối đa 5 năm; công nghệ chiến lược 100%, tối đa 10%)**, không phải cho vay trực tiếp như SI ghi.
* **Thêm hàng mới:** tiêu chí doanh nghiệp công nghệ cao nhóm 1 và 2 (Điều 14, 15) với các bậc vốn VND 100 tỷ và 6.000 tỷ (tỷ lệ R&D 0,5%/1%/2%; lao động R&D 1%/2,5%/5%); hỗ trợ hạ tầng công nghệ (gồm hạ tầng tính toán và dữ liệu; Điều 3, 4(6), 5(6)); ưu tiên dự án khu công nghệ cao có suất vốn đầu tư trên diện tích cao hơn trung bình (Điều 26).
* **Thông tư thi hành cần đọc:** 38/2026/TT-BKHCN, 40/2026/TT-BKHCN, 42/2026/TT-BKHCN, 48/2026/TT-BKHCN, 49/2026/TT-BKHCN; Nghị định 20/2026/NĐ-CP (chính sách khởi nghiệp), 264/2025/NĐ-CP (quỹ đầu tư mạo hiểm quốc gia).
* **Chưa có:** Quyết định 21/2026/QĐ-TTg (danh mục công nghệ chiến lược: mục "nền tảng điện toán đám mây"). Anh/chị gửi văn bản này tương tự (từ Thư viện Pháp luật) thì tôi đối chiếu tiếp. Văn bản trên Thư viện Pháp luật là cơ sở dữ liệu thương mại, không phải Công báo.
