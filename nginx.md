# Streaming Live Video and Storing Videos with NGINX Open Source

## Installing the Build Tools

Before compiling NGINX, you need to have some basic build tools installed: autoconf, gcc, git, and make. To download and install them, run the command for your operating system (if it’s not included here, consult the OS vendor documentation).

```
$ sudo apt update
$ sudo apt install build-essential git
```

## Installing Dependencies

The NGINX build also requires several dependencies: Perl Compatible Regular Expressions (PCRE), OpenSSL, and zlib for compression.

```
$ sudo apt install libpcre3-dev libssl-dev zlib1g-dev
```

## Installing Dependencies from Source

Compiling NGINX with the RTMP Module

```
$ cd /path/to/build/dir
$ git clone https://github.com/arut/nginx-rtmp-module.git
$ git clone https://github.com/nginx/nginx.git
$ cd nginx
$ ./auto/configure --ad-module=../nginx-rtmp-module
$ make
$ sudo make install
```

You can run nginx with systemctl or full path file binary!!

## Configuring NGINX

```
http {
    server {
        listen 80;
        root /var/www/html;
        server_name _;
        location /hls {
            # CORS setup
            add_header 'Access-Control-Allow-Origin' '*' always;
            add_header 'Access-Control-Expose-Headers' 'Content-Length';
            # Allow CORS preflight requests
            if ($request_method = 'OPTIONS') {
                add_header 'Access-Control-Allow-Origin' '*';
                add_header 'Access-Control-Max-Age' 1728000;
                add_header 'Content-Type' 'text/plain charset=UTF-8';
                add_header 'Content-Length' 0;
                return 204;
            }
            types {
                application/vnd.apple.mpegurl m3u8;
                video/mp2t ts;
            }
            add_header Cache-Control no-cache;
            alias /path/to/videos/hls;
        }
    }
}
```

## Split media file by ffmpeg converter

```
$ sudo apt install ffmpeg
$ ffmpeg -i demo.mp4 -profile:v baseline -level 3.0 -s 720x400 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls /path/to/videos/hls/demo.m3u8
```
