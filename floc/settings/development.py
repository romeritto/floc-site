import os

from floc.settings.base import *

DEBUG = True

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

INSTALLED_APPS += [
    'debug_toolbar',
]


MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

# Django debug toolbar setup

DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = ('127.0.0.1', )
