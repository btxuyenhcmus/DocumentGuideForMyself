# Hướng dẫn setup một con vpn đơn giản bằng openvpn của GCP

1. Trước tiên, search by keyword "OpenVPN access server"
2. Lauch, nhớ chọn region đúng nơi mình muốn nha!.
3. Sau GCP Deploy xong sẽ cho 2 đường link, truy cập vào đường link admin.
4. Sử dụng username và password mà GCP cung cấp, login vào accept install OpenVPN.
5. Truy cập vào tab `VPN Settings` -> Cho phép traffic của client thông qua Server.
6. Mục `DNS` yêu cầu client sử dụng DNS của server.
   - Google DNS: `8.8.8.8` và `8.8.4.4`
   - Clougflare: `1.1.1.1` và `1.0.0.1`
7. Login vào địa chỉ còn lại. Tải file locker-profile về.
8. Tạo file login.txt điền username, password thành 2 dòng.
9. Sửa file `client.ovpn` vừa mới tải về, dòng 58 - login trỏ vào file login.txt
10. Tải openvpn client về và import file vào là có thể sử dụng ngay.
11. Tắt port ssh

```
$ sudo ufw enable
...say yes if you sys warning
```

12. block ping response

```
$ sudo sysctl -w net.ipv4.icmp_echo_ignore_all=1
```

to open ping response

```
$ sudo sysctl -w net.ipv4.icmp_echo_ignore_all=0
```

13. Reopen ssh when your firewall disable 22 port (GCP)
    - Go to google Console -> Compute Engine.
    - Clickup to detail of instance and edit this.
    - add "startup-script" in custom-metadata
    ```
    #! /bin/bash
    ufw disable
    ```
    - reboot instance
