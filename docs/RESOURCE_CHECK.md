# Check nhanh khi BTC cấp API

Chạy từ thư mục `AI_Thuc_Chien_Toolkit_MiVN`, dùng Python 3 có sẵn, không cần cài thư viện.
Script chỉ gọi `https://api.thucchien.ai`; không nhận URL từ response và không theo redirect.

## 1. Điền key trong `.env`

Mở `.env` tại **gốc repo `aitc2026-team-500-mivn`** (cùng cấp `.env.example`,
không phải bên trong toolkit) và điền key Gateway BTC:

```dotenv
AITC_API_KEY=key_gateway_btc_cua_ban
```

Nếu chưa có file, sao chép `.env.example` ở gốc repo thành `.env`; nếu đã có,
chỉ thêm `AITC_API_KEY`, giữ nguyên các biến AI Log. Script tự đọc file này
theo vị trí script, không phụ thuộc thư mục terminal. `.env` đã được Git bỏ qua.
Không dán key vào chat hoặc commit key vào source. `AI_LOG_API_KEY` là token khác.

Biến `AITC_API_KEY` đã export trong terminal được ưu tiên hơn `.env` (kể cả khi rỗng);
chạy `unset AITC_API_KEY` nếu muốn dùng giá trị trong file.
Hỗ trợ `KEY=value` và giá trị bọc nháy đơn/đôi; comment đặt trên dòng riêng.
Không thực thi lệnh shell, nội suy biến hoặc hỗ trợ giá trị nhiều dòng trong `.env`.

## 2. Đọc resource, chưa gọi model

```bash
python3 scripts/check_resources.py
```

- `GET /key/info`: spend, max budget, RPM/TPM, concurrency của key nếu được trả về.
- `GET /team/info?team_id=...`: ngân sách/spend chung đội, hạn mức model trong metadata nếu có.
- `GET /v1/models`: danh sách model được Gateway công bố cho key.
- `remaining = max(0, max_budget - spend)` chỉ khi có cả hai số. Không cộng ngân sách key và đội.
- `null` / `UNVERIFIED`: API không cung cấp đủ thông tin; kiểm tra dashboard BTC. Không có nghĩa vô hạn.
- RPM/TPM là giới hạn cấu hình; không phải số request/token còn lại trong phút.
  Các header `x-ratelimit-*` được giữ riêng khi Gateway trả về.

Danh sách model không bảo đảm model đang phục vụ inference; chưa gọi thì chưa xác minh.
Hai máy dùng chung ngân sách đội; nên để một máy chạy smoke.

## 3. Một request nhỏ để kiểm tra inference

```bash
python3 scripts/check_resources.py --smoke
```

Chỉ gọi **một POST** với `deepseek-flash`, prompt `Reply with only OK.`,
`thinking: {"type": "disabled"}`, `max_tokens: 16`, không stream, không retry.
Không chạy qua mọi model, không tạo ảnh/video/audio và không tự đổi sang model đắt hơn.
Nếu Flash không có trong danh sách, budget đã hết hoặc budget đội chưa xác minh,
script ghi `SKIPPED`; xem dashboard/tài liệu BTC trước khi gọi thủ công.

Kết quả gồm trạng thái, latency, token usage và header chi phí nếu có. Sau POST,
script đọc lại budget đội; số liệu có thể cập nhật trễ hoặc gồm chi tiêu của máy khác.
Không coi chênh lệch spend là chi phí chính xác của riêng smoke. Giới hạn 16 token
là trần output, không phải trần tiền; input vẫn tính phí. Thiếu header cost không có nghĩa miễn phí.

`401/403`: kiểm tra key/quyền; `404`: kiểm tra endpoint với BTC; `429`: có thể do
rate hoặc budget, không tự retry. Timeout cũng có thể đã bị tính phí; kiểm tra
dashboard trước khi chủ động chạy lại. Mặc định timeout 15 giây mỗi request,
có thể chỉnh `--timeout 10` (1–60 giây).

## Lưu kết quả và kiểm thử

```bash
mkdir -p runs
python3 scripts/check_resources.py > runs/resource-check.json
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

Report chỉ chọn các field cần thiết, không dump raw `/key/info` hoặc lỗi HTTP.
Thư mục `runs/` đã được Git bỏ qua. Report vẫn chứa thông tin ngân sách nội bộ.
Exit code: `0` = các check hoàn tất và budget đội có số liệu (smoke OK nếu yêu cầu);
`1` = lỗi/thiếu dữ liệu/smoke bị bỏ qua; `2` = sai cấu hình/tham số. Exit `0` không
có nghĩa còn đủ tiền cho tác vụ lớn: luôn đọc `remaining`.

Nguồn: [Spend checking](https://docs.thucchien.ai/docs/round-2/api-reference/spend-checking),
[DeepSeek](https://docs.thucchien.ai/docs/round-2/user-guide/openai-deepseek),
[snapshot budget nội bộ](api-guides/10-pricing.md).
DeepSeek đã đối chiếu web ngày 2026-10-06; trang spend-checking không truy cập
được trong lần kiểm tra đó, nên schema budget theo snapshot ngày 2026-10-05.
Chưa xác minh live bằng key BTC. Nếu BTC đổi schema, giữ trạng thái UNVERIFIED và cập nhật theo tài liệu mới.
