from django.shortcuts import render

# Create your views here.
import time
import datetime as dt
import csv
from datetime import datetime, date, time, timedelta
from OBVapp.models import OBVindex

from django.shortcuts import HttpResponse
from .models import ComapnyStockData,StockDayData
from .tasks import celery_task_updating_stockdaydata #, Celery_Task_Updating_Stockdaydata
from math import ceil
import numpy


def celery_view(request):    
    print(" from celery vieww  ")
    celery_task_updating_stockdaydata.delay()
    #celery_task_updating_stockdaydata()

    today = datetime.today()

    # for first time using we will want to update right away because date field in model is auto now
    # if StockDayData.objects.count()  > 0:
    #     companies_obj= ComapnyStockData.objects.filter(update_time__lt=date(today.year, today.month, today.day))
    # else :
    #     companies_obj= ComapnyStockData.objects.all()

    # n = 2
    # l = numpy.array_split(numpy.array(companies_obj),n)

    # for companies_list in l :

    #     a =  Celery_Task_Updating_Stockdaydata(companies_list)
    #     a.start.delay()

    return HttpResponse(dt.datetime.now())



def test_view(request):
    return HttpResponse(dt.datetime.now())


def insert_company_csv(request):
    print("hello world")
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

    #p=StockDayData.objects.filter(company_stock_data__ticker="GNMX")
    #print(p)
    #l1= l[0].tolist()
    # l2= l[1].tolist()
    # l3= l[2].tolist()

    # print("  l ", l)

    # for o in l:
    #     for o1 in o:

    #         print(" com ",o1," l : ",o)

    # for com in numpy.nditer(l[0]):
    #      print(" com ",com)

    #return HttpResponse(dt.datetime.now())
    #StockDayData.objects.all().delete()
    #s= ComapnyStockData.objects.filter(ticker="AMD")
    #today = datetime.today()
    #ComapnyStockData.objects.all().update(update_time =date(today.year, today.month, 12))
    #print(s)
    #StockDayData.objects.all().delete()
    return HttpResponse(dt.datetime.now())
    #StockDayData.objects.all().delete()
    #return
    # now = datetime.now()
    # now_date =now.date()

    # day_after_10_days =now + timedelta(days=-10)
    # #p=StockDayData.objects.filter(ticker="AMD")
    # p=StockDayData.objects.filter(stock_date__lt=date(day_after_10_days.year, day_after_10_days.month, day_after_10_days.day))
    # #p.delete()

    # print(" p count ", p.count())
    # return HttpResponse(dt.datetime.now())
    #p=StockDayData.objects.all()
    #p=StockDayData.objects.all().prefetch_related('company_stock_data').all()

    #a = p.filter(company_stock_data__ticker="LMND")

    #print(" ******************* ",a)
    #s= ComapnyStockData.objects.filter(ticker="AMD")
    #print(" ################### ",s)

    #q=p.filter(company_stock_data__ticker="AMD")
    
    #print("qqq ",q)
    #print(p.company_stock_data.objects.filter(company_stock_data="LMND"))
    #today = datetime.today()
    #ComapnyStockData.objects.all().update(update_time =date(today.year, today.month, 12)) # 3 seconds
    return HttpResponse(dt.datetime.now())
    # pp = ComapnyStockData.objects.all()
    # today = datetime.today()
    # for p in pp:
    #     p.update_time =date(today.year, today.month, 13)
        
    #     p.save()
        #ComapnyStockData.objects.filter(stock_date =date(today.year, today.month, today.day)  )
    #return HttpResponse(dt.datetime.now())
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

    print (" load_db from csv file")
    lista = []
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
                #ComapnyStockData.objects.create(ticker=x ,company_name=row[1], stock_exchange= row[2] )
                lista.append(    ComapnyStockData(ticker=x ,company_name=row[1], stock_exchange= row[2] )        )
                line_count += 1
                print(line_count)

    ComapnyStockData.objects.bulk_create( lista)

    return HttpResponse(dt.datetime.now())

