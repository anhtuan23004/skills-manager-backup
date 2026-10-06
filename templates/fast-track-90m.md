# Fast-Track 90m Plan & QA (All-in-One)

> **Mục tiêu:** Bản kế hoạch & nghiệm thu tinh gọn trong 1 file duy nhất cho bài thi 90 phút. Thay thế toàn bộ các biểu mẫu rải rác (`brief`, `concept`, `execution-plan`, `final-qa`).

---

## 1. Khung đề bài & Deliverable bắt buộc (Chốt lúc T+10m)
- **Tên đề bài:** [Điền tiêu đề đề thi]
- **Yêu cầu cốt lõi (Deliverable tối thiểu):** [VD: 01 video mp4 60s + 01 poster PNG 1080x1920 + 01 bản thuyết minh PDF]
- **Quy chuẩn kỹ thuật bắt buộc:** [Format, độ phân giải, tỉ lệ khung hình, dung lượng tối đa, ngôn ngữ]
- **Workspace bài làm:** `chung-khao/bai-thi-[team]/`

---

## 2. Concept & Hướng triển khai (Chốt lúc T+18m)
- **Ý tưởng cốt lõi (1 câu):** [Thông điệp / giá trị chính mang lại]
- **Phong cách / Tông giọng (Tone & Mood):** [VD: Hiện đại, công nghệ, truyền cảm hứng, trang trọng]
- **Nhân vật / Bối cảnh chính:** [Đồng nhất xuyên suốt các asset]
- **Rủi ro lớn nhất & Phương án phòng ngừa (Fallback):** [VD: Nếu API video bị nghẽn -> Dùng slideshow ảnh motion/zoom + voiceover]

---

## 3. Phân công 2 Máy & Tiến độ thực thi (T+18m - T+65m)

| Mốc thời gian | Máy 1 (AI Generation & API) | Máy 2 (Biên tập, Layout & Tích hợp) | Checkpoint / Output |
|---|---|---|---|
| **T+18 - T+30** | Chạy prompt test mẫu (1 ảnh / 1 đoạn VO / 1 clip ngắn) | Soạn khung kịch bản / Outline bài viết / Dàn trang poster thô | Bản mẫu đầu tiên đạt chất lượng tối thiểu |
| **T+30 - T+55** | Chạy batch generation toàn bộ asset chính (Image, Video, Audio) | Rà soát chữ, ghép nối audio, chỉnh màu, dàn chữ trên Canva/Figma/Photoshop | Đủ 100% asset thô |
| **T+55 - T+65** | Ghép dựng bản nháp hoàn chỉnh (Draft v1) | Review đối chiếu yêu cầu đề bài, phát hiện lỗi chính tả/format | Draft v1 xem/đọc được toàn bộ |
| **T+65 - T+80** | Sửa tối đa 3 lỗi lớn nhất (Polish) | Hoàn thiện bản thuyết minh / tài liệu giải pháp đi kèm | Final Release Candidate |

---

## 4. Nhật ký API & Prompts (Ghi nhanh để làm bằng chứng)

| STT | Modality | Endpoint / Model | Prompt / Params tóm tắt | File đầu ra (`output/`) | Trạng thái (OK / Lỗi) |
|---|---|---|---|---|---|
| 1 | Text | `gpt-4o` / `gemini-2.5-flash` | Kịch bản 60s, 4 phân cảnh | `docs/script.md` | OK |
| 2 | Image | `flux-pro` / `imagen-3` | Key visual poster dọc 9:16 | `assets/poster_raw.png` | OK |
| 3 | Audio | ElevenLabs / OpenAI TTS | Voiceover giọng nam miền Bắc | `assets/voiceover.mp3` | OK |
| 4 | Video | Kling / Luma / Haiper | Motion 4 cảnh 5s | `assets/scene_01.mp4` | OK |

---

## 5. Final QA & Nghiệm thu nộp bài (T+80m - T+90m)

### Checklist tiêu chí BTC:
- [ ] **Mở và kiểm tra trực tiếp:** Đã mở file cuối cùng xem/nghe/đọc từ đầu đến cuối trên máy tính chưa?
- [ ] **Đúng định dạng & thông số:** Kích thước, tỉ lệ, đuôi file (.mp4, .png, .pdf, .zip) có đúng 100% yêu cầu đề?
- [ ] **Không dính lỗi cấm:** Không sai chính tả tiếng Việt, không lỗi typography, không vi phạm bản quyền/nhãn hiệu cấm.
- [ ] **Bằng chứng thực thi:** Đã lưu lại prompt và lịch sử gọi API chứng minh đội tự làm bằng AI.

### Lệnh đóng gói và mã băm SHA256 (Chạy trên Terminal):
```bash
# 1. Tính mã băm file sản phẩm chính
shasum -a 256 output/final_deliverable.*

# 2. Đóng gói thư mục nộp bài
zip -r submission_team500.zip output/ docs/ -x "*.DS_Store"

# 3. Tính mã băm file nộp bài
shasum -a 256 submission_team500.zip
```
- **Mã SHA256 file nộp bài:** `[Dán mã hash vào đây]`
- **Xác nhận của Đội trưởng:** ĐÃ DUYỆT BẢN CUỐI (Giờ chốt: T+.....)
