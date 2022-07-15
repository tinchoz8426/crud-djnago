from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from AppMembers.forms import RegisterUserForm

# Create your views here.
def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Bienvenido"))
            return redirect("Index")
        else:
            messages.error(request, ("Hubo un error"))
            return redirect("Login")
    return render(request, "authentication/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Has cerrado tu sesión"))
    return redirect('Index')

def regiter_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Regristo exitoso"))
            return redirect('Index')
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/register.html', {"form":form})