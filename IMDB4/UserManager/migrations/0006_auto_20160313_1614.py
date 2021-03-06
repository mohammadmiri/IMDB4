# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieManager', '0014_auto_20160310_1848'),
        ('UserManager', '0005_auto_20160310_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=200, null=True, verbose_name='عنوان')),
                ('movie', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_Watchlist', to='MovieManager.Movie', verbose_name='فیلم ها')),
            ],
        ),
        migrations.RemoveField(
            model_name='userimdb',
            name='watch_list',
        ),
        migrations.AlterField(
            model_name='userimdb',
            name='expireTimeToAccountPro',
            field=models.DateField(blank=True, null=True, verbose_name='زمان باقی مانده تا اتمام اعتبار'),
        ),
        migrations.AlterField(
            model_name='userimdb',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='user/pictures', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='userimdb',
            name='viewed_movie',
            field=models.ManyToManyField(blank=True, related_name='in_viewed_movie', to='MovieManager.Movie', verbose_name='فیلم ها دیده شده'),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='UserManager.UserIMDB', verbose_name='کاربران'),
        ),
    ]
