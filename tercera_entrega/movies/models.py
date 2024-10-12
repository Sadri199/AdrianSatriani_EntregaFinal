from django.db import models

# Create your models here.
class MoviesDB (models.Model):
    name = models.CharField(max_length=50)
    plot = models.CharField(max_length=50)
    main_actor = models.CharField(max_length=20)
    year = models.IntegerField()
    
    def __str__(self):
        return f"""Movie: {self.name} \n
Plot: {self.plot} \n
Main Actor: {self.main_actor} \n
Year of Release: {self.year}\n"""    