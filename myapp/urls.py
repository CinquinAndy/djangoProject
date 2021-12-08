from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('result/<int:number>', views.result, name="result"),
]
