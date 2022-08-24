from audioop import reverse
from re import template
from django.shortcuts import redirect
from django.contrib import auth
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import *
from django.contrib.auth import get_user_model


class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy("courses:detail")

    def get_success_url(self, *args, **kwargs):
        if kwargs != None:
            return reverse_lazy('detail', kwargs={'pk': kwargs['idnumber']})
        else:
            return reverse_lazy('courses')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('courses')
        return super(SignupView, self).get(*args, **kwargs)


class LoginView(FormView):
    login_url = '/login/'
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('courses')

    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None

    def clean(self, args, kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                emai = authenticate(email=email, password=password)
                if not emai:
                    raise forms.ValidationError('Email doesnot exist')
                raise forms.ValidationError('User doesnot exist')

            if not user.check_passsword(password):
                raise forms.ValidationError('Incorrect password')
        return super(LoginForm, self).clean(*args, **kwargs)


def logout(request):
    auth.logout(request)
    return redirect('courses')
