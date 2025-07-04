from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_EXPOSE_HEADERS = ['Content-Disposition']

CSRF_TRUSTED_ORIGINS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB', default=''),
        'USER': config('POSTGRES_USER', default=''),
        'PASSWORD': config('POSTGRES_PASSWORD', default=''),
        'HOST': config('POSTGRES_HOST', default=''),
        'PORT': config('POSTGRES_PORT', default='5432'),
    }
}
