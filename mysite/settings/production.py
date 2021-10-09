from .base import *

DEBUG = True
SECRET_KEY = 'django-insecure-v_2h85gz3p&=*kxg6y=revgb085*_p^dce=e%rh^8h1cxv+30!'
ALLOWED_HOSTS = ['164.90.237.146', 'localhost', '127.0.0.1']

try:
    from .local import *
except ImportError:
    pass
