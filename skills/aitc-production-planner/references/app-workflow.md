# Xây app theo đề

Chỉ đọc khi đề/người dùng yêu cầu app, API hoặc tương tác. Dùng cùng planner; đây là hướng dẫn thực thi trong agent hiện tại.

1. Từ requirements, viết luồng ngắn: input người dùng → xử lý/AI → output → tiêu chí đạt. Ghi rõ đầu ra nào cần demo, source hoặc deploy; chỉ thêm deploy khi được yêu cầu.
2. Xem source có sẵn trước. Xây interface phù hợp: CLI cho batch/script, Streamlit cho panel demo, FastAPI khi cần HTTP API. UI riêng vẫn có thể xây trực tiếp trên Gateway; không ép mọi yêu cầu frontend vào Streamlit.
3. Gọi API Gateway BTC trực tiếp theo [hướng dẫn API](../../../docs/api-guides/README.md) và [SKILL_EXECUTION](../../../docs/SKILL_EXECUTION.md). Khi đã có project, tích hợp vào code hiện tại; khi chưa có, tạo phần tối thiểu để chạy luồng của đề.
4. Trong execution-plan, mỗi task có file cần sửa, hành vi cần có và test quan sát được. Ưu tiên một luồng input → output chạy xuyên suốt trước khi thêm trang/tính năng.
5. Dùng payload/operation đúng [API guide](../../../docs/api-guides/README.md). Giữ key và live permission phía server; không đưa key vào JS trình duyệt. Mock transport trong test; không tự retry POST trả phí.
6. Kiểm tra happy path, input rỗng/sai, timeout/lỗi Gateway và output artifact. UI cần chạy và thao tác thực trong trình duyệt khi môi trường có hỗ trợ; compile không thay runtime/browser test. Thiếu dependency thì ghi phần chưa kiểm chứng.
7. Bàn giao lệnh chạy, cấu hình cần thiết, kết quả test, giới hạn còn lại. Tái dùng [final-qa](../../aitc-final-qa/SKILL.md) để đối chiếu mỗi requirement với evidence.

Không thêm auth, database, queue hoặc vector database chỉ vì project mẫu có sẵn. Chỉ chọn khi yêu cầu hoặc dữ liệu/luồng thực tế cần. Agent xây các chức năng cần thiết từ plan và helper có sẵn.
