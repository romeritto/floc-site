from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
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
    })

    return env
