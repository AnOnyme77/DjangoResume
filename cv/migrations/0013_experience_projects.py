# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0012_education_interest_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30, verbose_name='Intitulé du job')),
                ('compagny', models.CharField(max_length=30, verbose_name='Société et ville')),
                ('dates', models.CharField(max_length=30, verbose_name='Année de début et de fin')),
                ('description', models.TextField(verbose_name='Description du poste')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.PersonalInformation')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nom du projet')),
                ('url', models.URLField(null=True, verbose_name='Lien vers le projet')),
                ('description', models.TextField(verbose_name='Description du projet')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.PersonalInformation')),
            ],
        ),
    ]
