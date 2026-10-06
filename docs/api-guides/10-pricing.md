---
source: https://docs.thucchien.ai/docs/round-2/user-guide/pricing
checked: 2026-10-05
related_skill: aitc-orchestrator
operations: key-info
---

# Pricing snapshot

Đây là checklist, không phải bảng giá cố định. Trước phiên thi và trước batch
lớn, mở tài liệu nguồn rồi kiểm tra `/key/info` và `/team/info`.

## Nguyên tắc

- Text/embedding thường tính theo 1M token input/output.
- Reasoning token không hiện trong câu trả lời nhưng vẫn tính như output.
- Gemini image hiện tính theo ảnh ở độ phân giải mặc định; `gpt-image-*` tính
  theo image token, size và quality.
- Veo tính theo số giây ngay khi job được tạo.
- Web grounding cộng phí tìm kiếm ngoài token.
- TTS/STT tính theo text/audio token hoặc thời lượng tùy model.

Snapshot đáng chú ý ngày 2026-10-05: tài liệu ghi video lite 720p khoảng
`$0.05/giây`, fast 720p khoảng `$0.10/giây`, và model Veo chất lượng cao khoảng
`$0.40/giây`. Giá ảnh, text và search thay đổi theo model; xem bảng nguồn thay
vì chép số vào logic.

## Kiểm tra budget và quota

Tiện ích có sẵn: `python3 scripts/check_resources.py` từ gốc toolkit.
Xem [RESOURCE_CHECK](../RESOURCE_CHECK.md) để đọc budget/model/rate limit và
thử một request `deepseek-flash` bằng `--smoke` khi cần.

```bash
# Kiểm tra thông tin spend của key
curl -s -X GET "https://api.thucchien.ai/key/info" \
  -H "Authorization: Bearer $AITC_API_KEY"

# Kiểm tra danh sách model khả dụng
curl -s -X GET "https://api.thucchien.ai/v1/models" \
  -H "Authorization: Bearer $AITC_API_KEY"
```

Lấy `team_id` từ `/key/info` rồi gọi `/team/info?team_id=<team_id>` để xem tổng spend và budget của cả đội. Không đưa secret key vào file lưu trong repo.

## Tránh nhầm thông tin key và team

| API / field | Ý nghĩa |
|---|---|
| `/key/info` → `info.spend` | Chi tiêu riêng key, không phải tổng đội |
| `info.team_id` | Dùng truy vấn `/team/info?team_id=...` |
| `info.max_parallel_requests` | Số request đồng thời trên key |
| `/team/info` → `team_info.spend`, `max_budget` | Chi tiêu/ngân sách chung đội |
| `team_info.rpm_limit`, `tpm_limit` | Rate limit chung; chi tiết model trong `metadata.model_*_limit` |
| `/v1/models` → `data[].id` | Danh sách model key thực sự gọi được |

`max_budget=null` hoặc `info.models=[]` không có nghĩa ngân sách vô hạn hay không gọi được model. Đội có thể đặt giới hạn/model ở team.

Dùng trang quản lý BTC hoặc API `/team/info` để xem chi tiêu chính xác của đội.

## Ước lượng đủ để quyết định

- Text: `(input_uncached × giá_input + input_cached × giá_cached + output × giá_output) / 1.000.000`; không tính input cached hai lần. Output tính cả reasoning khi model có.
- Video: số giây × giá/giây theo model/độ phân giải × số lần tạo. Ví dụ lite 720p 4 giây: khoảng `$0.20`/job theo snapshot; 5 lần tạo khoảng `$1.00`.
- Grounding: phí token + phí tìm kiếm; một request có thể tạo nhiều truy vấn.
- Chi phí thực của lần gọi có thể có ở header `x-litellm-response-cost`; thiếu header không có nghĩa miễn phí.

Lưu tổng ước lượng vào task trước batch, cộng dự phòng cho lần sửa. Theo dõi số thực ở team; không cộng spend của một key với team spend vì bị đếm hai lần. Tái dùng embedding/asset đã đạt và chỉ đưa context cần thiết vào request sau.

API reference:
<https://docs.thucchien.ai/docs/round-2/api-reference/spend-checking>.
