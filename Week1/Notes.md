# Week 1 16/1/2024
## Basics of Docker
* to add Detail on Docker

## Running postgres on Docker 
docker run -it \
  -e POSTGRES_USER="root" \ 
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi_hw" \
  -v /c/DE_ZoomCamp2024/Week1/Homework/data:/var/lib/postgresql/data:rw \
  -p 5432:5432 \
  postgres:13

> -e env list Set = environment variables\
> -v volume list = Bind mount a volume\
> -p, --publish list ,Publish a container's port(s) to the host\
*here the volume is using the codescape location. 

## Running pgcli for commandline posgre
``` pgcli -h localhost -p 5432 -u root -d ny_taxi ```
## Running pgAdmin 
Pgadmin is a management tool to manage postgresql database 

Command Line for pgAdmin
```
  docker run -it 
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" 
  -e PGADMIN_DEFAULT_PASSWORD="root" 
  -p 8080:80 
  dpage/pgadmin4 
```

## Running pgAdmin and Posgres on same network 
### Postgres
```
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi_hw" -v /c/DE_ZoomCamp2024/Week1/Homework/data:/var/lib/postgresql/data:rw -p 5432:5432 --network=pg-network --name pg-database-hw postgres:13 
```
### pgAdmin
```
docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8079:80 --network=pg-network --name pgadmin_hw dpage/pgadmin4
```



