from django.shortcuts import render, redirect

from family_budget.models import Budget




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
        return render(request, 'budget/budget.html', {'budget':budget})
    else:
        return redirect('family_budget:index')