from django import forms
from accounts.models import User


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) 

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password'] 
        name_of_user = self.cleaned_data['username']
        user = User.objects.get(username=name_of_user)
        # AJAX left to add for user(available or not)  


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    