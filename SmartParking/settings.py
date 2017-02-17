"""
Django settings for SmartParking project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os, socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^$sybe8l#8cd#9nd5y0e&2=*6*b$qg+&1e^li%tm_9xqnvp_#u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['smparking.pythonanywhere.com', 'localhost', '0.0.0.0']

CSRF_COOKIE_SECURE = False


# Application definition

INSTALLED_APPS = [
    # 'iotdb_link.apps.IotdbLinkConfig',
    'resources.apps.ResourcesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'mptt',
    'mptt_graph',
    'polymorphic_tree',
    'polymorphic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SmartParking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['resources.templates.admin.resources'],
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

WSGI_APPLICATION = 'SmartParking.wsgi.application'

# TODO find a way to effectively connect to pythonanywhere or local
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# Check whether MySQL production server is reachable. Otherwise connect to localhost.
# data_connect = socket.socket()
host = 'smparking.mysql.pythonanywhere-services.com'
port = '3306'
# data_connect.connect((host,int(port)))
# MySQL on PythonAnyWhere
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'smparking$smartparking',
#         'USER': 'smparking',
#         'PASSWORD': 'smp312SQL',
#         'HOST': host,
#         'PORT': port,
#     }
# }

# MySQL on localhost
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartparking',
        'USER': 'spadmin',
        'PASSWORD': 'spadmin',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = '/static/'

# Number of GET/POST parameters allowed at once (it allow to delete up to such number of rows in database)

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# IoTdm server
IOTDM_IP = '127.0.0.1'
IOTDM_PORT = '8282'
IOTDM_SERVER = 'http://localhost:8282/'#'http://10.48.18.34:8282/'
# To connect with IoTdm handlers need to be imported in resources.apps.ResourcesConfig.ready
CHECK_IOTDM_RESPONSE = False