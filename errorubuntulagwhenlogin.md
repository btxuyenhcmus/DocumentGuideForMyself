# Lúc khởi động ubuntu thì bị treo

## Ngày xưa
- Nvidia có cung cấp các thông số để cộng đồng mã nguồn mở viết driver Nvidia cho linux trên các dòng máy cũ.

## Cách fix như sau:
1. Khi đang vào Ubuntu thì nhấn Ctrl + Alt + F2 -> F6, hoặc làm cách nào đó vào được terminal.

2. Gõ
```
sudo nano /etc/default/grub
```
Look at line below:
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```
Edit:
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
```

3. Cập nhập lại grub rồi khởi động lại máy:
```
sudo update-grub
sudo reboot
```

# Một trường hợp khác bị lỗi do không thể kích hoạt driver của Nvidia graphics (Thường trên đời máy lenovo)

1. Mặc dù bạn đã chọn trong driver là nvidia-390 hay cao hơn là nvidia-440 trong terminal hoặc trong `update & storing -> additional driver` nhưng trong thông tin detail của máy vẫn hiện thông tin graphic là intel bla bla. Nghĩa là lúc đó bạn không thể giao tiếp với nvidia-driver mặc dù bạn đã có các packages liên quan.
- Chế độ màng hình với các animation bị giật lag cũng như không kích hoạt được chế độ sắc nét.
- Không kết nối được với monitor.
- Không cài các extentions liên quan tới GPU để quan sát các báo sô.
- Bla bla ....
2. Để khắc phục điều này bạn cần **disable secure boot** trong menu configure trong lúc khởi động máy.
3. Trên máy lenovo, khở động lại máy, nhấn **F1**, chuyển qua tab **security**, chọn **disable** đối với **secure boot** 