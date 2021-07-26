from django.db import models
from django.test import TestCase
from Main_app.models import ComapnyStockData
from Main_app.Helper.time_helper import get_current_day, get_date_from_today, timedelta, time_delta_after_x_days
from Main_app.Helper.csv_helper import insert_companies_to_db_from_csv

# terminal python3 manage.py test Main_app.tests.test_time.TimeTest  --verbosity 2

# models test
class TimeTest(TestCase):
    def setUp(self):

        self.days_delta_amount  = -5
        self.today = get_current_day()
        self.today_date_only=self.today.date()



    def test_time_delta_(self):
        """
            testing to see if time delta accurate
        """
        print('######## 1: ',str(time_delta_after_x_days(self.days_delta_amount) ) )
        self.assertEqual( self.today_date_only  + timedelta(days=self.days_delta_amount) , time_delta_after_x_days(self.days_delta_amount ) ) 
        