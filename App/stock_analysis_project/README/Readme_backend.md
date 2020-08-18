# Stock Analysis Project
-------------------------

# written by idan z

## pip install packages:
-------------------------

pip install -U sphinx  
pip install autopep8  
pip install --pre django  , version 3.1  - 8.7.2020  
mysqlclient

pip install  djangorestframework
pip install django-crispy-forms

pip install django-webpack-loader

flower  
celery
pip install django-celery-results   -  https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html  
django-celery-beat



pip install django-import-export for init comapnies list from csv   - https://django-import-export.readthedocs.io/en/latest/installation.html  
django_extensions
debug_toolbar

## docs of the projects:
-----------

https://packaging.python.org/tutorials/creating-documentation/    
https://www.freecodecamp.org/news/sphinx-for-django-documentation-2454e924b3bc/ 
https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#toctree-directive   

using sphinx in folder docs

settings of sphinx in  conf.py:

```python
import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'stock_analysis_project.settings'
django.setup()
```

extensions = ['sphinx.ext.autodoc','sphinx.ext.graphviz','celery.contrib.sphinx',]


runing sphinx:

in prompt docs folder :

    sphinx-apidoc -o . ..
    make html

.. toctree::
   :maxdepth: 1
   :caption: Contents:
    OBVapp <OBVapp>

beautify page in firefox - addons :
app -> Markdown Viewer Webext


Interactive Python Shells
cmd - py manage.py shell_plus --ipython  --print-sql

### django_extensions:

making dot files with model that can be open with vscode (pic's of will also be added to docs)
py manage.py graph_models Main_app  > main_app_model.dot
py manage.py graph_models OBVapp > OBVapp__model.dot

### celery &  erlang

for runing localy, ~~changed to docker~~

base on: 
https://medium.com/@hassanzadeh.sd/celery-and-rabbitmq-in-django-just-couple-of-steps-to-get-async-working-and-monitoring-with-flower-707dcd7254e8  
https://docs.celeryproject.org/en/stable/userguide/monitoring.html  
https://www.distributedpython.com/2018/10/26/celery-execution-pool/  
installing them as server for tasks  
https://www.rabbitmq.com/

command for server up:
celery -A stock_analysis_project worker -l info
celery -A stock_analysis_project flower

celery worker --help

celery -A stock_analysis_project purge

https://github.com/celery/celery/issues/3759
 -  need to run as the link above because cant make concurrent  or preforked ..  need solo on win o/s

 celery -A stock_analysis_project worker -l info  --concurrency 1  -P solo  -E



 ### idea

 @cached_property django query

 check for faster query


 --print-sql


inserting the  next 2 lines into if statements trim 50% of running time
co = ComapnyStockData.objects.get(id=company_id)
obv_val  = OBVindex(company_stock_data = co, percentage_change= obv_percentege, obv=obv)



db_index=true django

### Backend Guide using sphinx:
stock_analysis_project\stock_analysis_project\doc\_build\html