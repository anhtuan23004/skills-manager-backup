# Bộ skill hình ảnh nên cân nhắc và 3 quy trình

Ghi nhận ngày 2026-10-06. "Nổi tiếng" là theo danh mục skill công khai; **chưa kiểm toán mã** từng skill. Theo `docs/MCP_SELECTION.md`, số sao không chứng minh độ an toàn hay việc BTC cho phép: phải đọc `SKILL.md` và script, chốt phiên bản, thử trên 2 máy. Phạm vi mã tiện ích mang vào thi cần BTC xác nhận riêng ([TEAM_RULES](../../../docs/TEAM_RULES.md)).

## Bộ skill

| Bộ skill | Làm gì | Dùng thế nào trong thi |
|---|---|---|
| anthropics/skills: `canvas-design`, `theme-factory`, `frontend-design` | `canvas-design` tạo poster/ảnh tĩnh PNG/PDF theo "nêu triết lý thiết kế rồi thể hiện"; hai skill kia về chữ, màu, bố cục | Chỉ làm **tham chiếu chỉ dẫn** cho bố cục/typography. `aitc-image-director` ghi: không dùng `canvas-design` nguyên bản để đặt sáng tạo cao hơn brief, không đưa font nguồn tham khảo vào bộ |
| Mẫu "HTML/CSS → PNG" (ví dụ Social Canvas: render bằng Playwright, đọc lại ảnh, đánh giá, lặp) | Ghép chữ và bố cục bằng code ở kích thước chính xác | Khớp nhất với bài học VTV (URX thắng Số 8). Playwright chỉ bật khi cần theo `MCP_SELECTION` |
| [huashu-design](huashu-design-lite.md) | Bộ công cụ HTML-native: slide, infographic, xuất PNG/PDF/PPTX/MP4, chấm phản biện | Dùng một phần, xem ghi chú riêng |
| Taste (lớp chống "AI slop") | Quy tắc thẩm mỹ, phong cách | Dùng như checklist phản biện, không phải công cụ sinh |
| Image Poster / Nano Banana skills (gọi nhà cung cấp ảnh ngoài) | Dựng prompt rồi gọi API ảnh ngoài | **Không dùng** (mọi AI phải qua Gateway BTC). Chỉ học cách dựng prompt: bố cục, ánh sáng, bảng màu |
| Bộ của đội | `aitc-image-director`, `vietnam-context-review`, `artifact-critic`, `final-qa`, MCP `aitc-local-media-qa` | Lõi để làm; skill ngoài chỉ bổ sung ý |

Gateway BTC nêu các alias ảnh `nano-banana-2-lite`, `nano-banana-2`, `nano-banana-pro` (kiểm tra lại availability) dùng `aspect_ratio`; model OpenAI image dùng `size`/`quality` và chỉ khi được cấp. Tỷ lệ đúng chưa chứng minh đủ độ phân giải đề: bố cục cuối nên ghép bằng HTML ở đúng kích thước. Chi tiết: [Image guide](../../../docs/api-guides/03-image-generation.md).

## Quy trình A — Infographic từ văn bản dài (luật, chính sách)
1. T+0–18: trích ý chính vào `templates/claims.csv`, mỗi ý kèm điều khoản gốc; chốt kích thước và đối tượng.
2. T+18–30: chọn một mạch kể (ví dụ bạn là ai → quyền → nghĩa vụ → điều cấm → làm gì); wireframe vùng; bảng màu tối đa 3 màu, chữ tương phản.
3. T+30–65: AI sinh hình minh họa **không chữ** theo từng vùng; HTML/CSS ghép chữ đã duyệt từ claims, render PNG ở kích thước đề.
4. T+65–90: phản biện: đối chiếu từng ý với claims, đọc chữ ở kích thước thật, sửa cục bộ.
5. T+90–112: xuất bản, final QA, manifest.

## Quy trình B — Tờ rơi hoặc poster
1. Thông điệp một câu, đối tượng.
2. Storyboard từng panel (6 panel với tờ gấp ba), mỗi panel một ý.
3. Style sheet chung (palette, phong cách, nhân vật).
4. Sinh một ảnh liền cho cả tờ hoặc các ảnh cùng style.
5. HTML ghép chữ lớn và call to action.
6. Kiểm tra khi gấp: panel sáng/tối đặt cạnh nhau, panel giữa là điểm nhấn.
7. Xuất PDF/PNG in; lưu prompt và thành phẩm trung gian.

## Quy trình C — Truyện tranh hoặc bộ ảnh nhiều trang
1. Chia nhịp truyện, mỗi trang một nhịp.
2. Tạo character sheet **trong phiên** (`image-director` chỉ cho tham chiếu tạo trong phiên).
3. Các trang sau dùng mô tả nhân vật cố định trong prompt. Nếu cần chỉnh sửa ảnh qua hội thoại, dùng endpoint chat có `modalities: ["image"]` mà guide đã nêu. Mức nhất quán thực tế là UNVERIFIED, nên thử nhỏ trước.
4. Chừa bong bóng thoại trống, điền chữ bằng HTML.
5. Ghép trang, xem cả bộ liền mạch.

## Vòng lặp chung
Sinh một mẫu nhỏ → mở ảnh thật để kiểm tra (hình thể, chữ Việt, tương phản, bố cục) → sửa cục bộ thay vì sinh lại toàn bộ. Tiết kiệm budget $50 của đội và giữ phần đã đạt.

## Nguồn tra cứu
- https://claudemarketplaces.com/skills/aiskillstore/marketplace/canvas-design
- https://claudskills.com/skills/social-canvas/
- https://elevarus.com/top-10-claude-code-skills-for-marketing/
- https://codenote.net/en/posts/anthropic-official-skills-catalog-overview/
- https://docs.apiyi.com/en/api-capabilities/nano-banana-image/skills
