# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-17 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_personnalinformation_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnalinformation',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='CV principal'),
        ),
    ]