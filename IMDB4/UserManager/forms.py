from .models import UserIMDB, ListCelebrity, ListMovie
from MovieManager.models import Genre, Movie
from CelebrityManager.models import Celebrity

from django.contrib.auth.models import User
from django import forms
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist

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
    favourite_movies = forms.CharField( required=False,)
    favourite_actors = forms.CharField( required=False,)
    favourite_directors = forms.CharField( required=False,)
    about_me = forms.CharField( required=False, )

    def save(self):
        user = UserIMDB.objects.create()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        djangoUser = User.objects.create_user(username=username, password=password, email=email)
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
        print("type: "+str(type(self.cleaned_data)))
        self.splitter_adder_movie(self.cleaned_data['favourite_movies'], user)
        self.splitter_adder_actor(self.cleaned_data['favourite_actors'], user)
        self.splitter_adder_director(self.cleaned_data['favourite_directors'], user)
        user.aboutMe = self.cleaned_data['about_me']
        # saving
        djangoUser.save()
        user.save()



    def add_favourite_genre(self, genre:bool, name:str, user:UserIMDB):
        if genre is True:
            try:
                genre = Genre.objects.get(name = name)
                user.favouriteGenre.add(genre)
            except:
                pass

    def splitter_adder_movie(self,string, user:UserIMDB):
        movie_names = string.split('-')
        for name in movie_names:
            movie = Movie.objects.filter(name=name).first()
            if movie is not None:
                user.favouriteMovie.add(movie)

    def splitter_adder_actor(self, string:str, user:UserIMDB):
        celebrity_names = string.split('-')
        for name in celebrity_names:
            celebrity = Celebrity.objects.filter(name=name).first()
            if celebrity is not None:
                user.favouriteActor.add(celebrity)

    def splitter_adder_director(self, string:str, user:UserIMDB):
        celebrity_names = string.split('-')
        for name in celebrity_names:
            celebrity = Celebrity.objects.filter(name=name).first()
            if celebrity is not None:
                user.favouriteDirector.add(celebrity)



# this is a custom form which is created to save list
class MakingListForm():

    cleaned_data={}

    def is_valid(self, data:dict):
        error=''
        if data['listName'] is not None:
            error='list name is null'
            return error
        elif data['type'] is not None:
            error='type of list is null'
            return error
        elif data['names'] is not None:
            error='names field is null'
            return error
        self.cleaned_data=data
        return 'True'

    def save(self, user):
        userIMDB = UserIMDB.objects.filter(user=user).first()
        newList = None
        if self.cleaned_data['type']=='movie':
            newList=ListMovie.objects.create()
        else:
            pass
        newList.date=datetime.date.today()
        newList.title=self.cleaned_data['listName']
        newList.user=userIMDB
        newList.save()

    def splitter_adder_celebrity(self, string:str, list:ListCelebrity):
        celebrity_names=string.split('-')
        for name in celebrity_names:
            celebrity=Celebrity.objects.filter(name=name).first()
            if celebrity is not None:
                list.celebrity.add(celebrity)

    def splitter_adder_movies(self, string:str, list:ListMovie):
        movies_names=string.split('-')
        for name in movies_names:
            movie=Movie.objects.filter(name=name).first()
            if movie is not None:
                list.movie.add(movie)


