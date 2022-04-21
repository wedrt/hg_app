from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Kill, Player, Package
from django.contrib.auth.models import User


def index(request, submit_kill_form=None, submit_package_form=None):
    if submit_kill_form is None:
        submit_kill_form = SubmitKill(user=request.user)
    if submit_package_form is None:
        submit_package_form = SubmitPackage(user=request.user)

    player_lives = request.user.player.lives

    return render(request=request, template_name='hg_app/index.html', context=locals())


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


def submit_kill(request):
    assert request.method == "POST"

    submit_kill_form = SubmitKill(request.POST, user=request.user)
    Kill.objects.create(
        victim=Player.objects.get(id=submit_kill_form.data['victim']),
        murderer=request.user.player,
        stealth_kill=submit_kill_form.data.get('stealth_kill', False)
    )
    messages.info(request, f"Kill zadán.")
    return index(request, submit_kill_form=submit_kill_form)


def submit_package(request):
    assert request.method == "POST"

    submit_package_form = SubmitPackage(request.POST, user=request.user)

    package = Package.objects.get(id=submit_package_form.data['package_id'])
    package.picked_up = True
    package.save()

    messages.info(request, f"Balíček zadán.")
    return index(request, submit_package_form=submit_package_form)
