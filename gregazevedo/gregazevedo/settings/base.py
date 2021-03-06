# Django settings for project project.
import os
from environ import Env, Path
import pathlib
from django.core.exceptions import ImproperlyConfigured

DEBUG = False


PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

env = Env(DEBUG=(bool, False),)
Env.read_env('.env')
DEBUG = env('DEBUG')

ADMINS = (
    ('Greg Azevedo', 'G@Lightmatter.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    str(PROJECT_ROOT / 'static_source'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'gregazevedo.gregazevedo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'gregazevedo.gregazevedo.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'localflavor',
    'django_extensions',
    'model_utils',
    'easy_thumbnails',
    'registration',
    'import_export',
    'social.apps.django_app.default',
    'floppyforms',
    'webpack_loader',

    'gregazevedo.home',
    'gregazevedo.account',
    'gregazevedo.util',
    'gregazevedo.blog',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'modelcluster',
    'taggit',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookOAuth2',
)

AUTH_USER_MODEL = 'account.User'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/login/'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


def prefixed_cookie(name):
    return 'gregazevedo_{}'.format(name)

SESSION_COOKIE_NAME = prefixed_cookie('sessionid')
CSRF_COOKIE_NAME = prefixed_cookie('csrftoken')
LANGUAGE_COOKIE_NAME = prefixed_cookie('django_language')

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

ALLOWED_HOSTS = [
    'localhost'
    '.herokuapp.com'
]

DEFAULT_FROM_EMAIL = 'hello@gregazevedo.com'
SERVER_EMAIL = 'error@gregazevedo.com'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(PROJECT_ROOT / 'templates')],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'gregazevedo.home.context_processors.settings',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]


WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': str(PROJECT_ROOT / 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

#  registration
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.

#  social
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'account.pipeline.save_facebook_details'
    )


SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook')
SOCIAL_AUTH_USER_MODEL = 'account.User'
SOCIAL_AUTH_DEFAULT_USERNAME = "new_social_auth_user"


WAGTAIL_SITE_NAME = "Greg Azevedo's Site"
