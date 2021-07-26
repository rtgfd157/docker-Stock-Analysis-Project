from django.db import models
from django.test import TestCase
from Main_app.models import ComapnyStockData
from Main_app.Helper.time_helper import get_current_day, get_date_from_today, time_delta_after_x_days,today_date_string
from Main_app.Helper.csv_helper import insert_companies_to_db_from_csv
from Main_app.Helper.yfinance_helper import api_call_ticker_and_history_return,yf
# terminal python3 manage.py test Main_app.tests.test_yfinance.yfinanceTest  --verbosity 2


# models test
class yfinanceTest(TestCase):
    def setUp(self):

        insert_companies_to_db_from_csv() # test db
        
       
        # queryset
        self.companies_obj_queryset = ComapnyStockData.objects.filter()[:10]
        self.day_after_x_amount_days = time_delta_after_x_days(-10)

    def test_call_yfinance(self):
        """
            test_call_yfinance
        """
        return
        for company_object in self.companies_obj_queryset:
        
            com_daily_history =  api_call_ticker_and_history_return(company_object, self.day_after_x_amount_days )
            print(" company_yfinance_history : ", com_daily_history, "type: ", type(com_daily_history))

            #self.assertEqual(self.split_to_size,  len(l))
            # ineractive testing ..

            # if history:

    def test_specifc_company_stocdays(self):
        """
            test_specifc_company_stocdays
        """
        

        company_yfinance_object = yf.Ticker("JNCE")
        print("time : ", str(self.day_after_x_amount_days ), today_date_string())
        # https://github.com/ranaroussi/yfinance/issues/318
        # https://github.com/ranaroussi/yfinance/issues/363   knowns bug's 
        company_yfinance_history =api_call_ticker_and_history_return(company_yfinance_object, self.day_after_x_amount_days )
        print("**********8")
        print(company_yfinance_history)
        for row in company_yfinance_history:
            print(row)
