from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path
from django.core.asgi import get_asgi_application
from chessApp.consumers import ChessConsumer

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter([
                    path('ws/game/<str:game_id>/', ChessConsumer.as_asgi()),
                ])
            )
        ),
})