import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =    os.path.join(BASE_DIR,'static','static_root')

STATICFILES_DIRS = (

    os.path.join(BASE_DIR,'static','static_dirs'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')


