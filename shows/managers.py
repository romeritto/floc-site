from django.db import models
from django.utils import timezone


class ShowManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().select_related('play')

    def upcoming(self):
        return self.filter(start_time__gte=timezone.now().date())

    def past(self):
        return self.filter(start_time__lt=timezone.now().date())
