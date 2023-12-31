"""
Django settings for hhc project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


# adminuser;'HHC4U'
# adminpass:'HHC'
# gm:pkkmzxdhpdfjsaus

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# use this if setting up on Windows 10 with GDAL installed from OSGeo4W using defaults
# if os.name == 'nt':
#     VIRTUAL_ENV_BASE = os.environ['VIRTUAL_ENV']
#     os.environ['PATH'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
#     os.environ['PROJ_LIB'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0=a+49(rf1647@9l3wuq#$m(l0&9(*-#w+0xr0f36yl152m3r1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    "phonenumber_field",
    "django.contrib.gis",
    
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

ROOT_URLCONF = 'hhc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR / 'templates'),
            str(BASE_DIR / 'static'),

        ],
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

WSGI_APPLICATION = 'hhc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = { 
    #          'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / "db.sqlite3",
    # }
             
       'default': {
       'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['db_name'],
        'USER': os.environ['db_user'],
        'PASSWORD': os.environ['db_pass'],
        'HOST': os.environ['db_host'],
        'PORT': os.environ['db_port'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

EMAIL_HOST = 'smtp.gmail.com' or None
EMAIL_HOST_USER = os.environ.get('email', None)
EMAIL_HOST_PASSWORD = os.environ.get('email_app_key',None)
EMAIL_PORT = 587
EMAIL_USE_TLS= True


PAYTM_MERCHANT_ID = 'WorldP64425807474247'
PAYTM_SECRET_KEY = 'kbzk1DSbJiV_03p5'
PAYTM_WEBSITE = 'WEBSTAGING'
PAYTM_CHANNEL_ID = 'WEB'
PAYTM_INDUSTRY_TYPE_ID = 'Retail'
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

AWS_ACCESS_KEY_ID = 'AKIAXUYDI7HIGDBBS2Q7'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'hhcbucket'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_LOCATION = 'static'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = str(BASE_DIR / 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = [str(BASE_DIR / 'static')]
# # Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
   
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''
# AWS_STORAGE_BUCKET_NAME = 'hhc-db-backup'
# AWS_QUERYSTRING_AUTH = False


# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'