from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import MoviesDB 

class AddingMovie (forms.Form): #I wanted to make a dropdown with a Genre value but it was too hard and i prefer to leave it for the next project.
    
    name = forms.CharField(max_length=50, min_length=5)
    plot = forms.CharField(max_length=100, min_length=5, required=False)
    main_actor = forms.CharField(max_length=20, min_length=4, validators=[RegexValidator(regex="^[a-zA-Z ]+$", message="Enter letters", code="invalid value")])
    year = forms.IntegerField(min_value=1950, max_value=2030)
    
    def clean_name (self): #This only works for "views.addMovies"
        name = self.cleaned_data["name"]
        if MoviesDB.objects.filter(name=name).exists():
            raise ValidationError("A movie with that name was already found! Cannot create it.")
        return name
    
    def clean_main_actor(self): #This only works for "views.addMovies"
        return self.cleaned_data["main_actor"].title()
    
class SearchMovie (forms.Form):
    
    name = forms.CharField(max_length=50, required=False)
    
class EditMovie (AddingMovie): #Empty class, just so it looks better on the code itself.
    ...
    
    def clean_name (self):
        name = self.cleaned_data["name"]
        return name