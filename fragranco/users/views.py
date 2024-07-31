from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy

from .forms import CreationForm, LoginForm, PasswordChange


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('products:index')
    template_name = 'users/signup.html'


class Login(LoginView):
    form_class = LoginForm
    success_url = reverse_lazy('products:index')
    template_name = 'users/login.html'

class PasswordChange(PasswordChangeView):
    form_class = PasswordChange
    template_name = 'users/password_change_form.html'
