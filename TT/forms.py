from django import forms
from django.contrib.auth.models import User

from TT.models.post import Post
from TT.models.user_tt import UserTT


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserTTForm(forms.ModelForm):
    class Meta():
        model = UserTT
        fields = ('description' ,'profile_pic')


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('content', 'post_pic')