from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_pass = request.POST["confirm_password"]

        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect("/accounts/register/")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Eamil already taken")
                return redirect("/accounts/register/")
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                user.save()
                print("user created")
        else:
            messages.info(request, "Password not match")
            return redirect("/accounts/register/")
        return redirect("/accounts/login")
    else:
        return render(request, "register.html")


def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info("Invalid Credential")
            redirect("login/")

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
