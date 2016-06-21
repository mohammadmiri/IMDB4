# -*- coding: utf-8 -*-



from django.db import models
# from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

import datetime


class Celebrity(models.Model):

    picture = models.ImageField(upload_to='celebrity/pictures', null=True, blank=True, verbose_name='عکس', )
    name = models.CharField(max_length=80, null=True, blank=True, verbose_name='نام', )
    workingFields = models.TextField(null=True, blank=True, verbose_name='حرفه', )
    biography = models.TextField(null=True, blank=True, verbose_name='بیوگرافی', )
    birthday = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد', )
    birthPlace = models.CharField(max_length=80, null=True, blank=True, verbose_name='محل تولد', )

    # def __str__(self):
    #     return self.name

    # is for test and should be moved to celebrity model
    # this function should return the top 4 rated movie related to specific celebrity
    @staticmethod
    def get_most_rated_film(celebrity):
        movie_actor = list(celebrity.movie_actors.all())
        movie_avamel = list(celebrity.movie_avamel.all())
        movies = movie_actor + movie_avamel
        result = []
        for movie in movies:
            if result.__len__() == 4:
                for element in result:
                    if movie.rate > element.rate:
                        element = movie
            else:
                result.append(movie)
        return result

    # return list of celebrity whose birthday is today
    # this function should be used in first page of website
    @staticmethod
    def get_born_today():
        celebrities = []
        for cele in Celebrity.objects.all():
            if cele.birthday is not None:
                if  cele.birthday.day == datetime.date.today().day and \
                        cele.birthday.month == datetime.date.today().month:
                    celebrities.append(cele)
        return celebrities

    def get_picture(self):
        if not self.picture:
            return "{% static 'UserManager/img/avatar.jpg' %}"
        else:
            return self.picture.url


class Video_Celebrity(models.Model):
    celebrity = models.ForeignKey(Celebrity)
    link = models.TextField(null=True, blank=True,)
    image = models.ImageField(upload_to='celebrity/video_images', null=True, blank=True)



