# How to generate a ssh key
```
$ ssh-keygen -t rsa
```
# How to copy publish ssh key from local to server google
```
add ssh key in edit instance
```
## Method 2
```
$ ssh-copy-id -i ~/.ssh/id_rsa.pub username@ip-host
```
## Method 3: manual
patse publish key to file `authorized_keys` in server
```
$ ~/.ssh/authorized_keys
```