---
source: https://docs.thucchien.ai/docs/round-2/user-guide/video-generation-veo3
checked: 2026-10-05
related_skill: aitc-video-director
operations: video-create,video-status,video-download
---

# Sinh video Veo 3.1

Video là quy trình bất đồng bộ ba bước:

Payload `requests/video.json` dùng cho một cảnh, không phải toàn bộ video dài:

```json
{
  "model": "veo-3.1-lite-generate-001",
  "prompt": "Máy quay cố định, một chiếc thuyền giấy trôi chậm từ trái sang phải trên mặt nước yên, ánh sáng ban ngày, không chữ.",
  "seconds": "4",
  "size": "1280x720"
}
```

`model`/`prompt` là trường API bắt buộc; helper yêu cầu `seconds` tường minh. Dùng string `"4"`, `"6"`, `"8"`. Chọn `size` theo đề, không tăng độ phân giải khi chưa kiểm tra cảnh mẫu.

### Bước 1: Tạo tác vụ sinh video (`POST /v1/videos`)
```bash
curl -s -X POST "https://api.thucchien.ai/v1/videos" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "veo-3.1-lite-generate-001",
    "prompt": "Máy quay cố định, một chiếc thuyền giấy trôi chậm từ trái sang phải trên mặt nước yên, ánh sáng ban ngày, không chữ.",
    "seconds": "4",
    "size": "1280x720"
  }' > job_create.json
# Lấy video_id từ phản hồi
VIDEO_ID=$(cat job_create.json | jq -r '.id')
```

### Bước 2: Kiểm tra tiến độ (`GET /v1/videos/{id}`)
```bash
curl -s -X GET "https://api.thucchien.ai/v1/videos/$VIDEO_ID" \
  -H "Authorization: Bearer $AITC_API_KEY"
```
Poll mỗi 10–15 giây cho đến khi `status` chuyển sang `completed`. Nếu `failed`, đọc chi tiết `error`.

### Bước 3: Tải video hoàn tất (`GET /v1/videos/{id}/content`)
```bash
curl -s -X GET "https://api.thucchien.ai/v1/videos/$VIDEO_ID/content" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -o "output.mp4"
```

| `status` phản hồi | Bước tiếp theo |
|---|---|
| `processing` / `queued` | Chờ khoảng 10–15 giây rồi kiểm tra lại; không tạo lại job mới |
| `completed` | Tải video qua endpoint `/content` |
| `failed` | Đọc thông báo lỗi; điều chỉnh prompt hoặc tham số trước khi tạo lại |
| POST timeout | Ghi nhận trạng thái chưa rõ; không bấm tạo lại ngay lập tức |

## Image-to-video

Khi muốn tạo video từ ảnh có sẵn, gửi form-data multipart với trường `input_reference` chứa file ảnh:

```bash
curl -s -X POST "https://api.thucchien.ai/v1/videos" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -F "model=veo-3.1-lite-generate-001" \
  -F "prompt=Chuyển động sóng nước nhẹ, góc máy giữ nguyên" \
  -F "seconds=4" \
  -F "size=1280x720" \
  -F "input_reference=@assets/start.png"
```

## Guard chi phí

- Luôn khai báo `seconds`: chỉ `4`, `6` hoặc `8`; thử 4 giây trước.
- Model lite hiện rẻ nhất trong tài liệu; kiểm tra pricing trước live call.
- Tác vụ bị tính phí khi tạo, kể cả không download.
- Không retry POST sau timeout/429; ghi trạng thái mơ hồ và kiểm tra trước.
- Poll khoảng 10 giây, không bắn liên tục.
- Image-to-video dùng multipart với `input_reference` và ảnh local được phép.

Thông số size được tài liệu liệt kê: `1280x720`, `1920x1080`, `720x1280`,
`1080x1920`. Sau download phải chạy media probe và xem/nghe file thật.

API reference: [create](https://docs.thucchien.ai/docs/round-2/api-reference/video-generation-start),
[status](https://docs.thucchien.ai/docs/round-2/api-reference/video-generation-status),
[download](https://docs.thucchien.ai/docs/round-2/api-reference/video-generation-download).
