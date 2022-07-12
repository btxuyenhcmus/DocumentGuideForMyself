# Setup mongo db by docker-compose

```
version: '3'

services:
    mongodb:
        container_name: mongodb
        image: mongo:4.0
        ports:
            - 27017:27017
        volumes:
            - DATA_DB:/data/db
        environment:
            MONGO_INITDB_ROOT_USERNAME: <username>
            MONGO_INITDB_ROOT_PASSWORD: <password>
```

# Export config

# Setup replSet for mongodb

## Setup PRIMARY mongo

1. Tạo container mongo với thuộc tính: `command: --replSet <nameset> --bind_ip_all`
2. Thao tác với mongo để init `replSet`.

   ```
   $ docker exec -it <mongo_container> bash
   $ mongo
   > rs.initiate()
   ```

Lúc này nó sẽ biến thành primary.

## Setup SECONDARY for mongodb

1. Tạo container mongo với thuộc tính: `command: --replSet <nameset> --bind_ip_all`

## Add secondary to primary

1. `>rs.add("host:port")`

## Enable secondaryOk for all secondary

1. `rs.secondaryOk()`

# Avoid switch to SECONDARY from PRIMARY

Trong quá trình phát triển, khó tránh khỏi chuyện up/down container liên tục. chúng ta cần tránh việc chuyển PRIMARY liên tục.

Set `priority` của tất cả các Node SECONDARY trở về `0`.

# Authenticate

Nếu như bạn setup mongodb không có root authenticated thì có thể thao tác bình thường.

Nếu có sử dụng authenticated thì cần phải sử dụng `*.keyFile`.

1. Create `*.keyFile`

   ```
   $ openssl rand -base64 756 > security.keyFile
   ```

2. Grant permission of docker and execute `keyFile`
   ```
   $ sudo chmod 400 security.keyFile
   $ sudo chown userdocker:groupdocker security.keyFile
   ```
3. Mount to docker and specific keyFile flag to command:
   ```
   ...
   container_name: mongodb
   image: mongo:4.0
   ports:
       - 27017:27017
   volumes:
       - DATA_DB:/data/db
       - ./security.keyFile:/data/security.keyFile
   command: --keyFile /data/security.keyFile --replset <setname> --bind_ip_all
   environment:
       MONGO_INITDB_ROOT_USERNAME: <username>
       MONGO_INITDB_ROOT_PASSWORD: <password>
   ...
   ```
4. initiate replSet and change host primary by ip public v4
5. copy `security.keyFile` vào server Secondary và cấp phát quyền như PRIMARY.
6. up container secondary như primary.
7. `rs.add("secondaryhost:port")`
8. Change all secondary priority to 0 to avoid change primary while development.

# Noted

Nếu muốn kh chạy có repl Set nữa thì ở các secondary hay primary chỉ cần tắt command đi sẽ có thể trở thành một mongodb độc lập
