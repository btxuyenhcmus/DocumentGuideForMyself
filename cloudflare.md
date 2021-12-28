# Transfer dns from namecheap to cloudflare

# SSL/TLS

## Overview

Chúng ta sẽ có 4 chế độ bảo mật.

- `Off (not secure)`: Website sẽ được truy cập dưới dạng không an toàn.
- `Flexible`: Website được bảo mật từ đầu browser đến cloudflare proxy, thời hạn là 1 năm theo gói cơ bản Universal. Lưu ý, tất cả các sub domain sẽ dùng chung 1 chứng chỉ với dns được xác thực bởi tổ chức cloudflare.
- `Full`: Website sẽ được bảo mật từ đầu browser đến cloudlfare và cả từ cloudflare đến origin server. Ở đây, từ browser sẽ dùng chứng chỉ universal của cloudflare, còn từ cloudflare đến origin server sẽ dùng chứng chỉ lưu trên server (có thể mua từ một tổ chức khác, hoặc dùng letsenscrypt free).
- `Full (strict)`: Tương tự như Full nhưng chứng chỉ ở origin server phải được down từ tổ chức đáng tin cậy của cloudflare. Tốt nhất nên tải từ mục origin certificates của cloudflare.

Edges certificates:

- Nơi quản lý chứng chỉ universal của cloudflare, và ở đây mình kh thể upload chứng chỉ mà có renew nếu như hết hạn chứng chỉ.
- Nơi cài đặt một số config (như auto rewrite http to https), lưu ý cái này mình config sẽ ảnh hưởng bước đầu đến việc lấy chứng chỉ cho origin server bằng letsencrypt.

Origin certificates:

- Download chứng chỉ từ cloudflare về và bỏ vào trong server của chúng ta.
- Nếu dùng letsencrypt thì không cần thiết.

## Lưu ý (kinh nghiệm xương máu

Khi bạn đã bật mode Full và đã có chứng chỉ ở origin server, Khi vào `chrome` báo website an toàn nhưng khi vào bằng `safari` hoặc `firefox` bị báo website không an toàn thì hãy xem lại cái link content bên trong website của bạn có cái nào là `http` hay không. hãy fix lại hết thành `https`
