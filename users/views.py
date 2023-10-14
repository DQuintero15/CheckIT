from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("dashboard")
        else:
            messages.add_message(
                request,
                level=messages.ERROR,
                message="Nombre de usuario o contraseña incorrectos",
            )
    else:
        if request.user.is_authenticated:
            return redirect("dashboard")
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})


def signUp(request):
    return render(request, "signup.html")


def signUpClient(request):
    if request.method == "GET":
        return render(request, "signup-client.html")
