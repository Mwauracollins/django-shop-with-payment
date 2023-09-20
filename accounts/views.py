from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from accounts.models import Profile


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("products.homepage")
        else:
            messages.success(request, "Incorrect Username or Password")
    return render(request, "accounts/login")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, "Username or email already exists.")
            else:
                # Create a new user
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                messages.success(request, "Account created for " + user.username)
                return redirect('accounts:login_page')

        else:
            messages.error(request, "Invalid inputs, Passwords do not match")

    return render(request, 'accounts/register.html')


def logout_view(request):
    return HttpResponse("Logout User")


@login_required(login_url='login_page')
def dashboard(request):
    return HttpResponse("Dashboard")
