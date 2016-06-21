# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 17:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CelebrityManager', '0001_initial'),
        ('MovieManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercriticism',
            name='userPro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserManager.UserIMDB', verbose_name=b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xa8\xd8\xb1'),
        ),
        migrations.AddField(
            model_name='typeofmovie',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
        migrations.AddField(
            model_name='teaser',
            name='movie',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teaser', to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
        migrations.AddField(
            model_name='statusofmovie',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
        migrations.AddField(
            model_name='rateuserformovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
        migrations.AddField(
            model_name='rateuserformovie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xa8\xd8\xb1'),
        ),
        migrations.AddField(
            model_name='post',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieManager.Movie', verbose_name=b'\xd9\xbe\xd8\xb3\xd8\xaa'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xa8\xd8\xb1'),
        ),
        migrations.AddField(
            model_name='movie_image',
            name='movies',
            field=models.ManyToManyField(related_name='images', to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85 \xd9\x87\xd8\xa7'),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movie_actors', through='MovieManager.Act', to='CelebrityManager.Celebrity', verbose_name=b'\xd8\xa8\xd8\xa7\xd8\xb2\xdb\x8c\xda\xaf\xd8\xb1\xd8\xa7\xd9\x86'),
        ),
        migrations.AddField(
            model_name='movie',
            name='avamel',
            field=models.ManyToManyField(related_name='movie_avamel', through='MovieManager.Avamel', to='CelebrityManager.Celebrity', verbose_name=b'\xd8\xb9\xd9\x88\xd8\xa7\xd9\x85\xd9\x84'),
        ),
        migrations.AddField(
            model_name='movie',
            name='awards',
            field=models.ManyToManyField(through='MovieManager.Award', to='CelebrityManager.Celebrity', verbose_name=b'\xd8\xac\xd9\x88\xd8\xa7\xdb\x8c\xd8\xb2'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(blank=True, to='MovieManager.Genre', verbose_name=b'\xda\x98\xd8\xa7\xd9\x86\xd8\xb1'),
        ),
        migrations.AddField(
            model_name='movie',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='MovieManager.KeyWord', verbose_name=b'\xda\xa9\xd9\x84\xd9\x85\xd8\xa7\xd8\xaa \xda\xa9\xd9\x84\xdb\x8c\xd8\xaf\xdb\x8c'),
        ),
        migrations.AddField(
            model_name='movie',
            name='posts',
            field=models.ManyToManyField(through='MovieManager.Post', to=settings.AUTH_USER_MODEL, verbose_name=b'\xd9\xbe\xd8\xb3\xd8\xaa \xd9\x87\xd8\xa7'),
        ),
        migrations.AddField(
            model_name='criticcriticism',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
        migrations.AddField(
            model_name='award',
            name='celebrity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CelebrityManager.Celebrity', verbose_name=b'\xd8\xa8\xd8\xa7\xd8\xb2\xdb\x8c\xda\xaf\xd8\xb1'),
        ),
        migrations.AddField(
            model_name='award',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
        migrations.AddField(
            model_name='avamel',
            name='celebrity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name=b'agent', to='CelebrityManager.Celebrity', verbose_name=b'\xd8\xa8\xd8\xa7\xd8\xb2\xdb\x8c\xda\xaf\xd8\xb1'),
        ),
        migrations.AddField(
            model_name='avamel',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name=b'agent', to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
        migrations.AddField(
            model_name='act',
            name='celebrity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CelebrityManager.Celebrity', verbose_name=b'\xd8\xa8\xd8\xa7\xd8\xb2\xdb\x8c\xda\xaf\xd8\xb1'),
        ),
        migrations.AddField(
            model_name='act',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85'),
        ),
    ]