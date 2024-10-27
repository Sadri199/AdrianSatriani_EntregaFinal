from django.db import models
from django.core.validators import RegexValidator


class MoviesDB (models.Model): #I wanted to make a RegexValidation for main_actor, but for some reason it didn't work.
    name = models.CharField(max_length=50, unique=True, default="Slow and Relaxed")
    plot = models.CharField(max_length=100, default="2 guys go really slow in their sports cars.")
    main_actor = models.CharField(max_length=20, default="Din Viesel") 
    year = models.IntegerField(default=1951)
    
    def __str__(self):
        return f'''Movie: "{self.name}" \n
Year: "{self.year}" \n'''  