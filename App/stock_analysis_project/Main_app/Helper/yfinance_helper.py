from Main_app.models import ComapnyStockData, StockDayData
import threading
import yfinance as yf
from Main_app.Helper.time_helper import today_date_string
lock= threading.Lock()
from datetime import datetime, date, time, timedelta



def api_call_ticker_and_history_return(company_stockdata_object_in, day_after_x_amount_days ):
    try:
        #print("try to fetch :  ", company_stockdata_object_in)
        
        company_yfinance_object = yf.Ticker(company_stockdata_object_in.ticker)
        print("company_yfinance_object ", company_yfinance_object)
        # https://github.com/ranaroussi/yfinance/issues/318
        # https://github.com/ranaroussi/yfinance/issues/363   knowns bug's 
        company_yfinance_history =company_yfinance_object.history(start="2021-07-16" ,end = "2021-07-26" ) 
        # -- return NoneType in celery in python3 manage.py test Main_app.tests.test_yfinance.yfinanceTest  --verbosity 2 look ok 
        print("company_yfinance_history ", company_yfinance_history)

    except:
        company_yfinance_object =None
        company_yfinance_history = None

    print("before company_yfinance_history : ", company_yfinance_history, "type: ", type(company_yfinance_history))
    
    return company_yfinance_object ,company_yfinance_history

def insert_daily_stock_vol(com_daily_history_from_yfinance, company_day_records_in_db, company_stockdata_object):
    """
        insert latest history of daily volums to db
        company_stockdata_object - relvent company object in db - in ComapnyStockData model
    """

    idx= 0 # counter on result
    print("com_daily_history_from_yfinance : ",com_daily_history_from_yfinance )
    for row in com_daily_history_from_yfinance:

        sdd = company_day_records_in_db.filter(stock_date =row[0].strftime('%Y-%m-%d') )

        if  not sdd.exists():
            lock.acquire()
            try:
                # bug dont insert first value ... (for now adding date in  now + timedelta(days=-5) above)
                
                sdd = StockDayData.objects.create(company_stock_data=company_stockdata_object, close=com_daily_history_from_yfinance['Close'][idx] ,
                                                volume= com_daily_history_from_yfinance['Volume'][idx] ,stock_date = row[0].strftime('%Y-%m-%d'))
      
            except:
                print("###########################")
                print("result['Close'][idx]  - ",com_daily_history_from_yfinance['Close'][idx] ,"result['Volume'][idx] - ",com_daily_history_from_yfinance['Volume'][idx] )
                print("###########################")
            lock.release()
        elif sdd.count() >1 :
            # check if record has more then one in db to same day and same stock
                        above_2 = above_2 + 1
                        print (" >1  ==> " ,sdd.count ," - ", sdd )


        


