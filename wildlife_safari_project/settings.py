from pathlib import Path
import os

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-d!i-&cfxb=2bc#sy27cz-4w=)b3e&tv*0*1655onvbl8y-%n$w'
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'f55f416eeb72.ngrok-free.app',  # Keep your ngrok domain
    'wildlife-safari.onrender.com',  # Add your Render hostname
    '.onrender.com'  # Wildcard for all Render subdomains (safety net)
]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wildlife_safari_app',
    'django_daraja',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wildlife_safari_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',  # Added for {% static %}
            ],
        },
    },
]

WSGI_APPLICATION = 'wildlife_safari_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# settings.py

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'wildlife_safari_app/static'),
]

# WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Middleware (add this if missing)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Keep this where it is
    'django.contrib.sessions.middleware.SessionMiddleware',  # NEW - Must come before auth
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # NEW - Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # NEW - Required for admin messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Media files (for uploaded images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MPESA Daraja API settings (sandbox)
MPESA_ENVIRONMENT = 'sandbox'
MPESA_CONSUMER_KEY = 'AXWLaqAjwtHGPFiqa0AG7iliPv0Uc34tHAYtYICSO2AOh9HA'
MPESA_CONSUMER_SECRET = 'kkf7CUn1RO4GjJn5ENkBaUlZbdtWlfjudb3ekna03A56z5Vnd6HIoYOTSmKqx4Ef'
MPESA_SHORTCODE = '174379'
MPESA_EXPRESS_SHORTCODE = '174379'
MPESA_SHORTCODE_TYPE = 'paybill'
MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
MPESA_CALLBACK_URL = 'https://f55f416eeb72.ngrok-free.app/api/callback/'

import os
from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model

def create_superuser(sender, **kwargs):
    if os.environ.get("RENDER_CREATE_SUPERUSER") == "1":
        User = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "allan")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "allan@gmail.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "allan123456")
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' created successfully.")

post_migrate.connect(create_superuser)
