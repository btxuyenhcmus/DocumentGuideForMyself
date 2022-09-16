# Xây dựng và triển khai Ứng dụng lên k8s của Digital Ocean

## Yêu cầu,

- Cài đặt `doctl`, commandline tool của digital ocean.
- Cài đặt `kubectl`, commandline tool của K8s.

## Bước 1, authenticate tài khoản digital ocean trên máy

```
$ doctl auth init
```

## Bước 2, Xây dựng một cái app đơn giản

app.py

```
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = """Hello {name}!
    Hostname: {hostname}"""
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

requirements.txt

```
Flask
```

## Bước 3, build Docker Image

Dockerfile

```
# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

## Bước 4, Tải docker image lên trên container registry của DigitalOcean

```
$ doctl registry create <your-registry-name>
```

```
$ doctl registry login
```

```
$ docker tag <your-app> registry.digitalocean.com/<your-registry-name>/<your-app>

$ docker push registry.digitalocean.com/<your-registry-name>/<your-app>
```

## Bước 5, tạo cluster

```
$ doctl kubernetes cluster create <your-cluster-name> --tag <your-tag> --auto-upgrade=true --node-pool "name=<your-pool-name>;count=2;auto-scale=true;min-nodes=1;max-nodes=3;tag=<your-tag>"
```

> The `--node-pool "name=mypool;count=2;auto-scale=true;min-nodes=1;max-nodes=3;tag=do-tutorial"` flags initializes the cluster with two _node pools_, named `mypool`, tags the nodes `do-tutorial`, and allows the pool to automatically scale in size between one and three nodes (depending on the needed capacity).

## Bước 6, Chạy app trên cluster

Xác thực k8s dùng registry, để cho k8s có thể pull image từ private registry mà ta đã setup từ trước đó

```
doctl registry kubernetes-manifest | kubectl apply -f -
```

Next, use this secret as an authentication token when pulling your images from your private registry and creating containers

```
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "registry-<your-registry-name>"}]}'
```

Use the two nodes and run multiple instances of your application at once. To do this, create a Deployment of your app, which is the object Kubernetes uses to maintain the desired state of your running containers. Run the following command to launch the app live in the cluster:

```
$ kubectl create deployment <your-app> --image=registry.digitalocean.com/<your-registry-name>/<your-app>
```

Try scaling up to run 20 replicas:

```
$ kubectl scale deployment/<your-app> --replicas=20
```

Tạo load balancer để đưa tất cả các replica ra ngoài với một cổng duy nhất.

```
$ kubectl expose deployment <your-app> --type=LoadBalancer --port=80 --target-port=80
```

Sau câu lệnh này kết quả sẽ trả về 1 load-balancer và IP tĩnh để chúng ta config dns và cho người dùng sử dụng.
