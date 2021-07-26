from django.test import TestCase

from rest_framework.test import APIRequestFactory
# Create your tests here.
from django.test.client import encode_multipart, RequestFactory
from Main_app.api.views import StockDayDataListView


from rest_framework.test import APIClient
from django.test import Client


c = Client()
response = c.get('/api/Company/StockDay/counter/')

print("response.status_code : ",response.status_code)
print("response.content : ",response.content)
print("response.data : ",response.data)
print("response.data.results : ",response.data.results)
print(" ----------lll------ ")
num = 16489
c = Client()
response = c.get('/api/test/')

print("response.status_code : ",response.status_code)
print("response.content : ",response.content)



num = 16489
response = c.get('/api/Company/StockDays/{}/'.format(num))

print("response.status_code : ",response.status_code)
print("response.content : ",response.content)


factory = RequestFactory()
#data = {'id': 'remember to email dave'}
#content = encode_multipart('BoUnDaRyStRiNg', data)
#content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'


request = factory.get("api//Company/StockDays/{}/".format(16489) )

print(" $$$$$$$$test$$$$$$$$$$$$ ")
print(" ")
print(" --------test1---------- ")

print("request: ",request)
view= StockDayDataListView.as_view()
response = view(request)
#print(response.content)
print(response.data)
print(" --------test1/---------- ")

print(" --------test2---------- ")
client = APIClient()
response=client.get("/api/Company/StockDays/16489/", format='json')
# view= StockDayDataListView.as_view()
#response = view(request)
#print(response.text)
print(request)

print("response.status_code : ",response.status_code)
#print("response.content : ",response.content)
print(" --------test2/---------- ")

print(" ")
print(" $$$$$$$$test$$$$$$$$$$$$ ")

# from django.urls import reverse
# from django.test import TestCase
#from Main_app.api.views import home_page

# class HomePageTest(TestCase):

#     def test_root_url_resolves_to_home_page_view(self):
#         found = reverse('StockDays-list',kwargs={'pk_company>': 16489})  #2
        
#         print("found ",found)
        #self.assertEqual(found.func, StockDayDataListView)