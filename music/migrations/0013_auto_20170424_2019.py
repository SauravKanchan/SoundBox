# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20170424_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='keep_this_album_private',
            new_name='keep_this_album_as_private',
        ),
    ]
