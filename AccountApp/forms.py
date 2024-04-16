from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import WebUser
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'})
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
    )
    birth_year = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year'})
    )
    birth_month = forms.CharField(
        max_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Month'})
    )
    birth_day = forms.CharField(
        max_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Day'})
    )
    gender = forms.ChoiceField(
        choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = WebUser
        fields = ['username', 'email', 'password1', 'password2', 'birth_year', 'birth_month', 'birth_day', 'gender']




class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))