from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        
    return HttpResponse("Login View")


def register_view(request):
    return HttpResponse("Sign Up view")


def logout_view(request):
    return HttpResponse("Logou User")


@login_required(login_url='login_page')
def dashboard(request):
    return HttpResponse("Dashboard")
