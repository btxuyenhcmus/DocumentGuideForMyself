## How to save username and password in git
Run
```
git config --global credential.helper store
```
then
```
git pull
```
After the first time enter username password, it auto save infomation in daemon and you don't need ente usrname password.

## How to use git command line when you had changed password
Run
```
git pull
```
After push commit, it will require new access token and save in global for the last times.