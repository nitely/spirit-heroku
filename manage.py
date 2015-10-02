#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    LOCAL_SETTINGS_PATH = os.path.join(os.path.dirname(__file__), 'project', 'settings', 'local_prod.py')

    if os.path.isfile(LOCAL_SETTINGS_PATH):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local_prod")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.heroku_prod")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
