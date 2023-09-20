from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path

from . import chessApp

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(chessApp.routing.websocket_urlpatterns))
        ),
})