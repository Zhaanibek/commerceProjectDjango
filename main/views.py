from http.client import HTTPResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'JANC - Главная',
        'content': 'Django Machine',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'JANC - О нас',
        'content': 'О нас',
        'text_on_page': 'Blah-blah-blah...'
    }

    return render(request, 'main/about.html', context)