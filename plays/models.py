from django.db import models
from django_resized import ResizedImageField

from actors.models import Actor


class Play(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        verbose_name=u'názov',
        max_length=255,
        blank=False,
    )
    author = models.CharField(verbose_name=u'autor', max_length=255)
    director = models.ForeignKey(
        Actor,
        verbose_name=u'režisér',
        related_name='directed_shows',
    )
    premiere_date = models.DateField(verbose_name=u'Dátum premiéry')
    image_preview = ResizedImageField(
        verbose_name=u'fotka pre náhľad',
        help_text=(
            u'Fotka by mala mať veľkosť 650x418 pixelov. '
            u'V opačnom prípade bude veľkosť zmenená automaticky.'
        ),
        upload_to='plays/previews',
        size=[650, 418],
        crop=['middle', 'center'],
        blank=True,
    )
    short_description = models.CharField(
        verbose_name=u'krátky popis',
        max_length=255,
    )
    full_description = models.TextField(
        verbose_name=u'dlhý popis',
    )
    actors = models.ManyToManyField(
        Actor,
        verbose_name=u'herci',
        related_name='plays',
        blank=True,
    )

    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Inscenácia'
        verbose_name_plural = u'Inscenácie'

        ordering = ['-pk']

    def __str__(self):
        return self.name