# AI Thực Chiến — Toolkit Chung khảo

## Bắt đầu ở đâu?
Khi BTC cấp API: chạy [check resource](docs/RESOURCE_CHECK.md) để xem model khả dụng,
budget key/đội và rate limit. `python3 scripts/check_resources.py` chỉ đọc thông tin;
thêm `--smoke` để thử đúng một request nhỏ `deepseek-flash`, tắt thinking.

Luồng chính: **đọc đề → lập plan → chọn skill → thực thi → kiểm chứng**. Dán [prompt bắt đầu](prompts/00_start.md) cùng đề vào agent đã cấu hình Gateway BTC. Agent chọn skill theo bài; không cần cài framework hay wrapper phức tạp để bắt đầu.

1. [Orchestrator](skills/aitc-orchestrator/SKILL.md) đọc đề/plan hiện có và chọn nhánh từ [routing](skills/aitc-orchestrator/references/routing.md).
2. Planner tạo [execution-plan](templates/execution-plan.md): mỗi task có requirement, skill, API guide tham chiếu, file output, check và timebox.
3. Nếu đã giao thực thi, agent làm mẫu/luồng đầu tiên rồi tiếp tục task trong phạm vi được cấp. Đọc từng skill và guide khi cần; thực thi trực tiếp theo [hướng dẫn](docs/SKILL_EXECUTION.md).
4. Sau mỗi task: kiểm tra output thật, ghi evidence và bước tiếp theo. Dùng [prompt tiếp tục](prompts/03_produce.md) khi quay lại bài đang làm.
5. Final QA → reflection nếu cần → người duyệt → đóng gói/nộp theo đề và quyền đã cấp. Hướng dẫn vận hành chi tiết ở [GUIDE](GUIDE.md).

## Gói này có gì?
| Thư mục | Nội dung |
|---|---|
| `skills/` | 15 skill và routing hướng dẫn agent; dùng chung quy tắc trong `docs/TEAM_RULES.md`. |
| `prompts/` | 10 prompt điều phối theo từng giai đoạn làm bài. |
| `templates/` | Execution-plan và các biểu mẫu brief, requirements, decisions, storyboard, asset ledger, QA. |
| `docs/` | Vận hành 2 máy, hướng dẫn gọi API BTC, chọn MCP, kiểm tra an toàn, video reflection. |
| `evals/` | 16 tình huống kiểm tra hành vi và xử lý tình huống của skill. |
| `scripts/` | Check resource Gateway BTC và test offline; Python stdlib, không cần cài dependency. |

## Ba ranh giới phải giữ
- **Bộ công cụ gồm chỉ dẫn và tiện ích kiểm tra:** Skills/prompts/docs hướng dẫn giải đề; script resource kiểm tra API được cấp, không phụ thuộc wrapper bên thứ ba.
- **Skill là chỉ dẫn; MCP là công cụ; model của agent là một lớp khác:** Cài skill của nguồn nào không bắt buộc gọi model của nguồn đó. Mọi AI trong phiên thi vẫn phải qua Gateway BTC.
- **Gói này là tài liệu chuẩn bị nội bộ của đội:** Không có tuyên bố “được phép toàn bộ”, “an toàn tuyệt đối” hoặc “bảo đảm điểm cao”. Đội tự chịu trách nhiệm kiểm tra tính tuân thủ quy chế thi của BTC.

MCP là tùy chọn. Đội có thể dùng skills kết hợp công cụ file/shell/media có sẵn trong agent, không bắt buộc cài thêm MCP.
