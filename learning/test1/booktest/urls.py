from django.urls import path
from . import views

app_name='booktest'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('addbook/', views.add_book, name='addbook'),
    path('action/', views.action, name='action'),
]