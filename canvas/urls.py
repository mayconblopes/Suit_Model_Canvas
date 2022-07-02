from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('smc/<str:pk>', views.smc, name="smc"),
    path('new/', views.new_smc, name="new_smc"),
    path('smc/conf-del/<str:pk>', views.conf_del_smc, name="conf_del_smc"),
    path('smc/del/<str:pk>', views.del_smc, name="del_smc"),

]