from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('user/<int:id>', views.current_user, name='current_user'),
    path('users', views.users, name='use')
]
