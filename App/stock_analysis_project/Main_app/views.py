from django.shortcuts import render

# Create your views here.
import time
import datetime as dt
import csv
from datetime import datetime, date, time, timedelta
from OBVapp.models import OBVindex

from django.shortcuts import HttpResponse
from .models import ComapnyStockData, StockDayData
# , Celery_Task_Updating_Stockdaydata
from .tasks import celery_task_updating_stockdaydata
from math import ceil
import numpy
from celery import chord, group, chain
from OBVapp.obv_index_maker2 import ObvIndexMakerClass
from OBVapp.tasks import obvindexmakerfunc

from Main_app.Helper.csv_helper import insert_companies_to_db_from_csv
def celery_view(request):
    print(" from celery vieww  ")
    # celery_task_updating_stockdaydata.delay()
    # celery_task_updating_stockdaydata()

    today = datetime.today()

    # for first time using we will want to update right away because date field in model is auto now
    if StockDayData.objects.count() > 0:
        companies_obj = ComapnyStockData.objects.filter(update_time__lt=date(
            today.year, today.month, today.day)).values_list('pk', flat=True)
    else:
        companies_obj = ComapnyStockData.objects.all().values_list('pk', flat=True)
    print("StockDayData.objects.count() : ", StockDayData.objects.count())
    print("companies_obj : ", companies_obj)

    companies_list_pk = []
    for ob in companies_obj.iterator():
        #print(" ob ", ob)
        companies_list_pk.append(ob)
        #print(" /ob ", ob)

    # n = 2
    # print(" before split")
    # l = numpy.array_split(numpy.array(companies_list_pk),n)
    # print(" after split")

    #part 1
    print("from task11")
    celery_task_updating_stockdaydata.delay(companies_list_pk[:len(companies_list_pk)//2])
    print("from task11/")

    # part 2
    print("from task21")
    celery_task_updating_stockdaydata.delay(companies_list_pk[len(companies_list_pk)//2:])
    print("from task22/")

    # job =   group(
    #         celery_task_updating_stockdaydata.si(companies_list_pk[:len(companies_list_pk)//2]),
    #         celery_task_updating_stockdaydata.si(companies_list_pk[len(companies_list_pk)//2:])
    # ) 


    # result = job.apply_async()
    # can be problem if 2 tasks will make  obv index  and create in the same time ,  but slim chances currently
    # line 68 - in celery_task_updating_stockdaydata()

    # not working  opening many tasks known bug  https://www.google.com/search?client=firefox-b-d&q=+Received+task%3A+celery.chord_unlock+chord
    #callback = obvindexmakerfunc.si()
    #chord (job)(callback)

    

    # group(  celery_task_updating_stockdaydata(companies_list_pk[:len(companies_list_pk)//2]).delay() ,
    #     celery_task_updating_stockdaydata(companies_list_pk[len(companies_list_pk)//2:]).delay()  )
    
    # chord(

    #     group(  celery_task_updating_stockdaydata(companies_list_pk[:len(companies_list_pk)//2]) ,
    #     celery_task_updating_stockdaydata(companies_list_pk[len(companies_list_pk)//2:])  ) ,
             
              
    #     a=ObvIndexMakerClass()

    # ).delay()

    # for companies_list in l :
    #     print("from loop11")

    #     print("from loop12")
    #     # a =  Celery_Task_Updating_Stockdaydata(companies_list)
    #     # a.start.delay()

    return HttpResponse(dt.datetime.now())


def test_view(request):
    return HttpResponse(dt.datetime.now())


def insert_company_csv(request):
    insert_companies_to_db_from_csv()

    # today = datetime.today()
    # companies_obj= ComapnyStockData.objects.filter(update_time__lt=date(today.year, today.month, today.day))[:1200:-1]

    # n =5
    # split = int(ceil(len(companies_obj)/4.))

    # columns = [companies_obj[i*split:(i+1)*split] for i in range(4)]

    #print (" lennnnnn ",columns[0])
    #n = 5

    #arr = []

    # for col in columns:

    #     for i in col:
    #         print(i)
    #     print("--------")

    #l = numpy.array_split(numpy.array(companies_obj),3)

    #print(" companies_obj " ,len(companies_obj))

    #B, C ,D= split_list(companies_obj)

    #val =  list(chunk(companies_obj, 3,len(companies_obj)) )

    # p=StockDayData.objects.filter(company_stock_data__ticker="GNMX")
    # print(p)
    #l1= l[0].tolist()
    # l2= l[1].tolist()
    # l3= l[2].tolist()

    # print("  l ", l)

    # for o in l:
    #     for o1 in o:

    #         print(" com ",o1," l : ",o)

    # for com in numpy.nditer(l[0]):
    #      print(" com ",com)

    # return HttpResponse(dt.datetime.now())
    # StockDayData.objects.all().delete()
    #s= ComapnyStockData.objects.filter(ticker="AMD")
    #today = datetime.today()
    #ComapnyStockData.objects.all().update(update_time =date(today.year, today.month, 12))
    # print(s)
    # StockDayData.objects.all().delete()
    return HttpResponse(dt.datetime.now())
    # StockDayData.objects.all().delete()
    # return
    # now = datetime.now()
    # now_date =now.date()

    # day_after_10_days =now + timedelta(days=-10)
    # #p=StockDayData.objects.filter(ticker="AMD")
    # p=StockDayData.objects.filter(stock_date__lt=date(day_after_10_days.year, day_after_10_days.month, day_after_10_days.day))
    # #p.delete()

    # print(" p count ", p.count())
    # return HttpResponse(dt.datetime.now())
    # p=StockDayData.objects.all()
    # p=StockDayData.objects.all().prefetch_related('company_stock_data').all()

    #a = p.filter(company_stock_data__ticker="LMND")

    #print(" ******************* ",a)
    #s= ComapnyStockData.objects.filter(ticker="AMD")
    # print(" ################### ",s)

    # q=p.filter(company_stock_data__ticker="AMD")

    #print("qqq ",q)
    # print(p.company_stock_data.objects.filter(company_stock_data="LMND"))
    #today = datetime.today()
    # ComapnyStockData.objects.all().update(update_time =date(today.year, today.month, 12)) # 3 seconds
    return HttpResponse(dt.datetime.now())
    # pp = ComapnyStockData.objects.all()
    # today = datetime.today()
    # for p in pp:
    #     p.update_time =date(today.year, today.month, 13)

    #     p.save()
    #ComapnyStockData.objects.filter(stock_date =date(today.year, today.month, today.day)  )
    # return HttpResponse(dt.datetime.now())
    '''
    pr=StockDayData.objects.filter().order_by('-id')[:10:-1]

    p = ComapnyStockData.objects.get(ticker="AEG")
    pr= StockDayData.objects.filter(company_stock_data=p)

    print("#############")
    for t in pr:
        print(t)
    #print(pr)
    print("#############")

    today = datetime.today()

    now = datetime.now()
    now_date =now.date()
    sdd = StockDayData.objects.filter(stock_date =date(today.year, today.month, today.day)  )

    if  not sdd.exists():
        print(" not exsist - ",sdd)
    else:
        print("exsist")

    
    with open('others/2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                x= row[0].replace("^","-")
                ComapnyStockData.objects.create(ticker=x ,company_name=row[1], stock_exchange= row[2] )
                line_count += 1
                print(line_count)
        print(f'Processed {line_count} lines.')
    '''


def delete_all_db(request):
    """
        wiil erase stockdaydata and company data and OBV index 
    """
    print(" ------   from  delete_all_db")
    StockDayData.objects.all().delete()
    ComapnyStockData.objects.all().delete()
    OBVindex.objects.all().delete()
    return HttpResponse(dt.datetime.now())


def load_db(request):
    """
        load db (companies)  from others/2.csv file
    """
    insert_companies_to_db_from_csv()
    
    return HttpResponse(dt.datetime.now())
