import os
import sys


sys.path.insert(0, '..')

PROJECT_ROOT = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_pgfulltext',
        'USER': os.environ.get('POSTGRES_USER', 'test_pgfulltext'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'test_pgfulltext'),
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = ()

SECRET_KEY = 'di!n($kqa3)nd%ikad#kcjpkd^uw*h%*kj=*pm7$vbo6ir7h=l'
INSTALLED_APPS = (
    'djorm_pgfulltext',
    'tests',
)

import django
if django.VERSION >= (1, 6):
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
else:
    TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'
