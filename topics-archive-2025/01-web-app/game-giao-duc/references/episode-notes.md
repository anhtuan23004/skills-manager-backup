# Ghi chú Tập 3 — An toàn vệ sinh thực phẩm (VTV2, 29/11/2025)
Video: `D52ScLtAO2U`. Phụ đề tự động, tên đội có thể sai; tập này ít chi tiết kỹ thuật.

- **Đề:** game mobile tương tác về an toàn thực phẩm cho học sinh THCS; chạy trên web, host công khai để giám khảo chơi. 120 phút, $50 API (Gemini). "Tất cả sản phẩm âm thanh/hình ảnh phải tạo bằng API do BTC cấp." Thi online, mỗi đội một giám thị, share screen.
- **Đội nhất:** Anti Neural (3 sinh viên năm nhất), 335 điểm. Advance 319; Micro Genius 278; BVA 242; Vui Hà 226; VN Credit Trust 219; MV AI 202; Tm My AI 183; Electron 157.
- **Cách làm:**
  - Anti Neural: game phức tạp, hình nền ghép từ nhiều thành phần sinh hoàn toàn bằng AI; crawler lấy dữ liệu từ trang chính thống Việt Nam; chọn kịch bản phổ biến rồi chèn kiến thức.
  - Micro Genius: khung game sớm, mascot hạt đậu, chữ không lỗi, 3 màn khác kiểu tương tác; viết lại câu lệnh để dùng API BTC sinh âm thanh nền thay công cụ ngoài.
  - Vui Hà: "Vệ sĩ thực phẩm", mascot trâu, chỉ số sức khỏe/kiến thức. Một đội làm game chạy "Người chạy tri thức" có front/back end.
  - MV AI: hình đẹp, tương tác nhỏ, thiếu thời gian CSS. Đội chọn 3D nên hình chưa sắc nét.
- **Kỹ thuật:** sinh hình theo bộ cùng style rồi ghép (khó ở chỗ giữ style); dùng AI làm trợ lý code front+back end.
- **Lỗi:** dùng công cụ sinh nhạc ngoài (bị nhắc); vào muộn 15–20 phút; setup thiết bị; **deploy là điểm nghẽn** — 30 phút cuối nhiều đội kẹt; 2/10 đội không kịp public hosting.
- **Giám khảo:** khen đa dạng tương tác, hình đẹp, đặt mình vào người dùng, scope hợp lý. Chê thông điệp "lộ", thiếu chơi lại, thiếu hướng dẫn, bố cục sai, game quá nhẹ, linh vật gấu trúc.
- **Deploy:** giám thị nói tốn nhiều thời gian deploy hơn các bài trước; khuyên từ ~50 phút cuối chuyển sang hoàn thiện + deploy; còn ~12 phút hỏi "lên live xong chưa". Không nêu nền tảng hosting.
