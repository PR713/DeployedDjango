from pathlib import Path

from . import env

# noinspection PyUnresolvedReferences
# flake8: noqa


PROJECT_NAME = "flashcard_workshop"

BASE_DIR = Path(__file__).parents[2]
APPS_DIR = BASE_DIR.joinpath(PROJECT_NAME)

SECRET_KEY = env("DJANGO_SECRET_KEY", "")

DEBUG = True

ALLOWED_HOSTS = []

# ------------- APPS -------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_spectacular",
    "debug_toolbar",
    "django_extensions",
    "corsheaders",
]

LOCAL_APPS = [
    "flashcard_workshop.accounts.apps.AccountsConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------- MIDDLEWARES -------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "djangorestframework_camel_case.middleware.CamelCaseMiddleWare",
]

# ------------- URLS -------------
ROOT_URLCONF = "flashcard_workshop.urls"
WSGI_APPLICATION = "flashcard_workshop.wsgi.application"

# ------------- TEMPLATES -------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [APPS_DIR.joinpath("templates")],
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

STATICFILES_DIRS = (BASE_DIR.joinpath("commons"),)

# ------------- PASSWORDS -------------
AUTH_USER_MODEL = "accounts.CustomUser"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]

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

# ------------- INTERNALIZATION -------------
LANGUAGE_CODE = "en"

LANGUAGES = (
    ("pl", "Polish"),
    ("en", "English"),
)

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = (BASE_DIR.joinpath("locale"),)

# ------------- STATIC -------------
STATIC_URL = env.str("DJANGO_STATIC_URL", default="/static/")
STATIC_ROOT = BASE_DIR.joinpath("public")

# ------------- MEDIA -------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")

# ------------- DEBUG TOOLBAR ------------
INTERNAL_IPS = [
    "127.0.0.1",
]

# ------------- REST FRAMEWORK ------------
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
}
SPECTACULAR_SETTINGS = {
    "TITLE": "FlashCard Workshop API",
    "DESCRIPTION": "",
    "CAMELIZE_NAMES": False,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
        "drf_spectacular.hooks.postprocess_schema_enums",
    ],
}

CORS_URLS_REGEX = r"^/api/.*$"
