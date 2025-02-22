from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Base directory of the project

SECRET_KEY = 'django-insecure-your-secret-key-here'  # Secret key for the Django application

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = []  # List of allowed hosts for the application

INSTALLED_APPS = [  # Applications installed in the Django project
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
]

MIDDLEWARE = [  # Middleware components for processing requests and responses
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media.urls'  # URL configuration for the project

TEMPLATES = [  # Template settings for rendering HTML
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_media.wsgi.application'  # WSGI application for deployment

DATABASES = {  # Database configuration for the project
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [  # Validators for user passwords
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

LANGUAGE_CODE = 'en-us'  # Default language code for the application

TIME_ZONE = 'UTC'  # Default time zone for the application

USE_I18N = True  # Enable internationalization

USE_TZ = True  # Enable timezone support

STATIC_URL = 'static/'  # URL for serving static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directories to search for static files

MEDIA_URL = 'media/'  # URL for serving media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory for storing uploaded media files

LOGIN_REDIRECT_URL = 'profile'  # Redirect URL after successful login
LOGOUT_REDIRECT_URL = 'home'  # Redirect URL after logout

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default field type for auto-generated primary keys
