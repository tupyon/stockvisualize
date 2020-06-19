from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'stockapp'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
    #url(r'^template/$', views.quotedisplay, name='quote'),  
    path('quote/',views.quotedisplay,name='tickerdisplay'),
    path('tickerserach/',views.tickerserach,name='tickerserach'),
]

