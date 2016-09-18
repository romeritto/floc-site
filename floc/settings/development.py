import os

from floc.settings.base import *

DEBUG = True

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'
