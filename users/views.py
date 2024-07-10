from django.shortcuts import render


def login(request):
    context = {
        'title': 'JANC - Авторизация',
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'JANC - Регистрация',
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'JANC - Кабинет',
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    pass