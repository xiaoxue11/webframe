from django.shortcuts import render
from django.core.cache import cache
from .models import Goodstype
from django_redis import get_redis_connection

def index(request):
    context = cache.get('index_page_data')
    if context is None:
        types = Goodstype.objects.all()
        context = {
            'types':types
        }
        cache.set('index_page_data',context, 3600)
    return render(request, 'goods/index.html', context)




