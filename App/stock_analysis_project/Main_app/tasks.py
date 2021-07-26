
from celery import shared_task
import time
from celery.decorators import periodic_task
from .models import ComapnyStockData, StockDayData
import yfinance as yf
import datetime as dt
from datetime import datetime, date, time, timedelta
import threading
import numpy
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time as t
import pandas as pd  # working with panda because data that return from y_finanace
from celery.utils.log import get_task_logger
from math import ceil



####################################

from Main_app.Helper.time_helper import get_current_day, time_delta_after_x_days,get_date_from_today
from Main_app.Helper.numpy_helper import split_array_numpy
from Main_app.Helper.thraeding_helper import start_thraeding
from OBVapp.obv_index_maker2 import ObvIndexMakerClass
from Main_app.Helper.yfinance_helper import api_call_ticker_and_history_return, insert_daily_stock_vol


@shared_task
def celery_task_updating_stockdaydata(companies_list):
    """
    Task that update every  4 hours ( task config in settins.py ), using yfinannce library.
    work with celery , celery beat (for periodic).
    """

    print(" $ Starting Task of updating daily stocks  volumes -  StockDayData - celery_task_updating_stockdaydata")
    
    #  because celery function wont get django model querySet of objects as argument)
    companies_obj = ComapnyStockData.value_list_into_querySet(companies_list) 

    print(" number of companies : ", companies_obj.count())
    
    split_to_size = 10
    splitted_list_of_querysets = split_array_numpy(split_to_size, companies_obj ) # splited list of querysets for threading

    #start_thraeding(split_to_size,splitted_list_of_querysets, make() ) - to uncomment when we want threaded

    for dt in splitted_list_of_querysets:
        make(dt)

    day_after_x_amount_days = time_delta_after_x_days(-11)
    # deleting all StockDayData that are obselete
    p=StockDayData.objects.filter(stock_date__lt=date(day_after_x_amount_days.year, day_after_x_amount_days.month, day_after_x_amount_days.day)).delete()

    a= ObvIndexMakerClass() ## updating OBV index with new values



def make(companies_obj_queryset):
    """
        main function  of celery_task_updating_stockdaydata .
        Looping on companies
    """
    
    day_after_x_amount_days = time_delta_after_x_days(-10)

    today_date_string = str(get_date_from_today())
    all_sdd=StockDayData.objects.all() # query in order not to call db too much

    for company_stockdata_object in companies_obj_queryset:

        t.sleep(2)
        print("~~~~{}~~~~".format(company_stockdata_object))


        # error in fetching historical  data with celery need to debug

        company_yfinance_object ,com_daily_history = api_call_ticker_and_history_return(company_stockdata_object, day_after_x_amount_days )  

        

        company_day_records_in_db = all_sdd.filter( company_stock_data=company_stockdata_object  )

        insert_daily_stock_vol(com_daily_history,  company_day_records_in_db, company_stockdata_object)


        company_stockdata_object.save() # will update check time, because we now checked with the api



