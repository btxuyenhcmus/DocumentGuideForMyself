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

1. Tạo container mongo với thuộc tính: `command: --replSet <nameset>`

## Add secondary to primary

1. `>rs.add("host:port")`

## Enable secondaryOk for all secondary

1. `rs.secondaryOk()`
