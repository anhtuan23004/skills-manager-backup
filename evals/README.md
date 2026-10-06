# Đánh giá skill trên đề tập
**18 tình huống giả định, không phải đề BTC. Chưa được chạy benchmark bằng model trong gói.**

## Cách chạy
Để kiểm tra luồng đọc đề → plan → skill → thực thi và đo tốc độ, dùng [6 đề luyện skill-first](skill-first-rehearsal.md). Đây là phần bổ sung cho 18 case JSON, chưa chạy bằng model.

Chỉ trong buổi luyện hợp lệ, dùng model/công cụ BTC nếu được cấp quyền test. Chọn 3–5 case sát điểm yếu của đội; có thể chạy toàn bộ khi đủ budget. Với cùng input và cùng model, so sánh **có skill** với **prompt cơ bản không skill**. Lưu prompt/output/timing/chi phí nếu đo được. Đừng thay đổi nhiều tham số một lần rồi quy công cho skill.

Đội trưởng/người không viết prompt chấm `PASS / PARTIAL / FAIL`, giải thích với câu/cảnh/file cụ thể. Case về an toàn/tuân thủ thất bại thì phải sửa trước dùng; không lấy điểm sáng tạo bù lỗi vi phạm. Sau sửa chạy lại đúng case đó và một case khác để tránh chỉ tối ưu một mẫu.

## Ghi kết quả
Không ghi đè `cases.json` như thể case ban đầu đã được chạy. Tạo báo cáo buổi luyện riêng:
```text
case_id,skill_version,model,condition_with_or_without_skill,
run_ref,observed_behavior,grade,reviewer,elapsed_seconds,cost_if_known,next_fix
```

AI tự chấm không thay thế người xem và đánh giá artifact thực tế. Các case hành vi là bài diễn tập nội bộ, không phải kiểm định thống kê hay mô phỏng điểm số chính thức của BGK.
