from django.db import models
from django.contrib.auth import get_user_model

from .utils import first_and_last_name_to_username


class ActorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('user')
