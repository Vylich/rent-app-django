import typing

from django.contrib.auth.models import Group
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Car, Order, Client


def in_group(group: list):
    def decorator(function):
        def wrapper(*args, **kwargs):
            user = args[0].user
            allow = False
            for _group in group:
                if user.groups.filter(name=_group).exists():
                    allow = True
            if allow:
                return function(*args, **kwargs)
            else:
                return redirect('Home')
        return wrapper

    return decorator


@receiver(post_save, sender=Car)
def add_in_log(sender, **kwargs):
    print(sender, kwargs)
    car = kwargs.get('instance')
    if not Order.objects.filter(car=car).exists():
        Order(car=car).save()
