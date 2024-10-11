import os
from .settings import *
from .settings import BASE_DIR
from decouple import config

SECRET_KEY = config('SECRET_KEY')  # Changed to remove the list
ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', '')]

CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('WEBSITE_HOSTNAME', '')]
DEBUG = True

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database

connection_string = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
print("Connection String:", connection_string)
parameters = {}

if connection_string:
    pairs = connection_string.split(' ')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)  # Use maxsplit=1 to handle '=' in values
            parameters[key.strip()] = value.strip()  # Stripping whitespace
        else:
            print(f"Warning: '{pair}' is not a valid key=value pair.")

# Debugging output for parsed parameters
print("Parsed database parameters:", parameters)

# Validate required keys
required_keys = ['dbname', 'host', 'port', 'user', 'password']
for key in required_keys:
    if key not in parameters:
        raise ValueError(f"Missing required database parameter: {key}")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'],
        'HOST': parameters['host'],
        'PORT': parameters.get('port', '5432'),  # Default to 5432 if not provided
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
        'OPTIONS': {
            'sslmode': 'require',  # Set SSL mode as required
        },
    }
}

LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
           },
       },
       'root': {
           'handlers': ['console'],
           'level': 'WARNING',
       },
       'loggers': {
           'django': {
               'handlers': ['console'],
               'level': 'WARNING',
               'propagate': False,
           },
       },
   }
