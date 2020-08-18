from rest_framework import serializers
from Main_app.models import ComapnyStockData ,StockDayData

class ComapnyStockDataSerializers(serializers.ModelSerializer):
    pass

    class Meta:
        model = ComapnyStockData
        fields = '__all__'


from rest_framework import serializers

from OBVapp.models import OBVindex
from Main_app.api.serializers import ComapnyStockDataSerializers

class  StockDayDataSerializers(serializers.ModelSerializer):
    #subject = serializers.StringRelatedField(read_only=True)
    company_stock_data = ComapnyStockDataSerializers(read_only=True)


    class Meta:
        model = StockDayData
        fields = '__all__'

class StockDayDataListSerializers(serializers.ModelSerializer):
    company_stock_data = ComapnyStockDataSerializers()

    class Meta:
        model = StockDayData
        fields = '__all__'

class CountSerializer(serializers.Serializer):
    company_count = serializers.IntegerField()
    stockdata_count = serializers.IntegerField()

    def get_company_count():
        return ComapnyStockData.objects.count()

    def get_stockdata_count():
        return StockDayData.objects.count()