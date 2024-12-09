from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username):
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, age=age, balance=0)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'authorization_page.html', {'info': info})

def base(request):
    return render(request, 'menu.html')


def platform(request):
    return render(request, 'platform.html')


def games(request):
    context = {
        'products': Game.objects.all()
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')
