# Deploy và xuất bản sản phẩm (VPS của đội)

Hướng dẫn chuẩn bị của đội, **không phải quy định BTC**. Skill điều phối: [aitc-deploy-publisher](../skills/aitc-deploy-publisher/SKILL.md). Lý do và bằng chứng từ chương trình truyền hình: [INSIGHTS_VTV_2025](INSIGHTS_VTV_2025.md).

**Quyết định của đội:** host là **VPS riêng do đội chuẩn bị trước ngày thi**, không dùng dịch vụ hosting bên thứ ba.

## 1. Khi nào cần
| Đề yêu cầu | Deploy? |
|---|---|
| Web, game, app, demo tương tác, hoặc "giám khảo mở/chơi trực tiếp" | **Có.** Quyết định ngay lúc giải mã đề. |
| Ảnh, video, text, audio, slide, tờ rơi | Không. Đóng gói file theo [submission-controller](../skills/aitc-submission-controller/SKILL.md). |
| Đề mở ("web, ebook...") | Chọn định dạng ít rủi ro nhất đáp ứng đề; web chỉ khi tăng giá trị rõ và còn thời gian. |

Tập 3 của chương trình cho thấy hai đội không kịp host game bị chấm thấp nhất bảng. Tập 2 cho thấy làm xong ở local không đủ.

## 2. Chuẩn bị VPS trước ngày thi
Chỉ chuẩn bị **hạ tầng**; không đưa mã sản phẩm, asset hoặc bản demo làm sẵn lên VPS (TEAM_RULES: không mang bài giải/project mẫu có sẵn vào thi). Script deploy chung không chứa sản phẩm là tiện ích; phạm vi mã tiện ích được mang vào thi cần BTC xác nhận riêng.

| Hạng mục | Việc phải xong | Kiểm tra |
|---|---|---|
| Địa chỉ | IP công khai cố định; tên miền trỏ đúng nếu dùng | Mở từ mạng ngoài đội (4G/máy khác) |
| HTTPS | Chứng chỉ cấp xong trước ngày thi (cấp phụ thuộc DNS đã lan truyền) | Trình duyệt không cảnh báo |
| Cổng/tường lửa | Mở 80/443 (và SSH cho 2 máy thi); không chặn theo IP | Quét cổng từ bên ngoài |
| Web server / reverse proxy | Phục vụ thư mục tĩnh; proxy tới app khi cần; fallback SPA; giới hạn upload và timeout phù hợp | Trang thử trả 200 |
| Runtime | Node/Python/Docker... đúng phiên bản đội dùng; process manager (systemd/pm2/docker compose) tự khởi động lại | Khởi động lại VPS vẫn tự chạy |
| Truy cập SSH | Cả 2 máy thi vào được bằng khóa SSH; dùng alias trong ssh config, **không dán khóa/mật khẩu vào prompt và không để agent đọc credential** | `ssh <alias>` từ từng máy |
| Mạng phòng thi | Máy thi kết nối được tới VPS qua SSH/SCP/HTTPS (chưa biết mạng có chặn không → UNVERIFIED cho đến khi thử) | Thử từ mạng giống điều kiện thi |
| Cấu trúc thư mục | `releases/<giờ-hoặc-commit>/` + liên kết `current` để chuyển/rollback tức thì | Thử chuyển và quay lại |
| Script deploy | Một lệnh: đẩy build → `releases/` → đổi `current` → reload; in ra URL | Chạy với trang rỗng |
| Biến môi trường | File env trên VPS, quyền hạn chế, ngoài thư mục phục vụ web và ngoài repo | Truy cập URL tới file env trả 404 |
| Tài nguyên | CPU/RAM/ổ đĩa đủ cho lượng giám khảo cùng lúc; log xoay vòng | Theo dõi trong buổi thử |
| Thời gian sống | Hỏi BTC link phải còn sống đến khi nào sau thi; gia hạn domain/VPS tương ứng | Ghi ngày hết hạn |

Buổi diễn tập: deploy một trang rỗng từ máy thi, mở từ điện thoại 4G, rollback, rồi xóa. Ghi thời gian từng bước vào [deploy-checklist](../templates/deploy-checklist.md).

## 3. Kiến trúc nên chọn (ít rủi ro nhất trước)
1. **Trang tĩnh sinh sẵn lúc build**, phục vụ bởi web server. Không lộ key, không đốt budget khi giám khảo mở.
2. **Tĩnh + app nhỏ sau reverse proxy** khi đề cần AI lúc chạy. Gateway BTC được gọi từ phía server bằng biến môi trường; có giới hạn tần suất và cache; timeout proxy đủ cho lời gọi chậm; trả thông báo thân thiện khi Gateway lỗi.
3. **Nhiều dịch vụ/cơ sở dữ liệu** chỉ khi đề yêu cầu rõ. Tốn thời gian nhất; không chọn vì "mẫu có sẵn".

Giám khảo chơi/duyệt sản phẩm sẽ dùng budget của đội nếu app gọi Gateway lúc chạy: tính trước ngưỡng chi.

## 4. Lỗi hay gặp khi lên VPS
- **Đường dẫn:** nếu site không ở gốc domain, đặt base path đúng hoặc dùng đường dẫn tương đối.
- **SPA tải lại 404:** cấu hình fallback về `index.html`.
- **HTTP/HTTPS lẫn lộn (mixed content):** tài nguyên http trên trang https bị chặn; dùng https hoặc đường dẫn tương đối.
- **Cache bản cũ:** thêm băm tên file hoặc tắt cache cho `index.html`, kiểm tra bằng tải lại cứng.
- **Quyền thư mục/file:** web server không đọc được bản mới; kiểm tra chủ sở hữu và quyền.
- **Timeout/kích thước:** lời gọi AI chậm bị proxy cắt; ảnh/audio lớn bị giới hạn upload; bật nén.
- **Phông chữ tiếng Việt:** UTF-8, phông chữ nằm trong build thay vì CDN ngoài; xem dấu trên link live.
- **Lộ file:** tắt liệt kê thư mục; không để `.env`, `.git`, khóa, log trong thư mục phục vụ web.
- **Key lộ:** mở nguồn trang và tab Network trên link live, không được thấy key.
- **Tài nguyên hết:** tiến trình dừng, ổ đĩa đầy; kiểm tra trạng thái dịch vụ sau deploy.
- **Quên rollback:** luôn giữ bản trước; chuyển `current` về bản cũ thay vì sửa tại chỗ.

## 5. Mốc thời gian đề xuất trong 120 phút
Giả định của đội, bám bảng thời gian của [GUIDE](../GUIDE.md#5-quy-trình-120-phút-trên-2-máy) và gợi ý của giám thị trong chương trình (khoảng 50 phút cuối chuyển sang hoàn thiện + deploy, 12 phút cuối hỏi đã live chưa).

| Mốc | Việc deploy |
|---|---|
| T+0–8 | Kiểm tra VPS sống: SSH từ cả 2 máy, HTTPS, chạy script deploy với trang rỗng |
| T+30 | Bản khung đã có URL thật; ghi lỗi build/đường dẫn/phông chữ |
| ~T+70 | Đóng băng tính năng; chỉ sửa lỗi; deploy bản cuối |
| T+100 | Link bản ứng viên mở được từ máy/mạng khác; chuẩn bị dự phòng |
| T+108 | Kiểm tra lại link live, smoke test lần cuối |
| T+112 | Freeze; ghi URL + commit/hash vào manifest |
| T+120–130 | Chỉ nộp; không deploy lại |

## 6. Smoke test trên link live
Dùng [deploy-checklist](../templates/deploy-checklist.md). Từ máy/mạng khác máy làm bài, không đăng nhập:
1. Trang chính mở được qua HTTPS, không lỗi console nghiêm trọng.
2. Chạy luồng chính từ đầu đến cuối (game: chơi hết một lượt; web: mọi menu chính; app: input → output).
3. Chữ tiếng Việt đúng dấu; ảnh/âm thanh tải được.
4. Di động nếu đề nhắm di động.
5. Không lộ key hay file nhạy cảm; lỗi Gateway/timeout có thông báo, không trắng trang.
6. Ghi URL, giờ, commit/hash, ảnh chụp màn hình làm evidence.

## 7. Dự phòng
- **Lỗi bản mới:** chuyển `current` về bản trước.
- **VPS hoặc mạng hỏng:** bản build tĩnh chạy được ở local kèm hướng dẫn một dòng; nếu BTC cho phép, ghi hình luồng chính bằng công cụ quay màn hình (không AI). Chỉ dùng khi leader/BTC đồng ý.
- Không tạo nội dung mới cho dự phòng.

## 8. Ranh giới
- Agent không đổi quyền chia sẻ, không đổi repo public, không nộp; thao tác trên VPS theo plan và phạm vi leader đã duyệt, không xóa/ghi đè ngoài thư mục deploy.
- Không đọc khóa SSH, `.env` hay credential vào ngữ cảnh agent; không dán chúng vào prompt.
- Mọi thứ trên link live là bản leader đã duyệt; không sửa sau freeze.
- Nơi nộp link, định dạng và thời gian sống do BTC quyết định; tài liệu này không thay hướng dẫn BTC.
