# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0015_auto_20170424_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.CharField(default='public', max_length=250),
        ),
    ]
