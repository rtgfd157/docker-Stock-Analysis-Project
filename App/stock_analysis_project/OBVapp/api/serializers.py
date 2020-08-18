from rest_framework import serializers

from OBVapp.models import OBVindex
from Main_app.api.serializers import ComapnyStockDataSerializers

class OBVindexSerializers(serializers.ModelSerializer):
    #subject = serializers.StringRelatedField(read_only=True)
    company_stock_data = ComapnyStockDataSerializers()


    class Meta:
        model = OBVindex
        fields = '__all__'
        #read_only_fields = ('__all__', )

 