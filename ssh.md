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

# How to setup authorized_keys for any user
```
$ mkdir ~/.ssh
$ chmod 700 ~/.ssh
$ vim ~/.ssh/authorized_keys
    # patse your ssh key to file
$ chomod 600 ~/.ssh/authorized_keys
```
If you are permission denied, you can't edit config in `/etc/ssh/ssh_config` and restart `ssh` service