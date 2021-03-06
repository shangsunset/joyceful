"""
Django base settings for joyceful project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

SETTINGS_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
PROJECT_DIR = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_DIR = os.path.abspath(PROJECT_DIR)

TEMPLATE_PATH = os.path.join(PROJECT_DIR, 'templates')
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)


STATIC_ROOT = os.path.join(PROJECT_DIR,'static_collected')

STATIC_URL = '/static/' # You may find this is already defined as such.

STATICFILES_DIRS = (
            os.path.join(PROJECT_DIR,'static'),


        )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['JOYCEFUL_SECRET_KEY']

ADMINS = ('yshang', 'shangsunset@gmail.com')

ALLOWED_HOSTS = ['104.236.33.114', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'photography',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'imagekit'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'joyceful.urls'

WSGI_APPLICATION = 'joyceful.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",

    # appended custom value
    'joyceful.context_processors.albums' ,

)


