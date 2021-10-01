from django.urls import path
from . import views

app_name = "acc"

urlpatterns = [
    path('', views.main, name="main"),
    path('login', views.login, name="login"),
    path('regist', views.regist, name="regist"),
]
