from django.contrib import admin
from django import forms

from .models import Play, PlayImage, PlayCharacter


class PlayImageInline(admin.TabularInline):
    model = PlayImage
    extra = 3


class PlayCharacterInline(admin.TabularInline):
    model = PlayCharacter
    extra = 5


class PlayAdminForm(forms.ModelForm):
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text=str(Play._meta.get_field('short_description').help_text),
        label=str(
            Play._meta.get_field('short_description').verbose_name
        ).capitalize(),
    )

    class Meta:
        model = Play
        fields = [
            'name', 'author', 'director', 'premiere_date', 'image_preview',
            'short_description', 'full_description',
        ]


class PlayModelAdmin(admin.ModelAdmin):
    form = PlayAdminForm
    inlines = [PlayCharacterInline, PlayImageInline, ]

admin.site.register(Play, PlayModelAdmin)