from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Extras(models.Model):
    choose = {
        "": "",
        "Male": "Male",
        "Female": "Female",
        "TransMasc": "Trans Masculine",
        "TransFem": "Trans Femenine",
        "NonBi": "Non Binary",
        "N/A": "Prefer to not answer"
    }
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=50, choices=choose, blank=True, null=True)
    profilePic = models.ImageField(upload_to="pfpics", blank=True, null=True)
