from decimal import Decimal
from django.db import models

from actors.models import Actor
from plays.models import Play
from .managers import ShowManager


class Show(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(
        verbose_name=u'miesto',
        max_length=255,
    )
    play = models.ForeignKey(
        Play,
        verbose_name=u'inscenácia',
        related_name='shows'
    )
    start_time = models.DateTimeField(verbose_name=u'čas začiatku')
    price = models.DecimalField(
        verbose_name=u'cena',
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
            ' (' +
            self.start_time.strftime('%b %d %Y %H:%M') +
            ')'
        )

