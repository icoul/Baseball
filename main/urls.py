from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^player/(?P<pk>[0-9]+)/$', views.stat, name='stat'),
]