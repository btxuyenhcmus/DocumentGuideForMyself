## Step 1 - Defining the Web Server Configuration
First, create a project directory for your WordPress setup called `wordpress` and navigate to it:
```
$ mkdir wordpress && cd wordpress
```
Next, make a directory for the configuration file:
```
$ mkdir nginx-conf
```
Open the file with `nano` or `vim`  or your favorite editor:
```
$ vim nginx-conf/nginx.conf
```
Paste the following code into the file. Be sure to replace `example.com` with your own domain name:
```
server {
        listen 80;
        listen [::]:80;

        server_name example.com www.example.com;

        index index.php index.html index.htm;

        root /var/www/html;

        location ~ /.well-known/acme-challenge {
                allow all;
                root /var/www/html;
        }

        location / {
                try_files $uri $uri/ /index.php$is_args$args;
        }

        location ~ \.php$ {
                try_files $uri =404;
                fastcgi_split_path_info ^(.+\.php)(/.+)$;
                fastcgi_pass wordpress:9000;
                fastcgi_index index.php;
                include fastcgi_params;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                fastcgi_param PATH_INFO $fastcgi_path_info;
        }

        location ~ /\.ht {
                deny all;
        }

        location = /favicon.ico { 
                log_not_found off; access_log off; 
        }
        location = /robots.txt { 
                log_not_found off; access_log off; allow all; 
        }
        location ~* \.(css|gif|ico|jpeg|jpg|js|png)$ {
                expires max;
                log_not_found off;
        }
}
```

## Step 2 - Defining Environment Variables
In your main project directory, `~/wordpress`, open a file called `.env`:
```
$ vim .env
```
Add the following variable names and values to the file. Remember to supply your own values here for each variable:
```
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_USER=your_wordpress_database_user
MYSQL_PASSWORD==your_wordpress_database_password
```
Because your `.env` file contains sensitive information, you will want to ensure that it is included in your project's `.gitignore` and `.dockerignore` file, which tell **Git** and **Docker** what file **not** to copy to your Git repositories and Docker images, respectively.
If you plan to work with Git for version control, initialize your current working directory as a repository with `git init`:
```
$ git init
```
Then open a `.gitignore` file:
```
$ vim gitignore
```
Add `.env` to the file:
```
.env
```
Save and close the file when you are finished editing.
Open the file:
```
$ vim .dockerignore
```
Add `.env` and you can optionally add files and directories associated with your application's development:
```
.env
.git
docker-compose.yml
.dockerignore
```
Save and close the file when you are finished.

## Step 3 - Defining services with Docker Compose
Open the `docker-compose.yml` file and paste the following code below:
```
version: '3'

services:
  db:
    image: mysql:8.0
    container_name: db
    restart: unless-stopped
    env_file: .env
    environment:
      - MYSQL_DATABASE=wordpress
    volumes: 
      - dbdata:/var/lib/mysql
    command: '--default-authentication-plugin=mysql_native_password'
    networks:
      - app-network

  wordpress:
    depends_on: 
      - db
    image: wordpress:5.1.1-fpm-alpine
    container_name: wordpress
    restart: unless-stopped
    env_file: .env
    environment:
      - WORDPRESS_DB_HOST=db:3306
      - WORDPRESS_DB_USER=$MYSQL_USER
      - WORDPRESS_DB_PASSWORD=$MYSQL_PASSWORD
      - WORDPRESS_DB_NAME=wordpress
    volumes:
      - wordpress:/var/www/html
    networks:
      - app-network

  webserver:
    depends_on:
      - wordpress
    image: nginx:1.15.12-alpine
    container_name: webserver
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - wordpress:/var/www/html
      - ./nginx-conf:/etc/nginx/conf.d
      - certbot-etc:/etc/letsencrypt
    networks:
      - app-network

  certbot:
    depends_on:
      - webserver
    image: certbot/certbot
    container_name: certbot
    volumes:
      - certbot-etc:/etc/letsencrypt
      - wordpress:/var/www/html
    command: certonly --webroot --webroot-path=/var/www/html --email sammy@example.com --agree-tos --no-eff-email --staging -d example.com -d www.example.com

volumes:
  certbot-etc:
  wordpress:
  dbdata:

networks:
  app-network:
    driver: bridge
```

## Step 4 - Obtaining SSL Certificates and Credentials
Create the containers with `docker-compose up` and the `-d` flag, which will run the `db`, `wordpress` and `webserver` containers in the background:
```
$ docker-compose up -d
```
You will see output confirming that your services have been created:
```
Output
Creating db ... done
Creating wordpress ... done
Creating webserver ... done
Creating certbot   ... done
```
Using `docker-compose ps`, check the status of your services:
If everything was successfull, your `db`, `wordpress` and `webserver` services will be `Up` and the `certbot` container will have exited with a `0` status messages (if not `0`, Exactly you error):
```
Output
  Name                 Command               State           Ports       
-------------------------------------------------------------------------
certbot     certbot certonly --webroot ...   Exit 0                      
db          docker-entrypoint.sh --def ...   Up       3306/tcp, 33060/tcp
webserver   nginx -g daemon off;             Up       0.0.0.0:80->80/tcp 
wordpress   docker-entrypoint.sh php-fpm     Up       9000/tcp           
```
