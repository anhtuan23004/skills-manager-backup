# Cài đặt, chuẩn bị môi trường và vận hành

Tài liệu này hướng dẫn chuẩn bị môi trường thi đấu, nạp skill cho AI agent và thực hiện kết nối với Gateway BTC mà không phụ thuộc vào code wrapper bên ngoài.

---

## 1. Chuẩn bị môi trường hệ thống

1. **Công cụ dòng lệnh:**
   - Đảm bảo `ffmpeg` và `ffprobe` đã có trong PATH (để kiểm tra kích thước, thời lượng, bitrate và trích xuất frame).
   - `curl` hoặc các thư viện HTTP tiêu chuẩn để test kết nối.
2. **Khóa API và Endpoint:**
   - Cấu hình biến môi trường trên máy:
     ```bash
     export AITC_API_KEY="khóa-api-do-btc-cấp"
     export AITC_GATEWAY_URL="https://api.thucchien.ai/v1"
     ```
   - **Tuyệt đối không đưa API key vào prompt, code lưu trong Git hoặc gửi ra ngoài.**
3. **Giám sát & Hook BTC:**
   - Đảm bảo các hook ghi log của BTC (`.agents`, `.ai-log`, `.github/hooks`, v.v.) hoạt động bình thường trên cả 2 máy thi đấu. Không sửa, xóa hay ghi đè các thư mục giám sát.

---

## 2. Nạp Skill và Bắt đầu phiên làm việc

1. **Khởi đầu với Agent:**
   - Mở agent lập trình / điều phối (được cấu hình trỏ model qua Gateway BTC).
   - Dán nội dung từ [prompts/00_start.md](../prompts/00_start.md) kèm toàn văn đề thi.
   - Chỉ định agent đọc [skills/aitc-orchestrator/SKILL.md](../skills/aitc-orchestrator/SKILL.md) và [docs/TEAM_RULES.md](TEAM_RULES.md).
2. **Tiến trình theo Plan:**
   - Agent phân tích đề, lập [execution-plan](../templates/execution-plan.md).
   - Mỗi task chỉ nạp đúng SKILL.md và tài liệu API tương ứng từ [docs/api-guides/](api-guides/).

---

## 3. Smoke Test kết nối Gateway BTC

Trước giờ thi hoặc đầu phiên luyện tập, chạy lệnh kiểm tra kết nối đơn giản để đảm bảo key và mạng thông suốt:

```bash
# Kiểm tra thông tin tài khoản / budget
curl -s -X GET "https://api.thucchien.ai/key/info" \
  -H "Authorization: Bearer $AITC_API_KEY"

# Thử nghiệm sinh văn bản ngắn
curl -s -X POST "https://api.thucchien.ai/v1/chat/completions" \
  -H "Authorization: Bearer $AITC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tên-model-được-cấp",
    "messages": [{"role": "user", "content": "Xin chào"}]
  }'
```

---

## 4. Quản lý sản phẩm và đóng gói nộp bài

1. **Thư mục sản phẩm cuối:**
   - Mọi sản phẩm hoàn thiện đặt tại `final/` trong workspace bài làm.
2. **Kiểm tra thông số kỹ thuật:**
   - Sử dụng `ffprobe` để đo chính xác thời lượng, khung hình và định dạng đối với video/audio theo đúng yêu cầu của đề.
3. **Tạo bảng kiểm kê (Manifest):**
   ```bash
   shasum -a 256 final/* > qa/manifest.sha256
   ```
4. **Đóng gói (nếu BTC yêu cầu nộp file nén):**
   ```bash
   zip -r submission/final.zip final/ qa/manifest.sha256
   ```
   *Lưu ý:* Nếu đề bài yêu cầu nộp trực tiếp file MP4/PNG/PDF/link Git thì nộp theo đúng định dạng yêu cầu của BTC, không bắt buộc đóng gói ZIP.
