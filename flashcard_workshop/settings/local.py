from . import env
from .base import *

SECRET_KEY = "secret_key"

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "flashcard_workshop"),
        "USER": env("POSTGRES_USER", "flashcard_workshop"),
        "PASSWORD": env("POSTGRES_PASSWORD", "flashcard_workshop"),
        "HOST": env("POSTGRES_HOST", "localhost"),
        "PORT": env("POSTGRES_PORT", "5432"),
    }
}

CORS_ALLOW_ALL_ORIGINS = True
