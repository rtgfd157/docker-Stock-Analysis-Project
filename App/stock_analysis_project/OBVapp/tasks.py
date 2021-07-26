from __future__ import absolute_import, unicode_literals


from celery import shared_task
import time
from celery.decorators import periodic_task
from .models import OBVindex
import yfinance as yf
import datetime as dt
from datetime import datetime, date, time, timedelta
from Main_app.models import ComapnyStockData ,StockDayData
from OBVapp.obv_index_maker2 import ObvIndexMakerClass
from celery.decorators import task


@shared_task
def celery_task1():
    """
        for testing purpose
    """

    #print("          awdsasd        1                && ")
    above_2 =0
    #now = datetime.now()
    today = datetime.today()

    now = datetime.now()
    now_date =now.date()

    day_after_10_days =now + timedelta(days=-10)
    day_after_10_days = day_after_10_days.date()

    l = str(now.date())

    #print("   --   ",today.year, today.month, today.day)
    #companies_obj= ComapnyStockData.objects.filter(update_time__lt=date(today.year, today.month, today.day)).count()
    companies_obj= ComapnyStockData.objects.filter(update_time__lt=date(today.year, today.month, today.day))
    #print(companies_obj)

    #return 0
    
    for com in companies_obj:
        
        print("~~~~",com,"~~~~")
        
        some_var = 0 # counter
        y_ob = yf.Ticker(com.ticker)

        # bug , look at runing task fix
        result =y_ob.history(start=str(day_after_10_days) ,end = str(l) )

        idx= 0 # counter on result
        for  row in result.iterrows():
            #print("i - ",idx,"value - ",result['Close'][idx])

            day_in_loop =now + timedelta(days=-idx)
            sdd = StockDayData.objects.filter(stock_date =date(day_in_loop.year, day_in_loop.month, day_in_loop.day), company_stock_data=com  )
            
            
            if  not sdd.exists():
                
                try:
                    sdd = StockDayData.objects.create(company_stock_data=com, close=result['Close'][idx] , volume= result['Volume'][idx] ,stock_date = day_in_loop)
                    some_var = some_var +1
                except:
                    print("###########################")
                    print("result['Close'][idx]  - ",result['Close'][idx] ,"result['Volume'][idx] - ",result['Volume'][idx] )
                    print("###########################")
            elif sdd.count() >1 :
                    above_2 = above_2 + 1
                    print (" >1  ==> " ,sdd.count ," - ", ssd )

            idx= idx+1 # counter on result
                    
        print("inserted : ",some_var)
        com.save()

            #sdd_add = StockDayData(company_stock_data=com, close= msft['Close'])
        
    print("above 2  -- ",above_2)
    #print(now)
    #print(now + timedelta(days=2))


    #result =y_ob.history(start='2020-03-13',end='2020-03-20')

    #print(result['Close'])
    #day_in_loop = now + timedelta(days=1)


    #sdd = StockDayData.objects.filter(stock_date=date(day_in_loop.year, day_in_loop.month, day_in_loop.day))


@shared_task
def make_obv(a,b):
    
    print(a)
    #print(pr)
    p = ComapnyStockData.objects.get(ticker="AEG") 
    
    OBVindex.objects.create(company_stock_data=p, percentage_change=1.25 , volume_change= 60000)
    return a+b

@shared_task
def obvindexmakerfunc():
    ObvIndexMakerClass()