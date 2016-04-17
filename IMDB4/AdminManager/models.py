# -*- coding: utf-8 -*-

from MovieManager.models import Movie, Reviewer_Review
from UserManager.models import User

from django.db import models





class News(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='عنوان', )
    subText = models.TextField(null=True, blank=True, verbose_name='خلاصه خبر', )
    text = models.TextField(null=True, blank=True, verbose_name='متن کامل خبر', )
    source = models.TextField(null=True, blank=True, verbose_name='منبع', )
    dateUpload = models.DateTimeField(null=True, blank=True, verbose_name='زمان آپلود', )
    image = models.ImageField(upload_to='admin/News/',null=True, blank=True, verbose_name='عکس خبر', )
    CategoryChoise = (
        ('iran_cinema', 'سینمای ایران'),
        ('world_cinema', 'سینمای جهان'),
        ('honarmandan', 'هنر مندان'),
        ('TV', 'تلویزیون'),
    )
    category = models.CharField(max_length=80, null=True, blank=True, choices=CategoryChoise, verbose_name='نوع خبر', )
    relate_news = models.ManyToManyField('self', through='tag', symmetrical=False)

    def __str__(self):
        return self.title[:50]



class tag(models.Model):
    content = models.CharField(max_length=50)
    news = models.ForeignKey(News, null=True, blank=True)



class Poll(models.Model):
    text = models.TextField(null=True, blank=True, verbose_name='متن', )
    date = models.DateField(null=True, blank=True, verbose_name='تاریخ', )

    def __str__(self):
        print('text: '+self.text)
        return self.text

    def get_percentage_polling(self):
        result_polling = {}
        total_vote = 0
        setOfPollOptions = self.polloption_set.all()
        for option in setOfPollOptions:
            total_vote += option.rate
        for option in setOfPollOptions:
            if total_vote==0:
                percentage=0
            else:
                percentage = int((option.rate/total_vote)*100)
            result_polling[option]=percentage
        return (result_polling, total_vote)



class PollOption(models.Model):
    pollNumber = models.IntegerField(null=True, blank=True, verbose_name='شماره گزینه', )
    poll = models.ForeignKey(Poll, verbose_name='نظر سنجی', )
    image = models.ImageField(upload_to='admin/PollImages/', verbose_name='عکس گزینه', )
    text = models.TextField(null=True, blank=True, verbose_name='متن', )
    rate = models.IntegerField(null=True, verbose_name='رای', )

    def __str__(self):
        return self.text



class poll_user_choose(models.Model):
    poll = models.ForeignKey(Poll, blank=True)
    user = models.ForeignKey(User, blank=True)
    number = models.IntegerField()



class FavouriteCritism(models.Model):
    critism = models.OneToOneField(Reviewer_Review, verbose_name='نقد', )

    def get_favourite_critism(self):
        return self.critism.critismOfCritic



class Gallery(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام', null=True, blank=True)
    GALLERY_NUMBER_CHOICE = (
        (1,'گالری ۱'),
        (2,'گالری ۲'),
        (3,'گالری ۳'),
        (4,'گالری ۴'),
    )
    galleryNumber = models.IntegerField(null=True, blank=True, verbose_name='شماره گالری', )




