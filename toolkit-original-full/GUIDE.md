# Bộ toolkit Chung khảo AI Thực Chiến

## 1. Phạm vi và cách đọc
Đây là bộ công cụ chuẩn bị cho **thử thách tạo ảnh, video, văn bản, âm thanh hoặc tổ hợp theo đề**. Không ép mọi bài thành website, chatbot hay MVP. Tài liệu BTC và điều lệ phân biệt Chung khảo với nhiệm vụ phát triển model/MVP ở các vòng sau. [B1, B3, W1]

Có ba lớp thông tin: **BTC quy định**; **đội xác nhận** (được chuẩn bị skills/prompts/MCP); **đề xuất nội bộ** (flow, giờ chốt trung gian, checklist chất lượng và công cụ trong gói). Gặp xung đột hoặc khoảng trống, hỏi BTC; không tự coi đề xuất này là luật.

## 2. Tính chất cuộc thi ảnh hưởng cách làm như thế nào?

**Đề xuất áp dụng:** sản phẩm phải trả lời tốt đề, hướng tới người nhận cụ thể, dùng tiếng Việt/bối cảnh Việt Nam phù hợp khi có liên quan, có chất lượng thể hiện và chứng minh được quá trình tạo. Không suy ra rằng đề nào cũng phải có quốc kỳ, hình ảnh công an, khẩu hiệu, lời ca ngợi hoặc câu chuyện an ninh. Không gọi việc dùng model nước ngoài qua API là tự huấn luyện/làm chủ model nền tảng.

Một sản phẩm nghệ thuật hoặc giải trí vẫn có thể phù hợp khi đề yêu cầu. “Giá trị” không chỉ là tuyên truyền hay hữu dụng công vụ. Không tự bịa tác động đo lường hoặc phỏng đoán gu BGK. Xem `docs/PUBLIC_VALUE_AND_JUDGING.md`.

## 3. Kiến trúc bộ công cụ
```text
Đề + luật + tài nguyên hợp lệ
           ↓
Orchestrator — chọn skill, chia việc, kiểm soát thời gian
           ↓
Brief → concept → kiểm tra bối cảnh → production plan
           ↓
TEXT / IMAGE / VIDEO / AUDIO (chỉ nhánh cần dùng)
           ↓
Critic dựa trên artifact thật → sửa lỗi lớn nhất
           ↓
Final QA → Reflection có bằng chứng → người duyệt → freeze
           ↓
Nộp file/source/prompts theo đề → quay video sau thi
```
**Skills** quyết định trình tự/cách phân tích. **Prompts** là lệnh gọi theo giai đoạn. **Gateway** là đường gọi AI. **MCP/CLI local** làm thao tác kỹ thuật. **Templates/log** giữ thông tin và bằng chứng. Các lớp này không thay thế nhau.

## 4. Bộ 15 skill
| ID | Skill | Sản phẩm của bước |
|---|---|---|
| 00 | Orchestrator | Bảng việc trên 2 máy; skill cần dùng; thời điểm dừng. |
| 01 | Brief Decoder | Danh sách yêu cầu, định dạng, tiêu chí chính thức, điểm chưa rõ. |
| 02 | Concept Choice | Tối đa 3 hướng; 1 hướng do đội chốt; lý do và phần không làm. |
| 03 | Vietnam Context Review | Kiểm tra bối cảnh/người nhận/giá trị/độ tin cậy, không tự đổi đề. |
| 04 | Production Planner | Shot list/content plan, phụ thuộc asset, ngân sách, fallback. |
| 05 | Text Producer | Script/copy/nội dung đúng loại đầu ra. |
| 06 | Image Director | Visual direction, prompt ảnh, nhận diện nhất quán, typography. |
| 07 | Video Director | Cảnh ngắn tập trung, hành động/camera, job và continuity. |
| 08 | Audio Producer | Voice-over, cách đọc, transcript, kiểm tra âm thanh. |
| 09 | Artifact Critic | PASS/FAIL/UNVERIFIED có vị trí bằng chứng; 3 sửa đổi ưu tiên. |
| 10 | Systematic Debug | Nguyên nhân khả dĩ; thử một giả thuyết; dừng tạo tác vụ trả phí trùng. |
| 11 | Final QA | Đủ đề + nội dung + kỹ thuật + nguồn gốc; người duyệt. |
| 12 | Solution Reflection | Nhận xét đề, quyết định, ý nghĩa, talking points 3–6 phút. |
| 13 | Submission Controller | Kiểm tra bản cuối/repo/quyền truy cập; đội tự nộp. |
| 14 | Toolkit Evaluator | Chạy đề tập; so sánh với/không skill; lỗi cần sửa trước thi. |

Mỗi skill có đầu vào, quy trình, đầu ra, tiêu chuẩn kiểm tra và điều kiện chuyển cho người. Không load cả 15 skill cho một tác vụ nhỏ. File `skills/INDEX.md` chỉ đường đến từng SKILL.md.

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
| 100–112 | Reflection từ bản hiện có + decision log. | Final QA, manifest, đối chiếu source/prompt. | Đội duyệt lời giải thích; cập nhật nếu final thay đổi. |
| 112–120 | Duyệt version cuối; không mở concept mới. | Freeze file, commit/push đúng quy trình BTC, chuẩn bị nộp. | Final và reflection nói về cùng một version. |
| 120–130 | Kiểm tra tên/link/attachment cùng người nộp. | Một người thao tác nộp và giữ xác nhận. | Chỉ nộp; không tiếp tục tạo/sửa sản phẩm. |

**Ba vai trò, không phải ba máy:** người chốt concept/ý nghĩa; người điều khiển AI/pipeline; người lắp ghép/QA. Sau bước concept, luôn có người kiểm tra độc lập. Không để hai máy đồng thời sửa một file; phân thư mục và người sở hữu. Hai máy cùng chịu budget/rate limit của đội.

## 6. Bộ công cụ thực thi
### Dùng mặc định
- Agent đã xác minh mọi AI qua Gateway BTC; nạp SKILL.md theo yêu cầu.
- Git và hook BTC giữ nguyên.
- Công cụ biên tập thông thường của đội; không bật tính năng AI ngoài BTC.
- Gateway CLI và media CLI của gói **chỉ khi phạm vi mã tiện ích chuẩn bị trước được BTC xác nhận**.

### MCP local tùy chọn
`runtime/mcp_server.py` có đúng 4 tool: `aitc_media_probe`, `aitc_contact_sheet`, `aitc_artifact_manifest`, `aitc_verify_manifest`. Không có tool tự gọi model, upload, tự submit, shell tùy ý hoặc Git mutation. Mã Python viết mới, hỗ trợ tập con MCP stdio; không phải sản phẩm chính thức của MCP/Anthropic/Microsoft.

Nếu host đã đọc file/chạy CLI tốt, không cần thêm MCP. Filesystem/Git reference server và Playwright MCP được nghiên cứu để chọn khi cần, không được cài tự động hoặc xem là an toàn/chấp thuận sẵn. 

## 7. Chuẩn bị quyết định và câu chuyện sau thi
Trong lúc làm, chỉ cần ghi vài quyết định lớn: chọn concept nào; vì sao; đổi cảnh/cách thể hiện nào; thử nghiệm nào buộc đổi hướng. Ghi đúng lý do, kể cả vì giới hạn thời gian/chi phí.

Reflection skill lập chuỗi **yêu cầu → quyết định thực tế → bằng chứng trong output → ý nghĩa dự kiến**. Phân biệt sự thật quan sát được, lý do đội xác nhận, tác động mong muốn và hạn chế. Không biến “muốn giúp người xem nhớ” thành “đã tăng nhận thức 80%”. Không đổi tên skill nhằm che việc dùng AI hỗ trợ tổng kết.

Chạy reflection trước khi hết giờ là chính sách bảo thủ trong gói, do tài liệu chưa xác nhận rõ quyền dùng AI sau T+120 để soạn video. Video sau thi dùng lời của đội trên bản đã duyệt. 

## 8. Mức sẵn sàng của gói
Đã chạy 48 kiểm thử offline: cấu trúc 15 skill, các guard cơ bản, HTTP mô phỏng, JSON-RPC stdio, FFmpeg/FFprobe, freeze/manifest/package. **Không suy ra từ kết quả này rằng prompt đã được benchmark tốt, host đã routing đúng, hook BTC đủ log, hay live API tương thích.** Xem `tests/TEST_REPORT.md`.

Trước khi dùng chính thức, đội phải hoàn thành: kiểm tra quyền tài nguyên; live smoke-test BTC; kiểm tra hook ghi/gửi; rehearsal đủ 2 máy/120 phút; đọc output thật; chốt người nộp. Không đưa dữ liệu mật, API key hoặc hồ sơ cá nhân vào prompt để “kiểm tra”.
