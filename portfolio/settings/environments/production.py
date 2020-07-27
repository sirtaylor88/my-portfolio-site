
"""
This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""

from portfolio.settings.components import config
from portfolio.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config('DOMAIN_NAME'),

    # We need this value for `healthcheck` to work:
    'localhost',
]
