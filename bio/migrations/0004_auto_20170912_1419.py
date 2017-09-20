# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_bio_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bio/')),
            ],
        ),
        migrations.AddField(
            model_name='bio',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bio',
            name='portrait',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bio.Portrait'),
        ),
    ]