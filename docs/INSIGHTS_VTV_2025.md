# Insight từ chương trình VTV "A.I Thực chiến 2025" (Tập 2 → Số 11)

Nguồn: phụ đề tự động tiếng Việt của 10 tập phát sóng (playlist `PLfl0aj6-FD1pzezaKuAMBp8Zf50vh4pNt`). Đây là **quan sát từ chương trình truyền hình, không phải quy định hay rubric của BTC**. Tên đội/điểm có thể sai do phụ đề; rubric chi tiết không được công bố (chỉ biết tổng 400 điểm: hội đồng kỹ thuật tối đa 100, mỗi giám khảo còn lại tối đa 75). Dùng để chuẩn bị, không dùng để suy ra luật thi.

## 1. Các tập đã phân tích

| Tập | Đề | Deliverable | Đội nhất (điểm) | Ghi chú rút ra |
|---|---|---|---|---|
| Tập 2 (`v_9QS5Nj5zo`) | Website du lịch bản vùng sâu | **Web, phải lên server** | Hồng Trà (354) | Chốt cấu trúc/module trước khi prompt; ảnh AI thiếu chân thực bị nghi ngờ; 2 đội chỉ chạy local |
| Tập 3 (`D52ScLtAO2U`) | Game mobile an toàn thực phẩm | **Game web, host công khai để giám khảo chơi** | Anti Neural (335) | Crawler lấy dữ liệu chính thống; 2/10 đội không kịp host → thấp nhất bảng |
| Số 4 (`5a1rbuS8hto`) | Báo cáo HĐQT Techcombank | Slide/tài liệu ≤10 trang | MTA Innogen (355) | Bám format báo cáo thật; dùng số liệu 2024 thay 2025 bị trừ nặng |
| Số 5 (`LixRqIPL19c`) | Infographic Luật BVDLCN | Ảnh infographic | (chưa đọc phần công bố) | Phải đối chiếu nội dung với văn bản luật; lỗi chữ Việt, tương phản; Fin AI kẹt ở bước đóng gói |
| Số 6 (`kJJzGhFRZwA`) | Truyện tranh chống lừa đảo | 5–10 trang A4, định dạng mở (web/ebook) | AI Avengers (364) | Làm thêm website; chừa bong bóng thoại trống rồi điền chữ; nộp cả video quá trình |
| Số 7 (`i4H8or6yxkI`) | Bản tin thời sự về AI VN | Video 60–80 giây | Aranic AI (349) | Clip AI ~8 giây → khó đồng nhất MC/giọng; phỏng vấn nhân vật AI bị coi là vượt ranh giới |
| Số 8 (`w6b4pbPD6Wo`) | Tờ rơi gấp ba về chất kích thích | Tờ A4 gấp ba | URX (356) | AI sinh ảnh, **HTML chèn chữ** → không lỗi chữ; nộp cả thành phẩm trung gian |
| Số 9 (`6ztiLZcNIQk`) | Podcast tâm lý người cao tuổi | Audio/video, 2 nhân vật, nhạc nền | IM AI (378) | Giọng lẫn Bắc/Nam giữa các block 8 giây; cử chỉ giọng ("dạ", cười) ghi điểm |
| Số 10 (`HFWc5YooY9w`) | Bài hát cho Hiệp hội dữ liệu quốc gia | Video lyric ~3 phút | Converge (378) | Lời dựa nguồn chính thống; "cưỡng từ" (hát sai dấu) là tối kỵ; API key thừa dấu chấm mất ~15 phút |
| Số 11 (`LvcYdKZohfg`) | Chiến dịch marketing Tết (Techcombank) | ≤10 slide/trang | Unicorn (350) | Phân công riêng người deploy; gom nhiều slide vào một prompt để tiết kiệm API |

## 2. Deploy: chỉ hai tập bắt buộc, nhưng hậu quả nặng

- **Tập 3:** game phải host công khai. Hai đội không kịp lên web không được đánh giá trọn vẹn, đứng cuối bảng (157 và 183 điểm). Giám thị nói deploy "tốn nhiều thời gian hơn các bài trước", khuyên từ khoảng **50 phút cuối** chuyển sang hoàn thiện + deploy; còn khoảng **12 phút** thì đã hỏi các đội "lên live xong chưa".
- **Tập 2:** hai đội làm xong ở local nhưng không lên server được; thuộc nhóm điểm thấp.
- Đội thắng Tập 11 (Unicorn) giao riêng một người lo deploy; đội thắng Tập 6 nộp cả website.
- **Không rõ từ chương trình:** nền tảng hosting nào, nộp bằng link hay file, deploy ảnh hưởng điểm bao nhiêu. Nơi nộp link và thời gian sống phải hỏi BTC.
- **Quyết định của đội:** host là VPS riêng chuẩn bị trước ngày thi; xem [DEPLOY](DEPLOY.md).

## 3. Điểm chung của đội thắng
1. Chuẩn bị pipeline/dự án sẵn, chốt concept đơn giản rồi làm sớm. (Phần "sẵn" cần BTC xác nhận phạm vi, xem TEAM_RULES.)
2. Chia vai rõ: prompt / code / ghép sản phẩm / deploy.
3. Lấy dữ liệu từ nguồn chính thống trước khi sinh nội dung (crawler hoặc prompt có cấu trúc).
4. Làm thêm một lớp hoàn chỉnh vượt mức tối thiểu (web cho truyện tranh, video cho podcast).
5. Tối ưu chi phí API (gom nhiều slide một prompt, prompt nhất quán).
6. **Tách chữ khỏi ảnh**: chữ do code/công cụ chèn, không để model ảnh vẽ chữ tiếng Việt.

## 4. Lỗi lặp lại
- **Chữ/dấu tiếng Việt** trong ảnh, video, giọng hát (Số 5–10).
- **Nhất quán** nhân vật/giọng qua các clip ~8 giây (Số 7, 9, 10).
- **Thời gian:** dồn việc cuối giờ; đổi hướng giữa chừng; dùng AI sinh code slide rồi chỉ còn 30 phút làm tay.
- **Công cụ ngoài API BTC:** bị giám thị nhắc (nhạc, Số 3 và 9).
- **Số liệu/nguồn sai** (năm 2024 thay 2025; ảnh AI không đúng địa phương).
- **Lỗi vặt tốn thời gian:** API key thừa một ký tự (~15 phút), máy treo, mạng chập chờn, vào muộn.

## 4b. Giám khảo thực sự quan tâm
Thông điệp rõ và đơn giản; chính xác về nội dung; mức tự động hóa bằng AI và chất lượng prompt; tư duy sản phẩm dùng được thật; đúng bối cảnh người nhận; vai trò người + AI. Trưởng ban giám khảo nói họ tìm "nghệ nhân AI", không chỉ "thợ AI". Ranh giới đạo đức: không phỏng vấn nhân vật do AI tạo như thể người thật.

## 5. Điều này đổi gì trong toolkit
- Thêm skill [aitc-deploy-publisher](../skills/aitc-deploy-publisher/SKILL.md), [DEPLOY.md](DEPLOY.md), [deploy-checklist](../templates/deploy-checklist.md) và [prompt deploy](../prompts/10_deploy.md).
- Deploy không còn là "chỉ khi được yêu cầu" mà là "quyết định ngay lúc giải mã đề": đề cần web/game/app chạy trực tuyến → lên bản khung sớm.
- QA/nộp có thêm bằng chứng link live; ghi nhận nộp cả video quá trình và thành phẩm trung gian nếu BTC yêu cầu.
- Hai tình huống eval mới (E17, E18).
- 10 topic 2025 đã chuyển vào [topics-archive-2025](../topics-archive-2025/INDEX.md); bài học chung nằm ở [topics/LESSONS](../topics/LESSONS.md), topic mới dựng từ [base template](../topics/_template/SKILL.md).
