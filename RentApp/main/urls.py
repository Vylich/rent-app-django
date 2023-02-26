from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('members.urls')),
    path('statistic', views.statistic, name='stats'),
    path('Podbor', views.Podbor, name='podbor'),
    path('Ocenka', views.Ocenka, name='ocen'),
    path('admin_panel', views.admin_panel, name='sysadmin'),
    path('Priem', views.Priem, name='priem'),
    path('home', views.home, name='Home'),
    path('cars', views.index, name='index'),
    path('clients', views.clients, name='cli'),
    path('car/<int:id>', views.current_car, name='current_car'),
    path('client/<int:id>', views.current_client, name='current_client'),
    path('userclient', views.userclient, name='uscli'),
    path('personalarea', views.personalarea, name='persarea'),
    path('reg_cli', views.reg_cli, name='reg_cli'),
]
