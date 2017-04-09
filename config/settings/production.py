# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''
from os.path import join
import os
from .common import *

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# INSTALLED_APPS
INSTALLED_APPS = Common.INSTALLED_APPS
# END INSTALLED_APPS

# SECRET KEY
SECRET_KEY = env('SECRET_KEY')
# END SECRET KEY

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
# END SITE CONFIGURATION

INSTALLED_APPS += ("gunicorn", )


# EMAIL
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL',
                         default='ankieta <noreply@prezydent.siecobywatelska.pl>')
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='[ankieta] ')
SERVER_EMAIL = values.Value()
# END EMAIL

# TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
# END TEMPLATE CONFIGURATION

# Your production stuff: Below this line define 3rd party library settings
MEDIA_ROOT = join(os.path.dirname(BASE_DIR), '../media')
RAVEN_CONFIG = {
    'dsn': env('RAVEN_DSN'),
}
INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
