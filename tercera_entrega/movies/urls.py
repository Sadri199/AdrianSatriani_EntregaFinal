from django.contrib import admin
from django.urls import path
from movies.views import homepage, testing, listMovies, addMovies

app_name = 'movies'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('test/', testing, name="testing"),
    path('listmovies/', listMovies, name="listMovies"),
    path("addmovies/<name>/<plot>/<mainActor>/<year>/", addMovies, name="addMovies"),
]