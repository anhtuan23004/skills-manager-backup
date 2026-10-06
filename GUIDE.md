# Bộ toolkit Chung khảo AI Thực Chiến

## 1. Phạm vi và cách đọc
Đây là bộ công cụ chuẩn bị cho **thử thách tạo ảnh, video, văn bản, âm thanh hoặc tổ hợp theo đề**. Không ép mọi bài thành website, chatbot hay MVP. Tài liệu BTC và điều lệ phân biệt Chung khảo với nhiệm vụ phát triển model/MVP ở các vòng sau. [B1, B3, W1]

Có ba lớp thông tin: **BTC quy định**; **đội xác nhận** (được chuẩn bị skills/prompts/MCP); **đề xuất nội bộ** (flow, giờ chốt trung gian, checklist chất lượng và tài liệu hướng dẫn trong gói). Gặp xung đột hoặc khoảng trống, hỏi BTC; không tự coi đề xuất này là luật.

## 2. Tính chất cuộc thi ảnh hưởng cách làm như thế nào?

**Đề xuất áp dụng:** sản phẩm phải trả lời tốt đề, hướng tới người nhận cụ thể, dùng tiếng Việt/bối cảnh Việt Nam phù hợp khi có liên quan, có chất lượng thể hiện và chứng minh được quá trình tạo. Không suy ra rằng đề nào cũng phải có quốc kỳ, hình ảnh công an, khẩu hiệu, lời ca ngợi hoặc câu chuyện an ninh. Không gọi việc dùng model nước ngoài qua API là tự huấn luyện/làm chủ model nền tảng.

Một sản phẩm nghệ thuật hoặc giải trí vẫn có thể phù hợp khi đề yêu cầu. “Giá trị” không chỉ là tuyên truyền hay hữu dụng công vụ. Không tự bịa tác động đo lường hoặc phỏng đoán gu BGK. Xem [PUBLIC_VALUE_AND_JUDGING](docs/PUBLIC_VALUE_AND_JUDGING.md).

## 3. Kiến trúc bộ công cụ
```text
Đề + luật + tài nguyên hợp lệ
           ↓
Orchestrator — chọn skill, chia việc, kiểm soát thời gian
           ↓
Brief → hướng giải → execution-plan (task/skill/API guide/output/check)
           ↓
Skill cần thiết → API Gateway BTC / công cụ môi trường → TEXT / IMAGE / VIDEO / AUDIO theo đề
           ↓
Critic dựa trên artifact thật → sửa lỗi lớn nhất
           ↓
Final QA → Reflection có bằng chứng → người duyệt → freeze
           ↓
Nộp file/source/prompts theo đề → quay video sau thi
```
**Skills** quyết định trình tự/cách phân tích. **Prompts** là lệnh gọi theo giai đoạn. **Gateway BTC** là đường gọi AI chính thức. **Templates/log** giữ thông tin và bằng chứng. Các lớp này không thay thế nhau. Không nạp toàn bộ toolkit đầu phiên và không tạo vòng phê duyệt mới cho phạm vi đã được giao thực thi; cách thức thực hiện chi tiết ở [SKILL_EXECUTION](docs/SKILL_EXECUTION.md).

## 4. Bộ 16 skill và 10 topic
Danh mục, thời điểm dùng và link từng SKILL.md ở [skills/INDEX.md](skills/INDEX.md); chọn theo deliverable bằng [routing](skills/aitc-orchestrator/references/routing.md). Mỗi skill có đầu vào, quy trình, đầu ra, tiêu chuẩn kiểm tra và điều kiện chuyển cho người. Không load cả 16 skill cho một tác vụ nhỏ.
Bài học chung và base template topic nằm ở [topics/INDEX.md](topics/INDEX.md) (rút từ chương trình VTV, không phải luật BTC); topic 2025 đã chuyển vào [topics-archive-2025](topics-archive-2025/INDEX.md), chỉ mở topic khớp đề. Đề cần link chạy trực tuyến thì dùng thêm skill 15 (deploy) và [DEPLOY](docs/DEPLOY.md).

## 5. Quy trình 120 phút trên 2 máy
Các mốc trung gian dưới đây là **đề xuất nội bộ**, không phải deadline mới của BTC. Tổng khung 120 phút +10 phút nộp dựa trên tài liệu training. [B1]

| Thời gian | Máy A — Nội dung/tạo sinh | Máy B — Sản xuất/kiểm tra | Cổng quyết định |
|---|---|---|---|
| 00–08 | Đọc đề, trích yêu cầu. | Kiểm tra tài nguyên, định dạng và trạng thái logging. | Đội xác nhận đầu ra; điểm mơ hồ được nêu rõ. |
| 08–18 | Đưa tối đa 3 concept, chạy context review. | Ước lượng thời gian/chi phí, thử kết nối nhỏ được phép. | Đội chọn concept, ghi lý do thật. |
| 18–30 | Script, storyboard hoặc outline; asset mẫu. | Chuẩn bị cấu trúc lắp ghép, tên file; kiểm tra asset mẫu. | Chứng minh pipeline khả thi; không chờ cuối mới thử export. |
| 30–65 | Tạo asset theo nhánh; ghi job ID/version. | Lắp bản nháp từ asset đã duyệt; text/audio có thể chạy ở đây. | Có bản thô thể hiện đủ cấu trúc, không chỉ asset rời. |
| 65–90 | Sửa asset lỗi, không phát triển nhiều hướng mới. | Critic, continuity, thông điệp, thời lượng, âm thanh. | Chọn bản cuối; bỏ phụ kiện không cần. |
| 90–100 | Chỉ sửa lỗi quan trọng. | Export bản ứng viên, mở/nghe/xem file thực. | Không dùng metadata để thay cho kiểm tra nội dung. |
| 100–112 | Reflection từ bản hiện có + decision log. | Final QA, đối chiếu source/prompt. | Đội duyệt lời giải thích; cập nhật nếu final thay đổi. |
| 112–120 | Duyệt version cuối; không mở concept mới. | Freeze file, commit/push đúng quy trình BTC, chuẩn bị nộp. | Final và reflection nói về cùng một version. |
| 120–130 | Kiểm tra tên/link/attachment cùng người nộp. | Một người thao tác nộp và giữ xác nhận. | Chỉ nộp; không tiếp tục tạo/sửa sản phẩm. |

Đề cần link chạy trực tuyến: bản khung lên link thật quanh T+30, đóng băng tính năng quanh T+70, kiểm tra link live từ máy khác ở T+100 và T+108 (xem [DEPLOY](docs/DEPLOY.md)); không để deploy dồn vào T+112–120.

**Ba vai trò, không phải ba máy:** người chốt concept/ý nghĩa; người điều khiển AI/pipeline; người lắp ghép/QA. Sau bước concept, luôn có người kiểm tra độc lập. Không để hai máy đồng thời sửa một file; phân thư mục và người sở hữu. Hai máy cùng chịu budget/rate limit của đội.

## 6. Bộ công cụ thực thi
### Dùng mặc định
- Agent đã xác minh mọi lệnh gọi AI đi qua Gateway BTC; nạp SKILL.md theo yêu cầu.
- Git và hook BTC giữ nguyên, kiểm tra ghi nhận log đầy đủ.
- Công cụ biên tập thông thường của đội (FFmpeg, trình xử lý âm thanh/ảnh/video offline); không bật tính năng AI ngoài BTC.
- Gọi trực tiếp các endpoint Gateway BTC bằng HTTP/cURL/SDK theo [tài liệu API](docs/api-guides/).

### MCP tùy chọn
MCP chỉ là lớp kết nối công cụ mở rộng nếu host của đội hỗ trợ. Nếu host đã có công cụ file/shell tốt, không cần cài thêm MCP. Tham khảo nguyên tắc chọn công cụ tại [MCP_SELECTION](docs/MCP_SELECTION.md); không tự ý cài đặt server ngoài mà chưa kiểm tra an toàn và sự cho phép của BTC.

## 7. Chuẩn bị quyết định và câu chuyện sau thi
Trong lúc làm chỉ ghi vài quyết định lớn vào [decisions](templates/decisions.md): chọn concept nào, vì sao, đổi gì, thử nghiệm nào buộc đổi hướng — kể cả lý do thời gian/chi phí. Reflection lập chuỗi **yêu cầu → quyết định thực tế → bằng chứng trong output → ý nghĩa dự kiến**, không biến ý định thành tác động đã đo (“muốn giúp người xem nhớ” ≠ “đã tăng nhận thức 80%”). Chạy reflection trước T+120 là chính sách bảo thủ của gói; video sau thi dùng lời của đội. Chi tiết ở [REFLECTION_GUIDE](docs/REFLECTION_GUIDE.md).

## 8. Mức sẵn sàng của gói
Toolkit tập trung hoàn toàn vào quy trình và kịch bản thực thi. Trước khi dùng chính thức, đội phải hoàn thành:
- Xác nhận phạm vi tài nguyên và thẩm quyền sử dụng với BTC.
- Live smoke-test với Gateway BTC: thử gọi text/ảnh/video với quota thật để nắm độ trễ và định dạng phản hồi.
- Kiểm tra hook ghi/gửi log của BTC trên cả 2 máy.
- Diễn tập đủ 2 máy trong khung 120 phút với đề mẫu.
- Không đưa dữ liệu mật, API key hoặc hồ sơ cá nhân vào prompt.
