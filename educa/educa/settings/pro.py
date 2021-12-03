from .base import *

DEBUG = False

ADMINS = {
    'Adedayo A', 'madedayo@gmail.com'
}

ALLOWED_HOSTS = ['.crashcourse.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'CrashCourse',
        'USER': 'joy',
        'PASSWORD': 'impulse001',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True