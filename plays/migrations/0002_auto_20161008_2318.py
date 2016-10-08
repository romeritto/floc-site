# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0004_auto_20160929_1244'),
        ('plays', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Meno postavy')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actors.Actor')),
            ],
        ),
        migrations.AlterModelOptions(
            name='playimage',
            options={'ordering': ['pk'], 'verbose_name': 'Fotka pre inscenáciu', 'verbose_name_plural': 'Fotky pre inscenáciu'},
        ),
        migrations.RemoveField(
            model_name='play',
            name='actors',
        ),
        migrations.AddField(
            model_name='play',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='plays', through='plays.PlayCharacter', to='actors.Actor', verbose_name='herci'),
        ),
        migrations.AddField(
            model_name='playcharacter',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plays.Play'),
        ),
    ]