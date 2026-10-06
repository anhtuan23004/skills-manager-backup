---
name: aitc-toolkit-evaluator
description: Kiểm thử skill, MCP và toàn bộ luồng hai máy trước ngày thi; dùng khi chuẩn bị hoặc thay đổi toolkit, không tự chạy benchmark tốn phí trong giờ thi.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 14 — Đánh giá toolkit trước thi

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Bộ skill hiện tại; evals/cases.json; máy thi; công cụ/hook/Gateway test được phép; ngân sách luyện.

## Quy trình
1. Kiểm tra metadata SKILL.md và route: đúng nhiệm vụ thì kích hoạt, sai nhiệm vụ thì không kéo thêm tool.
2. Lấy ca thử có outcome quan sát được; test cả đầu vào rõ, thiếu nguồn, prompt injection, typo Việt, mâu thuẫn format và hết giờ.
3. Chạy so sánh có skill/không skill trên cùng brief bằng Gateway được phép; cùng model và giới hạn. Không ghi performance giả khi chưa chạy.
   Với luồng skill-first mới, dùng [đề luyện routing và timing](../../evals/skill-first-rehearsal.md): đo thời gian tới plan thực thi được, output đầu tiên đạt và số lần phải sửa. Không kết luận nhanh hơn chỉ từ unit test hoặc số lượng file.
4. Đánh giá artifact/decision thật bởi người; creative quality không có test string đơn giản thay hoàn toàn.
5. Kiểm tra kỹ năng của agent: khả năng đọc đề, bám sát rubric, không tự ý mở rộng phạm vi, phân định rõ ràng giữa dữ kiện thật và suy đoán.
6. Test kết nối Gateway BTC qua agent thực tế; kiểm tra hook ghi nhận log đầy đủ.
7. Tổng duyệt đúng 2 máy, 120 phút + 10 phút nộp; không dùng máy thứ ba hoặc người ngoài hỗ trợ.
8. Ghi kết quả, lỗi và kinh nghiệm rút ra trước ngày thi.

## Đầu ra bắt buộc
evaluation-report.md: case / expected / observed / pass-fail-unverified / evidence / next fix. Readiness checklist cho hai máy.

## Kiểm tra trước khi trả kết quả
Không gọi bộ skill “đã benchmark tốt” khi mới kiểm tra cấu trúc. Không cài plugin mới trong phiên thi. Không suy ra an toàn chỉ vì MCP có nhiều sao GitHub.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
