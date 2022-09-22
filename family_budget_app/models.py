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
    



class BudgetItems(models.Model):
    name = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Name')
    price = models.DecimalField(verbose_name='Price')
    description = models.TextField(max_length=5500, null=True, blank=True, verbose_name='Description') 
    added = models.DateTimeField(auto_now_add=True, verbose_name='Added ad' )
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, verbose_name='Budget')
    
    CURRENCY_CHOICES = (
        ('usd', 'Dollar'),
        ('euro', 'Euro'),
    )
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default='usd')

    def __str__(self):
        return f'{self.name} - {self.price}'

