from django.db import models
from django.test import TestCase
from Main_app.models import ComapnyStockData
from Main_app.Helper.time_helper import get_current_day, get_date_from_today
from Main_app.Helper.csv_helper import insert_companies_to_db_from_csv

# terminal python3 manage.py test Main_app.tests.test_models.ComapnyStockDataTest  --verbosity 2

# models test
class ComapnyStockDataTest(TestCase):

    def setUp(self):

        insert_companies_to_db_from_csv() # test db
        
        # list value
        self.companies_obj_list = ComapnyStockData.objects.filter(update_time__lt=get_date_from_today()).values_list('pk', flat=True)
        
        # queryset
        self.companies_obj_queryset = ComapnyStockData.value_list_into_querySet(self.companies_obj_list)


    def test_number_of_value_list_vs_object_queryset(self):
        self.assertEqual(len(self.companies_obj_list),  len(self.companies_obj_queryset) )
