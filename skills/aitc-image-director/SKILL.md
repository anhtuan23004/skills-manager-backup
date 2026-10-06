---
name: aitc-image-director
description: Thiết kế hướng thị giác, prompt và kiểm tra ảnh theo đề; dùng cho poster, key visual, bộ ảnh hoặc frame cho video.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 06 — Chỉ đạo hình ảnh

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Brief; concept; tỷ lệ/kích thước từ đề; danh sách text chuẩn; nguồn hình/nhân vật được phép.

## Quy trình
1. Viết visual brief tối đa 8 dòng: thông điệp, chủ thể, bối cảnh, bố cục, màu/ánh sáng, khoảng trống, vùng chữ, điều phải tránh.
2. Mỗi ảnh có một trọng tâm. Gắn các lựa chọn thị giác với thông điệp, không viết mỹ từ thay quyết định cụ thể.
3. Bộ nhiều ảnh có consistency sheet: đặc điểm nhân vật, vật dụng, trang phục, style, palette, môi trường cố định. Tham chiếu phải được tạo trong phiên hoặc được BTC cho phép.
4. Prompt tách subject / context / composition / visual language / lighting / constraints. Negative instruction trong prompt không có nghĩa API hỗ trợ một field negative_prompt.
5. Chỉ dùng tham số đã được Gateway xác nhận; không tự thêm seed, reference array hay image editing endpoint vì nhà cung cấp gốc có hỗ trợ.
6. Tạo một mẫu nhỏ trước, xem ảnh thật. Kiểm tra hình thể, chữ, chi tiết văn hóa, logo vô ý, thông điệp, khả năng đọc ở kích thước cuối.
7. Tạo phiên bản sửa có kiểm soát; giữ bố cục đã đạt. Chữ tiếng Việt quan trọng kiểm tra từng ký tự; dùng lớp chữ biên tập nếu được phép.
8. Lưu prompt, model, input reference, output ID, phiên bản được chọn và lý do. Không ghi một ảnh là đúng chỉ vì prompt đã yêu cầu đúng.

## Công cụ và kiểm chứng theo task

Đọc [Image guide](../../docs/api-guides/03-image-generation.md) và [hướng dẫn thực thi](../../docs/SKILL_EXECUTION.md). Gọi endpoint tạo ảnh qua Gateway BTC theo schema được cung cấp; giải mã base64 và lưu ảnh vào workspace. Mở ảnh thực tế để kiểm tra và ghi bằng chứng theo requirement.

## Đầu ra bắt buộc
image-brief.md; prompt-Sxx.md; ảnh vNN; review vị trí lỗi; asset manifest.

## Kiểm tra trước khi trả kết quả
Không dùng canvas-design nguyên bản để đặt sáng tạo cao hơn brief. Không dùng AI tích hợp Canva/Photoshop. Không đưa font file của nguồn tham khảo vào bộ toolkit.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
