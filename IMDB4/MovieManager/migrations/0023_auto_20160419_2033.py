# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieManager', '0022_auto_20160419_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='sale',
            field=models.IntegerField(blank=True, null=True, verbose_name='فروش'),
        ),
    ]
