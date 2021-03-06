# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 12:47
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CelebrityManager', '0003_auto_20160224_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='birthPlace',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='محل تولد'),
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیح'),
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='celebrity/pictures', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='workingFields',
            field=models.TextField(blank=True, null=True, verbose_name='حرفه'),
        ),
    ]
