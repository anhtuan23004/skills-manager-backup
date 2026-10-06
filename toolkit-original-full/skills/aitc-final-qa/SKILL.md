---
name: aitc-final-qa
description: Kiểm tra bản nộp bằng yêu cầu, file thực tế và bằng chứng mới; dùng trước freeze, không thay thế kiểm tra bằng mắt/tai.
metadata:
  version: "1.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 11 — Kiểm tra bản cuối

Đọc [hợp đồng chung](references/contract.md) khi dùng skill lần đầu. Đây là skill viết mới cho bộ toolkit, không phải skill chính thức BTC.

## Đầu vào
Bản final cụ thể; requirements; metadata; claim/source ledger; prompts; repo trạng thái; hướng dẫn nộp.

## Quy trình
1. Chọn chính xác version và đường file sẽ nộp, không test một bản rồi nộp bản khác.
2. Mở ảnh/text; phát video/audio từ đầu đến cuối. Kiểm tra chính tả, dấu tiếng Việt, artifact, đọc được chữ, âm thanh và nhịp.
3. Dùng công cụ xác định kích thước, duration, codec, dung lượng. So với đề; không lấy thông số quay giám sát làm thông số sản phẩm.
4. Mỗi requirement có PASS/FAIL/UNVERIFIED và evidence. Kiểm tra lại correction sau vòng critique.
5. Chạy context-review cho claim hoặc hình nhạy cảm; rà nguồn/quyền tư liệu và không giả chứng nhận.
6. Kiểm tra file final, prompt/source, repo đúng BTC và không đưa secret vào package. Không sửa log BTC để “làm sạch”.
7. Repo media lớn: không tự push file > giới hạn training; giữ source/prompt trong repo, file nộp theo cổng. Không tự biến repo private thành public khi hướng dẫn mâu thuẫn.
8. Leader duyệt. Tạo manifest hash của final. Hash giúp kiểm tra phiên bản, không thay timestamp chứng thực hoặc đánh giá nội dung.

## Đầu ra bắt buộc
final-qa.md; manifest.json; unresolved items; tên người kiểm tra và thời điểm thật.

## Kiểm tra trước khi trả kết quả
Không nói PASS khi thiếu evidence. Không đồng nhất ffprobe thành công với đáp ứng đề. Không tự submit/đổi quyền chia sẻ.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
