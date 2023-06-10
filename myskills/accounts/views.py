import uuid
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail

def login_view(request):
    if request.user.is_authenticated:
        return redirect('courses')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('courses')  
        else:
            messages.error(request,'Invalid email or password')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login-view') 

def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password!=confirm_password:
            messages.error(request,"Passwords don't match")
            return redirect('register')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        auth_token = str(uuid.uuid4())
        user = CustomUser.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password,auth_token=auth_token)
        return redirect('login-view')
    return render(request,'accounts/signup.html')


def success(request):
    return render(request,'accounts/success.html')

def token_send(request):
    if not request.user.is_authenticated:
        return redirect('login-view')
    if request.user.is_verified:
        messages.info(request,"You are already verified")
        return redirect('courses')
    send_mail_for_verification(request.user.email,request.user.auth_token)
    return render(request,'accounts/token_send.html')

def verify(request,auth_token):
    if request.user.is_authenticated and request.user.is_verified:
        messages.info(request,"You are already verified")
        return redirect('courses')
    try:
        profile_obj = CustomUser.objects.filter(auth_token=auth_token).first()
        if profile_obj.email==request.user.email:
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request,"Your account has been verified")
            return redirect('success')
        else:
            messages.error(request,"")
            return redirect('error')
    except Exception as e:
        messages.error(request,"Some error occured")
        return redirect('error')

def error_page(request):
    return render(request,'accounts/error.html')

def send_mail_for_verification(email,token):
    subject = "Your account needs to be verified"
    message = f'Click on the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)