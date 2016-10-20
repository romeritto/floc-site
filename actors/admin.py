from django.contrib import admin
from django.contrib.auth.models import User
from django_reverse_admin import ReverseModelAdmin
from django import forms

from .models import Actor, Quote


class QuoteAdminForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text=str(Quote._meta.get_field('text').help_text)
    )

    class Meta:
        model = Quote
        fields = ['author', 'text']


class QuoteAdmin(admin.ModelAdmin):
    form = QuoteAdminForm


class ActorModelAdmin(ReverseModelAdmin):

    inline_type = 'tabular'
    inline_reverse = [
        ('user', {'fields': ['username', 'first_name', 'last_name', 'is_active']}),
    ]
    fields = ['bio', 'jobs', 'photo']

admin.site.register(Actor, ActorModelAdmin)

admin.site.register(Quote, QuoteAdmin)
