import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('courses')  
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        if request.user.is_authenticated:
            return redirect('courses')
        else:
            return render(request, 'login.html')


def register(request):
    return render(request,'accounts/signup.html')

def success(request):
    return render(request,'accounts/success.html')

def token_send(request):
    return render(request,'accounts/token_send.html')

def verify(request):
    return render(request,'accounts/token_send.html')

def error_page(request):
    return render(request,'accounts/error.html')
