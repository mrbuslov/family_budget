from django.shortcuts import render
from rest_framework import generics, permissions
from family_budget.models import *
from . import serializers
from account.models import Account
import api.permissions as overrided_permissions


class UserList(generics.ListAPIView): # UserList provides read-only access (via get) to a list of users
    queryset = Account.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView): # UserDetail - to one user
    queryset = Account.objects.all()
    serializer_class = serializers.UserSerializer


# ListCreateAPIView and RetrieveUpdateDestroyAPIView are the most common API method handlers: get and put for a list (ListCreateAPIView) 
# and get, update and delete for a single entity (RetrieveUpdateDestroyAPIView).
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [overrided_permissions.IsOwner]



class BudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = serializers.BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = serializers.BudgetSerializer
    permission_classes = [overrided_permissions.IsOwner]



class BudgetItemsList(generics.ListCreateAPIView):
    queryset = BudgetItems.objects.all()
    serializer_class = serializers.BudgetItemsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BudgetItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BudgetItems.objects.all()
    serializer_class = serializers.BudgetItemsSerializer
    permission_classes = [overrided_permissions.IsOwner]