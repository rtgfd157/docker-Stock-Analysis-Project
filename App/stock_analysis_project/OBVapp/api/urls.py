from django.urls import include, path
from rest_framework.routers import DefaultRouter,SimpleRouter

from OBVapp.api import views as kv

from OBVapp.api.views import OBVindexViewSet 



routerList_OBVapp = SimpleRouter()
routerList_OBVapp.register(r"OBVindex", kv.OBVindexViewSet, 'OBVindex')


urlpatterns = [

    #path("", include(router.urls)),


    #path("obvindex/", kv.OBVindexViewSet.as_view(), name="obv-index"  )
       
]


