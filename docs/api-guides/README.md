# API quick reference — AI Thực Chiến

Các file trong thư mục này là checklist thao tác của đội, tóm tắt từ tài liệu
BTC và được kiểm tra ngày **2026-10-05**. Tài liệu BTC và đề thi luôn có ưu
tiên cao hơn bản tóm tắt này.

## Chọn skill và API theo mục tiêu

**Cách đọc tiết kiệm context:** lần đầu đọc `00` và `01`; mỗi task chỉ mở một guide đúng operation. Chỉ mở `09` khi dùng OpenAI/DeepSeek, `10–11` khi chọn budget hoặc gặp 429. Không nạp cả 13 file hay mở lại web nếu schema đã đủ và không có thay đổi/lỗi thực tế.

Mỗi guide gồm payload có thể dùng làm điểm bắt đầu, lệnh, vị trí output và giới hạn của helper. Ví dụ là dữ liệu luyện, cần thay nội dung theo đề. Model trong ví dụ không bảo đảm key có quyền gọi; thêm model vào allowlist sau khi kiểm tra `/v1/models`.

Đọc guide của task được chọn trong [execution-plan](../../templates/execution-plan.md). [Routing](../../skills/aitc-orchestrator/references/routing.md) chọn skill; [SKILL_EXECUTION](../SKILL_EXECUTION.md) chỉ cách gọi helper trực tiếp, không bắt buộc tạo app.

| Mục tiêu | Skill và API guide |
|---|---|
| Viết, tóm tắt, phân tích | `aitc-text-producer` → [Text](02-text-generation.md) |
| Poster/ảnh | `aitc-image-director` → [Image](03-image-generation.md) |
| Video | `aitc-video-director` → [Video](04-video-generation.md) |
| Thuyết minh / transcript | `aitc-audio-producer` → [TTS](05-text-to-speech.md) / [STT](06-speech-to-text.md) |
| Thông tin mới | `aitc-text-producer` → [Grounding](07-web-grounding.md) |
| Tìm kiếm / RAG tài liệu nhỏ | `aitc-production-planner` → [RAG workflow](../../skills/aitc-production-planner/references/rag-workflow.md), [Embedding](08-embeddings.md) |

Mọi request gửi tới Gateway BTC:
- **Base URL:** `https://api.thucchien.ai/v1` (riêng `GET /key/info` dùng URL gốc `https://api.thucchien.ai/key/info`).
- **Headers:** `Authorization: Bearer $AITC_API_KEY`, `Content-Type: application/json` (trừ STT dùng `multipart/form-data`).

| Endpoint HTTP | Payload / Tham số chính | Kiểu dữ liệu trả về | Hướng dẫn |
|---|---|---|---|
| `POST /chat/completions` | `model`, `messages` | JSON (`choices[0].message.content`) | [Text](02-text-generation.md) |
| `POST /responses` | `model`, `input` | JSON (`output_text` hoặc `output`) | [Text](02-text-generation.md) |
| `POST /images/generations` | `model`, `prompt`, `n: 1`, `size` | JSON (`data[0].b64_json`) | [Image](03-image-generation.md) |
| `POST /videos` | `model`, `prompt`, `seconds`, `size` | JSON (`id` của video job) | [Video](04-video-generation.md) |
| `GET /videos/{id}` | Path param `id` | JSON (`status`: queued/processing/completed) | [Video](04-video-generation.md) |
| `GET /videos/{id}/content` | Path param `id` | Binary MP4 stream | [Video](04-video-generation.md) |
| `POST /audio/speech` | `model`, `input`, `voice` | Binary audio stream (MP3/WAV) | [TTS](05-text-to-speech.md) |
| `POST /audio/transcriptions` | Form-data `file`, `model` | JSON (`text` transcript) | [STT](06-speech-to-text.md) |
| `POST /embeddings` | `model`, `input` | JSON (`data[].embedding`) | [Embedding](08-embeddings.md) |
| `GET /key/info` | Không cần body | JSON thông tin quota/spend | [Pricing](10-pricing.md) |

## Danh mục

- [Giới thiệu](00-introduction.md)
- [Khái niệm cốt lõi](01-core-concepts.md)
- [Sinh văn bản](02-text-generation.md)
- [Sinh hình ảnh](03-image-generation.md)
- [Sinh video](04-video-generation.md)
- [Text-to-Speech](05-text-to-speech.md)
- [Speech-to-Text](06-speech-to-text.md)
- [Web grounding](07-web-grounding.md)
- [Embeddings](08-embeddings.md)
- [OpenAI và DeepSeek](09-openai-deepseek.md)
- [Pricing](10-pricing.md)
- [Rate limits](11-rate-limits.md)
- [Nguồn tham khảo](12-references.md)

## Quy tắc chung

1. Key chỉ đi qua biến môi trường `AITC_API_KEY`; không dán vào prompt/source.
2. Từ task trong plan, chuẩn bị payload và kiểm tra offline/dry-run trước live call.
3. Kiểm tra `ops/permission.json`, AI Log và Gateway BTC trước khi bật mạng.
4. Không retry POST tạo nội dung một cách mù quáng; request có thể đã tính phí.
5. Luôn mở/nghe/xem artifact thật trước khi freeze.
