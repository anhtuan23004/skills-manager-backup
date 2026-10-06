---
name: aitc-orchestrator
description: Nhận đề, chọn skill và điều phối thực thi theo plan cho text, ảnh, video, audio hoặc app/RAG khi đề yêu cầu; dùng lúc bắt đầu hoặc tiếp tục bài đang làm.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 00 — Điều phối bài thi

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Đề nguyên văn; giờ T trên hệ thống; rubric nếu có; tình trạng Gateway/hook; thành viên phụ trách hai máy; budget BTC đang hiển thị.

## Quy trình
1. Đọc [TEAM_RULES](../../docs/TEAM_RULES.md), đề và trạng thái công việc hiện có. Nếu đã có brief/plan được chấp thuận, tiếp tục task chưa xong; không lập lại toàn bộ.
2. Gọi brief-decoder; đội trưởng xác nhận các đầu ra bắt buộc. Trong lúc đó máy B kiểm tra kết nối, repo, hook, đường xuất file. Khi BTC cấp key, chạy `python3 scripts/check_resources.py` từ gốc toolkit theo [RESOURCE_CHECK](../../docs/RESOURCE_CHECK.md): model list, budget key/đội, rate limit. Chỉ thêm `--smoke` khi cần thử một request nhỏ có phí; dùng `deepseek-flash` tắt thinking, không thử hàng loạt model hoặc tự retry. Thiếu dữ liệu thì ghi UNVERIFIED, không suy ra budget vô hạn.
3. Gọi concept-choice để chọn tối đa 3 hướng, một hướng chính và một phương án giảm phạm vi. Không chạy nhiều agent tự trị mặc định.
4. Dùng vietnam-context-review khi có claim, biểu tượng, bối cảnh Việt Nam hoặc nội dung cần kiểm chứng. Bài nhỏ có thể gộp brief/concept/plan trong một lượt; quyết định đã được người dùng xác nhận không hỏi lại.
5. Đọc [bản đồ chọn skill](references/routing.md), rồi dùng production-planner viết [execution-plan](../../templates/execution-plan.md). Mỗi task phải có requirement, skill, helper/API guide, input, file output, check, phụ thuộc và timebox. Chỉ nạp producer/reference của task sắp làm. Chỉ xây giao diện khi deliverable cần.
6. Mục tiêu nội bộ theo [bảng 120 phút](../../GUIDE.md#5-quy-trình-120-phút-trên-2-máy): T+18 khóa concept; T+30 mẫu/pipeline đầu chạy được; T+65 bản nháp trọn vẹn; T+90 chọn bản cuối; T+100 bản ứng viên đã mở/xem/nghe; T+112 freeze. Điều chỉnh độ dài từng chặng theo đề, không đổi deadline BTC.
7. Critic kiểm tra từng phiên bản với brief gốc. Giới hạn 2 vòng sửa lớn; sửa cục bộ ưu tiên hơn sinh lại toàn bộ.
8. T+100–112: máy A làm reflection từ evidence; máy B kiểm tra/xuất bản cuối. Nếu bản cuối thay đổi sau reflection, cập nhật chỗ bị ảnh hưởng trước freeze.
9. Gần deadline: final QA và reflection nếu đề yêu cầu, người duyệt, manifest; chỉ commit/push/nộp theo yêu cầu và quyền đã được cấp. Với khung thi 120+10 phút đã xác nhận, T+120–130 chỉ nộp. Không auto-submit, đổi repo public hay đổi quyền link.
10. Sự cố: nếu vòng sửa >5 phút mà không tiến triển, báo leader và giảm phạm vi; không đổi toàn bộ công cụ.

## Đầu ra bắt buộc
Trong workspace: brief/requirements và execution-plan.md với các task có thể thực thi. Sau mỗi task, cập nhật trạng thái, đường dẫn bằng chứng và bước tiếp theo; FAIL thì debug, chưa kiểm tra thì UNVERIFIED.
Giữ các xác nhận brief/concept/final đã có; chỉ hỏi khi còn lựa chọn làm thay đổi phạm vi, quyền hoặc chi phí ngoài mức được cấp. Không dừng lại ở plan nếu người dùng đã yêu cầu triển khai trong phạm vi đó.
Chỉ dẫn bước tiếp theo trên từng máy, không quá 5 dòng.

## Kiểm tra trước khi trả kết quả
Không yêu cầu máy thứ ba. Không mặc định triển khai website. Không gọi AI trước khi xác nhận endpoint. Không viết sản phẩm mới sau freeze.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
