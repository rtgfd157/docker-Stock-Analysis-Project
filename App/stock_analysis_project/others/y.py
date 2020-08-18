import yfinance as yf
from datetime import datetime, date, time, timedelta
import numpy as np

#msft = yf.Ticker("EAE")
#print(msft.info)

#for i in msft.info:
#    print(i)
    
#print(msft.history(period="2020-07-10"))

import multiprocessing as mp

import numpy as np
from time import time



now = datetime.now()
now_date =now.date()

day_after_10_days =now + timedelta(days=-5)
day_after_10_days = day_after_10_days.date()

l = str(now.date())

print("---------")
print(l)
print(day_after_10_days)
print("---------")
x = 1
y_ob = yf.Ticker("AMD")
result =y_ob.history(start=str(day_after_10_days) ,end = str(l) )

#print(result)

#print(result)
x=0
#for i in result:
#    print("i - ",i,"value - ",result['Close'][x])
#    x= x+1
    
#for idx,item in enumerate(result-1):
#    print("i - ",idx,"value - ",result['Close'][idx])



idx= 0
for  row in result.iterrows():
    #a= datetime.fromtimestamp((row[0])
    #print("  +-+  ",result['Close'][idx])
    #print("i - ",idx,"value - ",result['Close']['AMD'][idx], ", close  - ",result['Volume']['AMD'][idx],"   ",row[0].strftime('%Y-%m-%d') )
    print("i - ",idx,"value - ",result['Close'][idx], ", close  - ",result['Volume'][idx],"   ",row[0].strftime('%Y-%m-%d') )
    idx= idx+1
    

# if __name__ == "__main__":
#     a_view()  