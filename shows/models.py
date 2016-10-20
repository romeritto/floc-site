from decimal import Decimal
from django.db import models

from actors.models import Actor
from plays.models import Play
from .managers import ShowManager


class Show(models.Model):
    id = models.AutoField(primary_key=True)
    play = models.ForeignKey(
        Play,
        verbose_name=u'inscenácia',
        related_name='shows'
    )
    location = models.CharField(
        verbose_name=u'miesto',
        help_text=u'Napr. Empírove divadlo Hlohovec',
        max_length=255,
    )
    location_verbose = models.CharField(
        verbose_name=u'celá adresa',
        help_text=u'Napr. Empírove divadlo, Koperníkova 23, 920 01 Hlohovec',
        max_length=255,
    )
    description = models.CharField(
        verbose_name=u'popis',
        help_text=u'Približne 2-3 vety, jedinečné pre každé predstavenie.',
        max_length=255,
    )
    start_time = models.DateTimeField(verbose_name=u'čas začiatku')
    price = models.DecimalField(
        verbose_name=u'cena',
        help_text=u'Pre dobrovoľné vstupné zvoľte cenu 0.',
        max_digits=6,
        decimal_places=2,
        default=Decimal(0.00),
    )

    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    class Meta:
        verbose_name = 'Vystúpenie'
        verbose_name_plural = 'Vystúpenia'

        ordering = ['-start_time']

    def __str__(self):
        return (
            self.play.name +
            ' - ' +
            self.location +
            ' (' +
            self.start_time.strftime('%b %d %Y %H:%M') +
            ')'
        )

