# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20170918_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='cv_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Nom du CV'),
        ),
    ]