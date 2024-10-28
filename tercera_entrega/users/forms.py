from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserCreate (UserCreationForm):   
    email = forms.EmailField()
    password1 = forms.CharField(label="Your Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    username = forms.CharField(label="Your Username")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}
    
class UserEdit (UserChangeForm):
    choose = {
        "": "",
        "Male": "Male",
        "Female": "Female",
        "TransMasc": "Trans Masculine",
        "TransFem": "Trans Femenine",
        "NonBi": "Non Binary",
        "N/A": "Prefer to not answer"
    }
    
    email = forms.EmailField()
    username = forms.CharField(label="Your Username")
    first_name = forms.CharField(label='Your Name', max_length="25")
    last_name = forms.CharField(label='Your Surname', max_length="25", required=False)
    profilePic = forms.ImageField(label="Upload a Picture!", required=False)
    birth_date = forms.DateField(label="Your Birthday", required=False, widget=forms.DateInput(attrs={"type": "date"}))
    genre = forms.ChoiceField(choices=choose, required=False)
    password = None
    
    class Meta():
        model = User
        fields = ["email", "username", "first_name", "last_name", "profilePic", "birth_date", "genre"]