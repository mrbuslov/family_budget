from unicodedata import category
from django.shortcuts import render, redirect

from family_budget.models import Budget, BudgetItems, Category




def index(request):
    if request.user.is_authenticated:
        # budgets = Budget.objects.filter(owner=request.user)
        budgets = Budget.objects.select_related("owner").all()
        return render(request, 'budget/index.html', {'budgets':budgets})
    else:
        return render(request, 'budget/index.html')


def budget(request, slug):
    if Budget.objects.filter(slug=slug).exists():
        budget = Budget.objects.get(slug=slug)
        categories = Category.objects.filter(budget=budget)
        budget_items = BudgetItems.objects.filter(budget=budget).order_by('category')
        context = {
            'budget':budget,
            'categories':categories,
            'budget_items': budget_items,
        }
        return render(request, 'budget/budget.html', context)
    else:
        return redirect('family_budget:index')