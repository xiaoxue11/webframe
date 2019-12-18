import hashlib
from .models import *
from django.core.cache import cache
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, logout, login

def hash_code(s, salt='myuser'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def register_view(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = hash_code(form.cleaned_data.get('password'))
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return redirect(reverse('user:login'))
        context = {'form': form}
        return render(request, 'user/register.html',context)
    form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'user/register.html', context)

def login_view(request):
    remember = request.POST.get('remember')
    next_url = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = hash_code(form.cleaned_data.get('password'))
        user = authenticate(username=username,password=password)
        login(request, user)
        if next_url:
            response = redirect(next_url)
        else:
            response = redirect(reverse('user:index'))
        if remember == 'on':
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
        else:
            response.delete_cookie('username')
        return response
    username = request.COOKIES.get('username')
    checked = 'checked'
    if username is None:
        username = ''
        checked = ''
    context = {
        'username': username,
        'checked': checked,
        'form': form,
    }
    return render(request, 'user/login.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse('user:login'))

#=================define user information================
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    context = cache.get('index_page_data')
    if context is None:
        books = BookInfo.objects.filter(user=user)
        print(books)
        context = {
            'books': books
        }
        cache.set('index_page_data', context, 3600)
    return render(request,'user/index.html', context)




