from distutils.debug import DEBUG
from pathlib import Path
import os
from wsgiref.simple_server import sys_version
from environs import Env
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str(
    "SECRET_KEY",
    default="django-insecure-x0dp25v51=wfb3lo5wibvw=t32v13oof#-b(_!f@-=+293m9j-",
)

DEBUG = env.bool("DEBUG", default=True)
# DEBUG = True

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'whitenoise.runserver_nostatic',

    # new app installed
    "accounts",
    "qrCode_App",
    "qrApi",
    
    # 3rd party app
    "widget_tweaks",
    "rest_framework",
    "rest_framework.authtoken",
    "django_social_share",
    
    # "rest_framework_swagger",
    "qrcode",
    "drf_spectacular",
    "drf_yasg",
    'cloudinary',
]

# REST_FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
}

AUTH_USER_MODEL = "accounts.CustomUser"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "qrCode_Project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "qrCode_Project.wsgi.application"


DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }

    "default": env.dj_db_url("DATABASE_URL")

}
#Google recaptcha against spam bot 
GOOGLE_RECAPTCHA_SITE_KEY = '6LfsF2khAAAAAEYG6JtpaqT0YRGDCURbDUOPtPoa' 

GOOGLE_RECAPTCHA_SECRET_KEY = '6LfsF2khAAAAAOvAiIeARmstT92aUBVXRv0WTMil'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# CLOUDINARY_STORAGE={
#     'CLOUD_NAME':'dtyafclf3',
#     'API_KEY':'866113161722838',
#     'API_SECRET':'rW0QqAVEUQleXMw0RboCgLf6KrM'
# }

# DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'

# Session configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# static 
STATIC_URL = "static/"
STATIC_DIR = BASE_DIR / STATIC_URL
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))] 
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage' 

# media file
MEDIA_URL = '/media_folder/'
MEDIA_DIR= BASE_DIR /'media_folder'
MEDIA_ROOT = MEDIA_DIR

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'index'