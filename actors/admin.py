from django.contrib import admin
from django.contrib.auth.models import User
from django_reverse_admin import ReverseModelAdmin

from .models import Actor, Quote


class ActorModelAdmin(ReverseModelAdmin):

    inline_type = 'tabular'
    inline_reverse = [
        ('user', {'fields': ['username', 'first_name', 'last_name', 'is_active']}),
    ]
    fields = ['bio', 'jobs', 'photo']

admin.site.register(Actor, ActorModelAdmin)

admin.site.register(Quote)
