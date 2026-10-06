# Runbook trên 2 máy
Nguồn thời gian/thiết bị: 'đã có trong tài liệu hướng dẫn của BTC'. Các giờ chốt giữa phiên là đề xuất đội.

## Khi đề mở
Mở `prompts/00_start.md`. Nạp đề đầy đủ và tài nguyên được phép. Chỉ nạp skill orchestrator/brief decoder trước. Đội trưởng xác nhận **loại file cuối**, yêu cầu bắt buộc, tiêu chí có thật và câu chưa rõ. Không tự xem đề ảnh/video thành bài ứng dụng.

## Khi chọn concept
Gọi `prompts/01_choose_concept.md`, tối đa 3 hướng; đánh giá phù hợp đề/ý nghĩa/chất lượng/thời gian/rủi ro. Máy B phản biện khả năng hoàn thành. `02_context_review.md` kiểm tra bối cảnh và độ tin cậy; không làm thành một vòng “đổi đề cho hợp cơ quan bảo trợ”. Đội chốt, ghi `decisions.md`.

## Khi sản xuất
Planner chia đầu ra thành phần nhỏ, đặt owner A/B, đặt thời gian duyệt mẫu, nguồn asset và fallback. Máy A tạo asset; Máy B xuất thử/lắp bản thô ngay khi có mẫu. Tên file `<ID>_<máy>_v<NN>.ext`, không ghi đè: `S02_A_v03.mp4`.

| Loại đề | Nhánh ưu tiên | Bản nháp phải có |
|---|---|---|
| Văn bản | outline → draft → critique → rewrite | Toàn bộ cấu trúc, không chỉ mở bài. |
| Ảnh/poster | visual direction → bố cục → ảnh → typography → QA | Đủ thông điệp và chữ bắt buộc, không chỉ ảnh đẹp. |
| Video | storyboard → keyframe/clip → VO → assemble → QA | Từ đầu đến cuối, dù asset chưa đều chất lượng. |
| Audio | script → pronunciation → TTS → edit → listen | Nội dung hoàn chỉnh, giọng nghe được. |
| Multimodal | Các nhánh có cùng concept/asset ledger | Đồng nhất nhân vật, câu chuyện và thuật ngữ. |

## Khi critique
Mở chính file hoặc nghe/xem thực tế; input vào critic là đề + version hiện tại + bằng chứng quan sát. Model không có công cụ đọc modality đó phải đánh dấu UNVERIFIED. Mỗi vòng giữ điểm tốt và sửa tối đa 3 lỗi lớn; không regenerate toàn bộ vì cảm giác.

## Khi gần hết giờ
T+90 chọn bản cuối, không mở hướng mới (xem [bảng 120 phút](../GUIDE.md#5-quy-trình-120-phút-trên-2-máy)); T+100–112 QA/Reflection song song. Reflection ghi version đang nói tới. Sau sửa final, cập nhật các nhận xét liên quan trước freeze. T+112–120 đội duyệt và freeze, commit/push theo BTC. T+120–130 chỉ nộp.

## Phân vùng file và giao việc
- Cùng một repo BTC, nhưng mỗi file có một người sửa chính. Chỉ merge sau khi người nhận biết version nào đã duyệt.
- Media lớn không ép vào Git thông thường nếu vượt giới hạn; dùng đường nộp BTC cho phép, giữ manifest/asset ledger. Không tự chia sẻ công khai.
- Luôn có một người duyệt final độc lập. Commit/push không chứng minh nội dung đã đúng đề; cần cả QA.
- Có thể dùng máy B chạy AI text/audio, không cứng nhắc coi chỉ máy A được gọi AI. Budget vẫn chung.

## Khi có sự cố
Budget429: dừng, kiểm tra chi tiêu. Rate429: chờ có giới hạn. Timeout POST tạo video: không bấm tạo lại ngay, lưu tình trạng chưa rõ/job nếu có. Mất logging/giám sát: ghi nhận và báo BTC, không tự chế hoặc sửa log. Không đổi sang chatbot/API ngoài BTC để “cứu bài”.
