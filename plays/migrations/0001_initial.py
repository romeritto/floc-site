# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0004_auto_20160929_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='názov')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=255, verbose_name='autor')),
                ('premiere_date', models.DateField(verbose_name='Dátum premiéry')),
                ('image_preview', django_resized.forms.ResizedImageField(blank=True, help_text='Fotka by mala mať veľkosť 650x418 pixelov. V opačnom prípade bude veľkosť zmenená automaticky.', upload_to='plays/previews', verbose_name='fotka pre náhľad')),
                ('short_description', models.CharField(max_length=255, verbose_name='krátky popis')),
                ('full_description', models.TextField(verbose_name='dlhý popis')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('actors', models.ManyToManyField(blank=True, related_name='plays', to='actors.Actor', verbose_name='herci')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directed_shows', to='actors.Actor', verbose_name='režisér')),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name_plural': 'Inscenácie',
                'verbose_name': 'Inscenácia',
            },
        ),
        migrations.CreateModel(
            name='PlayImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', django_resized.forms.ResizedImageField(blank=True, help_text='Fotka by mala mať veľkosť 1140x642 pixelov. V opačnom prípade bude veľkosť zmenená automaticky.', upload_to='plays/gallery', verbose_name='Fotka')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='plays.Play')),
            ],
        ),
    ]
