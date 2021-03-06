# Add to the file global_settings.py, not the local_settings.py
# Set the default value in that file and override the value in this file

#import global_settings
from .global_settings.py import *
import os
DEBUG = True 
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    #('Rebecca Ramnauth', 'rramnauth2220@bths.edu'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'name', # Or path to database file if using sqlite3.
        'USER': 'user', # Not used with sqlite3.
        'PASSWORD': 'pass', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

PROJECT_DIR = os.path.dirname(__file__)

#Absolute URL to where the site is going to be hosted.
SITE_URL = 'http://www.bthsstem.org/2017/main/app_portal/'

#Login URL
LOGIN_URL = SITE_URL + 'accounts/login/'

# Absolute filesystem path to the directory that will hold user-uploadedfiles.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/bthsstem/public_html/2017/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/","http://example.com/media/"

MEDIA_URL = 'http://www.bthsstem.org/2017/main/media/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# ADMIN_MEDIA_PREFIX = 'http://bthsstem.org/2017/media/spons-portal/admin/'

STATIC_ROOT = '/home/bthsstem/django-projects/bthsstem-2017-Website/portal/static/'

STATIC_URL = SITE_URL + 'static/'

TEMPLATE_DIRS = (
    '/home/bthsstem/django-projects/bthsstem-2017-Website/portal/templates/',
)


STATICFILES_DIRS = (
    '/home/bthsstem/django-projects/bthsstem-2017-Website/portal/static/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

ADMIN_MEDIA_PREFIX = '/2017/main/admin/media/'

EMAIL_USE_TLS = True
EMAIL_HOST='localhost'
EMAIL_HOST_PASSWORD='GzM9N1tpqlE0'
EMAIL_HOST_USER='Rebecca Ramnauth'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
