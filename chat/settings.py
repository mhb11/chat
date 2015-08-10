"""
Django settings for chat project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1

print "CHECKING_HEROKU!"
ON_HEROKU = os.environ.get('ON_HEROKU')
#ON_HEROKU = '1'
#heroku config:set ON_HEROKU=1 
#heroku ps:scale web=1 to put in a dyno

#git init
#git remote add origin https://github.com/mhb11/unconnectedredditpk.git
#git pull origin master
#git add <files>
#git push origin master

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$@g26q0b_p0#r7lif^%39oj-52lhm78z#rog(*n8f_z8(-6uxw'

# SECURITY WARNING: don't run with debug turned on in production!
if ON_HEROKU == '1':
    DEBUG=True
else:
    DEBUG=True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'djangotribune',
    'crispy_forms',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',   
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'chat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'chat.wsgi.application'

CRISPY_TEMPLATE_PACK = 'uni_form'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if ON_HEROKU == '1':
# Parse database configuration from $DATABASE_URL
    import dj_database_url
    print "ON_HEROKU!"
    DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
#DATABASES['default'] = dj_database_url.config()
else:
# Parse database configuration from $DATABASE_URL
    print "NOT_ON_HEROKU!"
# DATABASES['default'] = dj_database_url.config()
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'myproject',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'myprojectuser',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Oral'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'staticfiles'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
