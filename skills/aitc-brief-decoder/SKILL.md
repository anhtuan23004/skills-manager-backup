---
name: aitc-brief-decoder
description: Phân tích nguyên văn đề, trích deliverable và rubric, ghi rõ chỗ chưa xác định; dùng ngay khi mở đề và khi BTC bổ sung yêu cầu.
metadata:
  version: "1.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 01 — Giải mã đề

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Đề nguyên văn và tệp kèm theo; rubric chính thức nếu có; mốc thời gian và định dạng nộp.

## Quy trình
1. Đọc toàn bộ đề; xem hình/bảng khi parsed text không đầy đủ. Không coi các ví dụ trong tài liệu training là yêu cầu đề.
2. Tách: đầu ra; người xem; mục tiêu/thông điệp; nguồn/tài sản được phép; thông số file; nội dung phải/không được có; tiêu chí chấm; cách nộp.
3. Gán R01... cho từng yêu cầu. Mỗi mục có trích đoạn ngắn hoặc vị trí nguồn, cách kiểm tra và trạng thái.
4. Đánh dấu OFFICIAL cho yêu cầu có nguồn, ASSUMPTION cho suy luận đội, PROPOSED cho tiêu chí nội bộ. Không suy ra trọng số từ tổ chức bảo trợ.
5. Chọn loại bài: text, image, video, audio, kết hợp hoặc interactive nếu đề ghi. Đầu ra tối thiểu vẫn phải giữ mọi yêu cầu bắt buộc.
6. Nêu tối đa 3 câu hỏi ảnh hưởng lớn; các điều chưa rõ không trọng yếu có thể chốt giả định có nhãn để tiếp tục.
7. Viết một câu diễn giải đề và trình đội trưởng duyệt.

## Đầu ra bắt buộc
brief.md và requirements.csv: id, requirement, source, kind, check, owner, status, evidence.
Một câu: Tạo [đầu ra] cho [đối tượng] để [mục đích] theo [ràng buộc].

## Kiểm tra trước khi trả kết quả
Không nhầm video reflection 3–6 phút với video bài thi. Không tự tạo KPI, persona, dữ liệu hay thông số xuất. Không bỏ yêu cầu để kịp giờ mà vẫn ghi PASS.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
