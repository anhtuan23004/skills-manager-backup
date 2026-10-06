---
source: https://docs.thucchien.ai/docs/round-2/user-guide/google-search-grounding
checked: 2026-10-05
related_skill: aitc-text-producer
operations: text,responses
---

# Web grounding

Chỉ bật khi câu hỏi cần thông tin mới như tin tức, giá, lịch hoặc số liệu hiện
tại. Search tăng chi phí và token input.

## Gemini

Gọi `POST /chat/completions` với:

```json
{
  "model": "gemini-2.5-flash",
  "messages": [{"role":"user","content":"Tìm thông tin về [chủ đề] tính đến [ngày cần tra cứu], trả lời ngắn và nêu nguồn."}],
  "tools": [{"googleSearch":{}}]
}
```

Metadata có thể nằm ở `vertex_ai_grounding_metadata`, gồm truy vấn và nguồn.
Nếu hiển thị cho người dùng cuối, đọc yêu cầu hiển thị Search Suggestions của
Google trong tài liệu gốc. Không dùng `web_search_options` thay thế vì tài liệu
cảnh báo nó có thể bị bỏ qua.

## OpenAI

Gọi `POST /responses` với:

```json
{
  "model": "gpt-6-luna",
  "input": "Tìm thông tin về [chủ đề] tính đến [ngày cần tra cứu], trả lời ngắn và nêu nguồn.",
  "tools": [{"type":"web_search"}],
  "reasoning": {"effort":"low"},
  "max_output_tokens": 4000
}
```

DeepSeek không hỗ trợ web search. Chỉ bật search khi thực sự cần thông tin mới và ngân sách cho phép.

```bash
# Gọi qua cURL (ví dụ Gemini với search):
curl -s -X POST "https://api.thucchien.ai/v1/chat/completions" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-flash",
    "messages": [
      {"role": "user", "content": "Sự kiện thời sự công nghệ mới nhất hôm nay tại Việt Nam là gì?"}
    ],
    "tools": [{"googleSearch": {}}]
  }'
```

## Vị trí trường thông tin nguồn trích dẫn

| Response API | Ý nghĩa |
|---|---|
| Gemini `vertex_ai_grounding_metadata[]` | Thông tin grounding metadata khi model tìm kiếm web |
| `webSearchQueries` | Các từ khóa model đã dùng để tìm kiếm |
| `groundingChunks[].web.title/uri` | Tiêu đề và URL của nguồn web |
| `groundingSupports` | Đoạn trích dẫn đối chiếu tương ứng |
| OpenAI `output[]` loại `web_search_call` | Hoạt động tìm kiếm |
| OpenAI message `content[].annotations` | Dẫn nguồn gắn với câu trả lời |

Response không có metadata có thể nghĩa là model đã dùng tri thức có sẵn và không kích hoạt tìm kiếm; không tuyên bố đã kiểm tra web nếu chưa thấy thông tin nguồn trả về. Giới hạn phạm vi câu hỏi để tránh phát sinh chi phí search không cần thiết.

## QA nguồn

- Yêu cầu ngày cụ thể trong câu hỏi.
- Đọc URL/tiêu đề nguồn, không chỉ câu trả lời tổng hợp.
- Không biến citation thành bằng chứng nếu nguồn không hỗ trợ claim.
