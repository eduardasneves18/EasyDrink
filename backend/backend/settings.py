from pathlib import Path
import environ
import os
import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '@6p-h7#oy4unyb4+(@i&3eq(knbkvjkeyv&@*8+a%f45b@mfm1'

# 'django-insecure-dtz+me(f%+fd(8%jtse=!=nyqdtz2+l-p)i5c5d-8%9i41^^62'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # OAuth
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
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
    # 'carts',
    'users',
    'search',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        # 'drf_social_oauth2.authentication.SocialAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY': 'ERROR'
}

AUTHENTICATION_BACKENDS = (
    # Others auth providers (e.g. Google, OpenId, etc)

    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',

    # django-rest-framework-social-oauth2
    'drf_social_oauth2.backends.DjangoOAuth2',


    # Django
    'django.contrib.auth.backends.ModelBackend',
)

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# SOCIAL_AUTH_PIPELINE = {
#     'users.pipeline.update_user_social_data'
# }

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.9' 
SOCIAL_AUTH_FACEBOOK_KEY = env('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('FACEBOOK_SECRET')

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id, name, email', 'auth_type': 'rerequest'}
SOCIAL_AUTH_USER_FIELDS = ['email', 'username', 'first_name', 'password']


# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_SECRET')

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

#Custom user model
AUTH_USER_MODEL = "users.User"

# Configurações para enviar e-mails de confirmação
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT =  465
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') #utilizado para não deixar um e-mail em aberto, dificultando o envio de span por meio do mesmo.
# EMAIL_HOST_PASSWORDS = os.environ.get('EMAIL_HOST_PASSWORD')

GMAIL_CONTA = "testeseduarda@gmail.com"
GMAIL_FROM = "testeseduarda@gmail.com"
GMAIL_SENHA = 'testes_entra21'
GMAIL_SMTP= 'smtp.gmail.com: 587'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=4400),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

# estabelecendo a porta 8080 conforme foi registrado no frontend
# DEFAULT_PORT = "8080"