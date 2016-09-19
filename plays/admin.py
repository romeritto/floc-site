from django.contrib import admin

from .models import Play


class PlayModelAdmin(admin.ModelAdmin):
    fields = ['name', 'author', 'director', 'premiere_date', 'short_description',
              'full_description', 'actors', ]
    filter_horizontal = ('actors', )

admin.site.register(Play, PlayModelAdmin)