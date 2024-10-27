from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from users.forms import UserCreate
from users.models import Extras

def register (request):
    
    form = UserCreate()
    if request.method == "POST":
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("movies:homepage")
    return render (request, "users/register.html", {"form": form})

def loginIn (request):
    
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            Extras.objects.get_or_create(user=user)
            
            return redirect("movies:homepage")
    return render (request, "users/login.html", {"form": form})
