from .heroku_prod import *

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.postmarkapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'd80acb63-dcf3-4a05-b74d-e1933f1d9c9d'
EMAIL_HOST_PASSWORD = 'd80acb63-dcf3-4a05-b74d-e1933f1d9c9d'
DEFAULT_FROM_EMAIL = 'noreply@myforum.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
