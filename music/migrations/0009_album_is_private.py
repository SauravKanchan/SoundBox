# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_album_acces'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]
