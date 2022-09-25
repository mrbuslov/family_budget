from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('budget/', views.BudgetList.as_view()),
    path('budget/<int:pk>/', views.BudgetDetail.as_view()),
    path('budget_items/', views.BudgetItemsList.as_view()),
    path('budget_items/<int:pk>/', views.BudgetItemsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)