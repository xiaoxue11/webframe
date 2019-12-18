from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    books = BookInfo.objects.all()
    context = {'books': books}
    return render(request, 'booktest/index.html',context)

def detail(request, book_id):
    book = BookInfo.objects.get(pk=book_id)
    heros = book.heroinfo_set.all()
    context = {'heros': heros}
    return render(request, 'booktest/detail.html', context)

def show(request):
    response = HttpResponse()
    if 'name' in request.COOKIES:
        response.write(request.COOKIES['name'])
    #response.set_cookie('name','123')
    return response