---
name: aitc-final-qa
description: Kiểm tra bản nộp bằng yêu cầu, file thực tế và bằng chứng mới; dùng trước freeze, không thay thế kiểm tra bằng mắt/tai.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 11 — Kiểm tra bản cuối

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
Bản final cụ thể; requirements; metadata; claim/source ledger; prompts; repo trạng thái; hướng dẫn nộp.

## Quy trình
1. Chọn chính xác version và đường file sẽ nộp, không test một bản rồi nộp bản khác.
2. Với media/text: mở ảnh/text, phát video/audio từ đầu đến cuối; kiểm tra chữ, nội dung và âm thanh. Với app: chạy luồng người dùng và case lỗi theo requirement.
3. Nếu có file media, đo kích thước, duration, codec, dung lượng theo đề. Với app/RAG, kiểm tra chạy thử thực tế và bằng chứng nguồn; không dùng compile thay kiểm tra chức năng.
4. Mỗi requirement có PASS/FAIL/UNVERIFIED và evidence. Kiểm tra lại correction sau vòng critique.
5. Chạy context-review cho claim hoặc hình nhạy cảm; rà nguồn/quyền tư liệu và không giả chứng nhận.
6. Kiểm tra file final, prompt/source, repo đúng BTC và không đưa secret vào package. Không sửa log BTC để “làm sạch”.
7. Repo media lớn: không tự push file > giới hạn training; giữ source/prompt trong repo, file nộp theo cổng. Không tự biến repo private thành public khi hướng dẫn mâu thuẫn.
8. Leader duyệt. Tạo manifest hash của final. Hash giúp kiểm tra phiên bản, không thay timestamp chứng thực hoặc đánh giá nội dung.

## Công cụ và kiểm chứng theo task

Đọc execution-plan cùng requirements để chọn check theo deliverable. Với app: chạy luồng input → output và case lỗi theo [app workflow](../aitc-production-planner/references/app-workflow.md); với RAG: kiểm tra nguồn và câu ngoài tài liệu theo [RAG workflow](../aitc-production-planner/references/rag-workflow.md). Với media: kiểm tra bằng FFprobe/FFmpeg và xem/nghe file thực theo [SKILL_EXECUTION](../../docs/SKILL_EXECUTION.md). Không yêu cầu mọi loại check cho mọi bài; ghi UNVERIFIED cho framework, trình duyệt hoặc live API chưa chạy.

## Đầu ra bắt buộc
final-qa.md; manifest.json; unresolved items; tên người kiểm tra và thời điểm thật.

## Kiểm tra trước khi trả kết quả
Không nói PASS khi thiếu evidence. Không đồng nhất ffprobe thành công với đáp ứng đề. Không tự submit/đổi quyền chia sẻ.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
