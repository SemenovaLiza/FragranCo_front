from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class CreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last_name'}))
    username = forms.CharField(
                    widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'passworod'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'passworod confirmation'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class LoginForm(AuthenticationForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'passworod'}))
