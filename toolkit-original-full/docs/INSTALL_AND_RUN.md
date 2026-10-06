# Cài đặt, luyện thử và bật trong thi

## 1. Chọn mức dùng
**Mức A — chỉ skills/prompts:** đọc `skills/INDEX.md`; gọi SKILL.md phù hợp trong agent đã dùng Gateway BTC. Không cần Python/MCP riêng.

**Mức B — thêm công cụ local:** Python 3.10+, FFmpeg và FFprobe trong PATH. Mã Python dùng standard library, không cần pip package cho runtime. Các binary hệ thống phải được cài/kiểm tra trước thi. Có thể chạy `python --version`, `ffmpeg -version`, `ffprobe -version`.

**Mức C — MCP QA:** thêm server local 4 tool nếu host có MCP stdio và đội cần thao tác qua agent. Không cài thêm chỉ vì bộ toolkit có nó.

**Trước khi chuyển sang thi:** xác nhận phạm vi code/helper/templates được chuẩn bị trước. Không tự sao chép cả gói vào repo BTC. Không chép đè `.agents`, `.ai-log`, `.claude`, `.codex`, `.cursor`, `.gemini`, `.github`, `scripts` hoặc hook BTC. Host và cách discover skill chưa biết nên gói không tự sửa cấu hình IDE.

## 2. Đặt thư mục
Giải nén toolkit ở thư mục do đội quản lý. Trong **buổi luyện**, tạo workspace riêng:
```text
practice-workspace/
  ops/                gateway.json, permission.json
  requests/           payload của lần tập
  assets/             media đầu vào được phép
  runs/               kết quả gọi API theo máy và ID
  qa/                 contact sheet, manifest, kiểm tra
  final/              chỉ file dự định nộp
  submission/         package kiểm tra
```
Trong **phiên thi**, workspace tương ứng phải đặt trong phạm vi repo/tài nguyên BTC cho phép và được hook theo dõi đúng. Đường dẫn tuyệt đối phải do đội chọn, không lấy ví dụ như đường dẫn có thật.

Copy `config/gateway.example.json` thành `ops/gateway.json`; `config/permission.example.json` thành `ops/permission.json`. Chỉ dùng example payload trong luyện tập. Không chỉnh `.gitignore` của BTC tự động; fragment trong config chỉ là nội dung để người xem và hợp nhất nếu được phép.

## 3. Dùng skill không cần cài tự động
Mở `prompts/00_start.md`. Chỉ rõ đường dẫn toolkit thật cho agent, rồi đính kèm đề/luật/tài nguyên được phép. Ví dụ:
```text
Đọc skills/aitc-orchestrator/SKILL.md và references/contract.md của skill.
Đây là đề thi: [đề đầy đủ].
Đây là deadline và phạm vi tài nguyên được BTC xác nhận: [...].
Trước tiên chỉ phân tích đề, đưa hướng giải và các điểm cần tôi duyệt.
Không gọi AI khác ngoài Gateway BTC; chưa tự tạo media hoặc nộp bài.
```
Nếu agent không tự discover skill ở vị trí này, yêu cầu nó đọc file trực tiếp. Không tự chép skill vào thư mục hook bị BTC bảo vệ. Chỉ dùng cách tích hợp host mà BTC cho phép và đội đã kiểm thử.

## 4. Kiểm thử offline
Chạy tại thư mục toolkit:
```bash
python -m unittest discover -s tests -v
```
Báo cáo tạo gói: 48 tests đạt. Nếu máy đội thiếu FFmpeg, nhóm test media sẽ được skip: **không xem test skip là đã kiểm thử media**.

## 5. Gọi Gateway: dry-run trước
Tất cả lệnh dưới đây chạy tại thư mục toolkit; thay `WORKSPACE_ABS_PATH` bằng workspace thật. Đường dẫn payload bên trong dùng dấu `/`.
```bash
python runtime/gateway.py --root "WORKSPACE_ABS_PATH" --op text --payload requests/text.json
```
Không có `--live` thì chỉ kiểm tra cấu hình/payload, không HTTP, không tính phí. Dry-run **không chứng minh** key/model/endpoint hoạt động.

Muốn thử live, người phụ trách phải:
- Xác minh scope chuẩn bị trước và endpoint/model BTC.
- Hoàn tất onboarding/hook, kiểm tra cả việc ghi lẫn gửi log; wrapper không thay hook.
- Xác minh model của chính coding host/critic chạy qua BTC.
- Đánh dấu đúng ba check trong permission.json; dùng mode practice hoặc competition. Competition cần `end_at` ISO có múi giờ, tương ứng T+120.
- Cấu hình `AITC_API_KEY` qua môi trường/secret manager local; **không đưa vào chat, payload, code hoặc commit**. Đặt `AITC_ENABLE_NETWORK=YES` trong process gọi helper.
- Thêm `--live` vào lệnh sau khi kiểm tra; không gửi API key cho người tạo toolkit.

Các check dạng boolean là xác nhận của người, không phải công cụ tự chứng nhận việc BTC cho phép.

## 6. Thao tác ảnh/video/audio
```bash
python runtime/gateway.py --root "WORKSPACE_ABS_PATH" --op image --payload requests/image.json --machine A --live
python runtime/gateway.py --root "WORKSPACE_ABS_PATH" --op video-create --payload requests/video.json --machine A --live
python runtime/gateway.py --root "WORKSPACE_ABS_PATH" --op video-status --job-id "ACTUAL_JOB_ID" --machine A --live
python runtime/gateway.py --root "WORKSPACE_ABS_PATH" --op video-download --job-id "ACTUAL_JOB_ID" --machine A --live
python runtime/gateway.py --root "WORKSPACE_ABS_PATH" --op tts --payload requests/tts.json --machine B --live
python runtime/gateway.py --root "WORKSPACE_ABS_PATH" --op stt --payload requests/stt.json --attachment assets/voice.wav --machine B --live
```
Mỗi lần có thư mục `runs/A-...` hoặc `runs/B-...`, request và kết quả bổ sung. Tạo video xong phải dùng ID thật; status completed mới download. Poll theo khoảng tài liệu BTC hướng dẫn, không bắn liên tục. `video-create` có thể dùng `--attachment assets/start.png` cho input_reference; STT dùng upload multipart.

Wrapper không tự làm image editing/reference workflow, subtitle alignment, dựng timeline nhiều track, nhạc hoặc mọi tham số nâng cao. Dùng công cụ biên tập không-AI hoặc mở rộng trong phạm vi BTC cho phép. Không tự thêm external API để lấp tính năng thiếu.

## 7. QA media
```bash
python runtime/media.py --root "WORKSPACE_ABS_PATH" probe final/video.mp4
python runtime/media.py --root "WORKSPACE_ABS_PATH" contact-sheet final/video.mp4 qa/contact-v1.png --frames 9
python runtime/media.py --root "WORKSPACE_ABS_PATH" normalize-video assets/draft.mp4 final/video-v2.mp4 --width 1920 --height 1080 --fps 25
```
1920×1080/25fps chỉ là ví dụ lệnh, **không phải thông số mặc định của bài thi**. Lấy thông số từ đề. Normalize tạo file mới, không sửa bản cũ. Sau xử lý phải xem/nghe lại.

## 8. Cấu hình MCP local
```bash
python runtime/configure_mcp.py --root "WORKSPACE_ABS_PATH"
```
Lệnh in cấu hình `mcpServers` với executable/path thật; không sửa file host. Chỉ thêm entry này ở chỗ host/BTC cho phép. Host khác có thể dùng schema khác; gói chưa kiểm thử tất cả host.

MCP stdio chạy riêng được bằng:
```bash
python runtime/mcp_server.py --root "WORKSPACE_ABS_PATH"
```
Lệnh này chờ JSON-RPC từ client, không phải chat UI. Không trỏ root vào thư mục home hoặc toàn repo có secret/hook. Chọn một thư mục làm việc được kiểm soát. Không cài vào ChatGPT/Claude web để dùng trong phiên thi; host điều khiển cũng phải tuân thủ đường AI BTC.

## 9. Đóng băng và kiểm tra nộp
Sau khi người duyệt final:
```bash
python runtime/cli.py --root "WORKSPACE_ABS_PATH" freeze --directory final
python runtime/cli.py --root "WORKSPACE_ABS_PATH" verify
python runtime/cli.py --root "WORKSPACE_ABS_PATH" package --output submission/final.zip
```
Freeze không commit/push, không gửi gì cho BTC và không cung cấp dấu thời gian tin cậy độc lập. Package chỉ khi đề cho phép ZIP. Nếu đề cần MP4/JPG/TXT trực tiếp, nộp trực tiếp file đúng yêu cầu. Source/prompts trong repo BTC là phần riêng, không bị thay bằng ZIP media này. Ghi hình giám sát/video phản hồi xử lý theo đường nộp BTC yêu cầu, không ép vào attachment sản phẩm.

Nếu đóng băng nhầm trong buổi luyện, tạo workspace luyện mới. Nếu xảy ra trong thi, dừng để đội trưởng xử lý đúng quy trình và thời gian; không xóa log/freeze lén để làm tiếp sau T+120.
