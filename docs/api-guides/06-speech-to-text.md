---
source: https://docs.thucchien.ai/docs/round-2/user-guide/speech-to-text
checked: 2026-10-05
related_skill: aitc-audio-producer
operations: stt
---

# Speech-to-Text

`POST /audio/transcriptions` dùng `multipart/form-data`, không phải JSON thuần.
Request có trường `model` và file audio; transcript nằm ở `text`.

Payload `requests/stt.json` chỉ chứa model/field scalar; file được truyền riêng bằng CLI:

```json
{"model":"gemini-3.5-transcribe-preview"}
```

```bash
curl -s -X POST "https://api.thucchien.ai/v1/audio/transcriptions" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -F "file=@assets/voice.mp3" \
  -F "model=gemini-3.5-transcribe-preview"
```

Model tài liệu hiện liệt kê gồm `gemini-3.5-transcribe-preview`, các model
`gpt-4o-*-transcribe`, `gpt-transcribe` và `whisper-1`. Riêng
`gpt-transcribe` cần `response_format=json`.

Ví dụ khi chọn model đó và đã thêm allowlist:

```json
{"model":"gpt-transcribe","response_format":"json"}
```

## Upload và đọc kết quả

| Thành phần | Cách dùng |
|---|---|
| `file=@assets/voice.mp3` | File audio đầu vào gửi dưới dạng multipart form-data |
| `model` | Tên model transcribe được cấp quyền |
| Phản hồi `text` | Transcript nhận dạng được từ audio |
| Phản hồi `usage` | Thông tin token tiêu thụ |

Response mẫu trả về:

```json
{"text":"Nội dung được nhận dạng.","task":"transcribe","usage":{"input_tokens":51,"output_tokens":6,"total_tokens":57}}
```

## Lỗi thường gặp

- `STT requires --attachment`: thêm file vào lệnh live; dry-run payload hiện không chứng minh file đã đủ.
- `400` với `gpt-transcribe`: kiểm tra `response_format: "json"`.
- File quá lớn/codec không phù hợp: probe và chuyển/chia đoạn local theo khả năng được cấp; ghi offset để ghép transcript đúng thứ tự.
- Transcript trống/sai: nghe input, kiểm tra đoạn im lặng/tiếng nền/ngôn ngữ; không suy ra lỗi model chỉ từ phần mở rộng file.

## QA

- Kiểm tra MIME/codec thật và dung lượng trước upload.
- So transcript với các đoạn có tên riêng, số liệu và tiếng nền.
- Không tự sửa transcript rồi mô tả như output nguyên bản; lưu version rõ ràng.
- Audio nhạy cảm chỉ dùng nếu đề và quyền riêng tư cho phép.

API reference:
<https://docs.thucchien.ai/docs/round-2/api-reference/speech-to-text>.
