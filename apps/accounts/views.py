from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (RegisterForm,LoginForm)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'accounts/home.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    context = {'form': form}
    return render(request,'accounts/register.html',context)

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Login successful')
                return redirect('dashboard')
            else:
                messages.error(request,'Invalid email or password')
    context = {'form': form}

    return render(request,'accounts/login.html',context)


@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')


def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfully')

    return redirect('login')