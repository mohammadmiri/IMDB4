# -*- coding: utf-8 -*-

from .models import Movie,Genre,KeyWord, Teaser, Post, Act, Reviewer_Review, \
    User_Review, Avamel, Award, TypeOfMovie, StatusOfMovie, Movie_Celebrity_Image, RateUserForMovie, dialogue

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _




class postInline(admin.TabularInline):
    model = Post
    extra = 1

class ActInline(admin.TabularInline):
    model = Act
    raw_id_fields = ('celebrity',)
    extra = 1

class CriticCriticismInline(admin.TabularInline):
    model = Reviewer_Review
    extra = 1

class UserCriticismInline(admin.TabularInline):
    model = User_Review
    extra = 1

class AgentInline(admin.TabularInline):
    model = Avamel
    raw_id_fields = ('celebrity',)
    extra = 1

class TeaserInline(admin.TabularInline):
    model = Teaser
    extra = 1

class AwardInline(admin.TabularInline):
    model = Award
    raw_id_fields = ('celebrity', )
    extra = 1

class StatusOfMovieInline(admin.TabularInline):
    model = StatusOfMovie

class TypeOfMovieInline(admin.TabularInline):
    model = TypeOfMovie

class DialogueInline(admin.TabularInline):
    model = dialogue
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','rate', 'year', )
    list_display_links = ('name',)
    # list_filter = (GenreFilter,)
    search_fields = ['name']
    ordering = ('name',)
    inlines = [  DialogueInline, StatusOfMovieInline, TypeOfMovieInline, TeaserInline, ActInline,
                 AgentInline, AwardInline, CriticCriticismInline, UserCriticismInline, postInline , ]

    def get_view_on_site_url(self, obj=None):
        if obj is not None:
            return
            # return "http://localhost:8000/movie/show/"+str(obj.id)
        return "http://localhost:8000/"


class KeyWordAdmin(admin.ModelAdmin):
    ordering = ('word',)
    search_fields = ['word',]


class MovieCelebrityImageAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('id', 'name',)
    ordering = ('name',)
    search_fields = ['name',]
    raw_id_fields = ('celebrities', 'movies',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(Movie_Celebrity_Image, MovieCelebrityImageAdmin)

