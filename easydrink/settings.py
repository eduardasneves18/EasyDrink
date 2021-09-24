from pathlib import Path
import environ
import datetime
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#3)9h1ucmdu804#hcms@&5ozk6b%vl-ooz4)g8g4)sumiu10kk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'products',
    'carts',
    'discounts',
    'users',
    'search',
    'pages',
    'payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'easydrink.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [   BASE_DIR /  'templates'],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'easydrink.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/




# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

STATIC_URL = 'pages/static/'
MEDIA_URL = 'static/images/'

STATICFILES_DIRS =[ 
    os.path.join(BASE_DIR, 'pages/static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')#Run on terminal 'python manage.py collectstatic' this command line will bring all the static files when we come to production to a specified directory already set, on settings.py. 


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY': 'ERROR'
}

AUTHENTICATION_BACKENDS = (
    
    # Django
    'django.contrib.auth.backends.ModelBackend',
)

#Custom user model
AUTH_USER_MODEL = "users.User"


#Send e-mail
GMAIL_CONTA = "testeseduarda@gmail.com"
GMAIL_FROM = "testeseduarda@gmail.com"
GMAIL_SENHA = 'testes_entra21'
GMAIL_SMTP= 'smtp.gmail.com: 587'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=4400),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

CART_SESSION_ID = "cart"
CART_ITEM_MAX_QUANTITY = 100
