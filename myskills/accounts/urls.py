from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login_view,name="login-view"),
    path('logout_view/',logout_view,name='logout-view'),
    path('token_send/', token_send, name="token-send"),
    path('success/', success, name="success"),
    path('verify/<auth_token>/', verify, name="verify"),
    path('error/', error_page, name="error"),
]
