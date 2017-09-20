# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0006_auto_20170912_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='bio',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bio.Portrait'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]