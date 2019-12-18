from django.urls import path
from .views import *

app_name = 'login'
urlpatterns = [
    path('', index, name='index'),
    path('edit/', edit_log, name='edit'),
    path('action/', action, name='action'),
    path('logout/', logout, name='logout'),
]