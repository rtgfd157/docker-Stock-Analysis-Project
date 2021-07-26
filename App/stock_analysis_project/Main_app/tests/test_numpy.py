from django.db import models
from django.test import TestCase
from Main_app.models import ComapnyStockData
from Main_app.Helper.time_helper import get_current_day, get_date_from_today
from Main_app.Helper.csv_helper import insert_companies_to_db_from_csv
from Main_app.Helper.numpy_helper import split_array_numpy

# terminal python3 manage.py test Main_app.tests.test_numpy.NumpyDataTest  --verbosity 2

# models test
class NumpyDataTest(TestCase):

    def setUp(self):

        insert_companies_to_db_from_csv() # test db
        
        # list value
        self.companies_obj_list = ComapnyStockData.objects.filter(update_time__lt=get_date_from_today()).values_list('pk', flat=True)
        
        # queryset
        self.companies_obj_queryset = ComapnyStockData.value_list_into_querySet(self.companies_obj_list)

        self.split_to_size = 10 

    def test_number_of_numpy_split(self):

        l = split_array_numpy(self.split_to_size, self.companies_obj_queryset )

        self.assertEqual(self.split_to_size,  len(l))


    