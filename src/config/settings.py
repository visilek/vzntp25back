from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv("DJANGO_SECRET_KEY"))
SECRET_KEY_FALLBACKS = []

DEBUG = str(os.getenv("DJANGO_DEBUG", "False").lower() in ["1", "true"])

ALLOWED_HOSTS = ["*"]


# Application definition
DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
]
OWN_APPS = [
    "apps.authorisation.apps.AuthorisationConfig",
    "apps.documents.apps.DocumentsConfig",
    "apps.figures.apps.FiguresConfig",
    "apps.blog.apps.BlogConfig",
]
INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + OWN_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'VZ-ntp',
    'DESCRIPTION': 'Test project',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
}

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# Database settiongs
DATABASES = {
    "default": {
        "ENGINE": str(os.getenv("DJANGO_DATABASES_DEFAULT_ENGINE")),
        "HOST": str(os.getenv("DJANGO_DATABASES_DEFAULT_HOST")),
        "PORT": str(os.getenv("DJANGO_DATABASES_DEFAULT_PORT")),
        "NAME": str(os.getenv("DJANGO_DATABASES_DEFAULT_NAME")),
        "USER": str(os.getenv("DJANGO_DATABASES_DEFAULT_USER")),
        "PASSWORD": str(os.getenv("DJANGO_DATABASES_DEFAULT_PASSWORD")),
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Authorisation and authentication
AUTH_USER_MODEL = "authorisation.CustomUser"

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# CORS headers
# CORS_ALLOWED_ORIGINS = json.loads(os.getenv('DJANGO_CORS_ALLOWED_ORIGINS'))
# CORS_ALLOW_CREDENTIALS = os.getenv('JANGO_CORS_ALLOW_CREDENTIALS', 'False').lower()=='true'


# CSRF protection
# CSRF_TRUSTED_ORIGINS = json.loads(os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS'))
# CSRF_COOKIE_AGE = int(os.getenv('DJANGO_CSRF_COOKIE_AGE'))
CSRF_COOKIE_SAMESITE = "Lax"  # SCRF policy (Strict / Lax / None)
CSRF_USE_SESSIONS = False  # Put scrf token into cookie not into session info
CSRF_COOKIE_HTTPONLY = False  # Put csrf token into cookie, not into html page code


# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# I18n
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []


# Media storage
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
