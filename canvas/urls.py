from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('smc/<str:pk>', views.smc, name="smc"),

]