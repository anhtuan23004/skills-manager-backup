# Hạn chế và kiểm tra Gateway
Mã là helper viết mới; chưa gọi trực tiếp hệ thống BTC.

## Cấu hình
Base chỉ nhận HTTPS `api.thucchien.ai`, prefix rỗng hoặc `/v1`. Config ví dụ chọn `/v1`; tài liệu có ví dụ khác nhau theo công cụ, nên phải smoke-test tool/prefix trên hai máy. Model trong config chỉ là tên có trong tài liệu đội gửi, không phải danh sách availability đã xác minh hiện tại.

Mọi request phải có model trong allowlist do đội xem. Grounding mặc định tắt. Có hỗ trợ cấu trúc tools giới hạn nếu BTC cho phép và đội chủ động bật; không suy ra quyền search từ việc endpoint tồn tại. Các phiên bản API khác, model mới, features riêng phải tra BTC, không tự lấy provider gốc thay vào.

## Chi phí và retry
POST tạo nội dung không được helper tự retry. Timeout có thể đã tạo task/tính phí: trả trạng thái AMBIGUOUS, lưu run, để người kiểm tra trước khi thử lại. GET có retry giới hạn; budget429 dừng ngay, rate429 mới có thể chờ. Kết quả FAILED không đồng nghĩa BTC hoàn phí.

Veo trong tài liệu tính phí ngay khi tạo tác vụ, mặc định8s nếu thiếu tham số. Helper yêu cầu4/6/8s rõ ràng. Thử nhỏ trước khi nâng chất lượng.

Header cost chỉ là chi phí request khi có, không phải tổng chi tiêu đội. Helper không triển khai bộ đếm budget/rate-limit liên máy; hai người phải theo dõi budget chung trên hệ thống BTC và không tạo đợt request chồng chéo.

## Log và secret
`runs/` là record bổ sung, không thay `.ai-log` chính thức. Không sửa/xóa hook, giả tạo session log hoặc giấu prompt khỏi BTC. Không đặt API key, dữ liệu nhạy cảm trong prompt vì log có thể giữ nguyên.

Các request có thể chứa dữ liệu đội được phép dùng; chỉ nhập dữ liệu được cấp/quyền rõ, không bí mật công ty hoặc dữ liệu cá nhân không cần thiết. HTTP error body không tự echo vì có thể lộ nội dung nhạy cảm; đội kiểm tra theo quy trình BTC khi cần.

## Không phải hệ thống kiểm soát tuyệt đối
Allowlist và freeze là guard của các lệnh này. Chúng không ngăn một chương trình khác hoặc người dùng tự gọi mạng. Agent host phải được kiểm soát riêng, kể cả auto-complete, plugin AI, model fallback. Chuẩn bị trước, kiểm tra cấu hình thực tế, tắt đường AI không được phép.

## Checklist live smoke-test
1. Text: nhận một output ngắn không rỗng; xác minh hook ghi và gửi thành công.
2. Image: giải mã ảnh, mở được; không chỉ kiểm tra200OK.
3. Video: tạo4s nhỏ → lưu ID → poll → download → ffprobe/xem.
4. TTS/STT khi cần: nghe file, kiểm tra dấu/tên riêng; không nhầm tên đuôi file với codec.
5. Hai máy: cấu hình giống allowlist/prefix, run ID khác, budget chung, không ghi đè.
6. Chỉ cần smoke-test những modality sẽ chuẩn bị. Không tiêu hết key tập vào benchmark lớn.
