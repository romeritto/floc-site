# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 13:50
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160921_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='obsah'),
        ),
    ]