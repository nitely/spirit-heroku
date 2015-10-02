# -*- coding: utf-8 -*-

import os

LOCAL_SETTINGS_PATH = os.path.join(os.path.dirname(__file__), 'settings', 'local_prod.py')

if os.path.isfile(LOCAL_SETTINGS_PATH):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local_prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.heroku_prod")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)  # Serve static files
