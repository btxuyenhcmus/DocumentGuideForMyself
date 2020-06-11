# How do I change permistions for a folder and all of its subfolders and files in one step in Linux
```
# First, you shood excute all folder
find ~/path/to/folder -type d -exec chmod 777 {} \;

# Excute all file
find ~/path/to/folder -typ f -exec chmod 777 {}\;
```
> `d or f` mean `directory or file` and 777 mean full permistion
