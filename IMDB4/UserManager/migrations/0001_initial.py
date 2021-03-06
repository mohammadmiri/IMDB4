# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 17:40
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MovieManager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CelebrityManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPassToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.BigIntegerField(verbose_name=django.contrib.auth.models.User)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserIMDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True, verbose_name=b'')),
                ('birthday', models.DateField(null=True, verbose_name=b'\xd8\xaa\xd9\x88\xd9\x84\xd8\xaf')),
                ('picture', models.ImageField(null=True, upload_to=b'user/pictures', verbose_name=b'\xd8\xb9\xda\xa9\xd8\xb3')),
                ('profession', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'\xd8\xad\xd8\xb1\xd9\x81\xd9\x87')),
                ('aboutMe', models.TextField(blank=True, null=True, verbose_name=b'\xd8\xaf\xd8\xb1\xd8\xa8\xd8\xa7\xd8\xb1\xd9\x87 \xd9\x85\xd9\x86')),
                ('hasProAccount', models.BooleanField(default=False, verbose_name=b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xa8\xd8\xb1 \xd9\x88\xdb\x8c\xda\x98\xd9\x87')),
                ('expireTimeToAccountPro', models.DateField(null=True, verbose_name=b'\xd8\xb2\xd9\x85\xd8\xa7\xd9\x86 \xd8\xa8\xd8\xa7\xd9\x82\xdb\x8c \xd9\x85\xd8\xa7\xd9\x86\xd8\xaf\xd9\x87 \xd8\xaa\xd8\xa7 \xd8\xa7\xd8\xaa\xd9\x85\xd8\xa7\xd9\x85 \xd8\xa7\xd8\xb9\xd8\xaa\xd8\xa8\xd8\xa7\xd8\xb1')),
                ('favouriteActor', models.ManyToManyField(related_name='user_like_as_actor', to='CelebrityManager.Celebrity', verbose_name=b'\xd8\xa8\xd8\xa7\xd8\xb2\xdb\x8c\xda\xaf\xd8\xb1\xd8\xa7\xd9\x86 \xd9\x85\xd9\x88\xd8\xb1\xd8\xaf \xd8\xb9\xd9\x84\xd8\xa7\xd9\x82\xd9\x87')),
                ('favouriteDirector', models.ManyToManyField(related_name='user_like_as_director', to='CelebrityManager.Celebrity', verbose_name=b'\xda\xa9\xd8\xa7\xd8\xb1\xda\xaf\xd8\xb1\xd8\xaf\xd8\xa7\xd9\x86\xd8\xa7\xd9\x86 \xd9\x85\xd9\x88\xd8\xb1\xd8\xaf \xd8\xb9\xd9\x84\xd8\xa7\xd9\x82\xd9\x87')),
                ('favouriteGenre', models.ManyToManyField(to='MovieManager.Genre', verbose_name=b'\xda\x98\xd8\xa7\xd9\x86\xd8\xb1 \xd9\x87\xd8\xa7\xdb\x8c \xd9\x85\xd9\x88\xd8\xb1\xd8\xaf \xd8\xb9\xd9\x84\xd8\xa7\xd9\x82\xd9\x87')),
                ('favouriteMovie', models.ManyToManyField(related_name='in_favourite_movie', to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85 \xd9\x87\xd8\xa7\xdb\x8c \xd9\x85\xd9\x88\xd8\xb1\xd8\xaf \xd8\xb9\xd9\x84\xd8\xa7\xd9\x82\xd9\x87')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userIMDB', to=settings.AUTH_USER_MODEL, verbose_name=b'')),
                ('watch_list', models.ManyToManyField(related_name='in_watch_list', to='MovieManager.Movie')),
            ],
        ),
    ]
