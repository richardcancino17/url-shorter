from .base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'urlshorterdb',
        'USER': 'psql',
        'PASSWORD': 'psql',
        'HOST': 'db',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
APPSECRET_PROOF = False
