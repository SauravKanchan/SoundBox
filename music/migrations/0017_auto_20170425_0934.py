# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 04:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_album_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='user',
            new_name='name',
        ),
    ]
