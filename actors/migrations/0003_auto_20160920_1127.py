# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_actor_jobs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['-user'], 'verbose_name': 'Herec', 'verbose_name_plural': 'Herci'},
        ),
    ]
