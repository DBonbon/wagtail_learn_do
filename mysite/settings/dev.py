from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v_2h85gz3p&=*kxg6y=revgb085*_p^dce=e%rh^8h1cxv+30!'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['164.90.237.146', 'localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
