# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 17:40
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=100, verbose_name=b'\xd9\x86\xd9\x82\xd8\xb4 \xd8\xaf\xd8\xb1 \xd9\x81\xdb\x8c\xd9\x84\xd9\x85')),
                ('asli_ast', models.BooleanField(default=False, verbose_name=b'\xd8\xac\xd8\xb2 \xd8\xa8\xd8\xa7\xd8\xb2\xdb\x8c\xda\xaf\xd8\xb1\xd8\xa7\xd9\x86 \xd8\xa7\xd8\xb5\xd9\x84\xdb\x8c \xd8\xa7\xd8\xb3\xd8\xaa')),
            ],
        ),
        migrations.CreateModel(
            name='Avamel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[(b'kargardan', b'\xda\xa9\xd8\xa7\xd8\xb1\xda\xaf\xd8\xb1\xd8\xaf\xd8\xa7\xd9\x86'), (b'nevisande', b'\xd9\x86\xd9\x88\xdb\x8c\xd8\xb3\xd9\x86\xd8\xaf\xd9\x87'), (b'tahiey_konande', b'\xd8\xaa\xd9\x87\xdb\x8c\xd9\x87 \xda\xa9\xd9\x86\xd9\x86\xd8\xaf\xd9\x87'), (b'modir_tolid', b'\xd9\x85\xd8\xaf\xdb\x8c\xd8\xb1 \xd8\xaa\xd9\x88\xd9\x84\xdb\x8c\xd8\xaf'), (b'mojri_tarh', b'\xd9\x85\xd8\xaf\xdb\x8c\xd8\xb1 \xd8\xb7\xd8\xb1\xd8\xad'), (b'Dastyar_aval_kargardan', b'\xd8\xaf\xd8\xb3\xd8\xaa\xdb\x8c\xd8\xa7\xd8\xb1 \xd8\xa7\xd9\x88\xd9\x84 \xda\xa9\xd8\xa7\xd8\xb1\xda\xaf\xd8\xb1\xd8\xaf\xd8\xa7\xd9\x86'), (b'barname_riz', b'\xd8\xa8\xd8\xb1\xd9\x86\xd8\xa7\xd9\x85\xd9\x87 \xd8\xb1\xdb\x8c\xd8\xb2'), (b'modir_film_bardari', b'\xd9\x85\xd8\xaf\xdb\x8c\xd8\xb1 \xd9\x81\xdb\x8c\xd9\x84\xd9\x85 \xd8\xa8\xd8\xb1\xd8\xaf\xd8\xa7\xd8\xb1\xdb\x8c'), (b'tadvin', b'\xd8\xaa\xd8\xaf\xd9\x88\xdb\x8c\xd9\x86'), (b'tarrah_sahne_va_lebas', b'\xd8\xb7\xd8\xb1\xd8\xa7\xd8\xad \xd8\xb5\xd8\xad\xd9\x86\xd9\x87 \xd9\x88 \xd9\x84\xd8\xa8\xd8\xa7\xd8\xb3'), (b'tarrah_chehre_pardazi', b'\xd8\xb7\xd8\xb1\xd8\xa7\xd8\xad \xda\x86\xd9\x87\xd8\xb1\xd9\x87 \xd9\xbe\xd8\xb1\xd8\xaf\xd8\xa7\xd8\xb2\xdb\x8c'), (b'ahangsaz', b'\xd8\xa2\xd9\x87\xd9\x86\xda\xaf\xd8\xb3\xd8\xa7\xd8\xb2'), (b'seda_bardari', b'\xd8\xb5\xd8\xaf\xd8\xa7 \xd8\xa8\xd8\xb1\xd8\xaf\xd8\xa7\xd8\xb1'), (b'Seda_Gozari va mix', b'\xd8\xb5\xd8\xaf\xd8\xa7 \xda\xaf\xd8\xb0\xd8\xa7\xd8\xb1'), (b'akkas', b'\xd8\xb9\xda\xa9\xd8\xa7\xd8\xb3'), (b'jelvehaye_vije_meydani', b'\xd8\xac\xd9\x84\xd9\x88\xd9\x87 \xd9\x87\xd8\xa7\xdb\x8c \xd9\x88\xdb\x8c\xda\x98\xd9\x87'), (b'jelvehaye_vije_basari', b'\xd8\xac\xd9\x84\xd9\x88\xd9\x87 \xd9\x87\xd8\xa7\xdb\x8c \xd8\xa8\xd8\xb5\xd8\xb1\xdb\x8c'), (b'monshi_sahne', b'\xd9\x85\xd9\x86\xd8\xb4\xdb\x8c \xd8\xb5\xd8\xad\xd9\x86\xd9\x87'), (b'moshaver_film_name', b'\xd9\x85\xd8\xb4\xd8\xa7\xd9\x88\xd8\xb1 \xd9\x81\xdb\x8c\xd9\x84\xd9\x85 \xd9\x86\xd8\xa7\xd9\x85\xd9\x87'), (b'moshaver_honari', b'\xd9\x85\xd8\xb4\xd8\xa7\xd9\x88\xd8\xb1 \xd9\x87\xd9\x86\xd8\xb1\xdb\x8c'), (b'moshaver', b'\xd9\x85\xd8\xb4\xd8\xa7\xd9\x88\xd8\xb1')], max_length=40, null=True, verbose_name=b'\xda\xa9\xd8\xa7\xd8\xb1 \xd8\xa7\xd8\xac\xd8\xb1\xd8\xa7\xdb\x8c\xdb\x8c')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(blank=True, null=True, verbose_name=b'\xd9\x86\xd9\x88\xd8\xb9 \xd8\xac\xd8\xa7\xdb\x8c\xd8\xb2\xd9\x87')),
                ('festival', models.IntegerField(blank=True, choices=[(0, b'\xd8\xac\xd8\xb4\xd9\x86\xd9\x88\xd8\xa7\xd8\xb1\xd9\x87 \xd9\x81\xd8\xac\xd8\xb1'), (1, b'\xd8\xac\xd8\xb4\xd9\x86 \xd8\xae\xd8\xa7\xd9\x86\xd9\x87 \xd8\xb3\xdb\x8c\xd9\x86\xd9\x85\xd8\xa7')], null=True, verbose_name=b'\xd8\xac\xd8\xb4\xd9\x86\xd9\x88\xd8\xa7\xd8\xb1\xd9\x87')),
                ('date', models.DateField(blank=True, null=True, verbose_name=b'\xd8\xaa\xd8\xa7\xd8\xb1\xdb\x8c\xd8\xae')),
                ('type', models.CharField(blank=True, max_length=150, null=True, verbose_name=b'\xd9\x86\xd9\x88\xd8\xb9 \xd8\xa8\xd8\xae\xd8\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='CriticCriticism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name=b'\xd9\x85\xd8\xaa\xd9\x86')),
                ('nameOfCritic', models.CharField(blank=True, max_length=80, null=True, verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85 \xd9\x85\xd9\x86\xd8\xaa\xd9\x82\xd8\xaf')),
                ('like', models.FloatField(blank=True, null=True)),
                ('show_critic', models.BooleanField(default=False, verbose_name=b'\xd9\x86\xd8\xb4\xd8\xa7\xd9\x86 \xd8\xaf\xd8\xa7\xd8\xaf\xd9\x87 \xd8\xb4\xd9\x88\xd8\xaf')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True, null=True, upload_to=b'posters', verbose_name=b'\xd9\xbe\xd9\x88\xd8\xb3\xd8\xaa\xd8\xb1')),
                ('name', models.TextField(blank=True, null=True, verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85')),
                ('year', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xd8\xb3\xd8\xa7\xd9\x84 \xd8\xaa\xd9\x88\xd9\x84\xdb\x8c\xd8\xaf')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name=b'\xd9\x85\xd8\xaf\xd8\xaa \xd8\xb2\xd9\x85\xd8\xa7\xd9\x86')),
                ('rate', models.FloatField(blank=True, null=True, verbose_name=b'\xd8\xa7\xd9\x85\xd8\xaa\xdb\x8c\xd8\xa7\xd8\xb2')),
                ('numUserRated', models.IntegerField(blank=True, null=True, verbose_name=b'\xd8\xaa\xd8\xb9\xd8\xaf\xd8\xa7\xd8\xaf \xd8\xa7\xd9\x85\xd8\xaa\xdb\x8c\xd8\xa7\xd8\xb2 \xd8\xaf\xd9\x87\xd9\x86\xd8\xaf\xda\xaf\xd8\xa7\xd9\x86')),
                ('Summary', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name=b'\xd8\xae\xd9\x84\xd8\xa7\xd8\xb5\xd9\x87 \xd9\x81\xdb\x8c\xd9\x84\xd9\x85')),
                ('sale', models.CharField(blank=True, max_length=80, null=True, verbose_name=b'\xd9\x81\xd8\xb1\xd9\x88\xd8\xb4')),
                ('dialogue', models.TextField(blank=True, null=True, verbose_name=b'\xd8\xaf\xdb\x8c\xd8\xa7\xd9\x84\xd9\x88\xda\xaf')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'MovieImages', verbose_name=b'\xd8\xb9\xda\xa9\xd8\xb3')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name=b'\xd9\x85\xd8\xaa\xd9\x86')),
                ('date', models.DateField(verbose_name=b'\xd8\xaa\xd8\xa7\xd8\xb1\xdb\x8c\xd8\xae')),
                ('show_it', models.BooleanField(default=False, verbose_name=b'\xd9\x86\xd8\xb4\xd8\xa7\xd9\x86 \xd8\xaf\xd8\xa7\xd8\xaf\xd9\x87 \xd8\xb4\xd9\x88\xd8\xaf')),
            ],
        ),
        migrations.CreateModel(
            name='RateUserForMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(verbose_name=b'\xd8\xa7\xd9\x85\xd8\xaa\xdb\x8c\xd8\xa7\xd8\xb2')),
            ],
        ),
        migrations.CreateModel(
            name='StatusOfMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[(b'pish_tolid', b'\xd9\xbe\xdb\x8c\xd8\xb4 \xd8\xaa\xd9\x88\xd9\x84\xdb\x8c\xd8\xaf'), (b'film_bardari', b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85 \xd8\xa8\xd8\xb1\xd8\xaf\xd8\xa7\xd8\xb1\xdb\x8c'), (b'pas_tolid', b'\xd9\xbe\xd8\xb3 \xd8\xaa\xd9\x88\xd9\x84\xdb\x8c\xd8\xaf')], max_length=50, null=True, verbose_name=b'\xd9\x88\xd8\xb6\xd8\xb9\xdb\x8c\xd8\xaa')),
            ],
        ),
        migrations.CreateModel(
            name='Teaser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'Teaser/Images', verbose_name=b'\xd8\xb9\xda\xa9\xd8\xb3')),
                ('video_link', models.TextField(blank=True, null=True, verbose_name=b'\xd9\x84\xdb\x8c\xd9\x86\xda\xa9 \xd9\x88\xdb\x8c\xd8\xaf\xdb\x8c\xd9\x88')),
                ('date_uploaded', models.DateField(blank=True, null=True, verbose_name=b'\xd8\xaa\xd8\xa7\xd8\xb1\xdb\x8c\xd8\xae \xd8\xa7\xd9\xbe\xd9\x84\xd9\x88\xd8\xaf')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True, verbose_name=b'\xd9\x86\xd9\x88\xd8\xb9 \xd9\x81\xdb\x8c\xd9\x84\xd9\x85')),
            ],
        ),
        migrations.CreateModel(
            name='UserCriticism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name=b'\xd9\x85\xd8\xaa\xd9\x86')),
                ('show_it', models.BooleanField(default=False, verbose_name=b'\xd9\x86\xd8\xb4\xd8\xa7\xd9\x86 \xd8\xaf\xd8\xa7\xd8\xaf\xd9\x87 \xd8\xa8\xd8\xb4\xd9\x88\xd8\xaf')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieManager.Movie', verbose_name=b'\xd9\x81\xdb\x8c\xd9\x84\xd9\x85')),
            ],
        ),
    ]
