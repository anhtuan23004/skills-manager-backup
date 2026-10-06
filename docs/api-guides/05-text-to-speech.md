---
source: https://docs.thucchien.ai/docs/round-2/user-guide/text-to-speech
checked: 2026-10-05
related_skill: aitc-audio-producer
operations: tts
---

# Text-to-Speech

`POST /audio/speech` nhận JSON có `model`, `input`, `voice` và trả media bytes.

Lưu thành `requests/tts.json`; `input` chỉ chứa lời cần đọc, không lẫn hướng dẫn dựng video:

```json
{
  "model": "gemini-2.5-flash-preview-tts",
  "input": "Xin chào. Đây là đoạn thử phát âm tiếng Việt cho buổi luyện.",
  "voice": "Zephyr"
}
```

| Field | Quy tắc |
|---|---|
| `model` | Model TTS trong allowlist và được cấp quyền |
| `input` | Text cần chuyển thành tiếng nói; chuẩn hóa số/tên riêng trước |
| `voice` | Giọng đúng họ model; phân biệt chữ hoa/thường theo ví dụ BTC |

Đổi sang OpenAI khi được cấp: `model: "gpt-4o-mini-tts"`, `voice: "alloy"`; không giữ giọng `Zephyr`. Không tự thêm tham số tốc độ/định dạng riêng của provider nếu chưa kiểm tra Gateway.

```bash
curl -s -X POST "https://api.thucchien.ai/v1/audio/speech" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-flash-preview-tts",
    "input": "Xin chào. Đây là đoạn thử phát âm tiếng Việt cho buổi luyện.",
    "voice": "Zephyr"
  }' \
  -o "output.wav"
```

Kiểm tra định dạng và nghe thử:

```bash
ffprobe -v error -show_format -show_streams output.wav
```

## QA audio

- Chuẩn hóa cách đọc tên riêng, số, chữ viết tắt trước khi sinh.
- Không suy ra codec chỉ từ phần mở rộng; chạy media probe rồi nghe toàn bộ.
- Kiểm tra clipping, khoảng lặng đầu/cuối, tốc độ và phát âm tiếng Việt.
- Sinh thử đoạn ngắn trước; TTS được tính theo text/audio token.

API reference:
<https://docs.thucchien.ai/docs/round-2/api-reference/text-to-speech>.
