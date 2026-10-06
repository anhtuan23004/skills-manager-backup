---
source: https://docs.thucchien.ai/docs/round-2/user-guide/references
checked: 2026-10-05
related_skill: aitc-orchestrator
operations:
---

# Nguồn tham khảo

Ưu tiên theo thứ tự:

1. Đề thi và quy định BTC của phiên hiện tại.
2. [User Guide BTC](https://docs.thucchien.ai/docs/user-guide).
3. [API Reference BTC](https://docs.thucchien.ai/docs/api-reference).
4. Tài liệu nhà cung cấp được BTC dẫn: LiteLLM, Google Gemini/Agent Platform,
   OpenAI và DeepSeek.

Tài liệu nhà cung cấp giải thích khả năng model nhưng không thay thế route,
model allowlist, budget hoặc rule của Gateway BTC. Không đổi base URL sang nhà
cung cấp gốc chỉ vì ví dụ upstream dùng endpoint khác.

Khi có xung đột:

- đề thi hiện tại thắng tài liệu chuẩn bị;
- API Reference BTC thắng ví dụ cũ;
- ghi lại điểm chưa rõ và hỏi BTC thay vì suy đoán;
- cập nhật ngày `checked` khi sửa guideline.

## Mở đúng nguồn khi guide chưa đủ

| Vấn đề | Nguồn BTC cần mở |
|---|---|
| Chat request/response | [Text API](https://docs.thucchien.ai/docs/round-2/api-reference/text-generation) |
| Ảnh base64 / chat image | [Image API](https://docs.thucchien.ai/docs/round-2/api-reference/image-generation), [Chat image](https://docs.thucchien.ai/docs/round-2/api-reference/image-generation-chat) |
| Video field / job / tải file | [Create](https://docs.thucchien.ai/docs/round-2/api-reference/video-generation-start), [Status](https://docs.thucchien.ai/docs/round-2/api-reference/video-generation-status), [Download](https://docs.thucchien.ai/docs/round-2/api-reference/video-generation-download) |
| Giọng đọc / upload phiên âm | [TTS](https://docs.thucchien.ai/docs/round-2/api-reference/text-to-speech), [STT](https://docs.thucchien.ai/docs/round-2/api-reference/speech-to-text) |
| Model được cấp / budget / team | [Spend checking](https://docs.thucchien.ai/docs/round-2/api-reference/spend-checking) |

Sau khi tra, cập nhật đúng guide và ghi thay đổi có ích cho lần sau; không chép cả trang vào context mỗi lượt. Bám sát tài liệu chính thức từ BTC để tối ưu hóa việc gọi model và kiểm soát chi phí trong suốt quá trình thi đấu.
