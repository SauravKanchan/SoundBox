# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_auto_20170425_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='is_favorite',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AlterField(
            model_name='songs',
            name='is_favorite',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
