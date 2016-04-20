from .models import UserIMDB
from MovieManager.models import Genre, Movie
from CelebrityManager.models import Celebrity

from django.contrib.auth.models import User
from django import forms
from django.db.models import Model

import datetime

class UserIMDBForms(forms.Form):

    username = forms.CharField(max_length=50, label='نام کاربری', )
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, label='رمز', )
    re_password = forms.CharField(max_length=30, widget=forms.PasswordInput, label='تکرار رمز', )
    email = forms.EmailField(label='ایمیل', )
    first_name = forms.CharField(max_length=50, label='نام', )
    last_name = forms.CharField(max_length=50, label='نام خانودگی', )
    birthday_year = forms.IntegerField(label='سال', required=False)
    birthday_month = forms.IntegerField(label='ماه', required=False)
    birthday_day = forms.IntegerField(label='روز', required=False)
    profession = forms.CharField(max_length=100, label='حرفه', required=False)
    # favourite genres
    action = forms.BooleanField(label='اکشن', initial=False, required=False)
    animation = forms.BooleanField(label='انیمیشن', initial=False, required=False)
    biography =forms.BooleanField(label='بیوگرافی', initial=False, required=False)
    comedy = forms.BooleanField(label='کمدی', initial=False, required=False)
    romantic = forms.BooleanField(label='عاشقانه', initial=False, required=False)
    science_fiction = forms.BooleanField(label='علمی و تخیلی', initial=False, required=False)
    short = forms.BooleanField(label='کوتاه', initial=False, required=False)
    trailer = forms.BooleanField(label='تریلر', initial=False, required=False)
    fantasy = forms.BooleanField(label='فانتزی', initial=False, required=False)
    historical = forms.BooleanField(label='تاریخی', initial=False, required=False)
    horror = forms.BooleanField(label='ترسناک', initial=False, required=False)
    musical = forms.BooleanField(label='موزیکال', initial=False, required=False)
    criminal = forms.BooleanField(label='جنایی', initial=False, required=False)
    documentary = forms.BooleanField(label='مستند', initial=False, required=False)
    dram = forms.BooleanField(label='درام', initial=False, required=False)
    military = forms.BooleanField(label='جنگی',  initial=False, required=False)
    social = forms.BooleanField(label='اجتماعی', initial=False, required=False)
    # end of favourite genres
    favourite_movies = forms.TextInput()
    favourite_actors = forms.TextInput()
    favourite_directors = forms.TextInput()
    about_me = forms.Textarea()

    def save(self):
        djangoUser = User()
        user = UserIMDB.objects.create()
        djangoUser.username = self.cleaned_data['username']
        djangoUser.password = self.cleaned_data['password']
        djangoUser.email = self.cleaned_data['email']
        user.user = djangoUser
        user.birthday = datetime.date(year=self.cleaned_data['birthday_year'], month=self.cleaned_data['birthday_month'], day=self.cleaned_data['birthday_day'])
        user.profession = self.cleaned_data['profession']
        self.add_favourite_genre(self.cleaned_data['action'], 'action', user)
        self.add_favourite_genre(self.cleaned_data['animation'], 'animation', user)
        self.add_favourite_genre(self.cleaned_data['biography'], 'biography', user)
        self.add_favourite_genre(self.cleaned_data['comedy'], 'comedy', user)
        self.add_favourite_genre(self.cleaned_data['romantic'], 'romantic', user)
        self.add_favourite_genre(self.cleaned_data['science_fiction'], 'science_fiction', user)
        self.add_favourite_genre(self.cleaned_data['short'], 'short', user)
        self.add_favourite_genre(self.cleaned_data['trailer'], 'trailer', user)
        self.add_favourite_genre(self.cleaned_data['fantasy'], 'fantasy', user)
        self.add_favourite_genre(self.cleaned_data['historical'], 'historical', user)
        self.add_favourite_genre(self.cleaned_data['horror'], 'horror', user)
        self.add_favourite_genre(self.cleaned_data['musical'], 'musical', user)
        self.add_favourite_genre(self.cleaned_data['criminal'], 'criminal', user)
        self.add_favourite_genre(self.cleaned_data['documentary'], 'documentary', user)
        self.add_favourite_genre(self.cleaned_data['dram'], 'dram', user)
        self.add_favourite_genre(self.cleaned_data['military'], 'military', user)
        self.add_favourite_genre(self.cleaned_data['social'], 'social', user)
        self.splitter_adder_movie(self.favourite_movies, user)
        self.splitter_adder_actor(self.favourite_actors, user)
        self.splitter_adder_director(self.favourite_directors, user)
        user.aboutMe = self.about_me
        # saving
        user.save()



    def add_favourite_genre(self, genre:bool, name:str, user:UserIMDB):
        print('genre:'+str(genre))
        if genre is True:
            try:
                genre = Genre.objects.get(name = name)
                user.favouriteGenre.add(genre)
            except:
                pass

    def splitter_adder_movie(self,string, user:UserIMDB):
        print('movies: '+str(string))
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




