from django.conf.urls import url,include
from django.contrib import admin
from loginOrSignupSystem import views

urlpatterns = [
  url(r'^$',views.signup,name='signup'),
  url(r'^login/',views.login,name='login'),
  url(r'^signup/',views.signup,name='signUp')
] 