"""
Django local settings for joyceful project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from .base import *
import os



DATABASE_PATH = os.path.join(PROJECT_DIR, 'joyceful.db')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG






# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}




EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

