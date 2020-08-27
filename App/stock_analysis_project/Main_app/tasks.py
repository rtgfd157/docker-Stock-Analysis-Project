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
import pandas as pd  # working with panda because data that retur from y_finanace
from celery.utils.log import get_task_logger
from math import ceil

import concurrent.futures

from OBVapp.obv_index_maker2 import ObvIndexMakerClass

lock= threading.Lock()



@shared_task
def celery_task_updating_stockdaydata(companies_list):
    """
    Task that update every  4 hours ( task config in settins.py ), using yfinannce library.
    work with celery , celery beat (for periodic).
    """

    print("  Starting Task of updating daily stocks  volumes -  StockDayData ")
    #print("companies_list : ",companies_list)
    today = datetime.today()
    #companies_obj= ComapnyStockData.objects.filter(update_time__lt=date(today.year, today.month, today.day))#[:6:-1]

    # for first time using we will want to update right away because date field in model is auto now
    # if StockDayData.objects.count()  > 0:
    #     companies_obj= ComapnyStockData.objects.filter(update_time__lt=date(today.year, today.month, today.day))
    # else :
    #     companies_obj= ComapnyStockData.objects.all()

    #Posts.objects.filter(ownerid__in=[f.follow_id for f in following])
    print("companies_list :", len(companies_list) )
    companies_obj = ComapnyStockData.objects.filter(id__in= [f for f in companies_list] )
    #print("companies_obj ", companies_obj)

    print(" number of companies : ", companies_obj.count())
    
    n = 10
    l = numpy.array_split(numpy.array(companies_obj),n)

    futures = []
    with ThreadPoolExecutor(max_workers=n) as executor:
        
        for dt in l:
            #executor.submit(make, dt )
            futures.append(executor.submit(make, dt))

        while futures:
            for future in concurrent.futures.as_completed(futures):
                futures.remove(future)
                

    # https://github.com/googleapis/python-logging/issues/21
    t.sleep(2)
    print("---- finished threading")

    a= ObvIndexMakerClass() ## updating OBV index with new values
    return

    


def make(companies_obj):
    """
        main function  of celery_task_updating_stockdaydata .
        Looping on companies
    """
    above_2 =0
    today = datetime.today()

    now = datetime.now()
    now_date =now.date()

    day_after_10_days =now + timedelta(days=-5)
    day_after_10_days = day_after_10_days.date()

    l = str(now.date())


    all_sdd=StockDayData.objects.all() # query in order not to call db too much

    
    for com in   companies_obj:
    #for com in companies_obj:
        print("~~~~{}~~~~".format(com))
        
        some_var = 0 # counter
        y_ob = yf.Ticker(com.ticker)
        result =y_ob.history(start=str(day_after_10_days) ,end = str(l) )

        idx= 0 # counter on result
        for  row in result.iterrows():

            
            sdd = all_sdd.filter(stock_date =row[0].strftime('%Y-%m-%d'), company_stock_data=com  )
            
            if  not sdd.exists():
                lock.acquire()
                try:

                    # bug dont insert first value ... (for now adding date in  now + timedelta(days=-5) above)
                    
                    sdd = StockDayData.objects.create(company_stock_data=com, close=result['Close'][idx] , volume= result['Volume'][idx] ,stock_date = row[0].strftime('%Y-%m-%d'))
                    #arr.append(sdd)
                    #print("sdd ",sdd)

                    #print("result['Close'][idx]  - ",result['Close'][idx] ,"result['Volume'][idx] - ",result['Volume'][idx] , "   row[0].strftime('%Y-%m-%d') ",row[0].strftime('%Y-%m-%d') ," com ",com)
                    some_var += 1
                    
                except:
                    print("###########################")
                    print("result['Close'][idx]  - ",result['Close'][idx] ,"result['Volume'][idx] - ",result['Volume'][idx] )
                    print("###########################")
                lock.release()
            elif sdd.count() >1 :
                    above_2 = above_2 + 1
                    print (" >1  ==> " ,sdd.count ," - ", ssd )

            idx= idx+1 # counter on result

        print("inserted : {}".format(some_var))
        com.save() # will update company with current date

    # above 2 occurnce to date,stock -- should happen now
    if above_2 >0:
        print("above 2  -- {}".format(above_2) )

    
    # deleting all StockDayData
    p=StockDayData.objects.filter(stock_date__lt=date(day_after_10_days.year, day_after_10_days.month, day_after_10_days.day)).delete()

    # if p.count() >0:
    #     print("deleting {}  old objects ".format(p.count() ))
    #     p.delete()
