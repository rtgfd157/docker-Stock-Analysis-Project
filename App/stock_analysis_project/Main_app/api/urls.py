from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from Main_app.api import views as kv

from Main_app.api.views import StockDayDataListView ,StockDayDataViewSet,CounterData


routerList_Main_app = SimpleRouter()
routerList_Main_app.register(r"Company/StockDays/router", kv.StockDayDataViewSet, 'StockDayData')
from Main_app.views import test_view

urlpatterns = [

    #path("", include(router.urls)),

    path("Company/StockDays/<int:pk_company>/",
         StockDayDataListView.as_view(),
         name="StockDays-list"),
    #path("obvindex/", kv.OBVindexViewSet.as_view(), name="obv-index"  )


    path("Company/StockDay/counter/",
         CounterData.as_view(),
         name="counter-data"),

    path("test/",test_view,name="test" )  
]



