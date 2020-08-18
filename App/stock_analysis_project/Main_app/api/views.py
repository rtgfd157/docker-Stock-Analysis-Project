from rest_framework import generics, status, viewsets
from OBVapp.api.serializers import (OBVindexSerializers)
from rest_framework import views
from Main_app.models import StockDayData, ComapnyStockData
from rest_framework.generics import get_object_or_404

from Main_app.api.serializers import StockDayDataSerializers, StockDayDataListSerializers, CountSerializer
#from drf_multiple_model.views import ObjectMultipleModelAPIView
#from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination

from rest_framework.renderers import JSONRenderer
from rest_framework.mixins import ListModelMixin
from rest_framework import renderers
from rest_framework.response import Response


class StockDayDataViewSet(viewsets.ModelViewSet):
    #renderer_classes = [renderers.JSONRenderer]

    serializer_class = StockDayDataSerializers
    queryset = StockDayData.objects.filter().order_by('-stock_date').all()

    # def get_queryset(self):
    #     print(" ---------------check---------------")
    #     kwarg_pk = self.kwargs.get("pk")
    #     print(" kwarg_pk  ",kwarg_pk)
    #     return StockDayData.objects.filter(company_stock_data__id=kwarg_pk).order_by('-stock_date').all()


class StockDayDataListView(generics.ListAPIView):
    serializer_class = StockDayDataListSerializers
    

    def get_queryset(self,  *args, **kwargs):
        print(" ---------------check  view---------------")
        
        kwarg_pk = self.kwargs.get("pk_company")
         
        print(" kwarg_pk  ",kwarg_pk)
        return StockDayData.objects.filter(company_stock_data__id=kwarg_pk).order_by('stock_date').all()


# class CounterData(ListModelMixin,generics.GenericAPIView):
#     """
#         will return comapny count and stockdata count
#     """
#     serializer_class = CountSerializer
#     queryset = ComapnyStockData.objects.count()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class CounterData(views.APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        
        yourdata= {"company_count": CountSerializer.get_company_count(), "stockdata_count": CountSerializer.get_stockdata_count}
        results = CountSerializer(yourdata).data

        #print("results ",results)

        #print(Response(results))
        #return Response({"success": True})

        return Response(results)