# Chọn skill/MCP có căn cứ, không chọn theo số lượng

## Tiêu chuẩn lựa chọn của toolkit
Ưu tiên nguồn gốc rõ, phạm vi chức năng giải thích được, schema/cách chạy kiểm tra được, quyền vừa đủ và phù hợp thi tạo artifact. Số sao GitHub hoặc logo nhà cung cấp không chứng minh độ an toàn, tính tương thích hay việc BTC cho phép.

## Profile MCP đề xuất
| Thành phần | Trạng thái đề xuất | Quyền và lưu ý |
|---|---|---|
| Công cụ file/shell native của host | Ưu tiên nếu đã đủ | Quyền host cũng phải kiểm tra; không tự cấp toàn máy. |
| `aitc-local-media-qa` trong gói | Tùy chọn cho QA media/manifest | 4 tool, stdio local, một thư mục làm việc; không gọi model. Mã mới, chưa được host/BTC chứng nhận. |
| Filesystem reference MCP | Chỉ khi host không có file tool phù hợp | Roots của client có thể thay allowlist args; kiểm tra phạm vi thực sự. Không trỏ home hoặc repo root có secret/hook. |
| Git reference MCP | Không bật mặc định | Git CLI do người thao tác đủ cho 2 máy; tránh reset/force-push/tự đổi remote hoặc public repo. |
| Microsoft Playwright MCP | Chỉ khi đề thực sự cần web/HTML/interaction | Profile trình duyệt riêng, địa chỉ cần dùng; không điều khiển chatbot ngoài BTC hay auto-submit. Allowed origins không phải security boundary. |
| External AI/search/research MCP | Tắt mặc định | Không dùng làm đường vòng; AI/search chỉ theo tài nguyên/quyền BTC xác nhận. |

Các MCP reference được chính dự án mô tả là ví dụ/tham chiếu, không bảo đảm sẵn sàng production. Không tự cài `latest` trong phiên thi; chọn phiên bản, ghi lại, thử trên hai máy trước khi khóa cấu hình.

## Bốn tool local được cung cấp
1. `aitc_media_probe(path)`: đọc codec/duration/dimensions; không chấm nội dung.
2. `aitc_contact_sheet(path, output, frames)`: tạo PNG mới dưới qa/ để xem một số khung hình; không thay xem cả video hoặc nghe audio.
3. `aitc_artifact_manifest(directory)`: size/SHA-256; không đóng băng hay nộp.
4. `aitc_verify_manifest(manifest_path)`: phát hiện sửa/thêm/xóa so với bản lưu.

MCP server không có generic file write, upload, AI sampling, network client, Git mutation, task submission. Đây là phạm vi chức năng, **không phải sandbox hệ điều hành**. FFmpeg có quyền của process; chỉ dùng input đáng tin, phần mềm được cập nhật và quyền OS hạn chế. Chặn đường dẫn ở ứng dụng không bảo vệ khỏi mọi race condition hoặc lỗ hổng decoder.
