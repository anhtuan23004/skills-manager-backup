---
name: aitc-production-planner
description: Biến brief thành task thực thi gắn skill, helper/API, output và check; lập kế hoạch media hoặc xây app/RAG khi đề yêu cầu.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 04 — Kế hoạch sản xuất

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Concept và brief đã duyệt; deadline; budget hiện tại; cấu hình model đã gọi thử; năng lực hai máy.

## Quy trình
1. Xác định final artifact và requirement trước; lùi lại các nguyên liệu bắt buộc. Đọc [routing](../aitc-orchestrator/references/routing.md) để chọn skill. Không bắt buộc full multimodal hoặc app.
2. Gán asset ID A001... hoặc shot ID S01...; mỗi asset ghi requirement, owner máy, thời gian cần, trạng thái và đường file.
3. Với video: shotlist có thời lượng, hình, hành động, âm thanh, text overlay, input reference, điều kiện đạt; tổng thời lượng phải khớp đề. Test một cảnh khó trước khi sinh cả chuỗi.
4. Với ảnh: bố cục, điểm nhìn, vùng chữ, version plan; chữ quan trọng có thể đặt bằng công cụ biên tập thông thường, khi quy định cho phép.
5. Với text: outline và word count/format theo đề; với audio: kịch bản, nhịp đọc, cách phát âm, thời lượng đo.
6. Máy A phụ trách concept/prompt/visual generation. Máy B phụ trách audio/assembly/export/QA. Một người làm leader/ghi quyết định, không thêm máy.
7. Khoá convention filename `<ID>_<máy>_v<NN>.ext` (ví dụ `S02_A_v03.mp4`, `A001_B_v01.png`); một người sở hữu từng file đang sửa; không cùng ghi một JSONL. Asset lớn trao đổi bằng kênh được BTC cho phép, không tự tạo cloud chia sẻ ngoài.
8. Đặt trần chi phí mỗi task và dự phòng chung. Budget của cả đội là nguồn BTC, không cộng nhầm hai API key thành hai ngân sách.
9. Theo [bảng 120 phút](../../GUIDE.md#5-quy-trình-120-phút-trên-2-máy): T+65 có bản nháp đầy đủ; T+90 chọn final assets. Phương án dự phòng không được vi phạm format/nội dung đề.

## Nối plan với thực thi

- Dùng [execution-plan](../../templates/execution-plan.md) làm bảng chính: mỗi task có skill/reference, helper/operation + guide, input, output path, check/lệnh và tiêu chí đạt. Đọc [SKILL_EXECUTION](../../docs/SKILL_EXECUTION.md) để tái sử dụng Gateway/media thay vì viết wrapper mới.
- Với app/API/UI được yêu cầu, đọc [app workflow](references/app-workflow.md). Với hỏi đáp tài liệu, đọc [RAG workflow](references/rag-workflow.md). Không đọc cả hai nếu task không cần.
- Làm một luồng hoặc mẫu nhỏ có thể kiểm chứng trước, rồi mở rộng theo thứ tự phụ thuộc. Đã được giao thực thi thì tiếp tục task sau khi plan đủ rõ; giữ các quyết định đã xác nhận, không xin lại cùng một quyền.
- Task sinh nội dung ghi rõ dry-run/live và trần chi phí. Task biên tập local ghi không cần API. Sau check, cập nhật evidence và trạng thái thay vì lập lại plan.

## Đầu ra bắt buộc
execution-plan.md (hoặc bảng tương đương trong brief): task, skill, công cụ, file, check, phụ thuộc, người phụ trách và timebox. Thêm [production-plan.csv](../../templates/production-plan.csv) khi có nhiều asset và [storyboard.md](../../templates/storyboard.md) khi cần trình tự cảnh; không tạo storyboard cho bài chỉ có text hoặc app. Ghi critical path và fallback.

## Kiểm tra trước khi trả kết quả
Không dùng video sinh dài/đắt trước khi test cảnh. Không dành toàn bộ thời gian làm outline. Không tạo nhạc bằng dịch vụ AI ngoài; API sinh nhạc chưa được tài liệu xác nhận thì coi chưa có.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
