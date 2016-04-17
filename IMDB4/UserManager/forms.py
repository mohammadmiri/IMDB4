from .models import UserIMDB

from django import forms

class UserIMDBForms(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    birthday_year = forms.IntegerField()
    birthday_month = forms.IntegerField()
    birthday_day = forms.IntegerField()
    profession = forms.CharField(max_length=100)
    # favourite genres
    action = forms.BooleanField()
    animation = forms.BooleanField()
    biography =forms.BooleanField()
    comedy = forms.BooleanField()
    romantic = forms.BooleanField()
    science_fiction = forms.BooleanField()
    short = forms.BooleanField()
    trailer = forms.BooleanField()
    fantasy = forms.BooleanField()
    historical = forms.BooleanField()
    horror = forms.BooleanField()
    musical = forms.BooleanField()
    criminal = forms.BooleanField()
    documentary = forms.BooleanField()
    dram = forms.BooleanField()
    military = forms.BooleanField()
    social = forms.BooleanField()
    # end of favourite genres
    favourite_movies = forms.TextInput()
    favourite_actors = forms.TextInput()
    favourite_directors = forms.TextInput()
    about_me = forms.Textarea()










