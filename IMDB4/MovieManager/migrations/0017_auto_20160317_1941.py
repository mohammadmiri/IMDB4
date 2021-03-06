# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieManager', '0016_statusofmovie_is_red'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='posts',
            field=models.ManyToManyField(through='MovieManager.Post', to='UserManager.UserIMDB', verbose_name='پست ها'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManager.UserIMDB', verbose_name='کاربر'),
        ),
    ]
