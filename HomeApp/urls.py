from django.urls import path, include
from . import views

app_name = 'HomeApp'


urlpatterns = [
    path('', views.HomeView, name="ViewHome"),
    path('create_post/', views.CreatePostView, name="ViewCreatePost"),
    path('view_post/', views.ViewPostView, name="ViewPostView"),
    path('reply_post/<int:post_id>/', views.ViewPostDetail, name="ViewPostDetail"),
    path('edit_post/<int:post_id>/', views.ViewEditPost, name="ViewEditPost"),
    path('view_changes/<int:post_id>/', views.ViewChangesVersion, name="ViewChangesVersion"),
    path('rate_user/<int:user_id>/', views.ViewRateUser, name="ViewRateUser"),
    path('view_profile/<int:user_id>/', views.ViewUserProfile, name="ViewProfile"),
    path('delete_post/<int:post_id>', views.ViewDeletePost, name="ViewDeletePost")



]
