from asyncio import sleep
from django.contrib.auth.models import User, Group
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.groups.filter(name='Сис. Администратор'):
                return HttpResponseRedirect('admin_panel')
            elif user.groups.filter(name='Директор'):
                return HttpResponseRedirect('statistic')
            elif user.groups.filter(name='Оценщик'):
                return HttpResponseRedirect('Ocenka')
            elif user.groups.filter(name='Подборщик'):
                return HttpResponseRedirect('Podbor')
            elif user.groups.filter(name='Приемщик'):
                return HttpResponseRedirect('Priem')
            elif user.groups.filter(name='Клиент'):
                return HttpResponseRedirect('cars')
            else:
                return redirect('Home')

        else:
            messages.success(request, ("Неправильный логин или пароль."))
            return redirect('login')

            pass
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Выход выполнен!"))
    return redirect('Home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            group = form.cleaned_data['group']

            group.user_set.add(user)
            messages.success(
                request, ("Пользователь успешно зарегестрирован!"))
            return redirect('sysadmin')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {'form': form})


def users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'site/users.html', context=context)


def current_user(request: HttpRequest, id):
    user = get_object_or_404(User, pk=int(id))
    form = RegisterUserForm(instance=user)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Пользователь успешно отредактирован"))
            return redirect('sysadmin')

    return render(request, 'site/user.html', context=context)
