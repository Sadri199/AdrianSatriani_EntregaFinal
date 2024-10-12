from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from movies.models import MoviesDB

def testing(request):
    return HttpResponse("This is a test!")

def homepage(request):
    return render(request, 'index.html')

def listMovies(request):
    
       ##Armar un form pa esto o algo así
    return render(request, 'listMovies.html')

def addMovies (request, name, plot, mainActor, year):
    
    newMovie = MoviesDB(name=name, plot=plot, mainActor=mainActor, year=year) ##Armar un form pa esto o algo así
    newMovie.save()
    return render (request, 'addMovies.html', {'newMovie': newMovie})