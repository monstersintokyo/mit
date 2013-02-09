# coding=utf-8

from mit.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'mit.settings.development.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mit_development',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '', # Set to empty string for localhost.
        'PORT': '', # Set to empty string for default.
    }
}


MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# Possibility to override some settings from local dev machine
try:
    from mit.settings.development.local_settings import *
except ImportError:
    pass
