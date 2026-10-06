---
name: aitc-video-director
description: Viết shot prompt, tạo video qua Gateway, theo dõi job và duy trì mạch hình; dùng khi đề yêu cầu video hoặc đoạn chuyển động.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 07 — Chỉ đạo video

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Storyboard đã duyệt; source frame; thời lượng/tỷ lệ đề; model/endpoint được test; trần chi phí.

## Quy trình
1. Mỗi request tập trung một cảnh/một hành động. Sắp nhịp kể ở storyboard, không nhồi toàn bộ câu chuyện vào một clip ngắn.
2. Tách chuyển động nhân vật, máy quay và môi trường. Với image-to-video ưu tiên mô tả chuyển động, không mô tả lại dài dòng những gì source frame đã thể hiện.
3. Khóa chi tiết nhân vật/style qua reference và prompt, nhưng chỉ dùng tham số Gateway thực sự hỗ trợ; không bảo đảm consistency tuyệt đối.
4. Thử cảnh rủi ro bằng cấu hình rẻ/ngắn đã được cấp. Ghi rõ seconds, không dựa mặc định.
5. Quy trình video: create → lưu job ID ngay → poll đúng job → download khi completed. Khi processing không tạo lại job. Khi timeout sau POST, trạng thái có thể chưa xác định; hỏi leader, kiểm tra ledger/BTC trước khi tạo lại.
6. Chi phí video tính lúc tạo theo tài liệu BTC; không tự retry POST trả lỗi mạng để tránh tạo tác vụ trùng.
7. Xem clip thật đầu-giữa-cuối và xem chuyển cảnh trong bản ráp. Contact sheet không thay thế xem toàn video/audio.
8. Khi hết thời gian: dùng clip đạt nhất; chỉ đổi sang ảnh tĩnh có chuyển động/dựng thường nếu đề và quy định cho phép; không mô tả đó là video AI mới được sinh.
9. Máy B ráp, kiểm tra đồng bộ âm thanh/chữ và xuất. Không có yêu cầu mặc định phải deploy.

## Công cụ và kiểm chứng theo task

Đọc [Video guide](../../docs/api-guides/04-video-generation.md) và [hướng dẫn thực thi](../../docs/SKILL_EXECUTION.md). Thực hiện theo chuỗi: tạo video (`POST /videos`) → lưu job ID → poll trạng thái (`GET /videos/{id}`) → tải video khi hoàn tất (`GET /videos/{id}/content`). Dùng FFprobe và FFmpeg để kiểm tra thông số và trích xuất frame; ghép clip và audio bằng công cụ biên tập/FFmpeg; kiểm tra bằng xem và nghe thật.

## Đầu ra bắt buộc
video-jobs.csv; clips; review timecode; timeline/assembly instructions; final export theo đề.

## Kiểm tra trước khi trả kết quả
Không chỉ đoán job thành công từ HTTP 200. Không để clip lỗi/blank tiếp tục vào assembly. Không dùng model API ngoài dù Gateway chậm.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
