from django.contrib import admin

from .models import Play, PlayImage, PlayCharacter


class PlayImageInline(admin.TabularInline):
    model = PlayImage
    extra = 3


class PlayCharacterInline(admin.TabularInline):
    model = PlayCharacter
    extra = 5


class PlayModelAdmin(admin.ModelAdmin):
    fields = ['name', 'author', 'director', 'premiere_date', 'image_preview',
              'short_description', 'full_description', ]
    inlines = [PlayCharacterInline, PlayImageInline, ]

admin.site.register(Play, PlayModelAdmin)