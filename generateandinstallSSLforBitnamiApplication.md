# Generate And Install A Let's Encrypt SSL Certificate For A Bitnami Application

## Introduction

**Let's Encrypt** là tổ chức phát hành chúng chỉ (CA) miễn phí cấp chứng chỉ SSL. Bạn có thể sử dụng các chứng chỉ SSL này để bảo mật lượng truy cập đén và đi từ máy chủ ứng dụng bitnam của mình.

Hướng dẫn này sẽ hướng dẫn bạn quy trình tạo chứng chỉ SSL Let's Encrypt cho trên miền của bạn cũng như cài đặt và định cấu hình nó để hoạt động với stack bitnami application.

## Assumptions And Prerequisites (Giả thuyết và yêu cầu)

- Bạn đã deploy một ứng dụng bitnami và ứng dụng này được public IP address để Let's Encrypt có thể xác nhận domain của bạn.
- Bạn cần có các thông tin cần thiết để login vào instance bitnami, tức là tối giản nhất bạn có thể ssh vào bên trong instance cloud của bạn để có thể thao tác bên trong nó.
- Ban phải có một domain (recommend **[namecheap.com](www.namecheap.com)**.
- Bạn phải cấu hình domain DNS trỏ tới IP public instance (tab advantage DNS in namecheap).

## Use The bitnami HTTPS configuration tool

> Tool này không support cho ứng dụng bitnami sử dụng nginx websever.

Bitnami HTTPS Configuration Tool là tổ hợp các command line cho múc đích cấu hình ứng dựng bitnami. Ứng dụng được lưu trong thư mục `/opt/bitnami`.

Launch the Bitnami HTTPS Configuration Tool, execute the following command and follow the prompts:

```
$ sudo /opt/bitnami/bncert-tool
```

## Một cách tiếp cận khác với bitnami Nginx

> Lưu ý, chúng ta đang thao tác sửa đổi cấu trúc tệp và cấu hình cho ứng dụng. Chúng ta cần xác định structure bitnami stack.

```
$ test ! -f "/opt/bitnami/common/bin/openssl" && echo "Approach A: Using system packages." || echo "Approach B: Self-contained installation."
```

### Step 1: Install The Lego Client

```
$ cd /tmp
$ curl -Ls https://api.github.com/repos/xenolf/lego/releases/latest | grep browser_download_url | grep linux_amd64 | cut -d '"' -f 4 | wget -i -
$ tar xf lego_vX.Y.Z_linux_amd64.tar.gz
$ rm lego_vX.Y.Z_linux_amd64.tar.gz
$ sudo mkdir -p /opt/bitnami/letsencrypt
$ sudo mv lego /opt/bitnami/letsencrypt/lego
```

### Step 2: Generate A Let's Encrypt Certificate For Your Domain

> Để làm bước này thì bạn cần phải đảm bảo rằng domain của bạn đã trỏ đúng IP host nha, không là lỗi mình không chịu trách nhiệm đâu đấy

Turn off all Bitnami service:

```
$ sudo /opt/bitnami/ctlscript.sh stop
```

Request a new certificate for your domain as below, both with and without the www prefix

```
$ sudo /opt/bitnami/letsencrypt/lego --tls --email="EMAIL-ADDRESS" --domains="DOMAIN" --domains="www.DOMAIN" --path="/opt/bitnami/letsencrypt" run
```

Điền tất cả các thông tin cần thiết và đến phần type `CommonName` hãy điền domain của bạn.

Một tập chứng chỉ sẽ được tạo trong `/opt/bitnami/letsencrypt/certificates`. Bao gồm DOMAIN.crt và DOMAIN.key.

### Step 3: Configure The Web Server To Use The Let's Encrypt Certificate

Chúng ta sẽ bỏ các file chứng chỉ vào đúng nơi quy định của nó tùy thuộc vào phương thức tiếp cận mà mình đã test ở trên.

Mình sẽ đi đến với Nginx Với cách tiếp cận B

```
# Chuyển những chứng chỉ đang có thành cũ
$ sudo mv /opt/bitnami/nginx/conf/server.crt /opt/bitnami/nginx/conf/server.crt.old
$ sudo mv /opt/bitnami/nginx/conf/server.key /opt/bitnami/nginx/conf/server.key.old
$ sudo mv /opt/bitnami/nginx/conf/server.csr /opt/bitnami/nginx/conf/server.csr.old

# Chuyển chứng chỉ mới vào đúng thư mục
$ sudo ln -sf /opt/bitnami/letsencrypt/certificates/DOMAIN.key /opt/bitnami/nginx/conf/server.key
$ sudo ln -sf /opt/bitnami/letsencrypt/certificates/DOMAIN.crt /opt/bitnami/nginx/conf/server.crt

# Thiết lập các permission cho các file chứng chỉ
$ sudo chown root:root /opt/bitnami/nginx/conf/server*
$ sudo chmod 600 /opt/bitnami/nginx/conf/server*
```

Restart all bitnami services:

```
$ sudo /opt/bitnami/ctlscript.sh start
```

Done!
