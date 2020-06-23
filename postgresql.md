# Các tính năng cần thiết khi sử dụng postgresql (daemon not GUI)
## Dump database
Postgresql cung cấp công cộng `pg_dump` một cách đơn giản để backing từng database. Command phải được chạy dưới quyền có thể đọc database đó, trong ví dụ lần này là thao tác với database của **Odoo** nên có user postgres nhưng **owner** của các database là **odoo** (do thiết lập ban đầu).

1. Đăng nhập vào `postgres` user:
    ```
    $ su - postgres
    ```
2. Truy cập vào `psql`:
    ```
    $ psql -U odoo -d testdb2
    ```
    - **-U odoo**: Sử dụng qyền của odoo.
    - **-d testdb2**: Truy cập vào database.

    Xem tất cả các database có trong cơ sở dữ liệu của chúng ta
    ```
    testdb2=# \l
    ```
    ![psql-show](./src/static/psql-show.png)

    Tạo user postgres cho tương thích với user trên máy
    ```
    testdb2=# CREATE USER postgres;
    ```

    Cấp quyền truy cập cho user vừa tạo, (Postgresql - How to grant access to users), ở đây sẽ cho nó quyền của supperuser
    ```
    testdb2=# ALTER USER postgres WITH SUPERUSER;
    ```
3. Như vậy là đã xong với thao tác với psql, thoát khỏi `psql` và ở user `postgres`:
    ```
    pg_dump testdb2 > restoredb.dump
    ```
    Và như vậy là mình đã có một file được dump ra từ database
## Restore dump database
1. Trước tiên ta phải tạo một database mà mình muốn restore file dump vào:
    ```
    testdb2=# CREATE DATABASE restoredb WITH OWNER=odoo;
    ```
    Trong quá trình tạo có thể bị sai và việc xóa dẫn đến thông báo rằng có một sesions khác đang dùng database nên không xóa được, để xác định thằng nào đang dùng, mình sẽ list danh sách các session và database đang sử dụng.
    ```
    testdb2=# select pid as process_id, 
                usename as username, 
                datname as database_name, 
                client_addr as client_address, 
                application_name,
                backend_start,
                state,
                state_change
            from pg_stat_activity;
    ```
    ![psql-session](./src/static/psql-session.png)
2. Sau khi đã tạo được database, sẽ là bước restore
    ```
    $ psql restoredb < restoredb.dump
    ```

!!Done