# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminManager', '0012_poll_user_choose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='title',
        ),
    ]