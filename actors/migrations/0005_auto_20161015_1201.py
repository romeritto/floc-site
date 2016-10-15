# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0004_auto_20160929_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text=('Text výroku, ktorý sa zobrazí na úvodnej strane. Maximálna dĺžka je 200 znakov',), max_length=210, verbose_name='text')),
            ],
            options={
                'verbose_name_plural': 'Výroky',
                'verbose_name': 'Výrok',
            },
        ),
        migrations.AlterField(
            model_name='actor',
            name='jobs',
            field=models.CharField(default='Herec', help_text='Vymenujte úlohy daného človeka. Napr. Režisér a herec', max_length=255, verbose_name='úlohy'),
        ),
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actors.Actor', verbose_name='autor'),
        ),
    ]