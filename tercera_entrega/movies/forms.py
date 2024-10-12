from django import forms

class AddingMovie (forms.Form): #I wanted to make a dropdown with a Genre value but it was too hard and i prefer to leave it for the next project.
    
    name = forms.CharField(max_length=50)
    plot = forms.CharField(max_length=50, required=False)
    main_actor = forms.CharField(max_length=20)
    year = forms.IntegerField(min_value=1950)
    
class SearchMovie (forms.Form):
    
    name = forms.CharField(max_length=50, required=False)