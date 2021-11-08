# Add new user && sudo without passwd

The fist, you need run command above with root user

```
sudo useradd -m -d </path/to/user> -U -r -s /bin/bash <username>
```

After, add this user to visudo without passwd

```
sudo visudo
```

Typing,

```
username    ALL=(ALL) NOPASSWD:ALL
```
