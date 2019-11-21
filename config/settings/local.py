"""Development settings."""
from .base import *  # NOQA
from .base import env

# Base
DEBUG = True
# Security
SECRET_KEY = env('DJANGO_SECRET_KEY', default='PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH')
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "192.168.8.13",
    "192.168.0.3",
    "192.168.0.4",
    "192.168.8.12",
    "192.168.8.2",
    "192.168.1.68",
    "192.168.8.4",
    "192.168.8.9",
    "192.168.1.66",
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# Email
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405

# Celery
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
