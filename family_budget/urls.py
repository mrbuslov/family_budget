from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='family_budget'

urlpatterns = [
    path('', views.index, name='index'),
    path('budget/<str:slug>/', views.budget, name='budget'),
]
# + static(settings.STATIC_URL)