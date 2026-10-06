# Ghi chú thực hiện (rút từ mùa 2025)

Đây là quan sát từ chương trình, không phải luật BTC. Đề và quy định BTC luôn thắng. Nguồn chi tiết: [INSIGHTS](../docs/INSIGHTS_VTV_2025.md), [api-guides](../docs/api-guides/README.md).

## Làm khi nhận đề

| ID | Việc cần làm |
|---|---|
| L1 | Cần link online thì lên skeleton thật trước ~T+35, chốt tính năng ~T+70, một người riêng lo deploy ([DEPLOY](../docs/DEPLOY.md)). |
| L2 | Ảnh/video AI sinh **không chữ**; chữ tiếng Việt chèn bằng HTML/code. Xem từng trang ở kích thước thật. |
| L3 | Mỗi nhân vật có một ảnh tham chiếu và một giọng cố định; lặp lại cùng mô tả trong mọi prompt; thử một đoạn trước. |
| L4 | Mỗi số liệu/điều khoản có nguồn chính thống và đúng năm; ghi vào `templates/claims.csv`; chưa kiểm chứng thì đánh UNVERIFIED. |
| L5 | Smoke test trước T+10; bản chạy được đầu tiên trước T+45; không đổi hướng sau T+60. |
| L6 | Mỗi task có một owner (prompt, code/ghép, deploy, QA cuối). |
| L7 | Media chỉ sinh qua API BTC. Nhạc và slide: Gateway không có endpoint; hỏi BTC trước, nếu không thì bản không nhạc / dựng slide local. |
| L8 | Key chỉ trong `AITC_API_KEY`; `max_retries=0`; không retry POST sau timeout/429; gộp nhiều trang vào một prompt; thử 1 ảnh, 1 cảnh Veo 4 giây trước; kiểm tra budget bằng `check_resources.py`. |
| L9 | Xong đủ requirement bắt buộc rồi mới thêm đúng một lớp mở rộng. |
| L10 | Thông điệp một câu, nội dung chính xác, đúng người nhận, sản phẩm dùng được thật. |
| L11 | Ghi rõ nội dung do AI tạo; không đưa dữ liệu cá nhân thật vào prompt; không phỏng vấn nhân vật AI như người thật. |
| L12 | Tập trên đúng máy thi; sao lưu prompt, bản trung gian và file cuối. |
| L13 | Lưu prompt, request, bản trung gian, AI log; hỏi BTC có phải nộp không. |
| L14 | Mở/nghe/xem toàn bộ file cuối thật trước khi ghi DONE. |

## Giới hạn Gateway cần nhớ

- Có: text, ảnh, video Veo (4/6/8 giây, bất đồng bộ 3 bước), TTS, STT, embeddings, grounding. Không có: nhạc, xuất slide/tài liệu.
- Ảnh Nano Banana dùng `aspect_ratio`; `gpt-image-*` dùng `size` + `quality`.
- GPT-6 dùng `max_completion_tokens`/`max_output_tokens`; cap quá thấp thì content rỗng.
- Veo tính tiền ngay khi tạo job (lite 720p ≈ $0.05/giây); poll ~10 giây.
- Key chính thức $50, key test $1 / 20 RPM; xác nhận model bằng `GET /v1/models`.

## Lỗi hay gặp

- **Web/App:** chỉ chạy local; kế hoạch quá lớn phải làm lại; thiếu hướng dẫn chơi/dùng.
- **Tài liệu:** sai năm số liệu; sai logo/màu; biểu đồ sơ sài; trang tràn chữ.
- **Ảnh/in ấn:** sai dấu tiếng Việt; quá nhiều chữ và màu; nhân vật không nhất quán; kẹt ở bước đóng gói.
- **Video/audio:** giọng đổi giữa các đoạn; chuyển cảnh giật; thiếu nhạc nền; phát âm sai ("cưỡng từ").
