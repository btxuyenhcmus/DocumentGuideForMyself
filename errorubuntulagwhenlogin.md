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