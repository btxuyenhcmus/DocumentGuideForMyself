# Running Redis with dockerd and from source

## 1. Build redis with docker and using redis client to connect redis server.

- Create `redis.conf` file config to overide config of docker.

  ```
  requirepass RBOJ9cCNoGCKhlEBwQLHri1g+atWgn4Xn4HwNUbtzoVxAYxkiYBi7aufl4MILv1nxBqR4L6NNzI0X6cE
  ```

  Content file specific authenticate to connect to redis server

- Create `docker-compose.yml` file along side with file config.
  ```
  version: '2'
  services:
      redis:
          container_name: redis-server
          image: redis
          restart: unless-stopped
          ports:
          - "6379:6379"
          volumes:
          - "./redis.conf:/usr/local/etc/redis/redis.conf"
          command: redis-server /usr/local/etc/redis/redis.conf
  ```
- Run command `$ docker-compose up -d` to start redis container.

- Run above command to start redis client
  ```
  docker run -it --network some-network --rm redis redis-cli -h redis-server
  ```
  In place, some-network is name of net that redis-server container running on, you can see this by `$ docker inspect redis-server` and read in networkSetting tab

> Follow step by step is you can start redis server and running redis client to ...

## 2. Clear all caches in redis container

```
$ docker exec -it redis-container sh
redis -$ redis-cli
localhost:port->auth password
OK
localhost:port->flushall
OK
```
