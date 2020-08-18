
# Stock Analysis Project
--------------------------

### written by idan z

### *Backend* :
-----------------
 Python 3.8.4, Django 3.1 framework for website , Celery for tasks, sphinx for documataion, MySql  
For doc's of backend, go to - docs/_build/html/index.html 


### *FrontEnd* : 
-----------------
vue.js 3 , @vuese/cli for documantion  
For doc's of frontend. in prompt go to folder frontend, and run: vuese serve --open 

Commands For runing the project:


```cmd 
#celery -A stock_analysis_project worker -l  info  -E
```


## work with: 
```cmd 
celery -A stock_analysis_project worker -l info  --concurrency 1  -P solo  -E
```

### celery beat for timely tasks
```cmd
celery -A stock_analysis_project beat -l info
``` 


~~celery -A stock_analysis_project worker -l info --concurrency=4 -n idan-worker1 -E~~
~~celery -A stock_analysis_project worker -l info --concurrency=4 -n idan-worker2 -E~~

### flower for monitoring  - http://localhost:5555/
```cmd
celery -A stock_analysis_project flower  
```

```cmd
celery -A stock_analysis_project purge
```

With Flower web interface gaining the ability seeing  celery proccess.   

```python
py manage.py runserver
```

open xampp run appache and MySql

In prompt frontend folder :

 
```cmd
vue ui  --port 3000
```
```cmd 
npm run serve
```


http://localhost:8081/

From  Vue web interface, run the front end side.  

### In __README__ folder Backend/FrontEnd configuration explanation md files for this Project. 