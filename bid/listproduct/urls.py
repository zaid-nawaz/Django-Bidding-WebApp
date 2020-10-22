from django.conf.urls import url,include
from django.contrib import admin
from listproduct import views

urlpatterns = [
    url(r'^$',views.listproducts,name='listproducts')
] 