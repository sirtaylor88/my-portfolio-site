
"""
This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""

from portfolio.settings.components import config
from portfolio.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = False

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
    "tai-portfolio-production.herokuapp.com",
    "nhattainguyen.com",
    "www.nhattainguyen.com",

    # We need this value for `healthcheck` to work:
    'localhost',
]
