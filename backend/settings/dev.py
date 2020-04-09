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