from django.db import models


class BlogpostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('author', 'author__user')