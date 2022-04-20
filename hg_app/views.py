from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginForm, SubmitKill
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Kill, Player
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        form = SubmitKill(request.POST)
        kill = Kill()
        kill.victim = Player.objects.get(id=form.data['victim'])
        kill.stealth_kill = form.data.get('stealth_kill', False)
        kill.save()
        current_player = Player.objects.get(user=request.user)
        print(current_player)
        current_player.kills.add(kill)
        current_player.save()
        messages.info(request, f"Kill zadán.")
        return redirect("hg_app:index")
    else:
        form = SubmitKill()
        return render(request=request, template_name='hg_app/index.html', context={'submit_kill': form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrace proběhla úspěšně.")
            return redirect("hg_app:index")
        messages.error(request, "Registrace selhala.")
    form = NewUserForm()
    return render(request=request, template_name="hg_app/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Přihlásil(a) ses jako {username}.")
                return redirect("hg_app:index")
            else:
                messages.error(request, "Nesprávné přihlašovací jméno nebo heslo.")
        else:
            messages.error(request, "Nesprávné přihlašovací jméno nebo heslo.")
    form = LoginForm()
    return render(request=request, template_name="hg_app/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Odhlášení proběhlo úspěšně")
    return redirect("hg_app:index")

# def kill_request(request):
