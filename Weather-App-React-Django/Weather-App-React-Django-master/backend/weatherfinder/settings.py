"""
Django settings for weatherfinder project.

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# rename backend for clarity
BACKEND_DIR = BASE_DIR

# from 'backend' directory, frontend's path = '../frontend'
FRONTEND_DIR = os.path.abspath(os.path.join(BACKEND_DIR, '..', 'frontend'))

# Add static files directory to serve JS and CSS for frontend react app
# Static files directory = 'frontend/build/static'
STATICFILES_DIRS = [os.path.join(FRONTEND_DIR, 'build', 'static')]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3p109@z8(_&9a4%sz#3f@&d38n*2@!&!nro0o2(rwjiv(4(c=s'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# Run with "DJANGO_ENV=development ./manage.py runserver" for development
DEBUG = os.environ.get('DJANGO_ENV') == 'development'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # Whitenoise allows to take advantage of the staticfiles contrib app and its ecosystem.
    # We can serve static files with WhiteNoise and cache them with CDN for performance.
    'whitenoise.runserver_nostatic',

    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise middleware
    # With a couple of lines of config WhiteNoise allows your web app to 
    # serve its own static files, making it a self-contained unit that can be
    # deployed anywhere without relying on nginx, Amazon S3 or any other external 
    # service. (Especially useful on Heroku, OpenShift and other PaaS providers.)
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'weatherfinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(FRONTEND_DIR, 'build')],
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

WSGI_APPLICATION = 'weatherfinder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

STATIC_ROOT = os.path.join(BACKEND_DIR, 'static')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'

# Serve static files with WhiteNoise and cache them
WHITENOISE_ROOT = os.path.join(FRONTEND_DIR, 'build', 'root')

