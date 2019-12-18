from django.shortcuts import render
from .models import GoodsType


def index(request):
    types = GoodsType.objects.all()
    context = {
        'types': types,
    }
    return render(request, 'goods/index.html', context)


