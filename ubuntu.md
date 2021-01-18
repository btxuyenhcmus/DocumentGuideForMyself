# How do I change permistions for a folder and all of its subfolders and files in one step in Linux
```
# First, you shood excute all folder
find ~/path/to/folder -type d -exec chmod 777 {} \;

# Excute all file
find ~/path/to/folder -typ f -exec chmod 777 {}\;
```
> `d or f` mean `directory or file` and 777 mean full permistion

# Create venv enviroment for python
```
python -m venv name-venv
```
Next, activate the environment with the following command:
```
source name-venv/bin/activate
(venv) $ pip3 install flask
(venv) $ pip3 install django
```
To exit environment, input
```
deactivate
```
# List all user
```
cut -d: -f1 /etc/passwd
```
# Delete a user and its directory
```
sudo userdel username
sudo rm -r /home/username
```
# Add a home directory to an existing user
```
sudo usermod -d /home/directory user
```
# Create user with directory and bash
```
sudo useradd -m -d /home/username -U -r -s /bin/bash username
```
# How to set password for a user that you don't remmember old password
```
sudo passwd username
```
# Assigne UID and GID (user and group) for one or multi file/folder
```
sudo chown -R user:groud file/folder
```
Giải thích các thông số trong lệnh `ls -l`
 - Cột đầu tiên: `drwxr-xr-x` show các thông tin quyền rwx/read,write,excute và kí tự `d` đầu dòng thể hiện nó là tập tin `f` hoặc thư mục `d`.
 - Cột thứ 2: `2` thể hiện số lượng tập tin liên kết với thư mục đó.
 - Cột thứ 3 và cột thứ 4: thể hiện user/group.
 - Cột thứ 5: thể hiện kích thước.
 - Cột thứ 6: thể hiện ngày sửa cuối cùng.
 - C
