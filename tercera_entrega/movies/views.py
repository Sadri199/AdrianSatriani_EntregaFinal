from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, loader
from django.shortcuts import render, redirect, reverse
from movies.models import MoviesDB
from movies.forms import AddingMovie, SearchMovie

def testing(request):
    test = f"This is a test, nothing to see here."
    
    return HttpResponse(test)

def homepage(request):
    return render(request, 'index.html')

def listMovies(request):
    
    searching = SearchMovie(request.GET)
    if searching.is_valid():
        name = searching.cleaned_data.get("name")
        movies = MoviesDB.objects.filter(name__icontains=name)
    else:
        movies = MoviesDB.objects.all() #all the movies
    return render(request, "listMovies.html", {"movies": movies, "form":searching})

def addMovies (request):
    
    if request.method == "POST":
        addForm = AddingMovie(request.POST)
        
        if addForm.is_valid():
            addData = addForm.cleaned_data
            newMovie = MoviesDB(name=addData["name"], plot=addData["plot"], main_actor=addData["main_actor"], year=addData["year"]) 
            newMovie.save()
            return redirect("movies:addMovies")
    else:
        addForm = AddingMovie() #Empty form
        
    return render (request, 'addMovies.html', {"form": addForm})
    
def aboutMe (request):
    return render(request, "aboutMe.html")    
    