from django import forms
from accounts.models import User


class SignupForm(forms.Form):
    # username = forms.CharField(label='Your Username',max_length=75)
    # email = forms.EmailField(label='Email')
    # password = forms.CharField(widget=forms.PasswordInput) 
    
        # AJAX left to add for user(available or not)  
    class Meta:
        model = User
        fields=('username','email','password')
    
    def save(self,commit=True):
        pass


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    