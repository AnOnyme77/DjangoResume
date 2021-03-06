# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-13 17:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnalinformation',
            name='adr_country',
            field=models.CharField(max_length=50, null=True, verbose_name='Pays'),
        ),
        migrations.AddField(
            model_name='personnalinformation',
            name='adr_street',
            field=models.CharField(max_length=50, null=True, verbose_name='Rue et num\xe9ro'),
        ),
        migrations.AddField(
            model_name='personnalinformation',
            name='adr_zipcode',
            field=models.CharField(max_length=50, null=True, verbose_name='Commune et code postal'),
        ),
        migrations.AddField(
            model_name='personnalinformation',
            name='bithdate',
            field=models.DateTimeField(default=datetime.datetime(2012, 9, 16, 0, 0), verbose_name='Date de naissance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnalinformation',
            name='email',
            field=models.CharField(default='someone@somewhere.com', max_length=40, verbose_name='Adresse email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnalinformation',
            name='mobile_phone',
            field=models.CharField(default='+32496542311', max_length=40, verbose_name='T\xe9l\xe9phone portable'),
            preserve_default=False,
        ),
    ]
