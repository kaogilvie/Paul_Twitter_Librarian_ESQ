"""
Django settings for djangopaul project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_environ_variable("PAUL_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Application definition

INSTALLED_APPS += ()

MIDDLEWARE_CLASSES += ( )

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'paul', #this is incorrect
        'USER': 'postgres',
        'PASSWORD': get_environ_variable("PAUL_POSTGRES"),
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
