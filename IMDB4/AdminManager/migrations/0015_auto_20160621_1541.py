# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-21 15:41
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminManager', '0014_news_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن کامل خبر'),
        ),
    ]
