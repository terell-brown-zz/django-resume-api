#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_app.settings.production")
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_app.settings")
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_app.settings.local")
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_app.settings_local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
