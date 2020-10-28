from django.conf.urls import url,include
from django.contrib import admin
from seesomeproduct import views

urlpatterns = [
    url(r'^$',views.seesomeproduct,name='seesomeproduct'),
    url(r'^searchresults/',views.search,name='search'),
    url(r'^prodview/',views.prodview,name='prodview'),

] 