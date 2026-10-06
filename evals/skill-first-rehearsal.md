# Đề luyện chọn skill và thực thi

Các đề dưới là giả định, chưa chạy benchmark LLM. Dùng để kiểm tra luồng mới và đo câu hỏi “có nhanh hơn không”; không xem unit test như chứng minh tốc độ làm bài.

## Cách chạy

Trong buổi luyện được phép, dùng cùng model, công cụ, budget và deadline cho hai lượt: prompt thông thường và [prompt skill-first](../prompts/00_start.md). Workspace tách biệt; không cho lượt sau đọc output lượt trước. Đổi thứ tự giữa các đề để giảm lợi thế lượt sau. Với kiểm tra routing, chỉ yêu cầu plan để không gọi API tạo media.

| Đề giả định | Kiểm tra trên plan và output thực |
|---|---|
| Viết TXT tiếng Việt 300–350 từ về học tập, không cần app | Chọn text/QA; task có output TXT, cách đếm và đọc kiểm tra; không tạo UI/deploy/storyboard |
| Tạo poster PNG có tiêu đề tiếng Việt từ brief cho sẵn | Image + text khi cần; guide ảnh, vùng chữ, kiểm tra chính tả/kích thước, không apply web app mặc định |
| MP4 60 giây có thuyết minh, dùng hình/cảnh tạo trong buổi luyện | Text/video/audio; plan chia cảnh và có assembly, audio QA; không gửi một request video 60 giây |
| Phiên âm một WAV thành TXT | Audio/STT với attachment; không bắt chuẩn bị voice TTS/narration script |
| Demo hỏi đáp 3 tài liệu có nguồn trang; câu ngoài tài liệu phải báo không đủ dữ liệu | Planner đọc RAG/app references khi cần; task nối source ID, vector, retrieval, text và UI; không coi helper `rag_local.run` là pipeline hoàn chỉnh |
| Tiếp tục bài: task 1–2 DONE có evidence, task 3 TODO; người dùng đã giao triển khai | Đọc plan hiện có, chỉ nạp skill task 3, giữ output cũ và xác nhận đã có; không lập lại brief/concept hoặc dừng xin lại quyền |

## Ghi nhận

Ghi một hàng cho mỗi lượt: đề, điều kiện, model, skill version, thời điểm bắt đầu, giây tới plan có thể thực thi, giây tới output đầu tiên đạt, tổng thời gian, số lần sửa, chi phí thực nếu đo được, requirement đạt/chưa đạt, đường output/evidence và người đánh giá.

Chỉ so sánh thời gian khi chất lượng/requirement tương đương. Ghi NOT_RUN cho lượt chưa chạy; không suy ra tốc độ thi thật từ một đề. Nếu skill nạp quá nhiều tài liệu hoặc thêm task không phục vụ requirement, sửa routing tương ứng rồi luyện lại.
