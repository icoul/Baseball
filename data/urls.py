from django.conf.urls import url
from . import views

app_name = 'data'
urlpatterns = [
    url(r'^batter/$', views.batter, name = 'batter'),
    url(r'^batter/stat/$', views.batter_stat, name = 'batter_stat'),
    url(r'^pitcher/$', views.pitcher, name = 'pitcher'),
    url(r'^pitcher/stat/$', views.pitcher_stat, name = 'pitcher_stat'),
]
