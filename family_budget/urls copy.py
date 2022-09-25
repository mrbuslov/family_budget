from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='family_budget'

urlpatterns = [
    path('', views.index, name='index'),
    path('budget/<str:slug>/', views.budget, name='budget'),
    path('add_budget_item/', views.add_budget_item, name='add_budget_item'),
]
# + static(settings.STATIC_URL)