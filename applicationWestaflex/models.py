# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class EnregistreProcedure(models.Model):  
    id_procedure = models.BigAutoField(primary_key=True)
    client = models.CharField(max_length=100)
    pression = models.IntegerField()
    duree =  models.IntegerField()
    marge = models.IntegerField()
    diametre = models.IntegerField()
    reference = models.CharField(max_length=20)

class Statistiques(models.Model):
    client = models.CharField(max_length=100)
    reference = models.CharField(max_length=20)
    tube_defectueux = models.IntegerField()
    tube_non_defectueux = models.IntegerField()

class ProcedureSelectionnee(models.Model):
    id_procedure = models.IntegerField()