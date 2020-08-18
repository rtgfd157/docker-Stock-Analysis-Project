
### Build from start:
---------------------

docker-compose -f "docker-compose.yml" up -d --build



### install module nodes manualy (first time use) for frontend:
---------------------------------------------------------------

enter to the container working  from docker compose command , and there run.  
(I'm using docker Dashboard for getting to Cli)

~~```cmd
docker run -it  stock-analysis-project-docker-master_web  /bin/bash```~~

```cmd
cd /App/stock_analysis_project/frontend
```
```cmd 
npm install
```

run frontend container again

###
if web not up  wait for  mysql being logged-in and up, then restart  container