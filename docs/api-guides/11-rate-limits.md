---
source: https://docs.thucchien.ai/docs/round-2/user-guide/rate-limits
checked: 2026-10-05
related_skill: aitc-orchestrator
operations: key-info
---

# Rate limits snapshot

Giới hạn dùng chung theo đội trong cửa sổ trượt 60 giây. Snapshot tài liệu ngày
2026-10-05:

| Key | Budget | RPM chung | TPM chung | Song song/key |
|---|---:|---:|---:|---:|
| Chính thức | `$50` | `2,880` | `17,280,000` | `10` |
| Test | `$1` | `20` | `100,000` | `5` |

Model có thể có giới hạn thấp hơn; ví dụ tài liệu hiện ghi Gemini Pro
`96,000 TPM`, image Pro `48,000 TPM`, Veo `52 RPM`. Luôn đọc `/team/info` vì
giới hạn áp cho đội/key thực tế có thể khác snapshot.

## Tránh 429

- Đặt output token vừa đủ; Gateway giữ chỗ input + max output khi bắt đầu.
- Dùng model Flash/nhẹ cho phần lớn thử nghiệm.
- Dùng queue/semaphore, không vượt số request song song của key.
- GET có thể retry giới hạn với exponential backoff.
- POST timeout/429 có thể đã tạo job/tính phí: không tự retry.
- `429 Budget has been exceeded` không thể giải quyết bằng chờ.

Mọi key của đội dùng chung bộ đếm; chia hai máy không nhân đôi quota.

## Chẩn đoán 429 theo thứ tự

| Dấu hiệu | Kiểm tra | Hành động |
|---|---|---|
| Budget đã hết | `team_info.spend` so với `max_budget` | Dừng tạo task trả phí; chờ không tăng budget |
| Nhiều request cùng lúc | Số request đang chạy/key so với `max_parallel_requests` | Giảm concurrency, thống nhất lịch hai máy |
| Một model bị chặn dù ít request | `metadata.model_tpm_limit/model_rpm_limit` | Giảm context/token cap, phân bổ thời gian cho model đó |
| Nhiều model cùng bị chặn | `team_info.rpm_limit/tpm_limit` | Giãn toàn bộ luồng của đội |
| Giới hạn đội chưa tới nhưng vẫn 429 | Có thể giới hạn upstream dùng chung | Kiểm tra tình trạng BTC, đừng đổi key/endpoint để lách |

Với model giới hạn 96.000 TPM, cap 65.536 cộng input đã chiếm phần lớn cửa sổ trước khi có output. Chọn cap theo tác vụ; với reasoning cũng phải đủ cho phần suy nghĩ, không hạ tới mức câu trả lời rỗng.

## Phân biệt chính sách BTC và helper

Tài liệu BTC khuyên backoff với rate limit; helper hiện chỉ tự retry GET có giới hạn. POST lỗi mạng/429 không tự gửi lại. Nếu dùng SDK trong adapter riêng, tắt retry tự động (`max_retries=0`) để tránh nhiều tầng retry và kiểm tra job trước khi quyết định gọi lại.

Helper không có queue/semaphore hay bộ đếm dùng chung giữa hai máy. Với ít task, giao owner và lịch trong plan; chỉ xây hàng đợi khi số tác vụ thực tế cần. Poll video khoảng 10 giây/lần trên cùng ID; không gọi create mới để kiểm tra tiến độ.
