from rest_framework import serializers
from account.models import Account
from family_budget.models import *


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # The PrimaryKeyRelatedField represents the list of posts in this many-to-one relationship (many=True indicates that there can be more than one post).
    budgets_owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'is_admin', 'is_staff', 'is_superuser', 'budgets_owner']


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    budget_items_category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    budget = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'budget', 'budget_items_category']
    
class BudgetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email') # ReadOnlyField is a class that returns data unchanged. In this case, it is used to return the field instead of the standard ID.
    budget_items_budget = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['id', 'name', 'description', 'owner', 'budget_items_budget', 'slug']
        

class BudgetItemsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = BudgetItems
        fields = ['id', 'owner', 'name', 'price', 'description', 'added', 'budget', 'category']


