# Metabase

## Metabase là gì?

Metabase là công cụ mã nguồn mở hỗ trợ phân tích dữ liệu và chia sẻ chúng một cách dễ dàng. Metabase cho phép chúng ta đặt câu hỏi về dữ liệu và hiển thị câu trả lời dưới nhiều dạng biểu đồ khác nhau, thuận tiện cho việc đọc và xử lý thông tin.

Metabase có giao diện thân thiện, dễ sử dụng với cả những người dùng không có nhiều kiến thức về SQL, và có cả những tính năng cho những user có kiến thức tốt về SQL.

## Setup development

Assuming you have Docker installed and running, get the latest Docker image:

```
docker pull metabase/metabase:latest
```

Then start the Metabase container:

```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

This will launch a Metabase server on port 3000 by default.

Optional: to view the logs as Metabase initializes, run:

```
docker logs -f metabase
```

Once the Metabase startup completes, you can access your Metabase at localhost:3000.

## Production installation

Nếu như chạy development thì chúng ta sẽ gặp một tình trạng khi down container sẽ mất hết dữ liệu (questions, dashboard, users, etc...) mà trước đó chúng ta đã tạo. Vì các dự liệu này được lưu trong file .db với dạng DB H2 embedded.

Thay vào đó chúng ta sẽ connect tới một database engine khác như postgres để lưu trữ các thông tin này:
```
version: '3.3'

services:
  db:
    container_name: metabasedb
    image: mdillon/postgis
    restart: always
    environment:
      - POSTGRES_PASSWORD=easygop@2022!!
      - POSTGRES_USER=easygop
      - POSTGRES_DB=metabasedb
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - metabasedb:/var/lib/postgresql/data/pgdata
    networks:
      - postgres-network
  metabase:
    container_name: metabase
    volumes:
      # setup your SQLITE db (optional)
      - ./metabase-data:/metabase-data
    environment:
      - MB_DB_FILE=/metabase-data/metabase.db
      - MB_DB_TYPE=postgres
      - MB_DB_DBNAME=metabasedb
      - MB_DB_PORT=5432
      - MB_DB_USER=easygop
      - MB_DB_PASS=easygop@2022!!
      - MB_DB_HOST=db
    ports:
      - 80:3000
    image: metabase/metabase
    restart: always
    depends_on:
      - db
    networks:
      - postgres-network

volumes:
  metabasedb:

networks:
  postgres-network:
    driver: bridge
```