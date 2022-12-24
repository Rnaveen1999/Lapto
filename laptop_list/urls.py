from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('laptop_list',views.Home),
]