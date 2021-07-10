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