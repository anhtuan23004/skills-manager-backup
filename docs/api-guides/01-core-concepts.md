---
source: https://docs.thucchien.ai/docs/round-2/user-guide/core-concepts
checked: 2026-10-05
related_skill: aitc-orchestrator
operations:
---

# Khái niệm cốt lõi

- Xác thực: header `Authorization: Bearer <your_api_key>`.
- Base URL duy nhất: `https://api.thucchien.ai` hoặc hậu tố `/v1` khi SDK cần.
- Chọn model bằng trường `model`; không đổi endpoint sang nhà cung cấp ngoài.
- Text thường trả trong `choices`; ảnh/media có thể trả trong `data` hoặc bytes.
- `messages` dùng cho hội thoại; `prompt` thường dùng cho sinh ảnh/video.
- Response ngoài nội dung còn có usage, request ID hoặc header chi phí; lưu các
  trường này để theo dõi nhưng không coi chúng là bằng chứng chất lượng.

## Phân biệt lỗi

| Lỗi | Xử lý |
|---|---|
| `400` | Kiểm tra schema/tham số của model |
| `401` | Key thiếu hoặc sai |
| `403` | Model/route không được cấp |
| `429 rate` | Giảm song song, chờ và backoff |
| `429 budget` | Dừng; chờ không phục hồi ngân sách |

POST timeout có trạng thái mơ hồ: không tự gửi lại vì tác vụ có thể đã được tạo.

## JSON trực tiếp và SDK khác nhau ở đâu?

- Các payload trong guide là body HTTP JSON trực tiếp; không bọc thêm các khóa dư thừa.
- Khi dùng OpenAI Python SDK, các trường đặc thù của model (như cấu hình suy luận) được truyền qua `extra_body`. Khi gọi HTTP REST trực tiếp, các trường đó đặt ngang hàng ở cấp ngoài cùng của JSON body.
- Chat Completion dùng trường `messages`, API `/responses` dùng trường `input`.
- STT (`/audio/transcriptions`): gửi dưới dạng `multipart/form-data` chứa file audio và tên model.
- `stream: true`: server trả về chuỗi sự kiện Server-Sent Events (SSE). Nếu không cần hiển thị thời gian thực theo từng token, nên để `stream: false` hoặc bỏ qua để nhận trọn vẹn JSON object.

## Quy tắc xử lý lỗi và Retry

- **Yêu cầu GET (tra cứu trạng thái, tải file):** có thể thử lại an toàn (retry) 2–3 lần với backoff ngắn (1s, 2s) nếu gặp lỗi mạng tạm thời hoặc 429 rate limit.
- **Yêu cầu POST (tạo mới text, ảnh, video, audio):** không tự động retry mù quáng khi timeout, vì Gateway có thể đã tiếp nhận và trừ quota của đội. Kiểm tra dashboard hoặc job list trước khi thực hiện lại.
- **Lỗi 429 Budget:** Ngừng toàn bộ thao tác sinh AI trả phí; thông báo ngay cho đội trưởng để điều chỉnh kế hoạch. Chờ đợi không tự phục hồi ngân sách tài khoản.
