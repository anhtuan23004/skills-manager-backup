# Baseline process theo topic: quick win khi nhận đề

Mục tiêu: nhận đề xong trong **15–25 phút đầu** phải có một bản chạy được, đủ requirement bắt buộc, dù xấu. Thời gian còn lại dùng để nâng chất lượng. Mọi bước chỉ dùng endpoint trong [api-guides](api-guides/README.md) (kiểm tra ngày 2026-10-05). Đề thi và quy định BTC luôn thắng tài liệu này.

**Giả định cần xác nhận:** phiên thi khoảng 2 giờ (mùa 1 quan sát được; mùa 2 chưa rõ). Mốc thời gian dưới đây tính theo 120 phút, chia lại theo tỉ lệ nếu phiên khác. Model trong ví dụ phải có trong `GET /v1/models` của key đội.

## 0. Việc chuẩn bị trước ngày thi (không tính vào giờ thi)

1. Một thư mục `solution/` mẫu: `requests/ assets/ qa/ final/` ([SKILL_EXECUTION](SKILL_EXECUTION.md)).
2. Script gọi Gateway cho từng operation (text, image, video 3 bước, tts, stt, embeddings), đã chạy thử bằng key test (`$1`, 20 RPM). OpenAI SDK phải đặt `max_retries=0`.
3. Tool local đã cài và thử: `ffmpeg`/`ffprobe`, trình duyệt headless để render HTML ra PNG/PDF, thư viện dựng slide hoặc PDF. Script export của [huashu-design](../topics-archive-2025/03-hinh-anh/huashu-design/SKILL.md) là code bên thứ ba: cần đọc, được đội và BTC đồng ý rồi mới cài/chạy.
4. Bảng chuẩn hóa phát âm (`templates/pronunciation.csv`) và danh sách nguồn chính thống theo lĩnh vực (luật, số liệu 2025, thông tin nhà tài trợ).
5. Một bộ template HTML có sẵn chữ tiếng Việt đúng dấu cho poster, tờ rơi, infographic, trang truyện.
6. Các topic 2025 (đã chuyển vào `topics-archive-2025/`) đều có mục "Baseline quick win (API-based)"; topic mới dùng [base template](../topics/_template/SKILL.md) và [LESSONS](../topics/LESSONS.md).

## 1. 10 phút đầu, giống nhau cho mọi đề

| Phút | Việc | Điều kiện đạt |
|---|---|---|
| 0–3 | Đọc đề, ghi requirement vào `templates/requirements.csv`: định dạng, độ dài, số trang, người nhận, có cần link online không | Mỗi requirement bắt buộc có ID |
| 3–5 | `python3 scripts/check_resources.py` và `GET /v1/models` | Biết model được gọi, budget, RPM của đội |
| 5–8 | Smoke test đúng operation đề cần: 1 call text ngắn; nếu cần thì 1 ảnh, 1 TTS vài giây | Có file thật mở/nghe được |
| 8–10 | Chốt concept đơn giản nhất đáp ứng requirement; chọn nhóm bên dưới | Một câu thông điệp, một người nhận |

Quy tắc xuyên suốt, rút từ guide BTC và quan sát mùa 1:
- POST tạo ảnh/video/audio không retry mù quáng; lỗi `429 budget` thì dừng mọi call trả phí.
- Chữ tiếng Việt do HTML/code chèn, ảnh AI sinh với prompt "không chữ, không logo, chừa khoảng trống".
- Số liệu và nội dung pháp lý lấy từ nguồn chính thống, đúng năm; bật grounding chỉ khi cần thông tin mới.
- Mở file thật (xem, nghe, `ffprobe`) trước khi ghi PASS.
- Lưu bản đạt trung gian vào `final/` ngay, đừng chờ bản hoàn hảo.

## 2. Baseline theo nhóm và topic

Mỗi mục có: **Quick win** (bản đầu tiên chạy được), **Pipeline**, **Chi phí/guard**, **Fallback**, **Cổng QA**.

### Nhóm 1: Web & App (cần deploy, xem [DEPLOY](DEPLOY.md))

**Nguyên tắc chung:** bản quick win là **site tĩnh** với nội dung và ảnh sinh sẵn, deploy ngay ở phút ~30. Mọi tính năng gọi API thêm sau, và key chỉ nằm ở server, không bao giờ ở client.

**website-du-lich**
- Quick win (phút 0–35): một trang tĩnh có các module đã chốt (giới thiệu, điểm đến, văn hóa/ẩm thực, lịch trình, liên hệ), deploy lên VPS.
- Pipeline: 1) chốt cấu trúc/module trước khi prompt. 2) `chat/completions` tạo nội dung từng module, JSON có khóa rõ. 3) grounding cho thông tin địa phương, lưu URL nguồn. 4) `images/generations` (`nano-banana-2-lite`, `aspect_ratio` 16:9 cho hero, 4:3 cho thẻ) với prompt đúng bối cảnh địa phương, không chữ. 5) ghép HTML và deploy. 6) nâng cấp: bản đồ, tìm kiếm, chatbot RAG qua `embeddings` + text, gọi từ backend.
- Guard: mỗi ảnh một request riêng; ảnh AI thiếu chân thực bị nghi ngờ nên ghi rõ ảnh minh họa và ưu tiên ảnh đúng địa phương được phép dùng.
- Fallback: bỏ tính năng gọi API lúc chạy, giữ site tĩnh.
- Cổng QA: link công khai mở được từ máy khác, mobile OK, mọi nguồn có URL.

**game-giao-duc**
- Quick win (phút 0–40): game web một màn chơi được, dữ liệu câu hỏi nằm trong file JSON tĩnh, deploy sớm.
- Pipeline: 1) lấy nội dung chính thống (crawler hoặc grounding), lưu nguồn. 2) `chat/completions` (`response_format` JSON) sinh bộ câu hỏi, validate schema. 3) game HTML/JS một vòng chơi + điểm. 4) ảnh nhân vật/nền bằng Nano Banana, không chữ. 5) deploy; còn 50 phút thì chuyển sang hoàn thiện và deploy (giám thị mùa 1 nhắc mốc này). 6) nâng cấp: thêm màn, âm thanh `audio/speech`.
- Guard: kiểm tra nội dung giáo dục với nguồn trước khi đưa vào game; không nhúng key vào JS.
- Fallback: game ít màn nhưng chạy ổn định trên điện thoại.
- Cổng QA: người ngoài đội chơi được từ link, không lỗi ở màn đầu.

### Nhóm 2: Tài liệu / chiến lược (≤10 trang, không có API tạo slide)

**Nguyên tắc chung:** Gateway chỉ cho text và ảnh. Slide/tài liệu dựng **local** (HTML → PDF hoặc thư viện dựng slide), nên cần template chuẩn bị sẵn. Cần xác nhận với BTC định dạng nộp (PDF hay PPTX).

**bao-cao-tai-chinh**
- Quick win (phút 0–30): bộ khung đúng format báo cáo thật, mỗi trang có tiêu đề và số liệu thật, xuất PDF.
- Pipeline: 1) dàn trang ≤10 trang từ mẫu báo cáo thật. 2) lấy số liệu năm đúng (đề nói 2025 thì không dùng 2024); nếu đề cho dữ liệu thì dùng dữ liệu đó, nếu không thì grounding kèm ngày và URL. 3) `chat/completions` viết từng trang kèm bảng claim ([claims.csv](../templates/claims.csv)). 4) biểu đồ vẽ bằng code từ số liệu, không nhờ model ảnh vẽ số. 5) dựng PDF, kiểm tra từng trang.
- Guard: gom nhiều trang vào một prompt có cấu trúc để tiết kiệm token (đội thắng mùa 1 làm vậy); output cap vừa đủ.
- Fallback: ít trang hơn nhưng đủ số liệu và nhận định.
- Cổng QA: mỗi con số có nguồn và đúng năm, không trang tràn chữ.

**marketing-chien-dich**
- Quick win (phút 0–30): tài liệu 6–8 trang gồm insight, ý tưởng lớn, thông điệp, kênh, KPI, timeline.
- Pipeline: 1) chốt insight và một ý tưởng lõi. 2) `chat/completions` viết nội dung các phần trong một lượt có cấu trúc. 3) 2–4 key visual bằng Nano Banana (`16:9`, không chữ), chữ chèn bằng HTML. 4) dựng PDF/slide. 5) nâng cấp: mock-up bài đăng, video 4–8 giây bằng Veo lite.
- Guard: kiểm tra ngữ cảnh văn hóa Việt (lễ, kiêng kỵ) bằng `aitc-vietnam-context-review`.
- Fallback: bỏ phần visual động, giữ ý tưởng và kế hoạch.
- Cổng QA: ý tưởng khớp nhà tài trợ và người nhận, đủ trang theo đề.

### Nhóm 3: Hình ảnh / in ấn (chữ tiếng Việt là rủi ro số 1)

**Nguyên tắc chung:** quy trình **ảnh nền AI + chữ bằng HTML**. Pipeline chung: text → bố cục → ảnh nền không chữ → HTML chèn chữ → render PNG/PDF ở đúng kích thước → kiểm tra.

**infographic-phap-luat**
- Quick win (phút 0–30): infographic 1 trang, 4–6 khối thông tin, đã xuất PNG.
- Pipeline: 1) lấy văn bản luật chính thống, trích điều khoản cần dùng. 2) `chat/completions` tóm tắt thành khối ngắn, mỗi khối gắn điều khoản. 3) icon/nền bằng Nano Banana, `3:4` hoặc `9:16`, không chữ. 4) HTML chèn chữ, kiểm tra tương phản. 5) render PNG.
- Guard: đối chiếu từng khối với điều luật (bảng claim); không để model tự diễn giải.
- Fallback: infographic thuần HTML/CSS không ảnh AI.
- Cổng QA: đúng nội dung luật, không lỗi dấu, đọc được khi thu nhỏ, bước đóng gói xuất file đã được thử trước.

**truyen-tranh**
- Quick win (phút 0–40): 5 trang A4 có khung truyện, ảnh và thoại, xuất PDF.
- Pipeline: 1) kịch bản 5–10 trang, mỗi trang 2–4 khung (JSON). 2) sheet nhân vật: mô tả cố định lặp lại trong mọi prompt để nhất quán. 3) mỗi khung một ảnh, chừa bong bóng thoại trống. 4) HTML điền chữ vào bong bóng. 5) PDF, nâng cấp: bản web (đội thắng mùa 1 làm thêm).
- Guard: ảnh sinh từng request, chọn bản tốt rồi giữ lại; chỉ sinh lại khung hỏng.
- Fallback: ít trang, bố cục đơn giản, nhân vật phong cách vector.
- Cổng QA: nhân vật nhất quán qua các trang, thông điệp chống lừa đảo rõ, đủ 5–10 trang.

**to-roi-gap-ba**
- Quick win (phút 0–30): tờ A4 ngang gấp ba có 6 mặt đúng thứ tự gấp.
- Pipeline: 1) phân vai 6 mặt (bìa, mặt gấp trong, nội dung, liên hệ). 2) text ngắn gọn cho đúng người nhận. 3) 1–2 ảnh nền bằng Nano Banana. 4) HTML 297×210 mm, ba cột; kiểm tra khi in/gấp. 5) nộp cả file trung gian nếu đề cho phép (đội thắng mùa 1 nộp).
- Cổng QA: số liệu/nguồn đúng, chữ không bị cắt ở nếp gấp, nội dung phù hợp chủ đề nhạy cảm.

### Nhóm 4: Video & Audio (dựng từ đoạn ngắn; **không có endpoint nhạc**)

**Phát hiện quan trọng:** api-guides không có API sinh nhạc. TTS (`audio/speech`) và STT có; video chỉ Veo 4/6/8 giây. Nhạc nền và bài hát phải hỏi BTC trước ([evals E15](../evals/cases.json)). Nếu không có đường chính thức thì dùng bản không nhạc hoặc nguồn BTC cho phép.

**Chi phí tham khảo:** Veo lite 720p ≈ $0.05/giây → video 72 giây ≈ $3.6/lượt; dự trù ×3 cho sinh lại. Budget chính thức $50, Veo 52 RPM, poll mỗi ~10 giây.

**ban-tin-video (60–80 giây)**
- Quick win (phút 0–45): bản tin 60 giây ghép từ ảnh tĩnh + giọng đọc + phụ đề, nếu video AI chưa kịp.
- Pipeline: 1) kịch bản có mốc thời gian, mỗi đoạn ≤8 giây, tin lấy từ nguồn chính thống (grounding, có ngày). 2) `audio/speech` đọc toàn bài bằng một giọng cố định, đo thời lượng bằng `ffprobe`. 3) ảnh MC/cảnh bằng Nano Banana; cảnh Veo 4–8 giây dùng image-to-video (`input_reference`) để giữ nhất quán. 4) `ffmpeg` ghép, thêm phụ đề do code chèn. 5) xem toàn bộ bản dựng.
- Guard: thử 1 cảnh 4 giây trước; không phỏng vấn nhân vật AI như người thật.
- Fallback: ảnh tĩnh + chuyển động nhẹ bằng ffmpeg + giọng đọc.
- Cổng QA: 60–80 giây đúng khoảng, giọng và MC nhất quán, nguồn có thể truy vết.

**podcast-audio (2–4 phút, 2 nhân vật)**
- Quick win (phút 0–40): bản audio 2 giọng không nhạc nền, ghép thủ công.
- Pipeline: 1) kịch bản đối thoại, tính cách đối lập, có "dạ/vâng", cười. 2) chuẩn hóa tên riêng và số. 3) `audio/speech` từng lượt thoại với 2 voice cố định (đúng họ model), sinh thử 1 câu mỗi giọng trước. 4) `ffmpeg` ghép, chuẩn hóa âm lượng, kiểm tra khoảng lặng. 5) nâng cấp: video ảnh tĩnh + phụ đề.
- Guard: không đổi giọng giữa chừng; nếu đề yêu cầu nhạc nền mà chưa có nguồn hợp lệ thì hỏi BTC.
- Fallback: nộp bản không nhạc nếu đề cho phép, ghi rõ trong bài nộp.
- Cổng QA: nghe hết từ đầu đến cuối, giọng đúng tuổi/vùng miền, đúng độ dài.

**sang-tac-bai-hat (~3 phút + lyric video)**
- Quick win (phút 0–45): lyric video ảnh nền + lời chạy + giọng đọc/ngâm lời bài hát bằng TTS.
- Pipeline: 1) lời bài hát từ nguồn chính thống của đơn vị đề cập. 2) `chat/completions` viết lời, kiểm tra vần và dấu. 3) **hỏi BTC về nguồn nhạc**; nếu không có thì TTS đọc lời nhịp điệu, không giả vờ là hát. 4) ảnh nền Nano Banana. 5) `ffmpeg` dựng lyric video, đồng bộ bằng mốc thời gian.
- Guard: "cưỡng từ" (hát/đọc sai dấu) là tối kỵ; kiểm tra phát âm từng câu.
- Fallback: video lời + đọc, nêu rõ giới hạn công cụ.
- Cổng QA: lời đúng nguồn, đồng bộ lời và âm thanh, xem hết từ đầu đến cuối.

### Nhóm dự phòng cho mùa 2: dữ liệu thật / RAG

Dạng này chưa có trong mùa 1 nhưng mùa 2 nhấn mạnh dữ liệu sạch và bài toán thật.
- Quick win (phút 0–40): hỏi đáp trên tài liệu của đề, có trích nguồn, chạy local hoặc deploy.
- Pipeline ([RAG workflow](../skills/aitc-production-planner/references/rag-workflow.md)): 1) chunk tài liệu kèm source ID. 2) `embeddings` (`gemini-embedding-001`), lưu vector vào file JSON cùng model ID và hash. 3) embed câu hỏi, cosine top-K. 4) `chat/completions` trả lời chỉ dựa trên đoạn trích, kèm citation. 5) thử cả câu ngoài tài liệu, phải trả lời "không có trong tài liệu".
- Guard: không so vector hai model khác nhau; `gemini-embedding-2` gửi từng đoạn một request; không log vector vào ngữ cảnh.
- Cổng QA: citation đúng đoạn, không bịa khi thiếu evidence, dữ liệu cá nhân được xử lý theo quy định đề.

## 3. Điều cần hỏi BTC trước khi thi hoặc đầu phiên

1. Nhạc/bài hát: có endpoint hay công cụ nào được phép? Bản không nhạc có bị trừ không?
2. Định dạng nộp slide/tài liệu (PDF, PPTX) và công cụ dựng được phép.
3. Link deploy nộp ở đâu, cần sống bao lâu; thư viện/ảnh bên ngoài có được dùng không.
4. Phạm vi "chuẩn bị sẵn" cho phép (template, script, pipeline), xem [TEAM_RULES](TEAM_RULES.md).
5. Danh sách model mỗi key được cấp (khác `/key/info`), giới hạn Veo, TTS voice hỗ trợ tiếng Việt.

## 4. Việc nên làm tiếp trong toolkit

- Tạo script `run_baseline.py` cho mỗi nhóm (text → ảnh → HTML → PNG/PDF) đã thử trước giờ thi.
- Thêm bước kiểm tra an toàn và đạo đức vào QA (BTC nêu rõ tiêu chí này cho mùa 2).
- Cập nhật mục "Team notes" của từng topic sau mỗi buổi luyện, kèm thời gian thực tế mỗi bước.
