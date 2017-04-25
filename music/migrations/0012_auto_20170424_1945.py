# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20170424_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='acces',
            field=models.CharField(choices=[('public', 'public'), ('private', 'private')], default='public', max_length=250),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default='http://www.tubefilter.com/wp-content/uploads/2016/06/youtube-music-logo.jpg', upload_to=''),
        ),
    ]
