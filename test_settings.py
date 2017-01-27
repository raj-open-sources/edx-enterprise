"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from __future__ import absolute_import, unicode_literals

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "default.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.admin",  # only used in DEBUG mode
    "enterprise",
)

MIDDLEWARE_CLASSES = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

MIDDLEWARE = MIDDLEWARE_CLASSES  # Django 1.10 compatibility - the setting was renamed

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

SESSION_ENGINE = "django.contrib.sessions.backends.file"

LOCALE_PATHS = [
    root("enterprise", "conf", "locale"),
]

MAKO_TEMPLATES = {
    "main": []
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": {
                "django.contrib.auth.context_processors.auth",  # this is required for admin
                "django.contrib.messages.context_processors.messages",
            }
        }
    },
]

PLATFORM_NAME = "Test platform"

ROOT_URLCONF = "enterprise.urls"

SECRET_KEY = "insecure-secret-key"

# Default Site id
SITE_ID = 1

EDX_API_KEY = "PUT_YOUR_API_KEY_HERE"

ENTERPRISE_ENROLLMENT_API_URL = "http://localhost:8000/api/enrollment/v1/"

COURSE_CATALOG_API_URL = "http://localhost:18381/api/v1/"

LMS_ROOT_URL = "http://localhost:8000"

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

DEFAULT_FROM_EMAIL = 'course_staff@example.com'
