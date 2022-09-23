import uuid
from django.db import models
from account.models import Account




class Budget(models.Model):
    name = models.CharField(max_length=2000, verbose_name='Name', unique=True)
    slug = models.SlugField(null=True, blank=True, max_length=150, unique = True,verbose_name='Link', default=str(uuid.uuid4()).replace('-',''))
    description = models.TextField(max_length=5500, null=True, blank=True, verbose_name='Description') 
    owner = models.ForeignKey(Account,null=True, on_delete=models.CASCADE, verbose_name='Owner', blank=True)

    def __str__(self):
        return self.name
    
    # Changing our model for the admin panel
    class Meta:
        verbose_name_plural='Budgets'
        verbose_name= 'Budget'
        ordering=['name']


    def get_total_money_movement(self):
        income = 0
        expense = 0
        for budget_item in BudgetItems.objects.filter(budget=self):
            if budget_item.price > 0: income += budget_item.price
            else: expense += budget_item.price
        return [income, expense]

    



class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Name')
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, verbose_name='Budget')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'
        verbose_name= 'Category'
        ordering=['name']


class BudgetItems(models.Model):
    name = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Name')
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=20)
    description = models.TextField(max_length=5500, null=True, blank=True, verbose_name='Description') 
    added = models.DateTimeField(auto_now_add=True, verbose_name='Added ad' )
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, verbose_name='Budget')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    
    CURRENCY_CHOICES = (
        ('$', 'Dollar'),
        ('€', 'Euro'),
    )
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default='usd')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Budget Items'
        verbose_name= 'Budget Item'
        ordering=['name']

