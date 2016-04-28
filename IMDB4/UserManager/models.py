# -*- coding: utf-8 -*-

from CelebrityManager.models import Celebrity

from django.db import models
from django.contrib.auth.models import User

import datetime


class UserIMDB(models.Model):

    user = models.OneToOneField(User, blank=True, null=True)
    name = models.CharField(max_length=80, null=True, blank=True, verbose_name='نام', )
    birthday = models.DateField(null=True, verbose_name='تولد', )
    picture = models.ImageField(null=True, blank=True, upload_to="user/pictures", verbose_name='عکس', )
    profession = models.CharField(max_length=100, null=True, blank=True, verbose_name='حرفه', )
    favouriteGenre = models.ManyToManyField("MovieManager.Genre", verbose_name='ژانر های مورد علاقه', )
    favouriteActor = models.ManyToManyField(Celebrity, related_name='user_like_as_actor', verbose_name='بازیگران مورد علاقه', )
    favouriteDirector = models.ManyToManyField(Celebrity, related_name='user_like_as_director', verbose_name='کارگردانان مورد علاقه', )
    favouriteMovie = models.ManyToManyField("MovieManager.Movie", verbose_name='فیلم های مورد علاقه', related_name='in_favourite_movie')
    aboutMe = models.TextField(null=True, blank=True, verbose_name='درباره من', )
    hasProAccount = models.BooleanField(default=False, verbose_name='کاربر ویژه', )
    expireTimeToAccountPro = models.DateField(blank=True, null=True, verbose_name='زمان باقی مانده تا اتمام اعتبار', )
    viewed_movie = models.ManyToManyField("MovieManager.Movie", verbose_name='فیلم ها دیده شده', related_name='in_viewed_movie', blank=True)

    def set_expire_time(self, now, option):
        if option == 'Monthly':
            self.expireTimeToAccountPro = now + datetime.timedelta(days=31)
        elif option == 'yearly':
            self.expireTimeToAccountPro = now + datetime.timedelta(days=365)

    def get_picture(self):
        if not self.picture :
            return "{% static 'UserManager/img/avatar.jpg' %}"
        else:
            return self.picture.url

    def __str__(self):
        return str(self.name)


# this class map a big Integer number to each user existing in project for the following reasons:
# save a new password when a user wants to reset his/her password
class ResetPassToken(models.Model):
    user = models.OneToOneField(User)
    token = models.BigIntegerField(User)


class PostForCelebrity(models.Model):
    celebrity = models.ForeignKey(Celebrity, related_name='User_Posted_on')
    user = models.ForeignKey(UserIMDB, related_name='Posted_on_Celebrity')
    content = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)


class WatchList(models.Model):
    title = models.TextField(null=True, blank=True, max_length=200, verbose_name='عنوان',)
    movie = models.ManyToManyField("MovieManager.Movie", blank=True, related_name="in_Watchlist", verbose_name='فیلم ها',)
    user = models.ForeignKey(UserIMDB, blank=True, related_name="watchlist", verbose_name='کاربران',)
