---
source: https://docs.thucchien.ai/docs/round-2/user-guide/embeddings
checked: 2026-10-05
related_skill: aitc-production-planner
operations: embedding
---

# Embeddings và RAG cục bộ

`POST /embeddings` nhận `model` và `input`, trả vector trong `data[].embedding`.

Payload `requests/embedding.json`, dùng để tạo index hoặc embed câu hỏi:

```json
{
  "model": "gemini-embedding-001",
  "input": ["Đoạn tài liệu thứ nhất.", "Đoạn tài liệu thứ hai."]
}
```

Với một câu hỏi, `input` có thể là chuỗi hoặc danh sách một chuỗi. Không gửi văn bản rỗng và không log toàn bộ vector vào ngữ cảnh agent.

```bash
curl -s -X POST "https://api.thucchien.ai/v1/embeddings" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-embedding-001",
    "input": ["Đoạn tài liệu thứ nhất.", "Đoạn tài liệu thứ hai."]
  }'
```

Thông tin hiện tại trong tài liệu:

| Model | Chiều | Ghi chú |
|---|---:|---|
| `gemini-embedding-001` | 3072 | đa ngôn ngữ, tiếng Việt |
| `gemini-embedding-2` | 3072 | gửi một đoạn mỗi request |
| `text-multilingual-embedding-002` | 768 | đa ngôn ngữ |
| `text-embedding-3-small` | 1536 | OpenAI |
| `text-embedding-3-large` | 3072 | OpenAI |

Không so sánh vector từ hai model khác nhau. Dùng cùng model cho index và query.
Với tài liệu nhỏ, không cần cài vector database phức tạp. Flow đề xuất: chunk tài liệu kèm source ID → embedding từng batch → lưu vector vào mảng/file JSON → embed câu hỏi → tính cosine similarity xếp hạng top-K → đưa context có trích dẫn vào prompt Gateway text.

Kiểm tra dimension, nguồn chunk và giới hạn context trước khi gọi model.

## Đọc và lưu vector

API trả `data[]`; mỗi mục có `index` và `embedding`. Ghép theo `index` nếu có, kiểm tra số lượng bằng số đoạn đã gửi rồi lưu cùng chunk ID/source/page, model và hash nội dung.

`gemini-embedding-2` chỉ trả một vector khi gửi nhiều đoạn: gửi từng đoạn riêng, không âm thầm gán cùng vector cho mọi chunk. Các số chiều trong bảng là snapshot; kiểm tra chiều trả về thật trước khi truy xuất.

## Dùng lại để giảm token/chi phí

1. Chunk một lần và giữ source ID. Tài liệu không đổi, model không đổi thì tái dùng vector đã có.
2. Mỗi câu hỏi mới chỉ embed query; chọn top-k rồi gửi các đoạn cần thiết vào text, không gửi cả kho tài liệu.
3. Cùng dimension chưa đủ: hai model khác nhau không tạo vector so sánh được. Lưu model ID với index.
4. Giữ ánh xạ source ID; không bịa citation khi đoạn trùng hoặc evidence thiếu.

Lỗi cần chặn: response thiếu vector, chiều khác index, số vector khác số input, model index/query khác nhau. Thử cả câu có đáp án và câu ngoài tài liệu; top-k luôn có kết quả không có nghĩa câu hỏi đã có evidence. Chi tiết nối pipeline ở [RAG workflow](../../skills/aitc-production-planner/references/rag-workflow.md).
