# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20170424_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='acces',
            field=models.CharField(default='public', max_length=250),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
