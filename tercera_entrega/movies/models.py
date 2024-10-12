from django.db import models


class MoviesDB (models.Model): #I wanted to make a dropdown with a Genre value but it was too hard and i prefer to leave it for the next project.
    name = models.CharField(max_length=50)
    plot = models.CharField(max_length=100)
    main_actor = models.CharField(max_length=20)
    year = models.IntegerField()
    
    def __str__(self):
        return f'''Movie: "{self.name}" \n
Plot: "{self.plot}" \n
Main Actor: "{self.main_actor}" \n
Year of Release: "{self.year}"\n'''  