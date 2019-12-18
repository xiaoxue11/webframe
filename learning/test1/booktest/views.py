from django.shortcuts import render
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    books = Bookinfo.objects.all()
    context = {'books': books}
    return render(request, 'booktest/index.html', context)

def detail(request,book_id):
    book = Bookinfo.objects.get(pk=book_id)
    heros = book.heroinfo_set.all()
    context = {'heros':heros}
    return render(request, 'booktest/detail.html', context)

def add_book(request):
    return render(request,'booktest/add.html')

def action(request):
    title = request.POST.get('title','')
    Bookinfo.objects.create(title=title, pub_date=datetime(1899,1,1))
    books = Bookinfo.objects.all()
    context = {'books': books}
    return render(request, 'booktest/index.html', context)

