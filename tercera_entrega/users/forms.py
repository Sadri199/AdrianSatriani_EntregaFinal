from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserCreate (UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Your Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    username = forms.CharField(label="Your Username")
    #first_name = forms.CharField(label='Name')
    #last_name = forms.CharField(label='Surname')
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}
    