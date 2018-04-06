#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LimitationPolicy(models.Model):
    policy_name = models.CharField(max_length=30, verbose_name="Nom de la police")
    nb_cv = models.PositiveIntegerField(default=5, verbose_name="Nombre maximum de CV")
    can_be_translated = models.BooleanField(default=True, verbose_name="Peut être traduit")
    can_be_commented = models.BooleanField(default=True, verbose_name="Peut être commenté")

    def __str__(self):
        return self.policy_name


class ResumeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, verbose_name="Nom d'utilisateur")
    is_main_user = models.BooleanField(default=False, verbose_name="Utilisateur principal")

    def have_limitations(self):
        return False

    def __str__(self):
        return self.username


class LimitedResumeUser(ResumeUser):
    limitation_policy = models.ForeignKey("LimitationPolicy",
                                          verbose_name="Politique de limitation",
                                          on_delete=models.DO_NOTHING)

    def have_limitations(self):
        return False if self.user.is_superuser else True
    

class ResumePartView(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de visite")
    part = models.CharField(max_length=30, verbose_name="Partie du CV")
    resume = models.ForeignKey('PersonalInformation',
                               on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + " : " + self.resume.cv_name + " : " + self.part


class ResumeView(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de visite")
    resume = models.ForeignKey('PersonalInformation',
                               on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + " : " + self.resume.cv_name


class Skill(models.Model):
    name = models.CharField(max_length=30, verbose_name="Domaine de compétence")
    level = models.PositiveIntegerField(verbose_name="Pourcentage de compétence")
    cv = models.ForeignKey('PersonalInformation',
                           on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nom du projet")
    url = models.URLField(verbose_name="Lien vers le projet", null=True)
    description = models.TextField(verbose_name="Description du projet")
    cv = models.ForeignKey('PersonalInformation',
                           on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=30, verbose_name="Intitulé du job")
    compagny = models.CharField(max_length=30, verbose_name="Société et ville")
    dates = models.CharField(max_length=30, verbose_name="Année de début et de fin")
    description = models.TextField(verbose_name="Description du poste")
    cv = models.ForeignKey('PersonalInformation',
                           on_delete=models.CASCADE)

    def __str__(self):
        return self.dates + " - " + self.compagny


class Education(models.Model):
    name = models.CharField(max_length=30, verbose_name="Intitulé du diplôme")
    institution = models.CharField(max_length=30, verbose_name="Institution d'obtention")
    dates = models.CharField(max_length=30, verbose_name="Année de début et de fin")
    cv = models.ForeignKey('PersonalInformation',
                           on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name="Langue")
    level = models.CharField(max_length=30, verbose_name="Niveau dans la langue")
    cv = models.ForeignKey('PersonalInformation',
                           on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nom de l'intérêt")
    cv = models.ForeignKey('PersonalInformation',
                           on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PersonalInformation(models.Model):
    user = models.ForeignKey("ResumeUser", null=True, verbose_name="Utilisateur lié", on_delete=models.DO_NOTHING)
    cv_name = models.CharField(max_length=30, verbose_name="Nom du CV", null=True)
    name = models.CharField(max_length=30, verbose_name="Nom")
    last_name = models.CharField(max_length=30, verbose_name="Prénom")
    mobile_phone = models.CharField(max_length=40, verbose_name="Téléphone portable")
    email = models.EmailField(verbose_name="Adresse email")
    position = models.CharField(max_length=50, verbose_name="Job actuel")
    website = models.URLField(verbose_name="Site web", null=True)
    linkedin = models.URLField(verbose_name="LinkedIn", null=True)
    twitter_username = models.CharField(max_length=30, verbose_name="Nom d'utilisateur Twitter", null=True)
    github_username = models.CharField(max_length=30, verbose_name="Nom d'utilisateur Github", null=True)
    career_profile = models.TextField(verbose_name="Résumé de la carrière actuelle", null=True)
    is_main = models.BooleanField(default=False, verbose_name="CV principal")
    auth_for_stats = models.BooleanField(default=False, verbose_name="Authentification pour les statistiques")

    def __str__(self):
        return self.last_name + " " + self.name + " " + (self.cv_name if self.cv_name is not None else "" )
