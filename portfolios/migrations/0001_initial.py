# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tempo/')),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Tempo'),
        ),
        migrations.AlterUniqueTogether(
            name='portfolio',
            unique_together=set([('categorie', 'image'), ('categorie', 'index')]),
        ),
    ]