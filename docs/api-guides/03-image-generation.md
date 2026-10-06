---
source: https://docs.thucchien.ai/docs/round-2/user-guide/image-generation
checked: 2026-10-05
related_skill: aitc-image-director
operations: image
---

# Sinh hình ảnh

## Cách gọi API trực tiếp

Dùng cho poster, minh họa, key visual hoặc frame. Gửi `POST /images/generations`:

```bash
curl -s -X POST "https://api.thucchien.ai/v1/images/generations" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nano-banana-2-lite",
    "prompt": "Một mô hình nhà bằng giấy trên nền sáng, góc nhìn chính diện, chừa khoảng trống phía trên cho tiêu đề; không chữ, không logo.",
    "n": 1,
    "aspect_ratio": "16:9"
  }' > response.json
```

Phản hồi trả về dữ liệu ảnh mã hóa base64 tại `data[0].b64_json`. Trích xuất và giải mã thành file ảnh:

```bash
# Trích xuất và giải mã base64 (trên macOS/Linux)
cat response.json | jq -r '.data[0].b64_json' | base64 --decode > output.png
```

Các alias hiện được tài liệu nêu: `nano-banana-2-lite`, `nano-banana-2`,
`nano-banana-pro`; kiểm tra lại availability. `nano-banana` cũ được tài liệu
ghi ngừng hỗ trợ từ 2026-10-02.

## Chọn đúng họ tham số

| Họ model | Trường cần chọn | Không trộn |
|---|---|---|
| Nano Banana | `aspect_ratio`: `1:1`, `3:4`, `4:3`, `16:9`, `9:16`; `n:1` | `size` không có tác dụng theo tài liệu Nano Banana |
| OpenAI image | `size`: `1024x1024`, `1536x1024`, `1024x1536`; `quality`: `low`, `medium`, `high` | Không dùng `aspect_ratio` để thay size |

Ví dụ OpenAI, chỉ dùng nếu model được cấp và có trong allowlist:

```json
{"model":"gpt-image-2.5-flare","prompt":"Một chiếc thuyền giấy trên mặt nước, không chữ.","size":"1024x1024","quality":"low","n":1}
```

## Đọc output và lưu ý thực tế

Response chuẩn có `data[0].b64_json`. Nhận diện header bytes để lưu đúng định dạng `.png` (`\x89PNG`), `.jpg` (`\xff\xd8\xff`) hoặc `.webp` (`RIFF...WEBP`).

- Muốn nhiều ảnh: gửi từng request riêng; tránh gọi lặp lại không kiểm soát để tiết kiệm quota.
- Tỷ lệ đúng chưa chứng minh đủ độ phân giải đề; kiểm tra file thật, chữ tiếng Việt và bố cục trước khi quyết định sinh lại.
- Chỉnh chữ/bố cục cục bộ bằng công cụ biên tập khi phù hợp, giữ ảnh đã đạt để giảm số lần sinh.

## Cách chat (modalities: ["image"])

Model đa phương thức có thể dùng `POST /chat/completions` với `modalities: ["image"]`; ảnh nằm trong `choices[0].message.images[].image_url.url` dạng data URL. Khi cần chỉnh sửa ảnh qua hội thoại, sử dụng endpoint này và trích xuất data URL.

Model OpenAI `gpt-image-*` dùng `size` và `quality`; Nano Banana dùng
`aspect_ratio`. Không giả định hai nhóm nhận cùng tham số.

API reference: [standard](https://docs.thucchien.ai/docs/round-2/api-reference/image-generation),
[chat](https://docs.thucchien.ai/docs/round-2/api-reference/image-generation-chat).
