# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0007_auto_20170912_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bio',
            old_name='image',
            new_name='portrait',
        ),
    ]