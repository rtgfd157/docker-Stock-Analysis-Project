from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ComapnyStockData


@admin.register(ComapnyStockData)
class StockDataAdmin(ImportExportModelAdmin):

    """
    an ability in  admin  page to import/export  StockData to csv 
    xls file not work wit value True as is treat it as 1 ..
    """
    pass
