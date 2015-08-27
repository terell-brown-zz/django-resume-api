import os
import dj_database_url
from django.conf import settings





DEBUG = False
TEMPLATE_DEBUG = True
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_app.settings")
DATABASES = settings.DATABASES
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['stormy-depths-4606.herokuapp.com',]

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


