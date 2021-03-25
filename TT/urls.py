from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('logout/', views.user_logout, name='logout'),
    path('post/<int:id>/update', views.update_post, name='updatePost'),
    path('post/<int:id>/delete', views.update_post, name='deletePost'),
    path('user/<int:id>', views.user_profile, name='userProfile')
]