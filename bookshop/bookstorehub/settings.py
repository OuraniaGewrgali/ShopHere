from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-αλλαξε-με-δικο-σου"
DEBUG = True
ALLOWED_HOSTS = []   # αν βάλεις DEBUG=False, π.χ. ["127.0.0.1", "localhost"]

INSTALLED_APPS = [
    'bookapp',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store.apps.StoreConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bookstorehub.urls"
WSGI_APPLICATION = "bookstorehub.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "store" / "templates"],
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

# ---- ΣΗΜΑΝΤΙΚΟ: Βάση SQLite ----
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "el"
TIME_ZONE = "Europe/Athens"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "store" / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LOGIN_REDIRECT_URL = "store:book_list"
LOGOUT_REDIRECT_URL = "store:book_list"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "store:login"
