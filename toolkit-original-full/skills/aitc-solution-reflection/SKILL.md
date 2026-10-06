---
name: aitc-solution-reflection
description: Tổng kết trung thực cách giải đề, lý do lựa chọn và ý nghĩa output để chuẩn bị video sau thi; dùng khi bản cuối gần ổn định trước T+120.
metadata:
  version: "1.0"
  language: "vi"
  status: "prepared-not-btc-approved"
---
# 12 — Reflection và ý nghĩa

Đọc [hợp đồng chung](references/contract.md) khi dùng skill lần đầu. Đây là skill viết mới cho bộ toolkit, không phải skill chính thức BTC.

## Đầu vào
Đề; bản final hoặc version đang dùng; decision log; prompt/source; kết quả critic; xác nhận trực tiếp của thành viên nếu thiếu lý do.

## Quy trình
1. Lập evidence map: Requirement → Decision → Artifact evidence → Ý nghĩa dự kiến. Không yêu cầu hay tái dựng suy nghĩ bí mật của model.
2. Phân loại từng câu: FACT (nguồn quan sát), TEAM RATIONALE (quyết định ghi nhận/xác nhận), INTENDED IMPACT, LIMITATION, UNKNOWN.
3. Viết nhận xét đề: yêu cầu cốt lõi, điểm khó thực tế, điểm khiến đội phải lựa chọn; nêu dẫn chứng thay nhận xét tâng bốc BTC.
4. Chọn tối đa 3 quyết định quan trọng; nêu lựa chọn, lý do thực tế, phương án đã cân nhắc nếu có, bằng chứng trong output. Chưa có rationale thì hỏi đội, không bịa.
5. Nêu vai trò AI và con người, không chỉ liệt kê model. Không nhận tự huấn luyện model khi chỉ gọi API.
6. Nêu ý nghĩa ở mức chứng minh được: muốn giúp ai hiểu/làm gì; phần nào đã thể hiện; hiệu quả nào chưa được đo. Không nói “được cộng điểm” hay biết BGK nghĩ gì.
7. Viết takeaway một câu, bản 45 giây, và outline 3–6 phút: nhận xét đề → cách hiểu → lựa chọn → AI/con người → output/ý nghĩa → giới hạn/bài học. Chia lời cho thành viên theo đóng góp có thật.
8. Đội đọc và xác nhận. Nếu final đổi, cập nhật phần liên quan trước freeze; ghi hash/version làm căn cứ.
9. Sau T+120 sử dụng bản đã có để quay, không gọi AI tiếp theo mặc định bảo thủ khi BTC chưa xác nhận. Không sửa final artifact sau giờ vì đang làm video.

## Đầu ra bắt buộc
solution-reflection.md gồm evidence table, takeaway, 45-second script, 3–6 minute talking points, phân vai, câu chưa được nói, người duyệt.

## Kiểm tra trước khi trả kết quả
Không đổi tên skill để che mục đích; log có thể công khai kiểm tra. Không biến lý do “hết thời gian” thành chiến lược nghệ thuật. Không thêm ý nghĩa chỉ trong pitch mà artifact không có.

## Dừng và chuyển người
Thiếu dữ kiện quyết định/thiếu quyền/có mâu thuẫn luật: nêu rõ, không tự lấp chỗ trống.
Đội trưởng quyết định; chỉ tiếp tục trong phạm vi đã duyệt.
