# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminManager', '0010_polloption_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='polloption',
            name='pollNumber',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره گزینه'),
        ),
    ]
