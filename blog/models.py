from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from tinymce.models import HTMLField
from sorl.thumbnail import ImageField

from plays.models import Play
from actors.models import Actor


class Blogpost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        verbose_name=u'názov',
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )
    author = models.ForeignKey(
        Actor,
        verbose_name=u'autor',
        related_name='blogposts',
    )
    intro = models.CharField(
        verbose_name=u'výňatok',
        help_text=u'Použite úvodné 2-3 vety z článku.',
        max_length=255,
    )
    body = HTMLField(verbose_name=u'obsah')
    image = ImageField(
        verbose_name=u'fotka',
        upload_to='blog/',
    )
    related_play = models.ForeignKey(
        Play,
        verbose_name=u'pribuzná inscenácia',
        help_text=(u'Ak sa tento príspevok viaže k jednej z inscenácií, '
                   u'vyplňte toto pole'),
        related_name='blogposts',
        null=True,
        blank=True,
    )

    posted = models.DateTimeField(
        verbose_name=u'čas pridania',
        db_index=True,
        default=timezone.now,
    )
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Článok'
        verbose_name_plural = u'Články'

        ordering = ['-posted']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
