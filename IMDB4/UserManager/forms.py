from .models import UserIMDB
from MovieManager.models import Genre, Movie
from CelebrityManager.models import Celebrity

from django.contrib.auth.models import User
from django import forms
from django.db.models import Model

import datetime

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

    def save(self):
        user = UserIMDB.objects.create()
        user.username = self.username
        user.password = self.password
        user.email = self.email
        user.birthday = datetime.date(year=self.birthday_year, month=self.birthday_month, day=self.birthday_day)
        user.profession = self.profession
        self.add_favourite_genre(self.action, 'action', user)
        self.add_favourite_genre(self.animation, 'animation', user)
        self.add_favourite_genre(self.biography, 'biography', user)
        self.add_favourite_genre(self.comedy, 'comedy', user)
        self.add_favourite_genre(self.romantic, 'romantic', user)
        self.add_favourite_genre(self.science_fiction, 'science_fiction', user)
        self.add_favourite_genre(self.short, 'short', user)
        self.add_favourite_genre(self.trailer, 'trailer', user)
        self.add_favourite_genre(self.fantasy, 'fantasy', user)
        self.add_favourite_genre(self.historical, 'historical', user)
        self.add_favourite_genre(self.horror, 'horror', user)
        self.add_favourite_genre(self.musical, 'musical', user)
        self.add_favourite_genre(self.criminal, 'criminal', user)
        self.add_favourite_genre(self.documentary, 'documentary', user)
        self.add_favourite_genre(self.dram, 'dram', user)
        self.add_favourite_genre(self.military, 'military', user)
        self.add_favourite_genre(self.social, 'social', user)
        self.splitter_adder_movie(self.favourite_movies, user)
        self.splitter_adder_actor(self.favourite_actors, user)
        self.splitter_adder_director(self.favourite_directors, user)
        user.aboutMe = self.about_me
        # saving
        user.save()



    def add_favourite_genre(self, genre:bool, name:str, user:UserIMDB):
        if genre is True:
            genre = Genre.objects.get(name = name)
            user.favouriteGenre.add(genre)

    def splitter_adder_movie(self,string:str, user:UserIMDB):
        movie_names = string.split('-')
        for name in movie_names:
            try:
                movie = Movie.objects.get(name=name)
                user.favouriteMovie.add(movie)
            except Model.DoesNotExist:
                pass
            except Model.MultipleObjectsReturned:
                pass

    def splitter_adder_actor(self, string:str, user:UserIMDB):
        celebrity_names = string.split('-')
        for name in celebrity_names:
            try:
                celebrity = Celebrity.objects.get(name=name)
                user.favouriteActor.add(celebrity)
            except Model.DoesNotExist:
                pass
            except Model.MultipleObjectsReturned:
                pass

    def splitter_adder_director(self, string:str, user:UserIMDB):
        celebrity_names = string.split('-')
        for name in celebrity_names:
            try:
                celebrity = Celebrity.objects.get(name=name)
                user.favouriteDirector.add(celebrity)
            except Model.DoesNotExist:
                pass
            except Model.MultipleObjectsReturned:
                pass




