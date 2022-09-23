from django.shortcuts import render
from django.urls import path
from . import views as account_views
from django.conf import settings
app_name='account'

urlpatterns = [
    path('profile/', account_views.profile, name='profile'),
    path('login/', account_views.user_login ,name='login'),
    path('logout/', account_views.user_logout, name='logout'),
    path('registration/', account_views.registration, name='registration'),
]