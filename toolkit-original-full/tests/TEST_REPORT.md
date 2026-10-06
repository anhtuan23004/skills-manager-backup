# Báo cáo kiểm thử kỹ thuật
Ngày: 05/10/2026. Kết quả thực thi: **48 tests đạt, 0 lỗi, không có nhóm test bị skip trong môi trường tạo gói.**

## Đã chạy
| Nhóm | Số test | Phạm vi |
|---|---:|---|
| Workspace | 15 | Đường dẫn, không ghi đè, snapshot/đổi file, permission, deadline, freeze, ZIP. |
| Gateway | 18 | Allowlist/schema, chặn endpoint ngoài, network mock, phân loại 429, không retry POST, lưu text/ảnh, lọc key info, dry-run CLI. |
| MCP | 8 | Handshake, init gate, 4 tools, tool call, error, không shell; một lượt stdio subprocess thực. |
| Media | 5 | FFprobe/FFmpeg trên clip tổng hợp 1 giây: probe, contact sheet, normalize, guard. |
| Skill/config | 2 | 15 SKILL.md frontmatter/contract/heading/độ dài; JSON config. |

Python: 3.13.5. OS: Linux x86_64.
ffmpeg version 7.1.5-0+deb13u1 Copyright (c) 2000-2026 the FFmpeg developers

Lệnh: `python -m unittest discover -s tests -v`.

## Chưa kiểm thử
- Live API/key/model/path thực tế của BTC; không dùng API key của đội.
- Hook AI Log BTC có ghi/gửi đầy đủ mọi tác vụ của helper trong host thật.
- Tương thích trọn vẹn với từng Cursor/Cline/Codex/Gemini host; chưa có host do đội chọn.
- Benchmark chất lượng sáng tạo, hiệu quả prompt, điểm BGK hoặc thử nghiệm người dùng.
- Security audit độc lập hoặc mọi tình huống file decode/race condition. Server stdio là implementation nhỏ, không phải chứng nhận tương thích toàn bộ MCP.

Mọi network trong test đều là mô phỏng. Media test dùng file tổng hợp local, không phải AI generation. Không dùng “48 tests đạt” để tự khẳng định “sẵn sàng thi chính thức”.
