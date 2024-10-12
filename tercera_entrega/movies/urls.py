from django.contrib import admin
from django.urls import path
from movies.views import homepage, testing, listMovies, addMovies, aboutMe

app_name = 'movies'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('test/', testing, name="testing"),
    path('listmovies/', listMovies, name="listMovies"),
    path("addmovies/", addMovies, name="addMovies"),
    path("aboutme/", aboutMe, name="aboutMe"),
]