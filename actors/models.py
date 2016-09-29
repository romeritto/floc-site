from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

from actors.managers import ActorManager


class Actor(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=u'používateľ',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    jobs = models.CharField(
        verbose_name=u'Úlohy',
        help_text=u'Vymenujte úlohy daného človeka. Napr. Režisér a herec',
        max_length=255,
        default=u'Herec',
    )
    bio = models.TextField(
        verbose_name=u'biografia',
        help_text=u'Popis herca.',
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
        blank=True,
    )

    objects = ActorManager()

    class Meta:
        verbose_name = u'Herec'
        verbose_name_plural = u'Herci'

        ordering = ['-user']

    @property
    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.user.save()
        return super().save(*args, **kwargs)
