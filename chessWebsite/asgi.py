"""
ASGI config for Chess project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings')

import chessApp.routing

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(chessApp.routing.websocket_urlpatterns))
        ),
})
