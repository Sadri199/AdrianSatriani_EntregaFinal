from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, loader
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from movies.models import MoviesDB
from movies.forms import AddingMovie, SearchMovie, EditMovie

def homepage(request): #Working
    return render(request, 'index.html')

def listMovies(request): #Working
    
    searching = SearchMovie(request.GET)
    if searching.is_valid():
        name = searching.cleaned_data.get("name")
        movies = MoviesDB.objects.filter(name__icontains=name)
    else:
        movies = MoviesDB.objects.all() #all the movies
    return render(request, "movies/listMovies.html", {"movies": movies, "form":searching})

def viewingMovie(request, id): #Working
    movie = MoviesDB.objects.get(id=id)
    return render (request, "movies/viewMovie.html", {"movie": movie})

@login_required
def editingMovie(request, id): #Working
    movie = MoviesDB.objects.get(id=id)
    
    survey = EditMovie(initial={"name": movie.name, "plot": movie.plot, "main_actor": movie.main_actor, "year": movie.year})
    
    if request.method == "POST":
        survey = EditMovie(request.POST)
        if survey.is_valid():
            movie.name = survey.cleaned_data.get("name")
            movie.plot = survey.cleaned_data.get("plot")
            movie.main_actor = survey.cleaned_data.get("main_actor")
            movie.year = survey.cleaned_data.get("year")
            movie.save()
            
            return redirect ("movies:listMovies")
        
    return render (request, "movies/editingMovie.html", {"movie": movie, "form": survey})

# @login_required
# def deleteMovie (request, id): #Working, Normal View version
#     movie = MoviesDB.objects.get(id=id)
#     movie.delete()
#     return redirect ("movies:listMovies")

class EraseMovie(LoginRequiredMixin,DeleteView): #Working, Class Based View version
    model = MoviesDB
    template_name = "movies/eraseMovies.html"
    success_url = reverse_lazy("movies:listMovies")

# @login_required
# def addMovies (request): #Working, this will have 2 different versions, Normal View and View based on Class
    
#     if request.method == "POST":
#         addForm = AddingMovie(request.POST)
        
#         if addForm.is_valid():
#             addData = addForm.cleaned_data
#             newMovie = MoviesDB.objects.get_or_create(name=addData["name"], plot=addData["plot"], main_actor=addData["main_actor"], year=addData["year"])
#             return redirect("movies:addMovies")
#     else:
#         addForm = AddingMovie() #Empty form so we you re-enter you can fill the form again.
        
#     return render (request, 'movies/addMovies.html', {"form": addForm})

class CreateMovie(LoginRequiredMixin,SuccessMessageMixin,CreateView): #Working, both version work, i'll leave this one functioning, but in order to use the first one you must edit "movies.url" and the HTMLs "index", "editingMovies" and "listMovies".
    model = MoviesDB
    template_name = "movies/addMovies.html"
    fields = ["name", "plot", "main_actor", "year"]
    success_url = reverse_lazy("movies:CreateMovie")
    success_message = "Movie added to our Database!"
    
def aboutMe (request): #Working.
    return render(request, "movies/aboutMe.html")   

def testing(request): #Working
    return render(request, 'movies/test.html')
    