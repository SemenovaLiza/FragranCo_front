from django.views.generic import CreateView
from django.shortcuts import render

from django.urls import reverse_lazy
from .forms import UserCreationForm


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('products:index')
    template_name = 'users/sign_up.html'
