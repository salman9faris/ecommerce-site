from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .form import CustomUserCreationForm




def login_view(request):
    f = CustomUserCreationForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'user enter successfully')
            return redirect('home')
        else:
            messages.warning(request, 'incorrect username and password')
            return redirect('register')
    else:
        context = {}
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect("register")


def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        if f.is_valid():
            f.save()
            user = f.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('register')

        elif request.POST['password1'] != request.POST['password2']:
            messages.warning(request, 'incorrect password')
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username already exist")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "email id already exist")


    else:

        f = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': f})

