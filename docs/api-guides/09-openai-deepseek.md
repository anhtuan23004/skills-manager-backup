---
source: https://docs.thucchien.ai/docs/round-2/user-guide/openai-deepseek
checked: 2026-10-05
related_skill: aitc-text-producer
operations:
---

# Lưu ý cho OpenAI và DeepSeek

Vẫn dùng `https://api.thucchien.ai`; chỉ đổi `model`.

## OpenAI reasoning

- Dòng `gpt-5.6-*`, `gpt-6*`, `o3`, `o4-mini` dùng token suy nghĩ và token đó
  tính vào output/cost.
- Chat Completions: ưu tiên `max_completion_tokens`; `gpt-6*` từ chối
  `max_tokens`.
- Responses: dùng `max_output_tokens` và `reasoning:{"effort":"low"}`.
- Đừng đặt output limit quá thấp: model có thể dùng hết cho reasoning và trả
  content rỗng.
- Không gửi mức reasoning mà model không hỗ trợ; dùng bảng snapshot dưới đây.

| Model | Mức effort tài liệu BTC ghi nhận |
|---|---|
| `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol/terra/luna` | `none`, `low`, `medium`, `high`, `xhigh`, `max` |
| `gpt-6.1-sol`, `gpt-6-astra` | `low`, `medium`, `high`, `xhigh`, `max`; không `none` |
| `o3`, `o4-mini` | `low`, `medium`, `high` |

Không model nào trong bảng nhận `minimal`. `temperature`/`top_p` bị Gateway bỏ qua ở các model reasoning này; đừng dùng chúng để điều khiển mức suy nghĩ. Bắt đầu `low` cho tác vụ đơn giản, chỉ nâng khi chất lượng chưa đạt.

Gọi qua cURL với Chat:

```bash
curl -s -X POST "https://api.thucchien.ai/v1/chat/completions" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-6-luna",
    "messages": [{"role": "user", "content": "Trích xuất tên và ngày từ đoạn sau, trả JSON: [đoạn văn]"}],
    "reasoning_effort": "low",
    "max_completion_tokens": 4000
  }'
```

Endpoint Responses (`/responses`) đổi `messages` thành `input`, `reasoning_effort` thành `reasoning: {"effort": "low"}`, token cap thành `max_output_tokens`. Xem chi tiết ở [Text](02-text-generation.md).

Ảnh OpenAI `gpt-image-*` dùng `size` và `quality`, không dùng `aspect_ratio` như
Nano Banana. `gpt-transcribe` cần `response_format=json`.

## DeepSeek

- Dùng tên `deepseek-flash` hoặc `deepseek-v4-pro`; gateway không mở hai alias
  Flash cũ được tài liệu nhắc đến.
- Thinking bật mặc định; output suy nghĩ ở `message.reasoning_content` và vẫn
  tính tiền.
- Có thể tắt thinking cho phân loại/trích xuất bằng field JSON trực tiếp
  `"thinking": {"type": "disabled"}`. Khi dùng SDK OpenAI, truyền qua `extra_body`.
- Không dùng DeepSeek cho ảnh input/output, audio hoặc web search.

Nếu nhận 429, phân biệt rate và budget; không retry POST tạo artifact mù quáng.

Ví dụ gọi DeepSeek qua cURL:
```bash
curl -s -X POST "https://api.thucchien.ai/v1/chat/completions" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-flash",
    "messages": [{"role": "user", "content": "Phân loại câu '\''Dịch vụ tốt'\'' thành JSON có khóa sentiment, giá trị positive, neutral hoặc negative."}],
    "thinking": {"type": "disabled"},
    "response_format": {"type": "json_object"}
  }'
```

Prompt JSON mode cần nêu rõ yêu cầu trả về JSON; parse và validate kết quả trước khi đưa vào các bước tiếp theo. Nếu viết adapter dùng OpenAI Python SDK, cấu hình `max_retries=0` để tránh tự động gọi lại các tác vụ trả phí.
