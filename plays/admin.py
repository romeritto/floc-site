from django.contrib import admin

from .models import Play, PlayImage


class PlayImageInline(admin.TabularInline):
    model = PlayImage
    extra = 3


class PlayModelAdmin(admin.ModelAdmin):
    fields = ['name', 'author', 'director', 'premiere_date', 'image_preview',
              'short_description', 'full_description', 'actors', ]
    filter_horizontal = ('actors', )
    inlines = [PlayImageInline, ]

admin.site.register(Play, PlayModelAdmin)