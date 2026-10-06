---
name: aitc-submission-controller
description: Đóng gói, đối chiếu manifest và hướng dẫn người nộp đúng thời hạn; dùng sau final QA và trước/sau thao tác nộp của người.
metadata:
  version: "1.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 13 — Freeze và nộp

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Bản đã leader duyệt; manifest; source repo BTC; hướng dẫn nộp; deadline hiện trên hệ thống.

## Quy trình
1. Phân biệt deliverable chính, source/prompt, video reflection và video ghi hình giám sát. Không trộn tất cả vào một file mặc định.
2. So tên/version/hash bản nộp với bản QA. Giới hạn training: tổng attachment 500 MB, tối đa 20 file; vẫn đọc đề/cổng thực tế nếu có cập nhật.
3. Người kiểm tra repo/source/prompts và log theo BTC. Không ghi đè hooks hoặc tự thay đổi visibility repo để khớp một slide.
4. Từ T+120 chỉ thao tác nộp. Không gọi generation, sửa video, viết lại nội dung hay export bản có nội dung khác.
5. Người nộp thực hiện qua hệ thống; agent chỉ hỗ trợ checklist. Đòi evidence nộp thành công: trạng thái, thời gian, title/file đúng. Không kết luận “đã nộp” từ lệnh zip.
6. Giữ bản ghi hình gốc theo yêu cầu; video reflection là bản riêng. Bổ sung theo Google Form trong 24 giờ, thời lượng reflection theo hướng dẫn 3–6 phút.
7. Link video phải có quyền truy cập/tải theo BTC. Việc bật quyền là thao tác người xác nhận, không mở rộng quyền mặc định.
8. Sau nộp, không sửa source/final ngoài quy trình BTC; nếu cần đính chính, liên hệ BTC.

## Đầu ra bắt buộc
submission-checklist.md; receipt.md (chỉ điền khi thực sự có receipt); danh sách file/links đã xác minh.

## Kiểm tra trước khi trả kết quả
Không tự nộp, gửi mail, đổi quyền link hoặc làm public repo. Không coi ZIP có hash là đã qua cổng nộp. Không bỏ video giám sát.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
