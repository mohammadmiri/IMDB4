# -*- coding: utf-8 -*-

from .models import Movie,Genre,KeyWord, Teaser, Post, Act, CriticCriticism, \
    UserCriticism, Avamel, Award, TypeOfMovie, StatusOfMovie, Movie_Celebrity_Image

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
    model = CriticCriticism
    extra = 1

class UserCriticismInline(admin.TabularInline):
    model = UserCriticism
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

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','rate', 'year',)
    list_display_links = ('name',)
    # list_filter = (GenreFilter,)
    search_fields = ['name']
    ordering = ('name',)
    inlines = [  StatusOfMovieInline, TypeOfMovieInline, TeaserInline, ActInline, AgentInline, AwardInline,
                CriticCriticismInline, UserCriticismInline, postInline , ]




class KeyWordAdmin(admin.ModelAdmin):
    ordering = ('word',)
    search_fields = ['word',]


class MovieCelebrityImageAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ['name',]
    raw_id_fields = ('celebrities', 'movies',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(Movie_Celebrity_Image, MovieCelebrityImageAdmin)

