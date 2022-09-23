from django.contrib import admin
from .models import *

class BudgetAdmin(admin.ModelAdmin): 
    list_display = ('owner', 'name')
    search_fields = ('owner',)
    ordering=('owner',)
    fields = ('name', 'slug', 'description', 'owner')
    
    readonly_fields = ('slug',)

    class Meta:
        model = Budget

class BudgetItemsAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price')
    search_fields = ('name',)
    ordering=('name',)
    

    class Meta:
        model = BudgetItems


admin.site.register(Budget, BudgetAdmin)
admin.site.register(Category)
admin.site.register(BudgetItems, BudgetItemsAdmin)