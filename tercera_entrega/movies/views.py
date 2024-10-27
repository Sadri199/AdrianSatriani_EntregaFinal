from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, loader
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from movies.models import MoviesDB
from movies.forms import AddingMovie, SearchMovie, EditMovie

def homepage(request): #Main page.
    return render(request, 'index.html')

def listMovies(request): #A way for users to check the Database.
    
    searching = SearchMovie(request.GET)
    if searching.is_valid():
        name = searching.cleaned_data.get("name")
        movies = MoviesDB.objects.filter(name__icontains=name)
    else:
        movies = MoviesDB.objects.all() #all the movies
    return render(request, "movies/listMovies.html", {"movies": movies, "form":searching})

def viewingMovie(request, id): #Read working
    movie = MoviesDB.objects.get(id=id)
    return render (request, "movies/viewMovie.html", {"movie": movie})

def editingMovie(request, id): #Working, needs decorators
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

def deleteMovie (request, id): #Working, needs decorators
    movie = MoviesDB.objects.get(id=id)
    movie.delete()
    messages.success(request, "Movie deleted correctly.")
    return redirect ("movies:listMovies")

def addMovies (request): #Working, needs decorators
    messages.error (request, "Error!")
    
    if request.method == "POST":
        addForm = AddingMovie(request.POST)
        
        if addForm.is_valid():
            addData = addForm.cleaned_data
            newMovie = MoviesDB.objects.get_or_create(name=addData["name"], plot=addData["plot"], main_actor=addData["main_actor"], year=addData["year"]) ##As a note, i managed to make "name" a unique field, the downside is that it crashes with a 500, i tried my best to make a pop up appear telling the user that that specific name already exists in the DB but i couldn't make it work.
            return redirect("movies:addMovies")
    else:
        addForm = AddingMovie() #Empty form so we you re-enter you can fill the form again.
        
    return render (request, 'movies/addMovies.html', {"form": addForm})
    
def aboutMe (request): #Working.
    return render(request, "movies/aboutMe.html")   

def testing(request): #Working, needs decorators
    test = f"This is a test, nothing to see here."
    return HttpResponse(test) 
    