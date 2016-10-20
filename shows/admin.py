from django.contrib import admin
from django import forms

from .models import Show


class ShowModelForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text=str(Show._meta.get_field('description').help_text),
        label=str(
            Show._meta.get_field('description').verbose_name
        ).capitalize(),
    )

    class Meta:
        model = Show
        fields = [
            'play', 'location', 'location_verbose', 'description',
            'start_time', 'price',
        ]


class ShowModelAdmin(admin.ModelAdmin):
    form = ShowModelForm

admin.site.register(Show, ShowModelAdmin)
