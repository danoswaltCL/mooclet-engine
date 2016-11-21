'''
Django settings for AWS deployment
'''
# Need to set ENV_TYPE as environment variable in AWS console, e.g. ENV_TYPE='development'

import os
os.environ.setdefault('ENV_TYPE', 'test')
from .base import *
import secure


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True

#### AMAZON S3 STATICFILES STORAGE ####
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = secure.AWS_STORAGE_BUCKET_NAME
AWS_S3_ACCESS_KEY_ID = secure.AWS_S3_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = secure.AWS_SECRET_ACCESS_KEY

# Get environment-specific database settings from secure.py
DATABASES = {
	'default': secure.AWS_DATABASE[os.environ['ENV_TYPE']]
}