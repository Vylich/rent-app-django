from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(models.Model):
    TYPES = [
        ('online', 'Онлайн'),
        ('arend', 'Сдает'),
        ('buyer', 'Арендует'),
    ]
    name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(
        verbose_name='Фамилия', max_length=100, default=None)
    patronymic = models.CharField(
        verbose_name='Отчество', max_length=100, default=None)
    passport = models.IntegerField(verbose_name='Серия и номер ВУ')
    _type = models.CharField(
        verbose_name='тип', choices=TYPES, default='online', max_length=15)

    def __str__(self):
        return f'{self.last_name} {self.name}'


class UserCli(AbstractBaseUser):
    TYPES = [
        ('online', 'Онлайн'),
        ('arend', 'Сдает'),
        ('buyer', 'Арендует'),
    ]
    username = models.CharField(verbose_name='Никнейм', max_length=10)
    name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100)
    passport = models.IntegerField(verbose_name='Серия и номер ВУ')
    _type = models.CharField(
        verbose_name='тип', choices=TYPES, default='online', max_length=15)

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    MARKS = (
        (None, 'Без оценки'),
        ('good', 'Хорошее'),
        ('medium', 'Среднее'),
        ('bad', 'Ниже среднего')
    )
    STATUSES = (
        ('not_available', 'Сдана'),
        ('available', 'Сдается'),
        ('booking', 'Забронирована')
    )
    TERMS = (
        ('1', '1 месяц'),
        ('2', '3 месяца'),
        ('3', '6 месяцев')
    )
    brand = models.CharField(verbose_name='марка', max_length=50)
    model = models.CharField(verbose_name='модель', max_length=50)
    year = models.CharField(verbose_name='год', max_length=4)
    mark = models.CharField(verbose_name='оценка состояния',
                            choices=MARKS, default=None, max_length=15)
    owner = models.ForeignKey(
        Client, verbose_name='Хозяин', on_delete=models.CASCADE, null=False, blank=False)
    price = models.IntegerField('Цена', default=0)
    term = models.CharField(verbose_name='срок сдачи',
                            choices=TERMS, default='1', max_length=15)
    status = models.CharField(
        verbose_name='статус', choices=STATUSES, default='available', max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.brand} - {self.model} [{self.get_status_display()}]'


class Order(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='order_car')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='order_client', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.car} {self.client} {self.created_at}'
