# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0017_personalinformation_auth_for_stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='LimitationPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_cv', models.PositiveIntegerField(default=5, verbose_name='Nombre maximum de CV')),
                ('can_be_translated', models.BooleanField(default=True, verbose_name='Peut être traduit')),
                ('can_be_commented', models.BooleanField(default=True, verbose_name='Peut être commenté')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name="Nom d'utilisateur")),
                ('is_main_user', models.BooleanField(default=False, verbose_name='Utilisateur principal')),
                ('have_limitations', models.BooleanField(default=False, verbose_name='Est limité')),
            ],
        ),
        migrations.CreateModel(
            name='LimitedResumeUser',
            fields=[
                ('resumeuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cv.ResumeUser')),
                ('limitation_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.LimitationPolicy', verbose_name='Politique de limitation')),
            ],
            bases=('cv.resumeuser',),
        ),
        migrations.AddField(
            model_name='resumeuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
