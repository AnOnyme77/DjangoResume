# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-17 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20170913_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnalinformation',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]