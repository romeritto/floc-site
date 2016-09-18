from django.db import models
from django.contrib.auth.models import User

from actors.managers import ActorManager


class Actor(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=u"používateľ",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    bio = models.TextField(
        verbose_name=u"biografia",
        help_text=u'Popis herca.',
    )
    photo = models.ImageField(
        verbose_name=u'fotka',
        upload_to='actors/',
        help_text=(
            u'Fotka by mala mať veľkosť 336x376 pixelov. '
            u'V opačnom prípade bude veľkosť zmenená automaticky.'
        ),
        blank=True,
    )

    objects = ActorManager()

    class Meta:
        verbose_name = u'herec'
        verbose_name_plural = u'herci'

        ordering = ['-user']

    @property
    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.full_name
