from django.contrib.auth.models import User
from django.forms import ModelForm, NumberInput
from django.contrib.admin.widgets import AdminDateWidget
from django import forms

from .models import Client, Car


class ClientAddForm(ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ClientAddForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['patronymic'].widget.attrs['class'] = 'form-control'
        self.fields['passport'].widget.attrs['class'] = 'form-control'
        self.fields['_type'].widget.attrs['class'] = 'form-control'


class CarForm(ModelForm):

    class Meta:
        model = Car
        fields = ('brand', 'model', 'year', 'price', 'term', 'mark', 'owner')

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)

        self.fields['brand'].widget.attrs['class'] = 'form-control'
        self.fields['model'].widget.attrs['class'] = 'form-control'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['term'].widget.attrs['class'] = 'form-control'
        # self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['mark'].widget.attrs['class'] = 'form-control'
        self.fields['owner'].widget.attrs['class'] = 'form-control'


class ClientOnlineAddForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'passport')

    def __init__(self, *args, **kwargs):
        super(ClientOnlineAddForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['passport'].widget.attrs['class'] = 'form-control'
