from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('',,name=""),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
]
