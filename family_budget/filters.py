import django_filters
from django.forms.widgets import TextInput
from .models import Budget, BudgetItems
from django.db.models import Q


class BudgetFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="published", lookup_expr='gte')
    # end_date = DateFilter(field_name="published", lookup_expr='lte')
    # price = django_filters.NumericRangeFilter(field_name='price', lookup_expr='range')

    date = django_filters.DateRangeFilter(field_name="added", empty_label=None)
    title_content = django_filters.CharFilter(field_name='name', method='title_content_filter', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Name or description'}))


    # income_from = django_filters.NumberFilter(field_name='price', method='price_filter_more') # lookup_expr='gte'
    # income_to = django_filters.NumberFilter(field_name='price', method='price_filter_less') #  lookup_expr='lte'
    class Meta:
        model = Budget
        fields = ['title_content', 'date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(BudgetFilter, self).__init__(*args, **kwargs)

        
    # def price_filter_more(self, queryset, name, value):        
    #     budgets_list = []
    #     for budget in Budget.objects.filter(owner=self.user):
    #         total_income = 0
    #         for budget_item in BudgetItems.objects.filter(budget=budget, price__gte = 0):
    #             total_income += budget_item.price
    #         if budget not in budgets_list and total_income >= value: budgets_list.append(budget.id)
        
    #     return Budget.objects.filter(id__in=budgets_list)

    # def price_filter_less(self, queryset, name, value):       
    #     budgets_list = []
    #     for budget in Budget.objects.filter(owner=self.user):
    #         total_income = 0
    #         for budget_item in BudgetItems.objects.filter(budget=budget, price__lte = 0):
    #             total_income += budget_item.price
    #         if budget not in budgets_list and total_income <= value: budgets_list.append(budget.id)
        
    #     return Budget.objects.filter(id__in=budgets_list)

    def title_content_filter(self, queryset, name, value):
        return Budget.objects.filter(Q(name__icontains=value) | Q(description__icontains=value))

