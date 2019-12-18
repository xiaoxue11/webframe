from django.urls import path
from .views import *

app_name = 'goods'
urlpatterns = [
    path('', index, name='index'),
]