from django import forms

class AddingMovie (forms.Form):
    
    name = forms.CharField(max_length=50)
    plot = forms.CharField(max_length=50, required=False)
    main_actor = forms.CharField(max_length=20)
    year = forms.IntegerField(min_value=1950)
    
class SearchMovie (forms.Form):
    
    name = forms.CharField(max_length=50, required=False)