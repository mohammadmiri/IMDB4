# -*- coding: utf-8 -*-

from MovieManager.models import Movie, Reviewer_Review

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
        return self.firstHeadLine[:20]



class tag(models.Model):
    content = models.CharField(max_length=50)
    news = models.ForeignKey(News, null=True, blank=True)



class Poll(models.Model):
    title = models.TextField(null=True, verbose_name='عنوان', )
    text = models.TextField(null=True, verbose_name='متن', )

    def __str__(self):
        return self.text



class PollOption(models.Model):
    poll = models.ForeignKey(Poll, verbose_name='نظر سنجی', )
    image = models.ImageField(upload_to='admin/PollImages/', verbose_name='عکس گزینه', )
    rate = models.IntegerField(null=True, verbose_name='رای', )

    def __str__(self):
        return self.image.url



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




