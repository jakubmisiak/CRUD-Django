from apt import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from TT.forms import UserForm, UserTTForm, PostForm, CommentForm
from TT.models.comment import Comment
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
            return redirect('login')
    else:
        user_form = UserForm()
        user_tt = UserTTForm()
    return render(request,'register.html',
                  {'user_form':user_form,
                   'user_tt':user_tt})

@login_required
def home(request):
    current_user = UserTT.objects.get(user=request.user)
    posts = Post.objects.all().order_by('-date')
    posts_paginator = Paginator(posts,5)
    page_number=request.GET.get('page')
    page = posts_paginator.get_page(page_number)
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.userTT = current_user
            post.save()
        return redirect('home')

    context = {
        'page' : page,
        'form' : form
    }


    return render(request, 'log/home.html', context)



@login_required
def post(request, id):
    current_user = UserTT.objects.get(user=request.user)
    post = Post.objects.get(id=id)
    comments =  Comment.objects.all().filter(post=post).order_by('-id')
    for i in comments:
        print(i.content)
        print("---------")
        print(i.user)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.user = current_user
            comment.save()
        return redirect('post', id=post.id)
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }

    return render(request, 'log/post.html', context)

@login_required
def user_profile(request, id):
    user = UserTT.objects.get(id=id)
    post = Post.objects.all().filter(userTT=user)
    print(user.post_count())
    context = {
        'user':user,
        'post': post,
        'post_count': user.post_count(),
    }
    return render(request, 'log/userprofile.html', context)

@login_required
def update_post(request, id):
    post = Post.objects.get(id=id)
    current_user = UserTT.objects.get(user=request.user)
    form = PostForm(instance=post)

    if current_user!=post.userTT:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
        return redirect('post', id=post.id)

    context = {'form':form}
    return render(request, 'log/updatepost.html', context)


@login_required()
def delete_view(request, id):
    post = Post.objects.get(id=id)
    current_user = UserTT.objects.get(user=request.user)
    if post.userTT == current_user:
        post.delete()
        return redirect('home')
    else:
        return redirect('home')


@login_required()
def user_logout(request):
    logout(request)
    return redirect('login')

