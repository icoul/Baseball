from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/', include('data.urls')),
    url(r'^baseball/', include('main.urls')),

]
