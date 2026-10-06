---
name: aitc-production-planner
description: Lập kế hoạch sản xuất ảnh, video, text hoặc audio theo concept; chia việc cho hai máy và chốt phương án giảm phạm vi.
metadata:
  version: "1.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 04 — Kế hoạch sản xuất

Đọc [hợp đồng chung](references/contract.md) khi dùng skill lần đầu. Đây là skill viết mới cho bộ toolkit, không phải skill chính thức BTC.

## Đầu vào
Concept và brief đã duyệt; deadline; budget hiện tại; cấu hình model đã gọi thử; năng lực hai máy.

## Quy trình
1. Xác định final artifact trước; lùi lại các nguyên liệu bắt buộc. Không bắt buộc full multimodal.
2. Gán asset ID A001... hoặc shot ID S01...; mỗi asset ghi requirement, owner máy, thời gian cần, trạng thái và đường file.
3. Với video: shotlist có thời lượng, hình, hành động, âm thanh, text overlay, input reference, điều kiện đạt; tổng thời lượng phải khớp đề. Test một cảnh khó trước khi sinh cả chuỗi.
4. Với ảnh: bố cục, điểm nhìn, vùng chữ, version plan; chữ quan trọng có thể đặt bằng công cụ biên tập thông thường, khi quy định cho phép.
5. Với text: outline và word count/format theo đề; với audio: kịch bản, nhịp đọc, cách phát âm, thời lượng đo.
6. Máy A phụ trách concept/prompt/visual generation. Máy B phụ trách audio/assembly/export/QA. Một người làm leader/ghi quyết định, không thêm máy.
7. Khoá convention filename: S01_v01.ext; một người sở hữu từng file đang sửa; không cùng ghi một JSONL. Asset lớn trao đổi bằng kênh được BTC cho phép, không tự tạo cloud chia sẻ ngoài.
8. Đặt trần chi phí mỗi task và dự phòng chung. Budget của cả đội là nguồn BTC, không cộng nhầm hai API key thành hai ngân sách.
9. T+50 mục tiêu có bản nháp đầy đủ; T+85 chọn final assets. Phương án dự phòng không được vi phạm format/nội dung đề.

## Đầu ra bắt buộc
production-plan.csv và storyboard.md. Critical path; nhiệm vụ từng máy; checkpoints; fallback cho từng phụ thuộc rủi ro.

## Kiểm tra trước khi trả kết quả
Không dùng video sinh dài/đắt trước khi test cảnh. Không dành toàn bộ thời gian làm outline. Không tạo nhạc bằng dịch vụ AI ngoài; API sinh nhạc chưa được tài liệu xác nhận thì coi chưa có.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
