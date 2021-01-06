from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from TT.forms import UserForm, UserTTForm, PostForm
from TT.models.post import Post
from TT.models.user_tt import UserTT


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_tt = UserTTForm(data=request.POST)
        if user_form.is_valid() and user_tt.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            new_acc= user_tt.save(commit=False)
            new_acc.user = user

            if 'profile_pic' in request.FILES:
                new_acc.profile_pic = request.FILES['profile_pic']

            new_acc.save()
    else:
        user_form = UserForm()
        user_tt = UserTTForm()
    return render(request,'register.html',
                  {'user_form':user_form,
                   'user_tt':user_tt})

@login_required
def home(request):
    posts = Post.objects.all()
    posts_paginator = Paginator(posts,5)
    page_number=request.GET.get('page')
    page = posts_paginator.get_page(page_number)

    context = {
        'page': page
    }


    return render(request, 'log/home.html', context)





@login_required
def addPost(request):
    current_user = UserTT.objects.get(user=request.user)
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save()

            if 'post_pic' in request.FILES:
                post.profile_pic = request.FILES['post_pic']
            post.userTT=current_user
            post.save()
    else:
        post_form = PostForm()

    return render(request, 'log/addPost.html', {'post_form':post_form})
