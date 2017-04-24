import os

from umap.settings.base import *   # pylint: disable=W0614,W0401

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = "the answer to life the universe and everything"
INTERNAL_IPS = ('127.0.0.1', )
ALLOWED_HOSTS = ['cartes.data.gouv.fr', 'localhost', '127.0.0.1']

DEBUG = True

ADMINS = (
    ('theophile', 'theophile.merliere@beta.gouv.fr'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'umap',
    }
}

TEMPLATES[0]['DIRS'].insert(0, os.path.join(PROJECT_DIR, "templates"))


STATICFILES_DIRS = (
    (os.path.join(PROJECT_DIR, "static")),
    ("storage", os.path.join(PROJECT_DIR, "../LeafletStorage/")),
    ("reqs", os.path.join(PROJECT_DIR, "../LeafletStorage/reqs/")),
) + STATICFILES_DIRS

WSGI_APPLICATION = 'umap.wsgi.application'

COMPRESS_ENABLED = not DEBUG
COMPRESS_OFFLINE = True

LANGUAGE_CODE = 'fr'

AUTHENTICATION_BACKENDS = (
    'cartes.oauth.DataGouvOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_DATAGOUV_KEY = os.environ.get('DATAGOUV_KEY')
SOCIAL_AUTH_DATAGOUV_SECRET = os.environ.get('DATAGOUV_SECRET')

MIDDLEWARE_CLASSES += (
    'social_django.middleware.SocialAuthExceptionMiddleware',
)
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_BACKEND_ERROR_URL = "/"

LEAFLET_STORAGE_ALLOW_ANONYMOUS = False

# This setting will exclude empty maps (in fact, it will exclude all maps where
# the default center has not been updated)
UMAP_EXCLUDE_DEFAULT_MAPS = False

# How many maps should be showcased on the main page resp. on the user page
UMAP_MAPS_PER_PAGE = 5
# How many maps should be showcased on the user page, if owner
UMAP_MAPS_PER_PAGE_OWNER = 10

SITE_URL = "http://localhost:8000"
SHORT_SITE_URL = "http://s.hort"

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }

# POSTGIS_VERSION = (2, 1, 0)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# You need to unable accent extension before using UMAP_USE_UNACCENT
# python manage.py dbshell
# CREATE EXTENSION unaccent;
UMAP_USE_UNACCENT = True

# For static deployment
STATIC_ROOT = os.path.join(PROJECT_DIR, "../.venv/umap/var/static")

# For users' statics (geojson mainly)
MEDIA_ROOT = os.path.join(PROJECT_DIR, "../.venv/umap/var/uploads")

# Default map location for new maps
LEAFLET_LONGITUDE = 2
LEAFLET_LATITUDE = 51
LEAFLET_ZOOM = 6
