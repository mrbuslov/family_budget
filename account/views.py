from django.shortcuts import render, redirect, render
from account.forms import ProfileEditForm
from account.services import *

from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def user_login(request):
    if request.user.is_authenticated:
        return redirect('family_budget:index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = authenticate(email=email, password=password)
            except:
                return redirect('account:login')
                
            if user is not None:
                login(request, user)
                if 'next' in request.POST: return redirect(request.POST.get('next'))
                # return redirect('account:profile')
                return redirect('family_budget:index')
            else:  
                return render(request, 'account/login.html')
        else:  
            return render(request, 'account/login.html')

def user_logout(request):
    logout(request)
    return redirect('family_budget:index')



def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Account.objects.filter(email=email).exists():
            try: user = authenticate(email=email, password=password)
            except: pass                

            if user is not None:
                login(request, user)
                if 'next' in request.POST: return redirect(request.POST.get('next'))
                return redirect('family_budget:index')
                
        user = register_user(email, password)
        login(request, user)
        return render(request, 'account/registration_success.html', {'email':email})
    else:
        return render(request, 'account/registration.html')




@login_required(login_url='/login/')
def profile(request):
    account = Account.objects.get(pk=request.user.pk) 
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=account)
        if form.is_valid():
            form.save()    
        return redirect('account:profile')

    
    form = ProfileEditForm(instance=account)
    return render(request, 'account/profile.html', {'form':form,})
    
