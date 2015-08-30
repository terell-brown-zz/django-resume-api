import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kby933tj&bte3*_a+vah(z(&@qhk3mbv5^ru4w-q1d)px(pa16'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL ='/login/'
LOGIN_REDIRECT_URL = '/resume/index'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'builder',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'resume_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["/".join((BASE_DIR,"resume_app/templates")),
                "/".join((BASE_DIR,"builder/templates"))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'resume_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT =   '/home/ubuntu/Apps/Django/resume_app/src/static/static_root/'
STATIC_ROOT =    os.path.join(BASE_DIR,'static','static_root')

STATICFILES_DIRS = (
    #'/home/ubuntu/Apps/Django/resume_app/src/static/static_dirs/',
    os.path.join(BASE_DIR,'static','static_dirs'),
)
MEDIA_URL = '/media/'
#MEDIA_ROOT = '/home/ubuntu/Apps/Django/resume_app/src/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')

PRODUCTION_MODE = True
if PRODUCTION_MODE == True:
    import os
    import dj_database_url
    from django.conf import settings

    import os
    
    DEBUG = False
    TEMPLATE_DEBUG = True
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_app.settings")
    DATABASES = settings.DATABASES

    ## service error (500)
    DATABASES['default'] =  dj_database_url.config()

    print DATABASES
    print DATABASES['default']
    # # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # # Allow all host headers
    ALLOWED_HOSTS = ['localhost','stormy-depths-4606.herokuapp.com',]
    
    # # Static asset configuration
    # import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
         os.path.join(BASE_DIR, 'static'),
    )
