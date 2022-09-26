from django.shortcuts import render
from .forms import *
from django.views.generic import FormView
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout


# Create your views here.
class SignUpView(FormView):
    template_name= 'accounts/signup.html'
    form_class = SignupForm
    redirect_autheticated_user = True
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('courses')
        return super(SignUpView, self).get(*args, **kwargs)


# class LoginView()
def logout(request):
    auth.logout(request)
    return redirect('login')
