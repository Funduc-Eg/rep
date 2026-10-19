import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",  # встроенная админка
    "django.contrib.auth",  # встроенная авторизация
    "django.contrib.contenttypes",  # типы контента (нужно для auth)
    "django.contrib.sessions",  # сессии
    "django.contrib.messages",  # всплывающие сообщения
    "django.contrib.staticfiles",  # статика (css/js)
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # базовая безопасность
    "django.contrib.sessions.middleware.SessionMiddleware",  # сессии
    "django.middleware.common.CommonMiddleware",  # общие правила
    "django.middleware.csrf.CsrfViewMiddleware",  # защита от CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # request.user
    "django.contrib.messages.middleware.MessageMiddleware",  # messages framework
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # движок Django
        "DIRS": [BASE_DIR / "templates"],  # где искать общие шаблоны
        "APP_DIRS": True,  # искать также в templates/ приложений
        "OPTIONS": {
            "context_processors": [  # переменные во всех шаблонах
                "django.template.context_processors.request",  # request
                "django.contrib.auth.context_processors.auth",  # user
                "django.contrib.messages.context_processors.messages",  # messages
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
AUTH_USER_MODEL = "accounts.User"  # наша модель пользователя

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # драйвер PostgreSQL
        "NAME": os.getenv("POSTGRES_DB"),  # имя БД
        "USER": os.getenv("POSTGRES_USER"),  # пользователь
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),  # пароль
        "HOST": os.getenv("POSTGRES_HOST"),  # хост
        "PORT": os.getenv("POSTGRES_PORT"),  # порт
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",  # встроенный Redis-бэкенд
        "LOCATION": os.getenv("REDIS_URL"),  # адрес Redis
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"  # сессии — в Redis
SESSION_CACHE_ALIAS = "default"  # какой кэш использовать

LANGUAGE_CODE = "ru-ru"  # русский язык
TIME_ZONE = "Europe/Moscow"  # московское время
USE_I18N = True  # включить переводы
USE_TZ = True  # хранить время с таймзоной

STATIC_URL = "static/"  # URL для статики
STATICFILES_DIRS = [BASE_DIR / "static"]  # где искать статику
MEDIA_URL = "media/"  # URL для загруженных файлов
MEDIA_ROOT = BASE_DIR / "media"  # папка для файлов

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # тип PK по умолчанию
