from .base import *

DEBUG = False

if os.getcwd() == '/app':
    import dj_database_url
    DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
    }
    # Honor the 'X-Forwarded-Proto' header for request.is_secure().
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # Allow all host headers.
    ALLOWED_HOSTS = ['crash-course1.herokuapp.com']

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