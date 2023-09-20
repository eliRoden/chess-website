"""
ASGI config for Chess project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
from channels.routing import get_default_application
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings')
django.setup()
application = get_default_application()
