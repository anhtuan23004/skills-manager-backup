---
name: aitc-systematic-debug
description: Chẩn đoán lỗi Gateway, file, export hoặc đồng bộ trong lúc thi; dùng khi request lỗi, clip không tải được hoặc output không mở được.
metadata:
  version: "1.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 10 — Xử lý sự cố

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Thông báo lỗi không chứa secret; operation/model; thời điểm; job/request ID; lần cuối thành công; số phút còn.

## Quy trình
1. Ghi symptom và cách tái hiện nhỏ nhất; không đổi nhiều tham số/công cụ cùng lúc.
2. Phân loại: 401 key; 403 quyền/model; 400 schema/endpoint; 429 rate hoặc budget; timeout; processing; lỗi file/codec. Dựa thông báo thực tế, không chỉ mã HTTP.
3. 429 rate: đợi/backoff theo hướng dẫn. 429 budget: đợi không tăng ngân sách, dừng và giảm chi phí/báo leader.
4. Timeout sau POST tạo media: chưa biết tác vụ đã tạo chưa; không retry tự động. Poll job đã có, kiểm tra nhật ký/BTC.
5. Model/endpoint mismatch: đối chiếu docs BTC, không đổi sang API bên thứ ba hoặc gửi key BTC ra provider.
6. Kiểm tra một giả thuyết mỗi lần; test lại bằng cùng input nhỏ; lưu evidence kết quả.
7. Sau tối đa 5 phút không khắc phục: báo leader, chọn fallback đã duyệt giữ yêu cầu. Không chờ một job vô hạn.
8. Ghi incident và quyết định; không xóa record lỗi, không dựng log giả. Nếu lộ credential: dừng, liên hệ BTC; không tự sửa log gốc.

## Đầu ra bắt buộc
incident.md: symptom / evidence / hypothesis / test / result / next action / owner.

## Kiểm tra trước khi trả kết quả
Không ghi “fixed” khi chưa chạy lại. Không bắn request vô hạn. Không auto-update dependency hoặc đổi framework giữa phiên.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
