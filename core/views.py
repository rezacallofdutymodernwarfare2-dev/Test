from django.shortcuts import render
from core.forms import *
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                message = "ورود موفقیت‌آمیز بود"
            else:
                message = "نام کاربری یا رمز عبور اشتباه است"
    else:
        form = LoginForm()

    return render(request, "core/login.html", {
        "form": form,
        "message": message
    })