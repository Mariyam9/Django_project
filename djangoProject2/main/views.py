from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AbiturientForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UniverForm
from .models import Univer, Speciality, Study, Point
from .filters import UniverFilter


def index(request):
  #  univers = index.univer_set.all()
  #  myFilter = UniverFilter(request.GET, queryset=n)
  #  #context = {'myFilter': myFilter}
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def login(request):
    return render(request, "main/login.html")


def register(request):
    form = AbiturientForm()
    if request.method == 'POST':
        form = AbiturientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    return render(request, 'main/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def uni(request):
    if request.method == "POST":
        form = UniverForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = UniverForm()
    return render(request, 'main/uni.html', {'form':form})


def show(request):
    univers = Univer.objects.all()
    return render(request,"main/show.html",{'univers':univers})


def edit(request, name):
    univer = Univer.objects.get(name=name)
    return render(request,'main/edit.html', {'univer':univer})


def update(request, name):
    univer = Univer.objects.get(name=name)
    form = UniverForm(request.POST, instance = univer)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'main.edit.html', {'univer': univer})


def destroy(request, name):
    univer = Univer.objects.get(name=name)
    univer.delete()
    return redirect("/show")