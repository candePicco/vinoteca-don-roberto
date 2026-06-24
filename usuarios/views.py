from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import RegistroForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
    else:
        form = RegistroForm()

    return render(request, "registration/register.html", {"form": form})


class LoginUsuarioView(LoginView):
    template_name = "registration/login.html"


def logout_usuario(request):
    logout(request)
    return redirect("home")