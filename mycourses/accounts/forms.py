from django import forms
from accounts.models import User


class SignupForm(forms.Form):
    username = forms.CharField(label='Your Username',max_length=75)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput) 

    def clean(self):
        cleaned_data = super().clean()
        name_of_user = cleaned_data("username")
        valpwd = cleaned_data.get("password") 
        user = User.objects.get(username=name_of_user)
        print(valpwd,user)
        # AJAX left to add for user(available or not)  


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    