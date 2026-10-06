---
source: https://docs.thucchien.ai/docs/round-2/user-guide/text-generation
checked: 2026-10-05
related_skill: aitc-text-producer
operations: text,responses
---

# Sinh văn bản

## Endpoint

- `POST /chat/completions`: request có `model` và `messages`; kết quả chính ở
  `choices[0].message.content`.
- `POST /responses`: hữu ích cho model OpenAI và web search; kết quả SDK ở
  `output_text`.

Model Gemini được tài liệu liệt kê gồm dòng `gemini-2.5-*`, `gemini-3.1-*`,
`gemini-3.5-*` đến `gemini-3.8-flash`; dùng model thực tế có trong key của đội.

## Ví dụ gọi qua cURL

```bash
curl -s -X POST "https://api.thucchien.ai/v1/chat/completions" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-flash",
    "messages": [
      {"role": "system", "content": "Trả lời tiếng Việt ngắn gọn, dựa trên dữ liệu người dùng cung cấp."},
      {"role": "user", "content": "Tóm tắt thành 3 gạch đầu dòng: [nội dung cần tóm tắt]"}
    ],
    "max_tokens": 1024,
    "stream": false
  }'
```

| Field | Khi dùng / tránh lỗi |
|---|---|
| `model` | Bắt buộc; model key được cấp bởi BTC |
| `messages` | Bắt buộc cho chat; array các message, không phải chuỗi JSON lồng |
| `max_tokens` | Giới hạn ví dụ cho Gemini; reasoning OpenAI dùng `max_completion_tokens` |
| `temperature` | Tùy chọn theo model; không gửi hàng loạt tham số chỉ vì SDK hỗ trợ |
| `stream` | `false` để nhận trọn vẹn JSON |

## Endpoint Responses (`POST /responses`)

Ví dụ dùng cho OpenAI GPT-6:

```bash
curl -s -X POST "https://api.thucchien.ai/v1/responses" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-6-luna",
    "input": "Viết lại câu sau rõ hơn, giữ nguyên nghĩa: [câu cần sửa]",
    "reasoning": {"effort": "low"},
    "max_output_tokens": 4000
  }'
```

## Đọc response và xử lý lỗi

| API | Trường kết quả chính |
|---|---|
| Chat (`/chat/completions`) | `choices[0].message.content` |
| Responses (`/responses`) | `output_text` hoặc các khối text trong `output` |
| Usage | `usage.prompt_tokens`, `usage.completion_tokens` |

Content rỗng có thể do reasoning cap quá thấp hoặc response khác kiểu text. Kiểm tra đúng model/operation/schema trước khi gửi lại. `400` với GPT-6: thường cần thay `max_tokens` bằng `max_completion_tokens`.

## QA

- Kiểm tra yêu cầu định dạng, độ dài và ngôn ngữ trong output thật.
- Ghi nhận `finish_reason=length` và content rỗng do reasoning budget quá thấp.
- Không mặc định bật web search cho câu hỏi kiến thức ổn định.

API schema chi tiết:
<https://docs.thucchien.ai/docs/round-2/api-reference/text-generation>.
