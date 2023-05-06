import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'accounts/login.html')

def register(request):
    return render(request,'accounts/signup.html')
def success(request):
    return render(request,'accounts/success.html')

def token_send(request):
    return render(request,'accounts/token_send.html')