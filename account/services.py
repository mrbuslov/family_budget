from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Account



def register_user(email, password):
    user = Account.objects.create_user(password=password, email=email.lower())
    user.save()
    authenticate(email=email, password=password)
    return user