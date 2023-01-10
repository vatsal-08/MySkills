from django.shortcuts import render
from .forms import *
from django.views.generic import FormView 
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView 
from django.contrib.auth import logout as django_logout

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


class LoggingView(LoginView):
    template_name='accounts/login.html'
    form_class=LoginForm
    redirect_autheticated_user = True
    success_url = reverse_lazy('courses')

    def get(self,request):
        form = self.form_class
        message=''
        return render(request,self.template_name,context={'form':form,'message':message})
    

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(LoggingView, self).form_valid(form)
        
def logout(request):
    django_logout(request)
    return redirect('login')
