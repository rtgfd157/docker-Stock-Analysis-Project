from rest_framework import generics, status, viewsets
from OBVapp.api.serializers import (OBVindexSerializers)

from OBVapp.models import OBVindex
from rest_framework.generics import get_object_or_404

#from drf_multiple_model.views import ObjectMultipleModelAPIView
#from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination



class OBVindexViewSet(viewsets.ModelViewSet):
    serializer_class = OBVindexSerializers
    queryset = OBVindex.objects.all().order_by('-percentage_change')


