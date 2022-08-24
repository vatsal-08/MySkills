
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email',  'password1', 'password2']


class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
