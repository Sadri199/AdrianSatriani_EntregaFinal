from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class MoviesDB (models.Model): #Working with both Class Based Views and Normal Views.
    
    name = models.CharField(max_length=50, unique=True, default="Slow and Relaxed", error_messages={"unique": "A movie with that name was already found! Cannot create it."})
    plot = models.CharField(max_length=100, default='2 guys go really slow in their sports cars.')
    main_actor = models.CharField(max_length=20, default="din viesel", validators=[RegexValidator(regex="^[a-zA-Z ]+$", message="Enter letters only.", code="invalid value")]) 
    year = models.IntegerField(default=1951, validators=[MinValueValidator(1950, message="Year cannot go before 1950!"), MaxValueValidator(2030, message="Year cannot go after 2030!")])
    
    def clean_year(self):
        year = self.cleaned_data["year"]
        if 1950 <= year <= 2030:
            return year
        else:
            raise ValidationError("The year must be between 1950 and 2030!")
            
       
    def save(self): #This is just so the name of the actor looks better in the DB.
        self.main_actor = self.main_actor.title()
        super(MoviesDB,self).save()
    
    def __str__(self):
        return f'''Movie: "{self.name}" \n
Year: "{self.year}" \n'''  