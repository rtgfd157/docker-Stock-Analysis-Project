"""stock_analysis_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from Main_app.views import celery_view, insert_company_csv,delete_all_db, load_db
from django.conf import settings

from OBVapp.views import obv_index_maker_view, a_view
from core.views import IndexTemplateView

from Main_app.api.urls import routerList_Main_app
from OBVapp.api.urls import routerList_OBVapp
from rest_framework.routers import DefaultRouter,SimpleRouter




router = DefaultRouter()
router.registry.extend(routerList_Main_app.registry)
router.registry.extend(routerList_OBVapp.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('celerytask/', celery_view),
    path('insert_company_csv/', insert_company_csv),
    path('obv_index_maker_view/', obv_index_maker_view),
    path('a_view/', a_view),
    path('delete_all_db/', delete_all_db),
    path('load_db/', load_db),
    
    

    path('api/', include(router.urls)),
    path("api/",include("Main_app.api.urls")),
    # path("api/",include("OBVapp.api.urls")),


    #path('api-auth/',include("rest_framework.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point") # spa url 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
