---
source: https://docs.thucchien.ai/docs/round-2/user-guide/introduction
checked: 2026-10-05
related_skill: aitc-orchestrator
operations:
---

# Giới thiệu Gateway

Gateway BTC cung cấp một base URL cho nhiều nhà cung cấp AI:
`https://api.thucchien.ai`. API tương thích OpenAI ở các endpoint chính; đổi
model nhưng không đổi nơi giữ key.

## Checklist trước khi gọi

- Dùng Gateway key của đội, không dùng AI Log key bắt đầu bằng `aitc_`.
- Nạp `AITC_API_KEY` từ môi trường/secret manager, không ghi giá trị thật vào command mẫu hay chat.
- Giữ `AITC_ENABLE_NETWORK` chưa đặt trong lúc sửa payload/dry-run.
- Xác nhận model thực tế bằng `GET /v1/models`; `info.models` trong `/key/info` có thể rỗng hoặc chỉ chứa nhóm model của đội.
- Không đưa key vào JSON, prompt, screenshot, log bổ sung hoặc Git.

## Chuẩn bị môi trường gọi Gateway

| Mục | Hướng dẫn |
|---|---|
| `AITC_API_KEY` | Biến môi trường chứa API Key được BTC cấp. Không dán vào prompt hoặc code commit. |
| Base URL | `https://api.thucchien.ai/v1` cho hầu hết các API; `https://api.thucchien.ai` cho `/key/info`. |
| Workspace bài làm | Tạo thư mục riêng (ví dụ `chung-khao/solution/`) để chứa requests, assets và final output. |

### 1. Gọi qua cURL
```bash
# Smoke test sinh văn bản
curl -s -X POST "https://api.thucchien.ai/v1/chat/completions" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tên-model-được-cấp",
    "messages": [{"role": "user", "content": "Kiểm tra kết nối"}]
  }'
```

### 2. Cấu hình qua OpenAI SDK (Python)
Gateway BTC tương thích chuẩn OpenAI, chỉ cần trỏ `base_url` và truyền `api_key`:

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.thucchien.ai/v1",
    api_key=os.environ.get("AITC_API_KEY"),
    max_retries=0  # Tránh tự động retry các tác vụ tính phí
)

response = client.chat.completions.create(
    model="tên-model-được-cấp",
    messages=[{"role": "user", "content": "Xin chào"}]
)
print(response.choices[0].message.content)
```

## Chỉ mở nguồn ngoài khi cần

Schema và cách đọc output có sẵn trong guide từng operation. Tra nguồn BTC lại khi model không còn tồn tại, nhận 400/403 không giải thích được, cần tham số chưa mô tả hoặc chuẩn bị batch có chi phí lớn. Ngày `checked` là ngày đối chiếu tài liệu, không phải ngày chạy live.
