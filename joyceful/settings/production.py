
"""
Django production settings for joyceful project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from .base import *
import os



DATABASE_PATH = os.path.join(PROJECT_PATH, 'joycefuldb')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG



# Application definition

INSTALLED_APPS += (
    'south',
    'photography',
    'imagekit'
)




# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'joycefuldb',
        'USER': 'joyceful',
        'PASSWORD': 'sunset8321072',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

