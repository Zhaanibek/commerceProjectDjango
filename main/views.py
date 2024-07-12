from http.client import HTTPResponse
from django.shortcuts import render

from goods.models import Category
from main.api import get_currency_rate

def index(request):
    city = "Almaty" 
    currency_rate = get_currency_rate("USD", "KZT")

    context = {
        'title': 'JANC - Главная',
        'currency_rate': currency_rate,
        'content': 'Добро пожаловать на наш сайт!',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'JANC - О нас',
        'content': 'О нас',
        'text_on_page': 'Blah-blah-blah...'
    }

    return render(request, 'main/about.html', context)

