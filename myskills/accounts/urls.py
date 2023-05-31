from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('token/', token_send, name="token_send"),
    path('success/', success, name="success"),
    path('verify/<auth_token>/', verify, name="verify"),
    path('error/', error_page, name="error"),
]
