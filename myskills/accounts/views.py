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
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.utils.html import format_html

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
    if not request.user.is_authenticated:
        return redirect('login-view')
    if request.user.is_verified:
        messages.info(request,"You are already verified")
        return redirect('courses')
    try:
        profile_obj = CustomUser.objects.filter(auth_token=auth_token).first()
        if profile_obj.email==request.user.email and profile_obj.auth_token==request.user.auth_token:
            profile_obj.is_verified = True
            profile_obj.auth_token = str(uuid.uuid4())
            profile_obj.save()
            messages.success(request,"Your account has been verified")
            return redirect('courses')
        else:
            messages.error(request,"Some error occured")
            return redirect('courses')
    except Exception as e:
        messages.error(request,"Some error occured")
        return redirect('error')

def error_page(request):
    return render(request,'accounts/error.html')

def forgot(request):
    if request.method=='POST':
        email = request.POST.get('email','')
        profile = CustomUser.objects.filter(email=email).first()
        send_mail_for_reset_password(email,profile.auth_token)
        return render(request,"accounts/reset.html")
    return render(request,"accounts/forgot.html")

def reset(request):
    return render(request,"accounts/reset.html")

def reset_password(request,auth_token):
    if request.method=='POST':
        email = request.POST.get('email','')
        password1 = request.POST.get('password','')
        password2 = request.POST.get('confirm_password','')
        profile = CustomUser.objects.filter(email=email).first()
        if profile is None:
            messages.error(request,"User doesnt exist")
            return redirect('courses')
        if email=='':
            messages.error(request,"Email is empty")
            profile.auth_token = str(uuid.uuid4())
            profile.save()
            return redirect('courses')
        if profile.auth_token!=auth_token:
            profile.auth_token = str(uuid.uuid4())
            profile.save()
            messages.error(request,"Invalid Link")
            return redirect('courses')
        if password1!=password2:
            profile.auth_token = str(uuid.uuid4())
            profile.save()
            messages.error(request,"Passwords don't match")
            return redirect('courses')
        profile.password = make_password(password1)
        profile.auth_token = str(uuid.uuid4())
        profile.save()
        login_link = login_link = format_html('<b><a href="{}" style="color: green;">Login</a></b>', reverse('login-view'))
        message = format_html('Password successfully changed. Click here to {}.', login_link)
        messages.success(request,message)
        subject = "Password changed successfullly"
        message="Your account password is changed successfully"
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[email]
        send_mail(subject,message,email_from,recipient_list)
        return redirect('courses')
    profile = CustomUser.objects.filter(auth_token=auth_token).first()
    if profile is None:
        messages.error(request,"Old link or invalid link")
        return redirect('courses')
    context={"profile" : profile}
    return render(request,"accounts/reset_password.html",context)

def send_mail_for_verification(email,token):
    subject = "Your account needs to be verified"
    message = f'Click on the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)

def send_mail_for_reset_password(email,token):
    subject = "Password change request"
    email_from = settings.EMAIL_HOST_USER
    message=f'Click on the link to redirect to password reset link of your account http://127.0.0.1:8000/accounts/reset/{token}'
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)