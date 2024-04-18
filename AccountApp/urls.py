from django.urls import path
from . import views

app_name = 'AccountApp'

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name="ViewSignup"),
    path('login/', views.UserLoginView.as_view(), name="ViewLogin"),
    path('logout/', views.UserLogoutView.as_view(), name="ViewLogout"),
    path('search_user/', views.ViewFilterUser, name="ViewFilterUser"),

        # Rest API
    path('api/users/', views.UserSearchAPIView.as_view(), name="api_user_search"),
]
