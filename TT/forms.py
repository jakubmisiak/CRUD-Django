from django import forms
from django.contrib.auth.models import User

from TT.models.comment import Comment
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
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'my-field-text', 'cols':50, 'rows': 6,'style':'resize:none;' }), label='')
    class Meta():
        model = Post
        fields = ('content', 'post_pic')
        labels = {
            'post_pic': 'Add photo'
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('content', )
        labels = {
            'content':'Add comment',
        }