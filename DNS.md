# Các tip cấ u hình domain

## Setup domain

```
A record - @ - IP
A record - www - IP
```

## Setup subdomain

```
A record - sub - IP
A record - www.sub - IP
```

## Setup email

Create 5 MX record with following content:

```
MX Record - @ - ASPMX.L.GOOGLE.COM.
MX Record - @ - ALT1.ASPMX.L.GOOGLE.COM.
MX Record - @ - ALT2.ASPMX.L.GOOGLE.COM.
MX Record - @ - ALT2.ASPMX.L.GOOGLE.COM.
MX Record - @ - ASPMX3.GOOGLEMAIL.COM.
```

# Lưu ý khi chuyển từ namecheap sang cloudflare

Nếu bạn đã chuyển sang cloudflare và muốn sử dụng chứng chỉ TLS free của letsencrypt thì bạn cần phải tắt đi tính năng auto rewrite https trong phần cài đặt để letsencypt có thể check được.

Còn nếu bạn muốn sử dụng file thì download từ cloudfare về và bỏ vô trong nginx của bạn.
