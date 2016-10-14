from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.template.defaultfilters import date as _date
from django.utils.timezone import template_localtime
from django.conf import settings
from sorl.thumbnail.shortcuts import get_thumbnail

from jinja2 import Environment


def startswith(str1, str2):
    return str1.startswith(str2)


def environment(**options):

    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'startswith': startswith,
        'get_thumbnail': get_thumbnail,
        '_date': _date,
        'settings': settings,
    })

    env.filters.update({
        'localtime': template_localtime,
    })

    return env
