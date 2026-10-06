# AI Thực Chiến — Toolkit Chung khảo

## Bắt đầu ở đâu?
1. Đọc `GUIDE.md` để hiểu flow, vai trò và các điểm phải chốt.
2. Đọc `docs/INSTALL_AND_RUN.md`, khai báo những thành phần đã được BTC cho phép; không copy cả toolkit vào repo BTC một cách mặc định.
3. Trong agent đã cấu hình mọi AI qua Gateway BTC, mở `prompts/00_start.md` cùng đề bài. Agent dùng `skills/aitc-orchestrator/SKILL.md` để chọn skill cần thiết.
4. Dùng `docs/OPERATING_FLOW.md` làm bảng điều hành trên 2 máy. Ghi quyết định thực tế vào `templates/decisions.md`.
5. Khi gần hoàn tất: Final QA → Solution Reflection → đội duyệt → freeze trước T+120 → nộp đúng yêu cầu.

## Gói này có gì?
| Thư mục | Nội dung |
|---|---|
| `skills/` | 15 skill viết mới; mỗi skill có SKILL.md và contract. |
| `prompts/` | 10 prompt gọi theo giai đoạn. |
| `templates/` | 16 biểu mẫu trống: requirements, decisions, storyboard, asset ledger, claims, QA, reflection, submission… |
| `runtime/` | Python CLI gọi Gateway, kiểm tra/chuẩn hóa media, manifest/freeze/package và MCP local 4 tool. |
| `config/` | Cấu hình ví dụ; live network mặc định chưa được bật. |
| `examples/` | 6 payload kỹ thuật để tập API; không dùng output tập luyện làm bài thi thật. |
| `evals/` | 16 tình huống kiểm tra hành vi skill. Chưa chạy benchmark LLM thực tế. |
| `tests/` | 48 kiểm thử offline đã chạy đạt trong môi trường tạo gói; báo cáo giới hạn đi kèm. |
| `docs/` | Vận hành, cài đặt, chọn MCP, đánh giá giá trị, an toàn, video reflection. |

## Ba ranh giới phải giữ
- **Được chuẩn bị skills/prompts/MCP:** theo thông tin đội cung cấp. **Code wrapper, helper, template, font, stock media, tài nguyên đi kèm** không tự động thuộc ngoại lệ này; phải xác nhận phạm vi riêng.
- **Skill là chỉ dẫn; MCP là công cụ; model của agent là một lớp khác.** Cài skill của nguồn nào không bắt buộc gọi model của nguồn đó. Mọi AI trong phiên thi vẫn phải qua BTC.
- **Gói này chưa được BTC phê duyệt và chưa được kiểm thử live với Gateway/host của đội.** Không có tuyên bố “được phép toàn bộ”, “an toàn tuyệt đối” hoặc “bảo đảm điểm cao”.

MCP là tùy chọn. Đội có thể dùng skills + công cụ file/media có sẵn trong agent và CLI, không bắt buộc cài thêm MCP.
