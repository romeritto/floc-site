import os
from decimal import Decimal
from django.utils import timezone

os.environ["DJANGO_SETTINGS_MODULE"] = "floc.settings.development"
import django
django.setup()

from shows.models import Show
from plays.models import Play
from actors.models import Actor


def populate_actors():
    Actor.objects.create_with_user(
        first_name='Jano',
        last_name='Tanko',
        email='jano@tano.com',
        bio='Dobry som',
        jobs='Reziser',
    )
    Actor.objects.create_with_user(
        first_name='Palo',
        last_name='Konto',
        email='as@tano.com',
        bio='Dobry som najviac',
    )
    Actor.objects.create_with_user(
        first_name='Rogod',
        last_name='Majselfino',
        email='jano@majselfino.com',
        bio='Dobry som najvaac',
    )


def populate_plays():
    p = Play.objects.create(
        name='Dobra hra',
        author='Papito',
        director=Actor.objects.all()[1],
        premiere_date=timezone.now(),
        short_description='short desc',
        full_description='full desc',
    )

    p.actors.add(Actor.objects.all()[2])

    p = Play.objects.create(
        name='Lepsia',
        author='Papito papu',
        director=Actor.objects.all()[0],
        premiere_date=timezone.now(),
        short_description='short desc',
        full_description='full desc',
    )

    p.actors.add(Actor.objects.all()[1])


def populate_shows():
    Show.objects.create(
        location='Empirgo',
        play=Play.objects.get(pk=1),
        start_time=timezone.now(),
    )

    Show.objects.create(
        location='Empirgo',
        play=Play.objects.get(pk=2),
        start_time=timezone.now(),
        price=Decimal(15.01),
    )

if __name__ == '__main__':
    populate_actors()
    populate_plays()
    populate_shows()
