from django.shortcuts import render

# Create your views here.
import time
import datetime as dt
import csv
from datetime import datetime, date, time, timedelta

from django.shortcuts import HttpResponse
from Main_app.models import ComapnyStockData,StockDayData
from .tasks import make_obv
from .obv_index_maker2 import ObvIndexMakerClass

def obv_index_maker_view(request):
    #pr=StockDayData.objects.filter().order_by('-id')[:10:-1]

     

    a= ObvIndexMakerClass()

    #a.make()

    #make_obv.delay(10,10)
    return HttpResponse(dt.datetime.now())

import time
import asyncio
async def a_view(request):
    start = time.time()
    await asyncio.sleep(600) # when code come to here  await he stopes and keep forward
    print ("22222222")
    end = time.time()
    print("end - start =",end - start)
    print("hellop world")
    return HttpResponse(dt.datetime.now())
