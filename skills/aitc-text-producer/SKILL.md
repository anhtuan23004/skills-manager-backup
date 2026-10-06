---
name: aitc-text-producer
description: Viết script, nội dung hoặc văn bản đầu ra tiếng Việt từ brief đã duyệt; dùng cho bài text, lời bình, phụ đề hoặc câu chữ trong hình/video.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 05 — Sản xuất text

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Brief; concept; outline; dữ liệu có nguồn; độ dài/giọng điệu/định dạng yêu cầu.

## Quy trình
1. Chốt chức năng của văn bản: giải thích, kể chuyện, hướng dẫn, kêu gọi hành động hay nội dung độc lập. Không thêm mục tiêu ngoài đề.
2. Dựng outline ngắn theo requirement; viết bản nháp từ nguồn đã xác minh.
3. Phân biệt câu factual và câu sáng tạo. Gắn claim ID cho dữ kiện; không bịa trích dẫn, hotline, cơ quan, điều luật hoặc khảo sát.
4. Với narration, viết để nói; câu có nhịp, đúng dấu, không chèn chú thích kỹ thuật vào text đọc. Với phụ đề, giữ ý và kiểm tra đồng bộ sau xuất.
5. Với infographic/poster, rút ngắn mà giữ nghĩa; không lấy mỹ thuật làm lý do bỏ cảnh báo bắt buộc.
6. Đọc thử/đếm từ/đo thời lượng; không quy đổi số từ thành thời lượng chắc chắn. Ghi cách đo và phiên bản.
7. Critic đối chiếu brief; sửa nhiều nhất 3 điểm có tác động. Xuất UTF-8 và bản final không lẫn chú thích nội bộ.

## Công cụ và kiểm chứng theo task

Đọc [Text guide](../../docs/api-guides/02-text-generation.md) khi cần gọi text/responses và [hướng dẫn thực thi](../../docs/SKILL_EXECUTION.md). Nếu agent hiện tại đã chạy qua Gateway BTC và soạn thảo trực tiếp được thì không cần thêm bước gọi phụ qua script ngoài.

Nội dung cần thông tin mới: đọc [Grounding](../../docs/api-guides/07-web-grounding.md), chỉ bật search trong phạm vi được phép. Hỏi đáp tài liệu: theo [RAG workflow](../aitc-production-planner/references/rag-workflow.md); trả lời từ context có nguồn, nêu thiếu evidence khi không đủ dữ liệu.

## Đầu ra bắt buộc
text-vNN.md hoặc narration.txt; claim ledger; ghi rõ nội dung final và ghi chú không đưa vào thành phẩm.

## Kiểm tra trước khi trả kết quả
Không phóng đại ích lợi. Không mô tả sản phẩm như đã triển khai thật. Không mặc định văn phong hành chính vì cuộc thi được bảo trợ.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
