# Checklist deploy (VPS của đội)
Chỉ dùng khi đề yêu cầu sản phẩm chạy trực tuyến. Tick khi có evidence; chưa kiểm tra thì ghi UNVERIFIED.

## Trước ngày thi / diễn tập
[ ] VPS: IP công khai, HTTPS hợp lệ, mở 80/443; truy cập được từ mạng ngoài đội
[ ] SSH vào được từ cả 2 máy thi bằng alias (không lưu khóa/mật khẩu trong prompt hay repo)
[ ] Mạng phòng thi cho phép SSH/SCP/HTTPS tới VPS (đã thử trong điều kiện giống thi)
[ ] Cấu trúc `releases/` + `current`; đã thử chuyển và rollback
[ ] Script deploy một lệnh chạy được với trang rỗng; thời gian một lần deploy: ______ phút
[ ] Biến môi trường nằm ngoài thư mục web và ngoài repo; URL tới file env trả 404
[ ] VPS không chứa mã/asset sản phẩm làm sẵn
[ ] Thời gian link phải còn sống sau thi (BTC xác nhận): ______; domain/VPS còn hạn đến: ______

## Trong giờ thi
[ ] T+0–8: VPS sống (SSH 2 máy, HTTPS từ mạng ngoài, script chạy với trang rỗng)
[ ] Requirement ID của deliverable trực tuyến: ______
[ ] Nơi nộp link do BTC xác nhận: ______
[ ] Người chịu trách nhiệm deploy: ______ (không sửa tính năng 30 phút cuối)
[ ] Không đổi quyền chia sẻ/repo public; không có secret trong repo/build

## Mốc
| Mốc | URL | Giờ T | Commit/hash | Release | Ghi chú |
|---|---|---|---|---|---|
| Bản khung (~T+30) | | | | | |
| Bản cuối (~T+70) | | | | | |
| Bản ứng viên mở từ máy/mạng khác (T+100) | | | | | |
| Kiểm tra lại trước freeze (T+108) | | | | | |
| Freeze (T+112) | | | | | |

## Smoke test trên link live (máy/mạng khác, không đăng nhập)
[ ] Trang chính mở qua HTTPS, không cảnh báo chứng chỉ
[ ] Luồng chính chạy từ đầu đến cuối
[ ] Chữ tiếng Việt đúng dấu, phông chữ hiển thị đúng
[ ] Ảnh/âm thanh/tài nguyên tải được; thời gian tải chấp nhận được
[ ] Di động (nếu đề nhắm di động)
[ ] Không lộ key/.env/.git trong nguồn trang, tab Network hoặc liệt kê thư mục
[ ] Lỗi Gateway/timeout có thông báo, không trắng trang
[ ] Tải lại cứng không ra bản cũ
[ ] Link không yêu cầu đăng nhập (hoặc đúng theo hướng dẫn BTC)

## Dự phòng và nộp
[ ] Bản trước còn trong `releases/` để rollback
[ ] Bản dự phòng (build tĩnh + hướng dẫn / video quay màn hình nếu BTC cho phép): ______
[ ] URL + commit/hash đã ghi vào manifest
[ ] Người nộp link; trạng thái nộp thành công đã được chụp/ghi nhận
[ ] Sau freeze không deploy lại và không sửa file trên VPS

UNVERIFIED còn lại:
