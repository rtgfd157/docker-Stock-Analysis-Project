
### Build from start:
---------------------
stock analysis project is a project,  that take  a few thousands stock data (Ticker,company name , stock extchange),  and making OBV index.
"OBV index" is On-balance volume (OBV) is a technical trading momentum indicator that uses volume flow to predict changes in stock price. Joseph Granville first developed the OBV metric in the 1963 book Granville's New Key to Stock Market Profits. 

[On-Balance Volume (OBV) Definition](https://www.investopedia.com/terms/o/onbalancevolume.asp)


the program use yfinance library to fetch on daily basis the stock volume and price, and then making OBV index.
the website will show the most promising "obv index", i calculate change by percentages.


the app is using celery for making the api fetching.


### Build from start:
---------------------

docker-compose -f "docker-compose.yml" up -d --build



### install module nodes manualy (first time use) for frontend:
---------------------------------------------------------------

enter to the stock-analysis-project-docker-master_web container working  from docker compose command , and there run.  
(I'm using docker Dashboard for getting to Cli)

~~```cmd
docker run -it  stock-analysis-project-docker-master_web  /bin/bash```~~

```cmd
cd frontend
```
```cmd 
npm install
```

run frontend container again



## Browser:
[Project website](http://127.0.0.1:8000/)


###
if web not up  wait for  mysql being logged-in and up, then restart  container

message  " django.db.utils.OperationalError: (2003, "Can't connect to MySQL server on 'db' (111)") "