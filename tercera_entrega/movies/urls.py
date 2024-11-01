from django.contrib import admin
from django.urls import path
from movies.views import *

app_name = 'movies'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('test/', testing, name="testing"),
    path('movies/listmovies/', listMovies, name="listMovies"),
    path("movies/viewingMovie/<int:id>", viewingMovie, name="viewingMovie"),
    path("movies/editingMovie/<int:id>", editingMovie, name="editingMovie"),
    path("movies/deleteMovie/<int:pk>", EraseMovie.as_view(), name="EraseMovie"), 
    path("movies/addmovies/", CreateMovie.as_view(), name="CreateMovie"),
    path("aboutme/", aboutMe, name="aboutMe"),
]