import imp
from django.forms import ModelForm
from .models import Budget, BudgetItems, Category
from django import forms

class BudgetItemAddForm(ModelForm):
    class Meta:
        model = BudgetItems
        fields=('name', 'price', 'description', 'budget', 'category', 'currency')    

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name your income/expense'}),
            'description':forms.Textarea(attrs={'placeholder':'Write some details (optional)'}),
        } 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['budget'].empty_label = None
        self.fields['category'].empty_label = None



class CategoryAddForm(ModelForm):
    class Meta:
        model = Category
        fields=('name', 'budget')    

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name your category'}),
        } 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['budget'].empty_label = None


class BudgetAddForm(ModelForm):
    class Meta:
        model = Budget
        fields=('name', 'description')    

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name your budget'}),
            'description':forms.Textarea(attrs={'placeholder':'Write some details (optional)'}),
        } 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)