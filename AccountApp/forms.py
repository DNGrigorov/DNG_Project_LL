from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import WebUser

class SignUpForm(UserCreationForm):
    birth_year = forms.CharField(max_length=4)
    birth_month = forms.CharField(max_length=2)
    birth_day = forms.CharField(max_length=2)
    gender = forms.CharField(max_length=1)

    class Meta:
        model = WebUser
        fields = ['username', 'email', 'password1', 'password2', 'birth_year', 'birth_month', 'birth_day', 'gender']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))