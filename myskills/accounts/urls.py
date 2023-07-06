from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login_view,name="login-view"),
    path('logout_view/',logout_view,name='logout-view'),
    path('token_send/', token_send, name="token-send"),
    path('success/', success, name="success"),
    path('verify/<str:auth_token>/', verify, name="verify"),
    path('error/', error_page, name="error"),
    path('forgot/', forgot, name="forgot"),
    path('reset/', reset, name="reset-password"),
    path('reset/<auth_token>/', reset_password, name="reset-password"),
]
