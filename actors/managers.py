from django.db import models
from django.contrib.auth import get_user_model

from .utils import first_and_last_name_to_username


class ActorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('user')

    def create_with_user(self, email, first_name, last_name, username=None, **kwargs):

        def get_valid_username():
            base_username = first_and_last_name_to_username(first_name, last_name)
            username = base_username
            counter = 0

            while User.objects.filter(username=username).exists():
                counter += 1
                username = base_username + str(counter)

                if counter > 1000:
                    raise('Too many users using the same name')

            return username

        User = get_user_model()

        if username is None:
            username = get_valid_username()

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )

        # Validation
        self.model(user=user, **kwargs).full_clean()

        return super().create(user=user, **kwargs)
