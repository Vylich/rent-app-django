from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http.request import HttpRequest
# Create your views here.
from .forms import ClientAddForm, User, CarForm, ClientOnlineAddForm
from .models import Car, Order, Client
from .services import in_group


@in_group(['Приемщик', 'Сис. Администратор'])
def Priem(request):
    context = {
        'title': '',
        'form': ClientAddForm(),
        'clients': Client.objects.all()


    }
    if request.method == 'POST':
        form = ClientAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ("Пользователь успешно зарегестрирован!"))
    return render(request, 'site/Priem.html', context=context)


@in_group(['Сис. Администратор'])
def admin_panel(request: HttpRequest):
    context = {
        'users': User.objects.all(),
    }
    if request.method == 'POST':

        user = User.objects.get(pk=request.POST.get('ban_user'))
        user.is_active = False
        user.save()
        messages.success(request, ("Пользователь успешно заблокирован!"))
    return render(request, 'site/admin_panel.html', context=context)


@in_group(['Директор', 'Сис. Администратор'])
def current_car(request: HttpRequest, id):
    car = get_object_or_404(Car, pk=int(id))
    form = CarForm(instance=car)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('stats')
    return render(request, 'site/car.html', context=context)


def index(request):
    context = {
        'cars': Car.objects.filter(status='available')
    }
    if request.method == 'POST':
        # data = request.POST
        car = Car.objects.get(pk=request.POST.get('book'))
        # new_order = Order(client=Client.objects.get(pk=data['client']), car=car)
        car.status = 'booking'
        car.save()
        # new_order.save()
        messages.success(request, ("Автомобиль успешно забронирован"))
    return render(request, 'site/cars.html', context=context)


@in_group(['Директор', 'Сис. Администратор'])
def statistic(request):
    context = {
        'statistics_available_cars': Car.objects.filter(status='available'),
        'statistic_orders': Order.objects.all().order_by('-created_at'),
        'title': 'Cars',
        'cars': Car.objects.all(),
        'statistics_booking_cars': Car.objects.filter(status='booking'),
    }
    return render(request, 'site/statistics.html', context=context)


@in_group(['Подборщик', 'Сис. Администратор'])
def Podbor(request: HttpRequest):
    context = {
        'clients': Client.objects.all(),
        'cars': Car.objects.filter(status='available')
    }
    if request.method == 'POST':
        data = request.POST
        car = Car.objects.get(pk=data['car'])
        new_order = Order(client=Client.objects.get(
            pk=data['client']), car=car)
        car.status = 'not_available'
        car.save()
        new_order.save()
    return render(request, 'site/Podbor.html', context=context)


@in_group(['Оценщик', 'Сис. Администратор'])
def Ocenka(request: HttpRequest):
    context = {
        'form': CarForm()
    }
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'site/Ocenka.html', context=context)


def home(request):
    context = {
        'title': '',
    }
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'site/home.html', context=context)


def current_client(request: HttpRequest, id):
    client = get_object_or_404(Client, pk=int(id))
    form = ClientAddForm(instance=client)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ClientAddForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('priem')
    return render(request, 'site/client.html', context=context)


def clients(request):
    context = {
        'clients': Client.objects.all()
    }
    return render(request, 'site/clients.html', context=context)


def userclient(request):
    context = {
        'title': 'Cars',
        'cars': Car.objects.all(),
        'available_cars': Car.objects.filter(status='available'),
    }
    return render(request, 'site/userclient.html', context=context)


def personalarea(request):
    context = {
        'title': 'Cars',
        'cars': Car.objects.all()
    }
    return render(request, 'site/personalarea.html', context=context)


def reg_cli(request):
    context = {
        'title': '',
        'form': ClientAddForm()
    }
    if request.method == 'POST':
        form = ClientAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ("Пользователь успешно зарегестрирован!"))
            return redirect('index')
    return render(request, 'site/reg_cli.html', context=context)
