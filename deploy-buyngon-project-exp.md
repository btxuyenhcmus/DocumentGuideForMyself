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

4. Sau khi deploy lên thì gặp một vấn đề là `infra project` chưa ổn:
    - Chưa phân biệt giữa 3 môi trường `local`, `staging`, `production`.
    - File `.env` còn phân bố lung tung.
    - `Dockerfile` cần viết khác nhau ở 3 môi trường.

5. Xây dựng lại cấu trúc để có thể viết `bash scripts` deploy tự động sau này.
    - `Docker-compose` chia làm 3 file riêng, Docker-compose ở staging và production giống nhau, chỉ khác là các volumes config cần trỏ đến thư mục khác. Docker-compose ở local sẽ viết ít lại và bỏ đi 2 service `nginx` và `cerbot`.
    - `Dockerfile` ở staging và production giống nhau. Riêng phần api thì được expose thành port, còn web và admin là reactjs cần phải `RUN yarn build` thì mới đúng với quy tắt deploy reactjs. Còn trên local thì tất cả được expose ra port cho tiện debug cũng như code.
    - Tạo một file `.env.templates` để lưu tên các biến môi trường. ở các môi trường khác nhau mình sẽ copy thành một bảng `.env` và fill value vào trong các biến thích hợp.
    - Viết lại đúng thứ tự `depends_on` các services để đảm bảo run command đúng một lần.
    - Viết config nginx thành 2 thư mục `conf` và `conf.prod`.
    - Tất cả các images cần đánh `tags version alpine` cho nó.

6. Viết file `bash scripts` chạy tự động. (CI/CD)