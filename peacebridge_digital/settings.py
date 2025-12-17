import os
from pathlib import Path
from dotenv import load_dotenv

# -------------------------------
# BASE DIR
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv(BASE_DIR / '.env')

# -------------------------------
# SECRET KEY
# -------------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-default-secret-key")

# -------------------------------
# DEBUG MODE
# -------------------------------
DEBUG = True  # Change to False in production

# -------------------------------
# Allowed Hosts
# -------------------------------
ALLOWED_HOSTS = []

# -------------------------------
# Installed Apps
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Peaceapp.apps.PeaceappConfig',  # replace with your actual app
    'django_daraja'
]

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------
# URL Configuration
# -------------------------------
ROOT_URLCONF = 'peacebridge_digital.urls'

# -------------------------------
# Templates
# -------------------------------
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # for project-wide templates
        'APP_DIRS': True,                  # look in app folders automatically
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -------------------------------
# WSGI
# -------------------------------
WSGI_APPLICATION = 'peacebridge_digital.wsgi.application'


# -------------------------------
# DATABASE (SQLite)
# -------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),  # MUST be string
    }
}

# -------------------------------
# Password Validators
# -------------------------------
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

# -------------------------------
# Internationalization
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# -------------------------------
# Static Files
# -------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# -------------------------------
# Default Auto Field
# -------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------
# Login / Logout Redirects
# -------------------------------
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'

# -------------------------------
# Daraja (MPESA) Credentials
# -------------------------------
DAR_CONSUMER_KEY = os.getenv("DAR_CONSUMER_KEY")
DAR_CONSUMER_SECRET = os.getenv("DAR_CONSUMER_SECRET")
DAR_SHORTCODE = os.getenv("DAR_SHORTCODE")
DAR_PASSKEY = os.getenv("DAR_PASSKEY")
DAR_CALLBACK_URL = os.getenv("DAR_CALLBACK_URL")
