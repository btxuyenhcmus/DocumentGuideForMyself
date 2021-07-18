# Những điều cần lưu ý về proxy.

## Có tất cả 4 loại proxy:
- `Transparent poxy`: Chuyển hướng các request của máy bạn đến server mà không thay đổi bất kỳ thông tin nào cả.
- `Anonymous proxy`: Là loại tự nhận là proxy, nhưng nó sẽ không chuyển địa chỉ IP của bạn đến trang web giúp cho việc ngăn chặn hành vi đánh cắp thông tin danh tính và thói quen duyệt web của bạn. Chúng có thể ngăn trang web phục vụ bạn cách nội dung quảng cáo nhắm đến vị trí của bạn.
- `Distorting proxy`: Nó gần giống với anonymous proxy nhưng bằng cách chuyển địa chỉ IP sai làm cho bạn có thể xuất hiện từ một vị trí khác để tránh các hạn chế về nội dung truy cập.
- `High Anonymity proxy`: Nó liên tục thay đổi định kỳ địa chỉ IP hiển thị cho web server, khiến cho việc theo dõi truy cập thuộc về ai khó khăn hơn.

## Những điều có được.
- Nếu khi không bật proxy, bạn dùng chrome mở tab network lên bạn sẽ thấy mỗi request nó sẽ đến một ip dest khác nhau.
- Nhưng khi sử dụng proxy, all reqesut của browser bạn sẽ đi đến ip của proxy.
- Tùy mỗi loại proxy mà nó sẽ change header lúc gửi của bạn đi.

## Nên sử dụng thằng nào
- Thằng proxy server được sử dụng nhiều nhất là `squid`, hiện có hỗ trợ deploy bằng docker và docker compose.

Link reference [High Anonymity proxy](https://www.metahackers.pro/setup-high-anonymous-elite-proxy/)