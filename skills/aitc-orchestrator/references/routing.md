# Chọn skill từ deliverable

Đọc bảng này khi nhận đề hoặc khi đề đổi đầu ra. Đường dẫn trong bảng tương đối với file này. Skill là chỉ dẫn cho agent hiện tại, không tự tạo thêm agent/máy.

Luồng chung: [brief-decoder](../../aitc-brief-decoder/SKILL.md) → [production-planner](../../aitc-production-planner/SKILL.md) → skill của task → [artifact-critic](../../aitc-artifact-critic/SKILL.md) → [final-qa](../../aitc-final-qa/SKILL.md). Dùng [concept-choice](../../aitc-concept-choice/SKILL.md) nếu cần chọn hướng sáng tạo; bỏ bước lựa chọn lại khi hướng đã chốt.

| Đầu ra đề yêu cầu | Skill thực thi / reference cần đọc | Helper/API cần thiết | Bằng chứng đạt |
|---|---|---|---|
| Bài viết, tóm tắt, kịch bản | [text-producer](../../aitc-text-producer/SKILL.md) | [Text](../../../docs/api-guides/02-text-generation.md) | File UTF-8; kiểm tra nội dung, độ dài, nguồn |
| Poster hoặc bộ ảnh | [image-director](../../aitc-image-director/SKILL.md); text-producer khi có chữ | [Image](../../../docs/api-guides/03-image-generation.md) | Xem ảnh thật và kiểm tra kích thước/chữ |
| Video có lời bình | [video-director](../../aitc-video-director/SKILL.md), text-producer, [audio-producer](../../aitc-audio-producer/SKILL.md); image-director chỉ khi cần frame | [Video](../../../docs/api-guides/04-video-generation.md), [TTS](../../../docs/api-guides/05-text-to-speech.md), FFprobe | MP4 ráp hoàn chỉnh, thời lượng, xem/nghe từ đầu đến cuối |
| Thuyết minh hoặc transcript | [audio-producer](../../aitc-audio-producer/SKILL.md) | [TTS](../../../docs/api-guides/05-text-to-speech.md) / [STT](../../../docs/api-guides/06-speech-to-text.md) | Audio/transcript, tên riêng, thời gian nghe kiểm tra |
| Nội dung cần thông tin mới | [text-producer](../../aitc-text-producer/SKILL.md) | [Grounding](../../../docs/api-guides/07-web-grounding.md) | Nguồn thật hỗ trợ từng claim, ngày tra cứu |
| Hỏi đáp tài liệu/tìm kiếm ngữ nghĩa | Planner với [RAG workflow](../../aitc-production-planner/references/rag-workflow.md), text-producer cho câu trả lời | [Embedding](../../../docs/api-guides/08-embeddings.md) và Gateway text | Truy xuất đúng nguồn; câu ngoài tài liệu không được bịa |
| App, demo tương tác hoặc API được yêu cầu | Planner với [app workflow](../../aitc-production-planner/references/app-workflow.md), producer theo chức năng | Gateway BTC; xây giao diện theo yêu cầu | Một luồng người dùng chạy xuyên suốt và test theo yêu cầu |

Chỉ đọc [context-review](../../aitc-vietnam-context-review/SKILL.md) khi nội dung cần rà bối cảnh/claim; [debug](../../aitc-systematic-debug/SKILL.md) khi gặp lỗi; [reflection](../../aitc-solution-reflection/SKILL.md) và [submission](../../aitc-submission-controller/SKILL.md) khi tới bước đó. Không nạp cả 15 skill, cả bộ guide hoặc code nguồn GitHub vào đầu phiên.

## Từ plan sang hành động

1. Chốt workspace và output tối thiểu đáp ứng tất cả yêu cầu. Điền [execution-plan](../../../templates/execution-plan.md); file nhỏ có thể dùng bảng ngắn trong cùng brief.
2. Mở SKILL.md của task đầu, guide đúng operation và [cách chạy helper](../../../docs/SKILL_EXECUTION.md). Ghi lệnh/check cụ thể trong plan.
3. Nếu được yêu cầu thực thi, làm một mẫu hoặc một luồng xuyên suốt, kiểm tra thật rồi mở rộng. Chỉ nạp reference tiếp theo khi task đó bắt đầu.
4. Tiếp tục task đã chọn sau check đạt; sửa cục bộ khi lỗi. Đánh dấu phần chưa được chạy live rõ ràng.

## Ví dụ quyết định

- Nộp TXT 300–350 từ: text + QA; không scaffold app. Agent đã chạy qua Gateway có thể soạn trực tiếp, không cần gọi thêm một LLM wrapper chỉ để viết cùng bài.
- MP4 60 giây có narration: text → các cảnh video và TTS → ráp → QA. 60 giây là thời lượng bản ráp, không phải một request video 60 giây.
- Demo hỏi đáp 3 tài liệu: xác minh cần retrieval → chunk có source ID → embedding → truy xuất → text có dẫn nguồn → UI nếu đề cần.
