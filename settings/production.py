import os
import dj_database_url
from django.conf import settings
from .base import *

print 'production'
DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES
DATABASES['default'] =  dj_database_url.config()

# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # Allow all host headers
ALLOWED_HOSTS = ['localhost','my-resume-app.herokuapp.com',]

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'static'),
)