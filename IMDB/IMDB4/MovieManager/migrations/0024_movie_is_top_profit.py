# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-03 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieManager', '0023_auto_20160419_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_top_profit',
            field=models.BooleanField(default=False, verbose_name='پر فروش هست'),
        ),
    ]
