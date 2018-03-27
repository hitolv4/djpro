from .base import *

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('DJANGO_SECRET_KEY',default='wqxq670vlj6=9t^mtqyas%0e5t+)tag75!t*19yrrz9qno6=!v')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)