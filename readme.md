
### Build from start
docker-compose -f "docker-compose.yml" up -d --build


### install module nodes manualy (first time use) for frontend


docker run -it  stock-analysis-project-docker-master_web  /bin/bash

cd frontend

npm install


###
if web not up  wait for  mysql being log in and then restart  container