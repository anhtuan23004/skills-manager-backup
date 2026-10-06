---
name: aitc-audio-producer
description: Chuẩn bị narration, phát âm tiếng Việt, TTS/STT và kiểm tra âm thanh; dùng khi bài thi có voice-over hoặc audio.
metadata:
  version: "2.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 08 — Sản xuất audio

Áp dụng [quy tắc chung](../../docs/TEAM_RULES.md); chỉ đọc lại khi chưa có trong ngữ cảnh hoặc quy tắc thay đổi.

## Đầu vào
TTS: kịch bản đã duyệt, voice được Gateway hỗ trợ và thời lượng đề. STT: file audio được phép dùng và yêu cầu transcript. Cả hai: tên riêng/số/chữ viết tắt cần kiểm tra.

## Quy trình
Chọn nhánh theo task: TTS dùng bước 1–5; STT tập trung bước 6; áp dụng QA phù hợp ở bước 7–8. Không yêu cầu kịch bản/voice để phiên âm.

1. Tách narration final khỏi directions. Lập pronunciation sheet cho tên riêng, số, địa danh và chữ viết tắt.
2. Dùng giọng được cấp qua Gateway; không giả giọng người thật/cơ quan hay nhận endorsement không có nguồn.
3. Sinh đoạn thử ngắn, nghe thật. Chọn voice theo độ rõ và phù hợp thông điệp, không chỉ “trang trọng”.
4. TTS qua endpoint đã test; file output không mặc định MP3 chỉ vì đặt đuôi mp3, kiểm tra content type và ffprobe.
5. Đo thời lượng sau tạo. Chỉnh câu/nhịp trước khi tăng tốc quá mức.
6. STT có thể hỗ trợ rà lời, nhưng đối chiếu nghe của người với transcript và script, không coi STT là chứng thực.
7. Không tự thêm dịch vụ tạo nhạc. Nhạc/tư liệu chỉ dùng nếu BTC cấp/cho phép và có quyền sử dụng. Không có nguồn hợp lệ thì không dùng.
8. Kiểm tra âm lượng, clipping, khoảng im lặng, cân bằng nhạc-lời và đồng bộ. Không tuyên bố tuân thủ chuẩn phát sóng cụ thể khi BTC chưa yêu cầu hoặc chưa đo.

## Công cụ và kiểm chứng theo task

Chỉ đọc [TTS guide](../../docs/api-guides/05-text-to-speech.md) khi tạo giọng hoặc [STT guide](../../docs/api-guides/06-speech-to-text.md) khi phiên âm. Thực hiện gọi API trực tiếp theo [hướng dẫn thực thi](../../docs/SKILL_EXECUTION.md). Ghi output path, thời lượng và điểm nghe kiểm tra vào task. Task chỉ STT không cần kịch bản/voice TTS.

## Đầu ra bắt buộc
narration.txt; pronunciation.csv; voice takes; transcript nếu cần; audio-QA.md với thời điểm nghe.

## Kiểm tra trước khi trả kết quả
Không coi audio metadata đạt là nội dung nghe đạt. Không dùng auto-captions/AI voice built-in ngoài Gateway. Không thêm lời mô tả ngoài thông điệp đề.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
