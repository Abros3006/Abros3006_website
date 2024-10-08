import os
from .settings import *
from .settings import BASE_DIR
from decouple import config

SECRET_KEY = [config('SECRET_KEY')]
ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', '')]

CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ.get('WEBSITE_HOSTNAME', '')]
DEBUG = False

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_FILE_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database

connection_string = os.environ.get('AZURE_DATABASE_URL')
parameters = {pair.split('='): pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'],
        'HOST': parameters['host'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
    }
}