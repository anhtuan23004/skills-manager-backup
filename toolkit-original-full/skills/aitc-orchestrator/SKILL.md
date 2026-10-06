---
name: aitc-orchestrator
description: Điều phối toàn bộ lượt thi khi nhận đề hoặc cần biết bước tiếp theo; chọn skill theo ảnh, video, text, audio, kiểm soát hai máy và mốc thời gian.
metadata:
  version: "1.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 00 — Điều phối bài thi

Đọc [hợp đồng chung](references/contract.md) khi dùng skill lần đầu. Đây là skill viết mới cho bộ toolkit, không phải skill chính thức BTC.

## Đầu vào
Đề nguyên văn; giờ T trên hệ thống; rubric nếu có; tình trạng Gateway/hook; thành viên phụ trách hai máy; budget BTC đang hiển thị.

## Quy trình
1. Đọc TEAM_RULES và xác định bộ tài liệu BTC đang áp dụng. Không bắt đầu bằng tạo app.
2. Gọi brief-decoder; đội trưởng xác nhận các đầu ra bắt buộc. Trong lúc đó máy B kiểm tra kết nối, repo, hook, đường xuất file.
3. Gọi concept-choice để chọn tối đa 3 hướng, một hướng chính và một phương án giảm phạm vi. Không chạy nhiều agent tự trị mặc định.
4. Cho vietnam-context-review kiểm tra rủi ro/nội dung ở concept, không đợi đến bản cuối.
5. Production-planner lập danh sách phụ thuộc. Kích hoạt duy nhất những producer cần cho đề.
6. Mục tiêu nội bộ: T+18 khóa concept; T+50 có bản nháp trọn vẹn; T+85 có bản xem được; T+100 có bản kiểm tra; T+112 freeze. Điều chỉnh độ dài từng chặng theo đề, không đổi deadline BTC.
7. Critic kiểm tra từng phiên bản với brief gốc. Giới hạn 2 vòng sửa lớn; sửa cục bộ ưu tiên hơn sinh lại toàn bộ.
8. T+100–112: máy A làm reflection từ evidence; máy B kiểm tra/xuất bản cuối. Nếu bản cuối thay đổi sau reflection, cập nhật chỗ bị ảnh hưởng trước freeze.
9. T+112–120: người duyệt, manifest, push qua quy trình BTC. T+120–130 chỉ nộp. Không auto-submit, đổi repo public hay đổi quyền link.
10. Sự cố: nếu vòng sửa >5 phút mà không tiến triển, báo leader và giảm phạm vi; không đổi toàn bộ công cụ.

## Đầu ra bắt buộc
Bảng stage | máy/người | đầu vào | đầu ra | deadline | trạng thái | blocker.
Ba quyết định cần người xác nhận: brief; concept; final. Quyết định tiêu tiền lớn theo ngưỡng đội đặt.
Chỉ dẫn bước tiếp theo trên từng máy, không quá 5 dòng.

## Kiểm tra trước khi trả kết quả
Không yêu cầu máy thứ ba. Không mặc định triển khai website. Không gọi AI trước khi xác nhận endpoint. Không viết sản phẩm mới sau freeze.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
