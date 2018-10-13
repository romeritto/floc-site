from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.urls import reverse
from tinymce.models import HTMLField

from actors.managers import ActorManager, QuoteManager


class Actor(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=u'používateľ',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    jobs = models.CharField(
        verbose_name=u'úlohy',
        help_text=u'Vymenujte úlohy daného človeka. Napr. Režisér a herec',
        max_length=255,
        default=u'Herec',
    )
    bio = HTMLField(
        verbose_name=u'biografia',
        help_text=u'Popis herca. Použite 300-400 znakov.',
    )
    photo = ResizedImageField(
        verbose_name=u'fotka',
        help_text=(
            u'Fotka by mala mať veľkosť 336x376 pixelov. '
            u'V opačnom prípade bude veľkosť zmenená automaticky.'
        ),
        upload_to='actors/',
        size=[336, 376],
        crop=['middle', 'center'],
    )

    objects = ActorManager()

    class Meta:
        verbose_name = u'Herec'
        verbose_name_plural = u'Herci'

        ordering = ['user']

    @property
    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.user.save()
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('actors:actor-list')+'#'+self.user.username


class Quote(models.Model):
    author = models.ForeignKey(Actor, on_delete=models.CASCADE, verbose_name=u'autor')
    text = models.CharField(
        verbose_name=u'text',
        help_text=(
            u'Text výroku, ktorý sa zobrazí na úvodnej strane. '
            u'Maximálna dĺžka je 200 znakov',
        ),
        max_length=200,
    )

    objects = QuoteManager()

    class Meta:
        verbose_name = u'Výrok'
        verbose_name_plural = u'Výroky'

    def __str__(self):
        return self.text
