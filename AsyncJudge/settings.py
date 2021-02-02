import os
from pathlib import Path
#import django
from decouple import config


#django.setup()                                      
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "*33jplm7qjo*once-$9foaq5-1v*44rag1bclb(2tj%!m5jgor"

DEBUG = True
#SECRET_KEY = config("SECRET_KEY")

#DEBUG = config('DEBUG', default = False, cast = bool)

ALLOWED_HOSTS = ["*"]

#ROOT_URLCONF = f'{config("PROJECT_NAME")}.urls'

#WSGI_APPLICATION = f'{config("PROJECT_NAME")}.wsgi.application'
#ASGI_APPLICATION = f'{config("PROJECT_NAME")}.asgi.application'


INSTALLED_APPS = [
    'channels',
    'api',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'AsyncJudge.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'AsyncJudge.wsgi.application'
ASGI_APPLICATION = 'AsyncJudge.asgi.application'


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": 'redis://admin:adminadminadmin@3bbc5b24-2dae-4b03-8433-9bd73e7f2d4a.a618efcd6c3341158fb843970f0d7edd.databases.appdomain.cloud:32159',
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "MAX_ENTRIES": 1000
#         },
#     }
# }

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

# CELERY_BROKER_URL = 'rediss://admin:adminadminadmin@3bbc5b24-2dae-4b03-8433-9bd73e7f2d4a.a618efcd6c3341158fb843970f0d7edd.databases.appdomain.cloud:32159?ssl_cert_reqs=CERT_NONE'
# CELERY_RESULT_BACKEND = 'rediss://admin:adminadminadmin@3bbc5b24-2dae-4b03-8433-9bd73e7f2d4a.a618efcd6c3341158fb843970f0d7edd.databases.appdomain.cloud:32159?ssl_cert_reqs=CERT_NONE'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_ACKS_LATE = True

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": ["redis://admin:adminadminadmin@3bbc5b24-2dae-4b03-8433-9bd73e7f2d4a.a618efcd6c3341158fb843970f0d7edd.databases.appdomain.cloud:32159"],
#         },
#     },
# }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'judge',
#         'USER': 'postgres',
#         'PASSWORD': 'Himanshu',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }



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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
