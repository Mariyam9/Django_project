from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/login.html')

def login(request):
    userform = UserForm()
    return render(request, "main/login.html", {"form": userform})

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>You login successfully, {0}</h2>".format(email))
    else:
        userform = UserForm()
        return render(request, "main/login.html", {"form": userform})

def register(request):
    return render(request, 'main/register.html')