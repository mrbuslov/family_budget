from unicodedata import category
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from family_budget.forms import BudgetAddForm, BudgetItemAddForm, CategoryAddForm
from django.http import HttpResponseRedirect
from family_budget.models import Budget, BudgetItems, Category
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required




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
        form = BudgetItemAddForm()
        category_form = CategoryAddForm()

        context = {
            'budget':budget,
            'categories':categories,
            'budget_items': budget_items,
            'form':form,
            'category_form':category_form,
        }
        return render(request, 'budget/budget.html', context)
    else:
        return redirect('family_budget:index')


@login_required(login_url='/login/')
def add_budget_item(request):
    if request.is_ajax():
        budget_item_id = request.POST.get('budget_item_id', None)
        BudgetItems.objects.get(id=int(budget_item_id)).delete()
        return JsonResponse(data={
            'response': 'deleted',
        })

    if request.method == 'POST':
        form = BudgetItemAddForm(request.POST)
        if form.is_valid(): form.save()    
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = BudgetItemAddForm()
        return render(request, 'budget/add_budget_item.html', {'form':form})


@login_required(login_url='/login/')
def add_category(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid(): form.save()    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='/login/')
def add_budget(request):
    if request.method == 'POST':
        form = BudgetAddForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)    
            post.owner = request.user
            post.save()
        return redirect('family_budget:index')
    else:
        form = BudgetAddForm()
        return render(request, 'budget/add_budget.html', {'form':form})
