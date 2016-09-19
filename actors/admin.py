from django.contrib import admin
from django.contrib.auth.models import User
from django_reverse_admin import ReverseModelAdmin

from .models import Actor


class ActorModelAdmin(ReverseModelAdmin):

    inline_type = 'tabular'
    inline_reverse = [
        ('user', {'fields': ['username', 'first_name', 'last_name', 'email']}),
    ]
    fields = ['bio', 'jobs', 'photo']

admin.site.register(Actor, ActorModelAdmin)
