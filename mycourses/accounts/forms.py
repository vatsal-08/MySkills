from socket import fromshare
from django import forms
from accounts.models import User
class SignupForm(forms.Form):
    class Meta:
        model = User
        fields = ['username','email','name',  'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)