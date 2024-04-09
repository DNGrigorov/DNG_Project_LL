from django.urls import path, include
from . import views

app_name = 'HomeApp'


urlpatterns = [
    path('', views.HomeView, name="ViewHome"),
    path('create_post/', views.CreatePostView, name="ViewCreatePost"),
    path('view_post/', views.ViewPostView, name="ViewPostView"),
]
