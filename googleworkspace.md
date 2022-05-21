# Security

## 2-step verification

- Enable Allow users to turn on 2-Step Verification
- Enforcement:
  - On
  - New user enrollment period: Cho phép người dùng mới có thể đăng nhập không thông qua xác thực 2 bước trong khoản thời gian??
  - Enable Allow user to trust the device để khách hàng chọn thiết bị uy tín truy cập lâu dài không cần xác thực nhiều lần.
  - Methods: phương thức xác thực.
    - Any: Bao gồm các phương thức bên dưới.
    - Any except verification codes via text, phone call: Ngoại trừ tin nhắn sms hoặc cuộc gọi thoại.
    - Only security key: dùng mã code trong danh sách trước đó.

# Directory

## Users

- Suspend user: tắt quyền truy cập vào email của người dùng.
- Delete user: đặt lệnh xóa tài khoản của người dùng sau 7 ngày, tất cả tài liệu của user được đẩy sang một user mới.

## Group

tạo ra một email mới, khi nhận được email sẽ gửi tất cả các thành viên trong nhóm email đó. và email này chỉ dùng để nhận chứ không dùng để gửi.
