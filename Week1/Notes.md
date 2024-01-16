# Week 1 16/1/2024
##Basics of Docker

## Running postgres on Docker 
docker run -it \
  -e POSTGRES_USER="root" \ 
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /workspaces/DE_ZoomCamp2024/Data \
  -p 5432:5432 \
  postgres:13

> -e env list Set = environment variables\
> -v volume list = Bind mount a volume\
> -p, --publish list ,Publish a container's port(s) to the host\
* notes here the volume is using the codescape location. 


