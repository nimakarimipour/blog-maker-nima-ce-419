# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-13 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20170713_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
    ]
