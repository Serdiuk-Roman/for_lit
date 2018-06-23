
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('shortly_app.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
