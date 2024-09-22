"""
Django settings for WebSiteBase project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h*uy)p1az5@yer2v%*czb_kddyo*)ox89&n930ae6i*wfv4yf$'

DEBUG = False
ALLOWED_HOSTS = ['ambrosphere.onrender.com']
#ALLOWED_HOSTS=[]


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['ambrosphere.onrender.com', 'localhost', '127.0.0.1']



# Application definition

INSTALLED_APPS = [

    'admin_soft.apps.AdminSoftDashboardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Tutorial',
    'django_summernote',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'WebSiteBase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templets'],
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

WSGI_APPLICATION = 'WebSiteBase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'AmbroSphere',
        'USER': 'ambrosphere_user',
        'PASSWORD': 'LESieANvCCOzfxVFj4iuEk9UE4fUKXMN',
        'HOST': 'dpg-crmoht5umphs739i9mn0-a',  # Example: 'dpg-crmltft6l47c739so26g-a'
        'PORT': '5432',          # Or another port if specified by Render
    }
}
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://ambrosphere_user:LESieANvCCOzfxVFj4iuEk9UE4fUKXMN@dpg-crmoht5umphs739i9mn0-a.oregon-postgres.render.com/ambrosphere'
    )
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# Ensure this points to the correct directory for static files
STATICFILES_DIRS = [
    BASE_DIR / "static",  # This should match your project’s structure
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
JET_DEFAULT_THEME = 'default'  # Try with the default theme

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


