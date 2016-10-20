from django import forms
from django.contrib import admin
from django.db import models

from .models import Blogpost


class BlogpostAdminForm(forms.ModelForm):
    intro = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text=str(Blogpost._meta.get_field('intro').help_text)
    )

    class Meta:
        model = Blogpost
        fields = ['title', 'author', 'intro', 'body', 'image', 'related_play']


class BlogpostAdmin(admin.ModelAdmin):
    form = BlogpostAdminForm

admin.site.register(Blogpost, BlogpostAdmin)