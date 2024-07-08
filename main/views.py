from http.client import HTTPResponse
from django.shortcuts import render

from goods.models import Category

def index(request):

    category = Category.objects.all()

    context = {
        'title': 'JANC - Главная',
        'content': 'Django Machine',
        'category': category
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'JANC - О нас',
        'content': 'О нас',
        'text_on_page': 'Blah-blah-blah...'
    }

    return render(request, 'main/about.html', context)