# Trong Tip lần này mình sẽ nói về kinh nghiệm dựng dự án buyngon bằng `docker-compose`.

1. Vì dự án lần này mình không code chính nên cách tổ chức project của mấy bạn dev gặp các vấn đề sau:
    - Chia branch git không hợp lý, không có một branch quy định deploy production, một branch deploy staging.
    - File `.env` không nên có mặt trong git. chỉ nên có một file `.env.template` chứa cấu trúc các tham số. còn lại các môi trường khác nhau sẽ fill vào các thông số khác nhau.
    - Viết `Dockerfile` không cần thiết. project api được chạy bởi node image thì mình chỉ cần pull `node:12-alpine` về và `mount volumes` lấy luôn `node_modules` vào trong là được không cần phải build thêm một images khác mà chỉ khác biết là `npm install`.
    - Cần chia `docker-compose*.yml` thành 3 file riêng biệt: cho `local` cho `staging` cho `production`.
    - Theo thói quen các bạn chỉ chia nhỏ các prodct mà quên mất còn các config `webserver` thiếu `nginx or apache` và `letscrypt`.

2. Hiểu được các điều đó nên mình có tổ chứ lại. Và quan trọng là viết lại file `docker-compose` cho staging.
    - Viết lại các `services` sẵn có.
    - Thêm 2 `service` là `nginx` và `certbot`.
    - `Mount` thư mục `conf` vào nginx, mount `data` và `logs` vào `certbot`.
    - Run `docker-compose` lần đầu với certbot `command` `--staging -d dns`.
    - Sửa file conf nginx trể trỏ vào service mình muốn. nhớ dùng tên service. Run `docker-compose` lần 2 với `command` `--force-renewal -d dns`.
    - Restart `nginx` là có thể vào được `http, https`.

3. Vì trong project có 3 project con đó là `api, admin, web`.
    - Nên bên trong 3 proejct con có thêm 3 file `.env`.
    - Sửa lại các tham số từ như IP thì nên dùng tên service để auto generate IP.
    - Đối với api nên thay bằng tên miền.
    - Riêng `DB staging` nó còn phục vụ cho `local` thực hiện nên mình cần expose public port và open port đó ra ngoài cho các client cos thể kết nối tới ngoài internal sys.