# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_personalinformation_cv_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='career_profile',
            field=models.TextField(null=True, verbose_name='Résumé de la carrière actuelle'),
        ),
    ]