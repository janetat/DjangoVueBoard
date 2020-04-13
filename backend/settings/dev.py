from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#     ),
#    'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.AllowAny',
#          '# rest_framework.permissions.IsAuthenticated'
#     ),
# }

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

APPEND_SLASH = False

# debug toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'}

TIME_ZONE = 'Asia/Shanghai'

STATICFILES_DIRS = [
    os.path.join(FRONT_END_DIR, 'static'),
    os.path.join(FRONT_END_DIR, 'vue', 'dist', 'static'),
]
