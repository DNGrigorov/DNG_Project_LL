from django.urls import path, include
from . import views

app_name = 'AccountApp'

urlpatterns = [
    path('signup/', views.UserSignUpView, name="ViewSignup"),
    path('login/', views.UserLoginView, name="ViewLogin"),
]
