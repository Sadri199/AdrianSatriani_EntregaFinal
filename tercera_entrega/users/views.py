from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from users.forms import UserCreate, UserEdit
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

@login_required
def myProfile (request):
    extraInfo = request.user.extras
    form = UserEdit(instance=request.user, initial={"profilePic":extraInfo.profilePic})
    
    return render (request, "users/myProfile.html", {"form": form})

@login_required
def editProfile (request):
    extraInfo = request.user.extras
    form = UserEdit(instance=request.user, initial={"profilePic":extraInfo.profilePic, "genre": extraInfo.genre, "birth_date": extraInfo.birth_date})
    
    if request.method == "POST":
        form = UserEdit(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            
            new_pic = form.cleaned_data.get("profilePic")
            extraInfo.profilePic = new_pic if new_pic else extraInfo.profilePic
            extraInfo.birth_date = form.cleaned_data.get("birth_date")
            extraInfo.genre = form.cleaned_data.get("genre")
            extraInfo.save()
            form.save()
            
            return redirect ("users:myProfile")
        
    return render(request, "users/editProfile.html", {"form": form})

class ChangePassword (LoginRequiredMixin, PasswordChangeView):
    template_name="users/ChangePassword.html"
    success_url=reverse_lazy("users:myProfile")