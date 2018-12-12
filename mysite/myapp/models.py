# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Features(models.Model):
    location = models.CharField(db_column='LOCATION', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    latitude = models.TextField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longitude = models.TextField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    map = models.CharField(db_column='MAP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    elev = models.TextField(db_column='ELEV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'FEATURES'


class Flowers(models.Model):
    genus = models.CharField(db_column='GENUS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='SPECIES', max_length=30, blank=True, null=True)  # Field name made lowercase.
    comname = models.CharField(db_column='COMNAME', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'FLOWERS'


class Sightings(models.Model):
    name = models.CharField(db_column='NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    person = models.CharField(db_column='PERSON', max_length=30, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sighted = models.TextField(db_column='SIGHTED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SIGHTINGS'
        unique_together = (('name', 'person', 'location', 'sighted'),)

class Users(models.Model):
    username = models.TextField(unique=True)  # This field type is a guess.
    email = models.TextField()  # This field type is a guess.
    password = models.TextField()  # This field type is a guess.
    hashid = models.IntegerField(db_column='hashID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'USERS'
        unique_together = (('username', 'hashid'),)
