# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-10 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=30, null=True, unique=True)),
                ('class_field', models.CharField(blank=True, db_column='CLASS', max_length=30, null=True)),
                ('latitude', models.TextField(blank=True, db_column='LATITUDE', null=True)),
                ('longitude', models.TextField(blank=True, db_column='LONGITUDE', null=True)),
                ('map', models.CharField(blank=True, db_column='MAP', max_length=30, null=True)),
                ('elev', models.TextField(blank=True, db_column='ELEV', null=True)),
            ],
            options={
                'db_table': 'FEATURES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Flowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(blank=True, db_column='GENUS', max_length=30, null=True)),
                ('species', models.CharField(blank=True, db_column='SPECIES', max_length=30, null=True)),
                ('comname', models.CharField(blank=True, db_column='COMNAME', max_length=30, null=True, unique=True)),
            ],
            options={
                'db_table': 'FLOWERS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=30, null=True)),
                ('person', models.CharField(blank=True, db_column='PERSON', max_length=30, null=True)),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=30, null=True)),
                ('sighted', models.DateField(blank=True, db_column='SIGHTED', null=True)),
            ],
            options={
                'db_table': 'SIGHTINGS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(unique=True)),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('hashid', models.IntegerField(db_column='hashID')),
            ],
            options={
                'db_table': 'USERS',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='users',
            unique_together=set([('username', 'hashid')]),
        ),
        migrations.AlterUniqueTogether(
            name='sightings',
            unique_together=set([('name', 'person', 'location', 'sighted')]),
        ),
    ]
