# Thực thi từ skill và plan

Tài liệu này hướng dẫn cách chuyển từ plan sang thực thi trực tiếp, kết nối [danh mục skill](../skills/INDEX.md) với Gateway BTC và các công cụ dòng lệnh có sẵn trên máy.

## 1. Tổ chức Workspace thi đấu

Agent và đội chọn một workspace làm việc riêng (ví dụ `chung-khao/solution/`). Cấu trúc đề xuất trong workspace:
```text
solution/
  requests/           lưu payload JSON đã gửi (để đối chiếu)
  assets/             ảnh/audio mẫu, tài nguyên hợp lệ được cấp
  qa/                 ảnh trích xuất, kết quả kiểm tra chất lượng
  final/              sản phẩm hoàn thiện dự kiến nộp
```
Ghi plan và yêu cầu trực tiếp vào workspace thi đấu; không ghi bài giải hay sản phẩm vào thư mục toolkit.

## 2. Gọi Gateway BTC trực tiếp

Mọi tác vụ AI trong phòng thi đều được thực hiện qua Gateway BTC tại:
- **Base URL:** `https://api.thucchien.ai/v1` (hoặc `https://api.thucchien.ai` với một số endpoint đặc biệt)
- **Header:** `Authorization: Bearer $AITC_API_KEY`, `Content-Type: application/json`

Agent có thể gọi qua HTTP client của môi trường (curl, fetch, Python `urllib`/`requests`, hoặc OpenAI SDK trỏ `base_url`).

| Task | Endpoint BTC | Hướng dẫn chi tiết | Kiểm tra output |
|---|---|---|---|
| Text / script | `POST /chat/completions` hoặc `/responses` | [Text Guide](api-guides/02-text-generation.md) | Nội dung, văn phong tiếng Việt, độ dài, format |
| Ảnh | `POST /images/generations` | [Image Guide](api-guides/03-image-generation.md) | Giải mã base64, xem ảnh thực tế, typography |
| Video | `POST /videos` → poll `/videos/{id}` → `/videos/{id}/content` | [Video Guide](api-guides/04-video-generation.md) | Lưu job ID, tải file MP4, xem chuyển động |
| TTS | `POST /audio/speech` | [TTS Guide](api-guides/05-text-to-speech.md) | Nghe phát âm, kiểm tra ngữ điệu, đo thời lượng |
| STT | `POST /audio/transcriptions` (multipart) | [STT Guide](api-guides/06-speech-to-text.md) | Đối chiếu transcript với âm thanh gốc |
| Grounding | `POST /chat/completions` kèm tools tìm kiếm | [Grounding Guide](api-guides/07-web-grounding.md) | Kiểm tra tính xác thực nguồn và trích dẫn |
| Embeddings / RAG | `POST /embeddings` | [Embeddings Guide](api-guides/08-embeddings.md), [RAG Workflow](../skills/aitc-production-planner/references/rag-workflow.md) | Đúng model, chiều vector, cosine similarity |

## 3. Kiểm tra kỹ thuật và hoàn thành task

Dùng trực tiếp công cụ hệ thống có sẵn:

### Kiểm tra thông số media bằng FFprobe
```bash
ffprobe -v error -show_format -show_streams -of json final/video.mp4
```
Xác nhận width, height, codec, duration, audio channels theo đúng yêu cầu của đề.

### Trích xuất contact sheet để kiểm tra chuyển động (FFmpeg)
```bash
ffmpeg -i final/video.mp4 -vf "fps=1,scale=320:-1,tile=3x3" -frames:v 1 qa/contact-sheet.png
```

### Chuẩn hóa video theo thông số đề (nếu cần)
```bash
ffmpeg -i assets/raw.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p -c:a aac final/output.mp4
```

### Kiểm kê hash file (Manifest)
```bash
shasum -a 256 final/* > qa/manifest.sha256
```

## 4. Bằng chứng và cập nhật Plan

Sau mỗi task:
- Kiểm tra file thật bằng mắt/tai; metadata đạt **chưa đủ** để chứng minh nội dung đạt.
- Cập nhật trạng thái (`PASS` / `FAIL` / `UNVERIFIED`) và đường dẫn file bằng chứng vào [execution-plan](../templates/execution-plan.md).
- Không mặc định kết quả sinh ra lần cuối cùng là tốt nhất; so sánh các phiên bản và chọn bản đáp ứng đề tốt nhất.
