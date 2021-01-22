from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('logout', views.user_logout, name='logout')

]